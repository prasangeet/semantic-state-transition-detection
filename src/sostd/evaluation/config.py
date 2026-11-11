
"""Version-aware OSCaR-Lite evaluation configuration."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class EvaluationConfig:
    """Immutable configuration for OSCaR-Lite evaluation."""

    # Model configuration
    checkpoint: Path = Path("checkpoints/oscar_lite/best.pt")
    model_version: str = "v2"
    input_mode: str = "cached_features"
    tokenizer_name: str = "google/flan-t5-small"
    model_config: dict[str, Any] = field(default_factory=dict)

    # Dataset configuration
    split: str = "validation"
    feature_dir: Path = Path("data/OSCaR/cached_features_v2")
    expected_feature_dim: int = 768
    expected_num_tokens: int = 257
    expected_num_frames: int = 3

    # Output configuration
    output_dir: Path = Path("outputs/evaluations")

    # DataLoader configuration
    batch_size: int = 8
    num_workers: int = 0
    pin_memory: bool = True

    # Inference configuration
    device: str = "cuda"
    amp: bool = True
    max_state_tokens: int = 64
    max_transition_tokens: int = 96
    num_beams: int = 4
    repetition_penalty: float = 1.0
    no_repeat_ngram_size: int = 0
    length_penalty: float = 1.0

    # Reproducibility and sampling
    seed: int = 42
    limit: int | None = None

    SUPPORTED_VERSIONS = ("v1", "v2", "v3", "v4")

    FEATURE_DIMENSIONS = {
        "v1": 384,
        "v2": 768,
        "v3": 1024,
        "v4": 1024,
    }

    def __post_init__(self) -> None:
        """Normalize path fields and validate configuration."""

        object.__setattr__(self, "checkpoint", Path(self.checkpoint))
        object.__setattr__(self, "feature_dir", Path(self.feature_dir))
        object.__setattr__(self, "output_dir", Path(self.output_dir))

        object.__setattr__(
            self,
            "model_version",
            self.model_version.lower().strip(),
        )

        object.__setattr__(
            self,
            "model_config",
            dict(self.model_config),
        )

        self.validate()

    def validate(self) -> None:
        """Validate configuration values."""

        # Model version
        if self.model_version not in self.SUPPORTED_VERSIONS:
            raise ValueError(
                f"model_version must be one of: "
                f"{', '.join(self.SUPPORTED_VERSIONS)}. "
                f"Received: {self.model_version!r}."
            )

        # Input mode
        if self.input_mode != "cached_features":
            raise ValueError(
                "input_mode must be 'cached_features'."
            )

        # Dataset split
        if self.split not in {"validation", "test"}:
            raise ValueError(
                "split must be either 'validation' or 'test'."
            )

        # Feature dimensions
        expected_dimension = self.FEATURE_DIMENSIONS[self.model_version]

        if self.expected_feature_dim != expected_dimension:
            raise ValueError(
                f"expected_feature_dim for "
                f"{self.model_version.upper()} must be "
                f"{expected_dimension}, received "
                f"{self.expected_feature_dim}."
            )

        # Feature structure
        if self.expected_num_tokens != 257:
            raise ValueError(
                "expected_num_tokens must be 257."
            )

        if self.expected_num_frames != 3:
            raise ValueError(
                "expected_num_frames must be 3."
            )

        # Architecture configuration
        if self.model_version in {"v3", "v4"} and not self.model_config:
            raise ValueError(
                f"model_config must be provided for "
                f"{self.model_version.upper()}."
            )

        # V4-specific architecture validation
        if self.model_version == "v4":
            temporal_config = self.model_config.get(
                "temporal_fusion", {}
            )

            if not isinstance(temporal_config, dict):
                raise TypeError(
                    "model_config['temporal_fusion'] must be a dictionary."
                )

            hidden_dim = temporal_config.get("hidden_dim", 1024)

            if hidden_dim != 1024:
                raise ValueError(
                    "V4 currently requires temporal_fusion.hidden_dim "
                    "to be 1024."
                )

            encoder_config = self.model_config.get("encoder", {})

            if not isinstance(encoder_config, dict):
                raise TypeError(
                    "model_config['encoder'] must be a dictionary."
                )

            if not encoder_config.get("freeze_backbone", True):
                raise ValueError(
                    "V4 cached-feature evaluation requires "
                    "freeze_backbone=True."
                )

            if encoder_config.get("unfreeze_last_n_layers", 0) != 0:
                raise ValueError(
                    "V4 cached-feature evaluation requires "
                    "unfreeze_last_n_layers=0."
                )

        # DataLoader
        if self.batch_size < 1:
            raise ValueError("batch_size must be at least 1.")

        if self.num_workers < 0:
            raise ValueError("num_workers cannot be negative.")

        # Generation
        if self.max_state_tokens < 1:
            raise ValueError("max_state_tokens must be at least 1.")

        if self.max_transition_tokens < 1:
            raise ValueError("max_transition_tokens must be at least 1.")

        if self.num_beams < 1:
            raise ValueError("num_beams must be at least 1.")

        if self.repetition_penalty <= 0:
            raise ValueError(
                "repetition_penalty must be greater than 0."
            )

        if self.no_repeat_ngram_size < 0:
            raise ValueError(
                "no_repeat_ngram_size must be non-negative."
            )

        if self.length_penalty <= 0:
            raise ValueError(
                "length_penalty must be greater than 0."
            )

        # Reproducibility
        if self.seed < 0:
            raise ValueError("seed cannot be negative.")

        if self.limit is not None and self.limit < 1:
            raise ValueError("limit must be positive.")

        # Device and tokenizer
        if not isinstance(self.device, str) or not self.device.strip():
            raise ValueError("device cannot be empty.")

        if (
            not isinstance(self.tokenizer_name, str)
            or not self.tokenizer_name.strip()
        ):
            raise ValueError("tokenizer_name cannot be empty.")

    @classmethod
    def from_json(cls, path: str | Path) -> EvaluationConfig:
        """Load configuration from a JSON file."""

        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(path)

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Expected a JSON object.")

        unknown = set(data) - set(cls.__dataclass_fields__)

        if unknown:
            raise ValueError(
                f"Unknown configuration fields: {sorted(unknown)}"
            )

        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable configuration dictionary."""

        result = asdict(self)

        for key in ("checkpoint", "feature_dir", "output_dir"):
            result[key] = str(getattr(self, key))

        return result
