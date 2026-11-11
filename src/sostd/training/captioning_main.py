
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.data.collate import CaptioningCollator
from src.sostd.training.captioning_trainer import CaptioningTrainer


EXPECTED_FEATURE_DIM = 1024
EXPECTED_NUM_TOKENS = 257
IGNORE_INDEX = -100

SUPPORTED_VERSIONS = {"v3", "v4"}


class CachedFeatureEncoder(nn.Module):
    """Expose DINOv2 feature dimensions without running an encoder.

    Used only when the dataset supplies cached features with shape
    (B, T, N, D). The forward method must never be called.
    """

    def __init__(
        self,
        feature_dim: int = EXPECTED_FEATURE_DIM,
        num_tokens: int = EXPECTED_NUM_TOKENS,
    ) -> None:
        super().__init__()

        if feature_dim < 1 or num_tokens < 1:
            raise ValueError(
                "feature_dim and num_tokens must be positive."
            )

        self.hidden_size = feature_dim
        self.output_dim = feature_dim
        self.num_tokens = num_tokens

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        raise RuntimeError(
            "CachedFeatureEncoder cannot process images. "
            "The dataset must supply cached DINOv2 features."
        )


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a JSON configuration."""

    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Configuration not found: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    if not isinstance(config, dict):
        raise ValueError(
            "Training configuration must be a JSON object."
        )

    return config


def set_seed(seed: int) -> None:
    """Set Python, NumPy, and PyTorch random seeds."""

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def _require_mapping(
    config: dict[str, Any],
    key: str,
) -> dict[str, Any]:
    value = config.get(key, {})

    if not isinstance(value, dict):
        raise TypeError(
            f"config['{key}'] must be a JSON object."
        )

    return value


def _resolve_version(config: dict[str, Any]) -> str:
    """Resolve the model version, defaulting to V3 for old configs."""

    model_config = _require_mapping(config, "model")

    version = str(
        model_config.get(
            "version",
            config.get("version", "v3"),
        )
    ).strip().lower()

    if version not in SUPPORTED_VERSIONS:
        raise ValueError(
            f"Unsupported model version: {version!r}. "
            f"Expected one of {sorted(SUPPORTED_VERSIONS)}."
        )

    return version


def _build_cached_encoder(
    encoder_config: dict[str, Any],
    expected_feature_dim: int,
    expected_num_tokens: int,
) -> CachedFeatureEncoder:
    """Validate cached-feature settings and build the feature adapter."""

    freeze_backbone = bool(
        encoder_config.get("freeze_backbone", True)
    )
    unfreeze_layers = int(
        encoder_config.get("unfreeze_last_n_layers", 0)
    )

    if not freeze_backbone or unfreeze_layers != 0:
        raise ValueError(
            "Cached-feature training requires a frozen encoder "
            "and unfreeze_last_n_layers=0."
        )

    return CachedFeatureEncoder(
        feature_dim=expected_feature_dim,
        num_tokens=expected_num_tokens,
    )


def build_model(
    model_config: dict[str, Any],
    input_mode: str = "raw_frames",
    version: str = "v3",
    expected_feature_dim: int = EXPECTED_FEATURE_DIM,
    expected_num_tokens: int = EXPECTED_NUM_TOKENS,
    object_num_classes: int | None = None,
) -> nn.Module:
    """Build the requested V3 or V4 model.

    V3 follows the original constructor and configuration layout.
    V4 is configured for the cached-feature experiment.
    """

    version = version.strip().lower()

    if version not in SUPPORTED_VERSIONS:
        raise ValueError(
            f"Unsupported model version: {version!r}."
        )

    encoder_config = dict(
        model_config.get("encoder", {})
    )
    decoder_config = dict(
        model_config.get("language_decoder", {})
    )
    temporal_config = dict(
        model_config.get("temporal_fusion", {})
    )

    # ---------------------------------------------------------
    # V3
    # ---------------------------------------------------------

    if version == "v3":
        from src.sostd.models.v3.encoders.dinov2_encoder import (
            DINOv2Encoder,
        )
        from src.sostd.models.v3.language.flan_t5_decoder import (
            FlanT5Decoder,
        )
        from src.sostd.models.v3.oscar_lite import (
            OSCaRLite,
        )

        if input_mode == "cached_features":
            encoder = _build_cached_encoder(
                encoder_config,
                expected_feature_dim,
                expected_num_tokens,
            )

        elif input_mode == "raw_frames":
            encoder = DINOv2Encoder(
                freeze_backbone=bool(
                    encoder_config.get("freeze_backbone", True)
                ),
                unfreeze_last_n_layers=int(
                    encoder_config.get(
                        "unfreeze_last_n_layers",
                        4,
                    )
                ),
                image_size=int(
                    encoder_config.get("image_size", 224)
                ),
            )

        else:
            raise ValueError(
                f"Unsupported input_mode: {input_mode!r}."
            )

        language_decoder = FlanT5Decoder(
            model_name=decoder_config.get(
                "model_name",
                "google/flan-t5-base",
            ),
            freeze_backbone=bool(
                decoder_config.get("freeze_backbone", True)
            ),
            unfreeze_last_n_layers=int(
                decoder_config.get("unfreeze_last_n_layers", 0)
            ),
        )

        resampler_config = dict(
            model_config.get("visual_resampler", {})
        )

        return OSCaRLite(
            encoder=encoder,
            language_decoder=language_decoder,
            max_frames=int(
                model_config.get("max_frames", 3)
            ),
            temporal_hidden_dim=int(
                temporal_config.get("hidden_dim", 1024)
            ),
            temporal_num_heads=int(
                temporal_config.get("num_heads", 16)
            ),
            temporal_num_layers=int(
                temporal_config.get("num_layers", 4)
            ),
            num_queries=int(
                resampler_config.get("num_queries", 32)
            ),
            dropout=float(
                model_config.get("dropout", 0.1)
            ),
        )

    # ---------------------------------------------------------
    # V4
    # ---------------------------------------------------------

    if input_mode != "cached_features":
        raise ValueError(
            "The V4 experiment requires cached DINOv2-Large "
            "features. Set data.input_mode='cached_features'."
        )

    if object_num_classes is None or object_num_classes < 2:
        raise ValueError(
            "V4 requires object_num_classes >= 2."
        )

    encoder = _build_cached_encoder(
        encoder_config,
        expected_feature_dim,
        expected_num_tokens,
    )

    from src.sostd.models.v4.language.flan_t5_decoder import (
        FlanT5Decoder,
    )
    from src.sostd.models.v4.oscar_lite import (
        OSCaRLite,
    )

    language_decoder = FlanT5Decoder(
        model_name=decoder_config.get(
            "model_name",
            "google/flan-t5-base",
        ),
        freeze_backbone=bool(
            decoder_config.get("freeze_backbone", True)
        ),
        unfreeze_last_n_layers=int(
            decoder_config.get("unfreeze_last_n_layers", 0)
        ),
    )

    # V4's temporal fusion uses learned queries directly.
    # Keep the number of queries configurable in temporal_fusion.
    return OSCaRLite(
        encoder=encoder,
        language_decoder=language_decoder,
        max_frames=int(
            model_config.get("max_frames", 3)
        ),
        temporal_hidden_dim=int(
            temporal_config.get("hidden_dim", 1024)
        ),
        temporal_num_heads=int(
            temporal_config.get("num_heads", 16)
        ),
        temporal_num_layers=int(
            temporal_config.get("num_layers", 4)
        ),
        num_queries=int(
            temporal_config.get("num_queries", 32)
        ),
        object_num_classes=object_num_classes,
        action_num_classes=None,
        dropout=float(
            model_config.get("dropout", 0.1)
        ),
    )


def _build_object_vocabulary(
    training_samples: list[Any],
    vocabulary_path: Path,
    resume: bool,
) -> Any:
    """Build the V4 object vocabulary from training annotations only."""

    from src.sostd.data.object_vocabulary import ObjectVocabulary

    if not training_samples:
        raise ValueError(
            "Cannot build an object vocabulary from an empty "
            "training sample list."
        )

    labels: list[str] = []

    for sample_index, sample in enumerate(training_samples):
        annotation = getattr(sample, "annotation", None)

        if annotation is None:
            raise TypeError(
                f"Training sample {sample_index} has no annotation."
            )

        object_name = getattr(
            annotation,
            "object_name",
            None,
        )

        if (
            not isinstance(object_name, str)
            or not object_name.strip()
        ):
            raise ValueError(
                "Invalid annotation.object_name in training "
                f"sample {sample_index}."
            )

        labels.append(object_name.strip())

    # This vocabulary is built exclusively from training samples.
    generated_vocabulary = ObjectVocabulary.from_labels(labels)

    if resume:
        if not vocabulary_path.is_file():
            raise FileNotFoundError(
                "Cannot resume V4 without its saved object vocabulary: "
                f"{vocabulary_path}"
            )

        saved_vocabulary = ObjectVocabulary.load(
            vocabulary_path
        )

        if (
            saved_vocabulary.class_to_idx
            != generated_vocabulary.class_to_idx
        ):
            raise ValueError(
                "The saved object vocabulary differs from the "
                "vocabulary reconstructed from the training split. "
                "Refusing to resume with a changed class mapping."
            )

        if (
            saved_vocabulary.class_counts
            != generated_vocabulary.class_counts
        ):
            raise ValueError(
                "Saved object class counts differ from the current "
                "training annotations."
            )

        return saved_vocabulary

    vocabulary_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    generated_vocabulary.save(vocabulary_path)

    return generated_vocabulary


def _configure_cuda(
    engine_config: dict[str, Any],
) -> torch.device:
    """Validate and select the CUDA device."""

    if not torch.cuda.is_available():
        raise RuntimeError(
            "CUDA is required for OSCaR-Lite training."
        )

    requested_device = str(
        engine_config.get("device", "cuda:0")
    )

    if requested_device == "auto":
        requested_device = "cuda:0"

    if not requested_device.startswith("cuda"):
        raise ValueError(
            "Training requires CUDA. "
            f"Received device={requested_device}."
        )

    device = torch.device(requested_device)

    if device.index is None:
        device = torch.device(
            "cuda",
            torch.cuda.current_device(),
        )

    if device.index >= torch.cuda.device_count():
        raise ValueError(
            f"CUDA device {device.index} is unavailable."
        )

    torch.cuda.set_device(device)
    engine_config["device"] = str(device)

    return device


def _build_data_loaders(
    train_dataset: Any,
    validation_dataset: Any,
    collator: CaptioningCollator,
    data_config: dict[str, Any],
) -> tuple[DataLoader, DataLoader]:
    """Construct the training and validation DataLoaders."""

    batch_size = int(
        data_config.get("batch_size", 2)
    )
    num_workers = int(
        data_config.get("num_workers", 4)
    )

    if batch_size < 1:
        raise ValueError(
            "batch_size must be at least 1."
        )

    if num_workers < 0:
        raise ValueError(
            "num_workers cannot be negative."
        )

    loader_options: dict[str, Any] = {
        "batch_size": batch_size,
        "num_workers": num_workers,
        "pin_memory": bool(
            data_config.get("pin_memory", True)
        ),
        "collate_fn": collator,
    }

    if num_workers > 0:
        loader_options["persistent_workers"] = bool(
            data_config.get("persistent_workers", True)
        )

        prefetch_factor = data_config.get(
            "prefetch_factor",
            2,
        )

        if prefetch_factor is not None:
            prefetch_factor = int(prefetch_factor)

            if prefetch_factor < 1:
                raise ValueError(
                    "prefetch_factor must be positive."
                )

            loader_options["prefetch_factor"] = prefetch_factor

    train_loader = DataLoader(
        train_dataset,
        shuffle=True,
        drop_last=bool(
            data_config.get("drop_last", False)
        ),
        **loader_options,
    )

    validation_loader = DataLoader(
        validation_dataset,
        shuffle=False,
        drop_last=False,
        **loader_options,
    )

    return train_loader, validation_loader



def _format_parameter_count(count: int) -> str:
    """Return an exact count with a readable millions/billions suffix."""
    if count >= 1_000_000_000:
        return f"{count:,} ({count / 1_000_000_000:.3f}B)"
    if count >= 1_000_000:
        return f"{count:,} ({count / 1_000_000:.3f}M)"
    if count >= 1_000:
        return f"{count:,} ({count / 1_000:.3f}K)"
    return f"{count:,}"


def _print_parameter_summary(model: nn.Module) -> None:
    """Print total, trainable/frozen, and per-component parameter counts.

    Components are the model's direct child modules. Parameter identities are
    de-duplicated across components so tied/shared weights are not counted
    more than once in the breakdown. Any parameters registered directly on
    the root model are reported as ``<root>``.
    """
    total_params = list(model.parameters())
    total = sum(parameter.numel() for parameter in total_params)
    trainable = sum(
        parameter.numel()
        for parameter in total_params
        if parameter.requires_grad
    )
    frozen = total - trainable

    if total == 0:
        raise ValueError("The model contains no parameters.")
    if trainable == 0:
        raise ValueError("The model has no trainable parameters.")

    print("\n" + "=" * 72)
    print("MODEL PARAMETER SUMMARY")
    print("=" * 72)
    print(f"Total parameters:      {_format_parameter_count(total)}")
    print(f"Trainable parameters:  {_format_parameter_count(trainable)}")
    print(f"Frozen parameters:     {_format_parameter_count(frozen)}")
    print(f"Trainable percentage:  {100.0 * trainable / total:.2f}%")
    print(f"Frozen percentage:     {100.0 * frozen / total:.2f}%")
    print("-" * 72)
    print(f"{'Component':<32} {'Total':>15} {'Trainable':>15} {'Frozen':>15}")
    print("-" * 72)

    seen_parameter_ids: set[int] = set()
    root_total = root_trainable = 0

    # Parameters attached directly to the root module (not a child module).
    for parameter in model.parameters(recurse=False):
        parameter_id = id(parameter)
        if parameter_id in seen_parameter_ids:
            continue
        seen_parameter_ids.add(parameter_id)
        root_total += parameter.numel()
        if parameter.requires_grad:
            root_trainable += parameter.numel()

    if root_total:
        print(
            f"{'<root>':<32} {root_total:>15,} "
            f"{root_trainable:>15,} {root_total-root_trainable:>15,}"
        )

    for component_name, component in model.named_children():
        component_total = component_trainable = 0
        for parameter in component.parameters():
            parameter_id = id(parameter)
            if parameter_id in seen_parameter_ids:
                continue
            seen_parameter_ids.add(parameter_id)
            component_total += parameter.numel()
            if parameter.requires_grad:
                component_trainable += parameter.numel()

        component_frozen = component_total - component_trainable
        print(
            f"{component_name:<32} {component_total:>15,} "
            f"{component_trainable:>15,} {component_frozen:>15,}"
        )

    print("-" * 72)
    print(
        f"{'TOTAL':<32} {total:>15,} "
        f"{trainable:>15,} {frozen:>15,}"
    )
    print("=" * 72 + "\n")


def run_training(
    config: dict[str, Any],
    resume: bool | None = None,
) -> CaptioningTrainer:
    """Run an OSCaR-Lite V3 or V4 training experiment."""

    if not isinstance(config, dict):
        raise TypeError(
            "config must be a dictionary."
        )

    training_config = _require_mapping(
        config,
        "training",
    )
    data_config = _require_mapping(
        config,
        "data",
    )
    model_config = _require_mapping(
        config,
        "model",
    )
    engine_config = dict(
        _require_mapping(config, "engine")
    )

    version = _resolve_version(config)

    epochs = int(
        training_config.get("epochs", 50)
    )
    seed = int(
        training_config.get("seed", 42)
    )

    input_mode = str(
        data_config.get("input_mode", "raw_frames")
    )

    expected_feature_dim = int(
        data_config.get(
            "expected_feature_dim",
            EXPECTED_FEATURE_DIM,
        )
    )
    expected_num_tokens = int(
        data_config.get(
            "expected_num_tokens",
            EXPECTED_NUM_TOKENS,
        )
    )

    if epochs < 1:
        raise ValueError(
            "Training epochs must be at least 1."
        )

    if input_mode not in {
        "raw_frames",
        "cached_features",
    }:
        raise ValueError(
            "input_mode must be 'raw_frames' or 'cached_features'."
        )

    if expected_feature_dim != EXPECTED_FEATURE_DIM:
        raise ValueError(
            f"DINOv2-Large requires {EXPECTED_FEATURE_DIM}-dimensional "
            f"features, received {expected_feature_dim}."
        )

    if expected_num_tokens != EXPECTED_NUM_TOKENS:
        raise ValueError(
            f"DINOv2-Large at 224x224 requires "
            f"{EXPECTED_NUM_TOKENS} tokens, "
            f"received {expected_num_tokens}."
        )

    if version == "v4" and input_mode != "cached_features":
        raise ValueError(
            "V4 is configured for cached DINOv2-Large features. "
            "Set data.input_mode='cached_features'."
        )

    encoder_config = _require_mapping(
        model_config,
        "encoder",
    )

    if input_mode == "cached_features":
        if not bool(
            encoder_config.get("freeze_backbone", True)
        ):
            raise ValueError(
                "Cached features cannot be used to fine-tune DINOv2."
            )

        if int(
            encoder_config.get("unfreeze_last_n_layers", 0)
        ) != 0:
            raise ValueError(
                "Cached-feature training requires "
                "unfreeze_last_n_layers=0."
            )

    feature_dir = Path(
        data_config.get(
            "feature_dir",
            "data/OSCaR/cached_features_v3_large",
        )
    )

    default_checkpoint_dir = (
        "checkpoints/oscar_lite_v4"
        if version == "v4"
        else "checkpoints/oscar_lite_v3"
    )

    checkpoint_dir = Path(
        training_config.get(
            "checkpoint_dir",
            default_checkpoint_dir,
        )
    )

    should_resume = (
        bool(training_config.get("resume", False))
        if resume is None
        else resume
    )

    latest_checkpoint = checkpoint_dir / "latest.pt"

    if should_resume:
        if not latest_checkpoint.is_file():
            raise FileNotFoundError(
                "Cannot resume because the latest checkpoint "
                f"does not exist: {latest_checkpoint}"
            )
    elif latest_checkpoint.exists():
        raise FileExistsError(
            f"A checkpoint already exists in {checkpoint_dir}. "
            "Use --resume or select a new checkpoint directory."
        )

    set_seed(seed)

    # ---------------------------------------------------------
    # Device
    # ---------------------------------------------------------

    device = _configure_cuda(engine_config)

    print("=" * 72)
    print(f"OSCaR-Lite {version.upper()} Training")
    print("=" * 72)
    print(f"Device: {device}")
    print(f"GPU: {torch.cuda.get_device_name(device)}")
    print(f"Input mode: {input_mode}")
    print(
        f"Feature shape: "
        f"({expected_num_tokens}, {expected_feature_dim})"
    )
    print(f"Epochs: {epochs}")
    print(f"Seed: {seed}")
    print(f"Feature directory: {feature_dir}")
    print(f"Checkpoint directory: {checkpoint_dir}")

    # ---------------------------------------------------------
    # Dataset construction
    # ---------------------------------------------------------

    dataset_options = {
        "input_mode": input_mode,
        "expected_feature_dim": expected_feature_dim,
        "expected_num_tokens": expected_num_tokens,
    }

    print("\nBuilding training dataset...")

    train_dataset, train_report = build_temporal_dataset(
        split="train",
        feature_dir=feature_dir,
        **dataset_options,
    )

    print("\nBuilding validation dataset...")

    validation_dataset, validation_report = build_temporal_dataset(
        split="validation",
        feature_dir=feature_dir,
        **dataset_options,
    )

    if len(train_dataset) == 0:
        raise ValueError(
            "Training dataset is empty."
        )

    if len(validation_dataset) == 0:
        raise ValueError(
            "Validation dataset is empty."
        )

    for split_name, dataset in (
        ("training", train_dataset),
        ("validation", validation_dataset),
    ):
        actual_mode = getattr(
            dataset,
            "input_mode",
            None,
        )

        if actual_mode != input_mode:
            raise RuntimeError(
                f"{split_name} dataset resolved to {actual_mode!r}; "
                f"expected {input_mode!r}."
            )

    print(f"\nTraining samples: {len(train_dataset)}")
    print(f"Validation samples: {len(validation_dataset)}")
    print(f"Training clips built: {train_report.clips_built}")
    print(
        "Validation clips built: "
        f"{validation_report.clips_built}"
    )

    # ---------------------------------------------------------
    # V4 object vocabulary
    # ---------------------------------------------------------

    vocabulary = None
    object_to_idx = None
    object_num_classes = None

    if version == "v4":
        vocabulary_path = (
            checkpoint_dir / "object_vocabulary.json"
        )

        vocabulary = _build_object_vocabulary(
            training_samples=train_report.samples,
            vocabulary_path=vocabulary_path,
            resume=should_resume,
        )

        object_to_idx = vocabulary.class_to_idx
        object_num_classes = len(object_to_idx)

        if object_num_classes < 2:
            raise ValueError(
                "V4 object classification requires at least "
                "two object classes."
            )

        class_weights = torch.as_tensor(
            vocabulary.class_weights(),
            dtype=torch.float32,
        )

        if class_weights.ndim != 1:
            raise ValueError(
                "Object class weights must be one-dimensional."
            )

        if class_weights.numel() != object_num_classes:
            raise ValueError(
                "Object class-weight count does not match "
                "the vocabulary size."
            )

        if not torch.isfinite(class_weights).all():
            raise ValueError(
                "Object class weights contain non-finite values."
            )

        if torch.any(class_weights <= 0):
            raise ValueError(
                "Object class weights must all be positive."
            )

        # JSON-compatible values are passed through the trainer
        # configuration. CaptioningTrainer must forward these to
        # CaptioningEngine in the corresponding trainer update.
        engine_config["object_weight"] = float(
            engine_config.get("object_weight", 0.25)
        )
        engine_config["object_class_weights"] = (
            class_weights.tolist()
        )

        print("\nV4 object supervision")
        print(f"Object classes: {object_num_classes}")
        print(f"Vocabulary: {vocabulary_path}")
        print(
            "Object loss weight: "
            f"{engine_config['object_weight']}"
        )
        print("Class weighting: inverse-square-root frequency")

    # ---------------------------------------------------------
    # Tokenizer and collator
    # ---------------------------------------------------------

    tokenizer_name = model_config.get(
        "tokenizer_name",
        "google/flan-t5-base",
    )

    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_name
    )

    collator = CaptioningCollator(
        tokenizer=tokenizer,
        max_state_length=int(
            data_config.get("max_state_length", 128)
        ),
        max_transition_length=int(
            data_config.get("max_transition_length", 128)
        ),
        # V3: None, preserving the original batch format.
        # V4: training vocabulary; unknown validation labels -> -100.
        object_to_idx=object_to_idx,
    )

    train_loader, validation_loader = _build_data_loaders(
        train_dataset=train_dataset,
        validation_dataset=validation_dataset,
        collator=collator,
        data_config=data_config,
    )

    # ---------------------------------------------------------
    # Model initialization
    # ---------------------------------------------------------

    print(
        f"\nInitializing OSCaR-Lite {version.upper()}..."
    )

    model = build_model(
        model_config=model_config,
        input_mode=input_mode,
        version=version,
        expected_feature_dim=expected_feature_dim,
        expected_num_tokens=expected_num_tokens,
        object_num_classes=object_num_classes,
    )

    encoder_dim = int(
        getattr(
            model.encoder,
            "hidden_size",
            getattr(model.encoder, "output_dim", -1),
        )
    )

    if encoder_dim != expected_feature_dim:
        raise RuntimeError(
            f"Encoder feature dimension is {encoder_dim}; "
            f"expected {expected_feature_dim}."
        )

    encoder_trainable = sum(
        parameter.numel()
        for parameter in model.encoder.parameters()
        if parameter.requires_grad
    )

    if input_mode == "cached_features" and encoder_trainable != 0:
        raise RuntimeError(
            "Cached-feature training must not have trainable "
            "encoder parameters."
        )

    # Print exact model-wide counts and a component-level breakdown before
    # constructing the optimizer or starting any training epochs.
    _print_parameter_summary(model)

    print("Model configuration:")
    print(f"  Version: {version.upper()}")
    print(f"  Input mode: {input_mode}")
    print(f"  Encoder feature dimension: {encoder_dim}")
    print(f"  Encoder trainable parameters: {encoder_trainable:,}")
    if version == "v4":
        print(f"  Object classes: {object_num_classes}")
    print(
        "  Temporal fusion configuration:",
        model_config.get("temporal_fusion", {}),
    )
    if version == "v3":
        print(
            "  Visual resampler configuration:",
            model_config.get("visual_resampler", {}),
        )

    # ---------------------------------------------------------
    # Trainer
    # ---------------------------------------------------------

    trainer_config = dict(config)
    trainer_config["engine"] = engine_config

    trainer = CaptioningTrainer.from_config(
        model=model,
        config=trainer_config,
        checkpoint_dir=checkpoint_dir,
    )

    # ---------------------------------------------------------
    # Resume
    # ---------------------------------------------------------

    if should_resume:
        next_epoch = trainer.resume(model)

        print(
            f"\nResuming from checkpoint. "
            f"Next epoch index: {next_epoch}"
        )

    # ---------------------------------------------------------
    # Training
    # ---------------------------------------------------------

    print(
        f"\nStarting OSCaR-Lite {version.upper()} training..."
    )

    history = trainer.fit(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        epochs=epochs,
    )

    print("\nTraining completed.")
    print(f"History entries: {len(history)}")
    print(
        f"Best validation loss: {trainer.best_metric:.6f}"
    )
    print(
        f"Checkpoints: {checkpoint_dir.resolve()}"
    )

    if vocabulary is not None:
        print(
            "Object vocabulary: "
            f"{(checkpoint_dir / 'object_vocabulary.json').resolve()}"
        )

    return trainer


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Train OSCaR-Lite V3 or V4 using raw frames "
            "or cached DINOv2-Large features."
        )
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=Path(
            "configs/oscar_lite_v3_captioning.json"
        ),
        help="Path to the JSON training configuration.",
    )

    resume_group = parser.add_mutually_exclusive_group()

    resume_group.add_argument(
        "--resume",
        action="store_true",
        help="Resume from the latest checkpoint.",
    )

    resume_group.add_argument(
        "--no-resume",
        action="store_true",
        help="Start a fresh training run.",
    )

    args = parser.parse_args()

    config = load_config(args.config)

    resume = (
        True
        if args.resume
        else False
        if args.no_resume
        else None
    )

    run_training(
        config=config,
        resume=resume,
    )


if __name__ == "__main__":
    main()
