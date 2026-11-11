
from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Literal

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset

from src.sostd.data.temporal_sample_builder import TemporalSample


InputMode = Literal["auto", "raw_frames", "cached_features"]


class TemporalDataset(Dataset):
    """Temporal dataset supporting raw frames and cached visual features.

    Input modes:
        raw_frames:
            Loads images using the configured frame loader.

        cached_features:
            Loads precomputed feature tensors from disk.

        auto:
            Uses raw frames when a frame loader is provided;
            otherwise uses cached features.

    Backward compatibility:
        TemporalDataset(samples, frame_loader)
        TemporalDataset(samples, split_name="train", ...)
    """

    TEMPORAL_KEYS = ("Frame_1", "Frame_2", "Frame_3")

    INPUT_MODES = {
        "auto",
        "raw_frames",
        "cached_features",
    }

    def __init__(
        self,
        samples: list[TemporalSample],
        split_name: str | Any = "train",
        feature_dir: str | Path = "data/OSCaR/cached_features",
        frame_loader: Any | None = None,
        transform: Callable[[Any], Any] | None = None,
        expected_feature_dim: int | None = None,
        expected_num_tokens: int | None = 257,
        input_mode: InputMode = "auto",
        cache_extension: str = ".pt",
    ) -> None:
        # Backward compatibility:
        # TemporalDataset(samples, frame_loader)
        if not isinstance(split_name, str):
            if frame_loader is not None:
                raise TypeError(
                    "frame_loader was provided both positionally "
                    "and by keyword."
                )

            frame_loader = split_name
            split_name = "train"

        if split_name not in {"train", "validation"}:
            raise ValueError(
                f"Unsupported split_name: {split_name!r}."
            )

        if input_mode not in self.INPUT_MODES:
            raise ValueError(
                f"Unsupported input_mode {input_mode!r}. "
                f"Choose one of {sorted(self.INPUT_MODES)}."
            )

        if (
            expected_feature_dim is not None
            and expected_feature_dim <= 0
        ):
            raise ValueError(
                "expected_feature_dim must be positive."
            )

        if (
            expected_num_tokens is not None
            and expected_num_tokens <= 0
        ):
            raise ValueError(
                "expected_num_tokens must be positive."
            )

        if not cache_extension.startswith("."):
            raise ValueError(
                "cache_extension must begin with a period."
            )

        self.samples = samples
        self.split_name = split_name

        self.feature_dir = (
            Path(feature_dir).expanduser() / split_name
        )

        self.frame_loader = frame_loader
        self.transform = transform

        self.expected_feature_dim = expected_feature_dim
        self.expected_num_tokens = expected_num_tokens

        self.cache_extension = cache_extension

        if input_mode == "auto":
            self.input_mode = (
                "raw_frames"
                if frame_loader is not None
                else "cached_features"
            )
        else:
            self.input_mode = input_mode

        if (
            self.input_mode == "raw_frames"
            and self.frame_loader is None
        ):
            raise ValueError(
                "raw_frames mode requires a frame_loader."
            )

    def __len__(self) -> int:
        return len(self.samples)

    @staticmethod
    def _to_tensor(image: Image.Image) -> torch.Tensor:
        """Convert a PIL image to a float32 RGB tensor in CHW format."""

        array = np.asarray(
            image.convert("RGB"),
            dtype=np.uint8,
        ).copy()

        return (
            torch.from_numpy(array)
            .permute(2, 0, 1)
            .contiguous()
            .float()
            .div_(255.0)
        )

    def _load_image(
        self,
        repository_path: str,
    ) -> torch.Tensor:
        """Load and transform one image."""

        image = self.frame_loader.load(repository_path)

        if isinstance(image, Image.Image):
            transformed = (
                self.transform(image)
                if self.transform is not None
                else image
            )

        elif isinstance(image, torch.Tensor):
            transformed = image

            if self.transform is not None:
                transformed = self.transform(transformed)

        else:
            raise TypeError(
                "frame_loader.load() must return a PIL image "
                "or torch.Tensor. "
                f"Got {type(image).__name__}."
            )

        if isinstance(transformed, Image.Image):
            tensor = self._to_tensor(transformed)

        elif isinstance(transformed, torch.Tensor):
            tensor = transformed

        else:
            raise TypeError(
                "The frame transform must return a PIL image "
                "or torch.Tensor. "
                f"Got {type(transformed).__name__}."
            )

        if tensor.ndim != 3:
            raise ValueError(
                "Expected transformed image with shape (C, H, W), "
                f"got {tuple(tensor.shape)}."
            )

        if not tensor.is_floating_point():
            tensor = tensor.float()

        if not torch.isfinite(tensor).all():
            raise ValueError(
                "Transformed frame contains non-finite values."
            )

        return tensor

    def _validate_feature(
        self,
        features: Any,
        feature_name: str,
        cache_path: Path,
    ) -> None:
        """Validate one cached visual feature tensor."""

        if not isinstance(features, torch.Tensor):
            raise TypeError(
                f"Invalid {feature_name} features in {cache_path}: "
                f"expected torch.Tensor, "
                f"got {type(features).__name__}."
            )

        if features.ndim != 2:
            raise ValueError(
                f"Invalid {feature_name} shape in {cache_path}: "
                f"expected 2 dimensions, "
                f"got {tuple(features.shape)}."
            )

        if (
            self.expected_num_tokens is not None
            and features.shape[0] != self.expected_num_tokens
        ):
            raise ValueError(
                f"Invalid {feature_name} token count in {cache_path}: "
                f"expected {self.expected_num_tokens}, "
                f"got {features.shape[0]}."
            )

        if (
            self.expected_feature_dim is not None
            and features.shape[1] != self.expected_feature_dim
        ):
            raise ValueError(
                f"Feature dimension mismatch in {cache_path} "
                f"for {feature_name}: "
                f"expected {self.expected_feature_dim}, "
                f"got {features.shape[1]}. "
                "The cache may belong to a different "
                "encoder configuration."
            )

        if not features.is_floating_point():
            raise TypeError(
                f"Invalid {feature_name} dtype in {cache_path}: "
                f"expected floating-point features, "
                f"got {features.dtype}."
            )

        if not torch.isfinite(features).all():
            raise ValueError(
                f"Non-finite values found in {feature_name} "
                f"features in {cache_path}."
            )

    def _load_cached_features(
        self,
        cache_path: Path,
    ) -> dict[str, Any]:
        """Load and validate one cached temporal feature sample."""

        if not cache_path.is_file():
            raise FileNotFoundError(
                f"Cached feature file not found: {cache_path}. "
                "Generate the feature cache first or select "
                "input_mode='raw_frames'."
            )

        cached = torch.load(
            cache_path,
            map_location="cpu",
            weights_only=True,
        )

        if not isinstance(cached, dict):
            raise TypeError(
                f"Invalid cache format in {cache_path}: "
                "expected a dictionary."
            )

        required_keys = {
            "before",
            "during",
            "after",
        }

        missing_keys = required_keys.difference(cached)

        if missing_keys:
            raise KeyError(
                f"Missing keys in feature cache {cache_path}: "
                f"{sorted(missing_keys)}."
            )

        self._validate_feature(
            cached["before"],
            "before",
            cache_path,
        )

        self._validate_feature(
            cached["after"],
            "after",
            cache_path,
        )

        during = cached["during"]

        if not isinstance(during, dict):
            raise TypeError(
                f"Invalid 'during' features in {cache_path}: "
                "expected a dictionary."
            )

        for frame_idx, features in during.items():
            self._validate_feature(
                features,
                f"during[{frame_idx}]",
                cache_path,
            )

        return cached

    def _load_raw_frames(
        self,
        sample: TemporalSample,
    ) -> dict[str, Any]:
        """Load all RGB frames belonging to a temporal sample."""

        during = {
            frame_idx: self._load_image(path)
            for frame_idx, path in sample.during_frames.items()
        }

        return {
            "before": self._load_image(
                sample.before_frame_path
            ),
            "during": during,
            "after": self._load_image(
                sample.after_frame_path
            ),
        }

    def _load_features(
        self,
        index: int,
    ) -> dict[str, Any]:
        """Load cached features for a sample index."""

        cache_path = (
            self.feature_dir
            / f"sample_{index}{self.cache_extension}"
        )

        return self._load_cached_features(cache_path)

    @staticmethod
    def _build_frame_paths(
        sample: TemporalSample,
    ) -> dict[str, Any]:
        """Preserve source image paths for all temporal frames."""

        return {
            "before": str(sample.before_frame_path),
            "during": {
                frame_idx: str(path)
                for frame_idx, path in sample.during_frames.items()
            },
            "after": str(sample.after_frame_path),
        }

    def __getitem__(
        self,
        index: int,
    ) -> dict[str, Any]:
        """Return one temporal sample with its annotations and paths."""

        if index < 0 or index >= len(self.samples):
            raise IndexError(
                f"Sample index out of range: {index}"
            )

        sample = self.samples[index]
        annotation = sample.annotation

        # Source paths are preserved independently of input mode.
        # This is necessary because cached-feature evaluation still
        # needs the original images for visual comparison reports.
        frame_paths = self._build_frame_paths(sample)

        if self.input_mode == "raw_frames":
            inputs = self._load_raw_frames(sample)
        else:
            inputs = self._load_features(index)

        frame_conversations = {
            key: annotation.frame_annotations[key].conversations
            for key in self.TEMPORAL_KEYS
            if key in annotation.frame_annotations
        }

        return {
            "before": inputs["before"],
            "during": inputs["during"],
            "after": inputs["after"],

            "annotation": annotation,

            "frame_indices": {
                "before": sample.before_frame_idx,
                "during": list(sample.during_frames.keys()),
                "after": sample.after_frame_idx,
            },

            "frame_paths": frame_paths,

            "state_descriptions": dict(
                annotation.state_descriptions
            ),

            "transition_description": (
                annotation.transition_description
            ),

            "object": annotation.object_name,
            "action": annotation.action_narration,

            "frame_conversations": frame_conversations,

            "transition_conversation": (
                annotation.transition_conversation
            ),
        }
