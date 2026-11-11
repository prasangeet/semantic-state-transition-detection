"""Checkpoint-aware model and checkpoint loading for OSCaR-Lite."""

from __future__ import annotations

import importlib
import re
from pathlib import Path
from typing import Any

import torch
import torch.nn as nn


class CachedFeatureEncoder(nn.Module):
    """Parameter-free adapter for precomputed DINOv2 features."""

    def __init__(self, feature_dim: int, num_tokens: int = 257) -> None:
        super().__init__()
        if feature_dim < 1 or num_tokens < 1:
            raise ValueError("feature_dim and num_tokens must be positive.")
        self.hidden_size = int(feature_dim)
        self.output_dim = int(feature_dim)
        self.num_tokens = int(num_tokens)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        raise RuntimeError(
            "CachedFeatureEncoder cannot process raw images; pass cached "
            "features directly to OSCaR-Lite."
        )


class ModelLoader:
    """Construct the requested model version and strictly load its checkpoint.

    V4 dimensions represented in checkpoint tensor shapes are inferred
    automatically. Attention heads and decoder options are not encoded
    uniquely in weights, so they must come from model_config.
    """

    SUPPORTED_VERSIONS = {"v1", "v2", "v3", "v4"}
    CHECKPOINT_KEYS = ("model_state_dict", "state_dict", "model")
    BLOCK_RE = re.compile(r"^temporal_fusion\.encoder_blocks\.(\d+)\.")
    INDEX_PATTERNS = (
        re.compile(r"^temporal_fusion\.(?:state_query_blocks|state_decoder_layers|query_decoder_layers)\.(\d+)\."),
        re.compile(r"^temporal_fusion\.(?:transition_query_blocks|transition_decoder_layers)\.(\d+)\."),
    )

    def __init__(
        self,
        checkpoint: str | Path,
        device: str | torch.device = "cuda",
        model_version: str = "v2",
        model_config: dict[str, Any] | None = None,
        input_mode: str = "cached_features",
        expected_feature_dim: int | None = None,
        expected_num_tokens: int = 257,
    ) -> None:
        self.checkpoint = Path(checkpoint)
        self.device = torch.device(device)
        self.model_version = model_version.lower().strip()
        self.model_config = dict(model_config or {})
        self.input_mode = input_mode
        self.expected_feature_dim = expected_feature_dim
        self.expected_num_tokens = expected_num_tokens

    def _validate_environment(self) -> None:
        if self.device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA is unavailable.")
        if not self.checkpoint.is_file():
            raise FileNotFoundError(self.checkpoint)
        if self.model_version not in self.SUPPORTED_VERSIONS:
            raise ValueError(
                f"Unsupported model version {self.model_version!r}; "
                f"choose from {sorted(self.SUPPORTED_VERSIONS)}."
            )
        if self.input_mode != "cached_features":
            raise ValueError("Only cached-feature evaluation is supported.")
        if self.expected_num_tokens != 257:
            raise ValueError("Expected feature token count must be 257.")

        dimensions = {"v1": 384, "v2": 768, "v3": 1024, "v4": 1024}
        expected = dimensions[self.model_version]
        if self.expected_feature_dim not in (None, expected):
            raise ValueError(
                f"{self.model_version.upper()} requires {expected}-dimensional "
                f"features; got {self.expected_feature_dim}."
            )

    def _load_checkpoint(self) -> dict[str, Any]:
        checkpoint = torch.load(
            self.checkpoint, map_location="cpu", weights_only=False
        )
        if not isinstance(checkpoint, dict):
            raise TypeError("Checkpoint must be a dictionary.")
        return checkpoint

    def _extract_state_dict(
        self, checkpoint: dict[str, Any]
    ) -> dict[str, torch.Tensor]:
        state = None
        for key in self.CHECKPOINT_KEYS:
            candidate = checkpoint.get(key)
            if isinstance(candidate, dict):
                state = candidate
                break

        if state is None and checkpoint and all(
            isinstance(value, torch.Tensor) for value in checkpoint.values()
        ):
            state = checkpoint
        if not isinstance(state, dict) or not state:
            raise KeyError(
                "Could not locate model weights in checkpoint. "
                f"Available keys: {list(checkpoint)}"
            )

        cleaned: dict[str, torch.Tensor] = {}
        for key, value in state.items():
            if not isinstance(value, torch.Tensor):
                raise TypeError(f"Checkpoint entry {key!r} is not a tensor.")
            normalized = key.removeprefix("module.")
            if normalized in cleaned:
                raise ValueError(f"Duplicate state-dict key: {normalized}")
            cleaned[normalized] = value
        return cleaned

    @staticmethod
    def _import_class(module_path: str, class_name: str) -> type:
        try:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as exc:
            raise ImportError(
                f"Could not load {class_name} from {module_path}."
            ) from exc

    @staticmethod
    def _section(config: dict[str, Any], name: str) -> dict[str, Any]:
        value = config.get(name, {})
        if not isinstance(value, dict):
            raise TypeError(f"model_config[{name!r}] must be a dictionary.")
        return value

    def _version_module(self, component: str) -> str:
        if self.model_version in {"v3", "v4"}:
            return f"src.sostd.models.{self.model_version}.{component}"
        return f"src.sostd.models.{component}"

    def _load_model_classes(self):
        model_cls = self._import_class(
            self._version_module("oscar_lite"), "OSCaRLite"
        )
        decoder_cls = self._import_class(
            self._version_module("language.flan_t5_decoder"),
            "FlanT5Decoder",
        )
        return model_cls, decoder_cls

    def _build_legacy_or_v3_model(self) -> nn.Module:
        model_cls, decoder_cls = self._load_model_classes()
        if not self.model_config:
            if self.model_version == "v2":
                return model_cls()
            raise ValueError(f"{self.model_version.upper()} requires model_config.")

        encoder_cfg = self._section(self.model_config, "encoder")
        decoder_cfg = self._section(self.model_config, "language_decoder")
        temporal_cfg = self._section(self.model_config, "temporal_fusion")
        resampler_cfg = self._section(self.model_config, "visual_resampler")

        if self.model_version == "v3":
            if not encoder_cfg.get("freeze_backbone", True):
                raise ValueError("V3 cached-feature evaluation requires a frozen encoder.")
            if encoder_cfg.get("unfreeze_last_n_layers", 0) != 0:
                raise ValueError("Cached V3 features cannot unfreeze encoder layers.")
            encoder = CachedFeatureEncoder(1024, self.expected_num_tokens)
            defaults = (1024, 16, 4, 32)
        else:
            encoder_cls = self._import_class(
                self._version_module("encoders.dinov2_encoder"),
                "DINOv2Encoder",
            )
            variant = "small" if self.model_version == "v1" else "base"
            encoder = encoder_cls(
                variant=variant,
                freeze_backbone=encoder_cfg.get("freeze_backbone", True),
                unfreeze_last_n_layers=encoder_cfg.get("unfreeze_last_n_layers", 0),
                image_size=encoder_cfg.get("image_size", 224),
            )
            defaults = (256, 4, 2, 8) if self.model_version == "v1" else (512, 8, 3, 16)

        decoder = decoder_cls(
            model_name=decoder_cfg.get("model_name", "google/flan-t5-base"),
            freeze_backbone=decoder_cfg.get("freeze_backbone", True),
            unfreeze_last_n_layers=decoder_cfg.get("unfreeze_last_n_layers", 0),
        )
        return model_cls(
            encoder=encoder,
            language_decoder=decoder,
            max_frames=self.model_config.get("max_frames", 3),
            temporal_hidden_dim=temporal_cfg.get("hidden_dim", defaults[0]),
            temporal_num_heads=temporal_cfg.get("num_heads", defaults[1]),
            temporal_num_layers=temporal_cfg.get("num_layers", defaults[2]),
            num_queries=resampler_cfg.get("num_queries", defaults[3]),
            dropout=self.model_config.get("dropout", 0.1),
        )

    @staticmethod
    def _matching_tensor(
        state: dict[str, torch.Tensor], suffixes: tuple[str, ...]
    ) -> tuple[str, torch.Tensor] | None:
        matches = [
            (key, tensor)
            for key, tensor in state.items()
            if any(key == suffix or key.endswith("." + suffix) for suffix in suffixes)
        ]
        if len(matches) > 1:
            raise ValueError(
                "Ambiguous checkpoint tensors: " + ", ".join(k for k, _ in matches)
            )
        return matches[0] if matches else None

    def _infer_v4_dimensions(self, state: dict[str, torch.Tensor]) -> dict[str, int]:
        blocks = {
            int(match.group(1))
            for key in state
            if (match := self.BLOCK_RE.match(key))
        }
        if not blocks or blocks != set(range(max(blocks) + 1)):
            raise ValueError(
                "Cannot infer a contiguous V4 temporal encoder depth from "
                "temporal_fusion.encoder_blocks.* checkpoint keys."
            )

        transition_queries = self._matching_tensor(
            state, ("temporal_fusion.transition_queries",)
        )
        if transition_queries is None:
            raise ValueError("Checkpoint is missing temporal_fusion.transition_queries.")
        query_shape = tuple(transition_queries[1].shape)
        if len(query_shape) != 3 or query_shape[0] != 1:
            raise ValueError(f"Unexpected transition_queries shape: {query_shape}")

        # ObjectHead is registered as model.object_head. Infer its output
        # classes from its final Linear weight, without assuming a submodule name.
        object_weights = [
            (key, tensor)
            for key, tensor in state.items()
            if key.startswith("object_head.") and key.endswith(".weight")
            and tensor.ndim == 2
        ]
        if not object_weights:
            raise ValueError("Could not find a 2D weight tensor under object_head.")
        # The classifier's output dimension is the class count. Prefer the
        # final Linear layer when several Linear layers are present.
        object_weight = object_weights[-1][1]

        return {
            "hidden_dim": int(query_shape[-1]),
            "num_queries": int(query_shape[1]),
            "num_layers": len(blocks),
            "object_num_classes": int(object_weight.shape[0]),
        }

    def _build_v4_model(self, state: dict[str, torch.Tensor]) -> nn.Module:
        if not self.model_config:
            raise ValueError(
                "V4 requires model_config for settings not encoded in weights, "
                "including temporal_fusion.num_heads and decoder settings."
            )

        model_cls, decoder_cls = self._load_model_classes()
        encoder_cfg = self._section(self.model_config, "encoder")
        temporal_cfg = self._section(self.model_config, "temporal_fusion")
        decoder_cfg = self._section(self.model_config, "language_decoder")

        if not encoder_cfg.get("freeze_backbone", True):
            raise ValueError("V4 cached-feature evaluation requires a frozen encoder.")
        if encoder_cfg.get("unfreeze_last_n_layers", 0) != 0:
            raise ValueError("Cached V4 features cannot unfreeze encoder layers.")

        feature_dim = self.expected_feature_dim or 1024
        if feature_dim != 1024:
            raise ValueError("V4 requires 1024-dimensional cached features.")

        inferred = self._infer_v4_dimensions(state)

        # Config values, when present, must agree with the checkpoint.
        configured = {
            "hidden_dim": temporal_cfg.get("hidden_dim"),
            "num_layers": temporal_cfg.get("num_layers"),
            "num_queries": temporal_cfg.get("num_queries"),
            "object_num_classes": self.model_config.get(
                "object_num_classes",
                self._section(self.model_config, "object_head").get("num_classes"),
            ),
        }
        for name, value in configured.items():
            if value is not None and int(value) != inferred[name]:
                raise ValueError(
                    f"Config/checkpoint mismatch for {name}: "
                    f"config={value}, checkpoint={inferred[name]}."
                )

        heads = temporal_cfg.get("num_heads")
        if heads is None:
            raise ValueError(
                "temporal_fusion.num_heads is required; it cannot be inferred "
                "unambiguously from checkpoint weights."
            )
        heads = int(heads)
        if heads < 1 or inferred["hidden_dim"] % heads:
            raise ValueError(
                f"num_heads={heads} is invalid for hidden_dim={inferred['hidden_dim']}."
            )

        # These V4 constructor settings also affect state-dict structure.
        state_queries = temporal_cfg.get("state_queries", self.model_config.get("state_queries", 16))
        query_layers = temporal_cfg.get("query_layers", self.model_config.get("query_layers", 2))
        max_frames = int(self.model_config.get("max_frames", 3))
        dropout = float(self.model_config.get("dropout", 0.1))

        decoder_name = decoder_cfg.get(
            "model_name",
            self.model_config.get("tokenizer_name", "google/flan-t5-base"),
        )
        decoder = decoder_cls(
            model_name=decoder_name,
            freeze_backbone=decoder_cfg.get("freeze_backbone", True),
            unfreeze_last_n_layers=decoder_cfg.get("unfreeze_last_n_layers", 0),
        )
        encoder = CachedFeatureEncoder(feature_dim, self.expected_num_tokens)

        return model_cls(
            encoder=encoder,
            language_decoder=decoder,
            max_frames=max_frames,
            temporal_hidden_dim=inferred["hidden_dim"],
            temporal_num_heads=heads,
            temporal_num_layers=inferred["num_layers"],
            num_queries=inferred["num_queries"],
            state_queries=int(state_queries),
            query_layers=int(query_layers),
            object_num_classes=inferred["object_num_classes"],
            action_num_classes=None,
            dropout=dropout,
        )

    def _build_model(self, state: dict[str, torch.Tensor]) -> nn.Module:
        if self.model_version == "v4":
            return self._build_v4_model(state)
        return self._build_legacy_or_v3_model()

    def load(self) -> nn.Module:
        """Build the architecture and load all checkpoint weights strictly."""
        self._validate_environment()
        checkpoint = self._load_checkpoint()
        state = self._extract_state_dict(checkpoint)
        model = self._build_model(state)

        try:
            model.load_state_dict(state, strict=True)
        except RuntimeError as exc:
            raise RuntimeError(
                f"Strict {self.model_version.upper()} checkpoint loading failed. "
                "No checkpoint keys were ignored. The evaluation architecture "
                f"must match training exactly. Original error: {exc}"
            ) from exc

        model.to(self.device)
        model.eval()
        return model
