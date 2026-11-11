from __future__ import annotations

from pathlib import Path
from typing import Any

import torch
from tqdm.auto import tqdm

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.models.encoders.dinov2_encoder import DINOv2Encoder


FEATURE_DIR = Path("data/OSCaR/cached_features_v3_large")

EXPECTED_TOKENS = 257
EXPECTED_DIM = 1024

DEVICE = torch.device("cuda:0")


def _is_valid_cache(path: Path) -> bool:
    """Check whether an existing cache contains valid DINOv2-Large features."""

    if not path.is_file():
        return False

    try:
        cached = torch.load(
            path,
            map_location="cpu",
            weights_only=True,
        )

        if not isinstance(cached, dict):
            return False

        required_keys = {"before", "during", "after"}

        if not required_keys.issubset(cached):
            return False

        def valid_tensor(tensor: Any) -> bool:
            return (
                isinstance(tensor, torch.Tensor)
                and tuple(tensor.shape) == (
                    EXPECTED_TOKENS,
                    EXPECTED_DIM,
                )
                and torch.is_floating_point(tensor)
                and torch.isfinite(tensor).all().item()
            )

        if not valid_tensor(cached["before"]):
            return False

        if not valid_tensor(cached["after"]):
            return False

        during = cached["during"]

        if not isinstance(during, dict) or not during:
            return False

        return all(
            valid_tensor(features)
            for features in during.values()
        )

    except (
        OSError,
        RuntimeError,
        EOFError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return False


def _validate_image_tensor(
    tensor: Any,
    name: str,
) -> torch.Tensor:
    """Validate an RGB tensor returned by TemporalDataset."""

    if not isinstance(tensor, torch.Tensor):
        raise TypeError(
            f"Expected a tensor for {name}, "
            f"received {type(tensor).__name__}."
        )

    if tensor.ndim != 3 or tensor.shape[0] != 3:
        raise ValueError(
            f"Expected {name} with shape (3, H, W), "
            f"received {tuple(tensor.shape)}."
        )

    if not tensor.is_floating_point():
        raise TypeError(
            f"Expected floating-point image tensor for {name}, "
            f"received {tensor.dtype}."
        )

    if not torch.isfinite(tensor).all().item():
        raise ValueError(
            f"Non-finite pixel values found in {name}."
        )

    if tensor.min().item() < 0.0 or tensor.max().item() > 1.0:
        raise ValueError(
            f"Expected {name} pixel values in [0, 1]."
        )

    return tensor


def _extract_sample_features(
    encoder: DINOv2Encoder,
    sample: dict[str, Any],
) -> dict[str, Any]:
    """Extract features for all frames in one temporal sample."""

    before = _validate_image_tensor(
        sample["before"],
        "before",
    )

    after = _validate_image_tensor(
        sample["after"],
        "after",
    )

    during = sample["during"]

    if not isinstance(during, dict) or not during:
        raise ValueError(
            "Temporal sample must contain at least one during frame."
        )

    during_items = list(during.items())

    during_tensors = [
        _validate_image_tensor(
            tensor,
            f"during[{frame_idx}]",
        )
        for frame_idx, tensor in during_items
    ]

    # Encode all frames together to reduce inference overhead.
    frame_tensors = [
        before,
        *during_tensors,
        after,
    ]

    images = torch.stack(frame_tensors, dim=0).to(DEVICE)

    with torch.inference_mode():
        features = encoder(images)

    expected_shape = (
        len(frame_tensors),
        EXPECTED_TOKENS,
        EXPECTED_DIM,
    )

    if tuple(features.shape) != expected_shape:
        raise RuntimeError(
            f"Unexpected encoder output shape: "
            f"expected {expected_shape}, "
            f"received {tuple(features.shape)}."
        )

    if not torch.isfinite(features).all().item():
        raise RuntimeError(
            "DINOv2-Large generated non-finite features."
        )

    features = features.cpu().contiguous()

    during_features = {
        frame_idx: features[index + 1]
        for index, (frame_idx, _) in enumerate(during_items)
    }

    return {
        "before": features[0],
        "during": during_features,
        "after": features[-1],
    }


def _save_cache(
    cache: dict[str, Any],
    save_path: Path,
) -> None:
    """Save a feature cache atomically."""

    temporary_path = save_path.with_suffix(".tmp")

    try:
        torch.save(cache, temporary_path)
        temporary_path.replace(save_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def precompute_features() -> None:
    """Precompute frozen DINOv2-Large features for OSCaR."""

    if not torch.cuda.is_available():
        raise RuntimeError(
            "CUDA is required for DINOv2-Large feature precomputation."
        )

    torch.cuda.set_device(DEVICE)

    print(f"Using device: {DEVICE}")
    print(f"GPU: {torch.cuda.get_device_name(DEVICE)}")

    encoder = DINOv2Encoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=0,
    ).to(DEVICE)

    encoder.eval()

    if encoder.hidden_size != EXPECTED_DIM:
        raise ValueError(
            f"Expected feature dimension {EXPECTED_DIM}, "
            f"received {encoder.hidden_size}."
        )

    if encoder.num_tokens != EXPECTED_TOKENS:
        raise ValueError(
            f"Expected {EXPECTED_TOKENS} tokens, "
            f"received {encoder.num_tokens}."
        )

    trainable_parameters = encoder.get_num_trainable_parameters()

    if trainable_parameters != 0:
        raise RuntimeError(
            "Expected a completely frozen DINOv2-Large encoder, "
            f"but found {trainable_parameters:,} trainable parameters."
        )

    print(
        f"Encoder: {encoder.MODEL_NAME}\n"
        f"Parameters: {encoder.get_num_parameters():,}\n"
        f"Trainable parameters: {trainable_parameters:,}\n"
        f"Output shape: ({EXPECTED_TOKENS}, {EXPECTED_DIM})"
    )

    FEATURE_DIR.mkdir(parents=True, exist_ok=True)

    for split in ("train", "validation"):
        print(f"\nBuilding temporal dataset for '{split}'...")

        dataset, build_result = build_temporal_dataset(
            split=split,
            feature_dir=FEATURE_DIR,
            expected_feature_dim=EXPECTED_DIM,
            expected_num_tokens=EXPECTED_TOKENS,
            input_mode="raw_frames",
        )

        if dataset.input_mode != "raw_frames":
            raise RuntimeError(
                f"Expected raw_frames mode, "
                f"received {dataset.input_mode!r}."
            )

        split_dir = FEATURE_DIR / split
        split_dir.mkdir(parents=True, exist_ok=True)

        print(f"Samples: {len(dataset)}")
        print(f"Clips seen: {build_result.clips_seen}")
        print(f"Samples built: {build_result.clips_built}")

        skipped = 0
        computed = 0

        progress = tqdm(
            range(len(dataset)),
            desc=f"Precomputing {split}",
            unit="sample",
        )

        for idx in progress:
            save_path = split_dir / f"sample_{idx}.pt"

            if _is_valid_cache(save_path):
                skipped += 1
                progress.set_postfix(
                    generated=computed,
                    skipped=skipped,
                )
                continue

            # Use TemporalDataset's public interface.
            # This also uses its configured RGBFrameLoader.
            sample = dataset[idx]

            cache = _extract_sample_features(
                encoder,
                sample,
            )

            _save_cache(cache, save_path)

            computed += 1

            progress.set_postfix(
                generated=computed,
                skipped=skipped,
            )

        print(
            f"\n{split} complete:\n"
            f"  Generated: {computed}\n"
            f"  Skipped valid: {skipped}\n"
            f"  Total: {len(dataset)}"
        )

    print("\nFeature precomputation complete.")
    print(f"Cache directory: {FEATURE_DIR.resolve()}")
    print(f"Encoder: {encoder.MODEL_NAME}")
    print(
        f"Feature shape: ({EXPECTED_TOKENS}, {EXPECTED_DIM})"
    )


if __name__ == "__main__":
    precompute_features()