from __future__ import annotations

from pathlib import Path
from typing import Any

import torch
from torch.utils.data import Dataset

from src.sostd.data.temporal_dataset import TemporalDataset


class EvaluationDataset(Dataset):
    """Adapt the OSCaR temporal dataset for model evaluation."""

    def __init__(self, dataset: TemporalDataset) -> None:
        self.dataset = dataset

    def __len__(self) -> int:
        return len(self.dataset)

    @staticmethod
    def _select_during_frame(
        during: dict[int, torch.Tensor],
    ) -> tuple[int, torch.Tensor]:
        """Select the earliest during-frame feature tensor."""

        if not during:
            raise ValueError(
                "Evaluation sample must contain a during frame."
            )

        frame_index = sorted(during.keys())[0]
        return frame_index, during[frame_index]

    @staticmethod
    def _select_during_frame_path(
        during_paths: dict[int, str],
        frame_index: int,
    ) -> str:
        """Retrieve the path corresponding to the selected during frame."""

        if not during_paths:
            raise ValueError(
                "Evaluation sample must contain a during-frame image path."
            )

        if frame_index not in during_paths:
            raise KeyError(
                "Selected during-frame index "
                f"{frame_index} has no corresponding image path."
            )

        return str(during_paths[frame_index])

    @staticmethod
    def _validate_image_path(
        path: Any,
        name: str,
    ) -> str:
        """Validate and normalize an image path."""

        if not isinstance(path, (str, Path)):
            raise TypeError(
                f"{name} must be a string or pathlib.Path, "
                f"received {type(path).__name__}."
            )

        path = str(path)
        if not path:
            raise ValueError(f"{name} must not be empty.")

        return path

    @staticmethod
    def _validate_feature_tensor(
        tensor: torch.Tensor,
        name: str,
    ) -> None:
        """Validate one cached feature tensor with shape (N, D)."""

        if not isinstance(tensor, torch.Tensor):
            raise TypeError(f"{name} must be a torch.Tensor.")

        if tensor.ndim != 2:
            raise ValueError(
                f"{name} must have shape (N, D), "
                f"but received {tuple(tensor.shape)}."
            )

        if tensor.shape[0] < 1 or tensor.shape[1] < 1:
            raise ValueError(f"{name} must not be empty.")

        if not tensor.is_floating_point():
            raise TypeError(
                f"{name} must be floating-point, "
                f"received dtype {tensor.dtype}."
            )

        if not torch.isfinite(tensor).all():
            raise ValueError(
                f"{name} contains non-finite values (NaN or Inf)."
            )

    def __getitem__(self, index: int) -> dict[str, Any]:
        sample = self.dataset[index]

        required_keys = {
            "before",
            "during",
            "after",
            "annotation",
            "state_descriptions",
            "transition_description",
            "object",
            "action",
            "frame_indices",
            "frame_paths",
        }

        missing = required_keys - sample.keys()
        if missing:
            raise KeyError(
                f"Evaluation sample is missing fields: {sorted(missing)}"
            )

        # Select the same during-frame feature and image path.
        during_frame_index, during = self._select_during_frame(
            sample["during"]
        )

        before = sample["before"]
        after = sample["after"]

        self._validate_feature_tensor(before, "before")
        self._validate_feature_tensor(during, "during")
        self._validate_feature_tensor(after, "after")

        if before.shape != during.shape or before.shape != after.shape:
            raise ValueError(
                "Cached feature dimensions must match across temporal "
                "frames. Received before="
                f"{tuple(before.shape)}, "
                f"during={tuple(during.shape)}, "
                f"after={tuple(after.shape)}."
            )

        frames = torch.stack([before, during, after], dim=0)

        source_paths = sample["frame_paths"]
        if not isinstance(source_paths, dict):
            raise TypeError("frame_paths must be a dictionary.")

        image_paths = {
            "before": self._validate_image_path(
                source_paths["before"], "before image path"
            ),
            "during": self._select_during_frame_path(
                source_paths["during"], during_frame_index
            ),
            "after": self._validate_image_path(
                source_paths["after"], "after image path"
            ),
        }

        return {
            "frames": frames,
            "annotation": sample["annotation"],
            "state_descriptions": sample["state_descriptions"],
            "transition_description": sample["transition_description"],
            "object": sample["object"],
            "action": sample["action"],
            "frame_indices": sample["frame_indices"],
            "image_paths": image_paths,
        }


def evaluation_collate(
    samples: list[dict[str, Any]],
) -> dict[str, Any]:
    """Collate cached feature tensors and preserve metadata."""

    if not samples:
        raise ValueError("Cannot collate an empty batch.")

    frames = [sample["frames"] for sample in samples]

    for index, tensor in enumerate(frames):
        if not isinstance(tensor, torch.Tensor):
            raise TypeError(
                f"Sample {index} frames must be a tensor."
            )

        if tensor.ndim != 3 or tensor.shape[0] != 3:
            raise ValueError(
                f"Sample {index} must have feature shape (3, N, D); "
                f"received {tuple(tensor.shape)}."
            )

        if not tensor.is_floating_point():
            raise TypeError(
                f"Sample {index} frames must be floating-point."
            )

        if not torch.isfinite(tensor).all():
            raise ValueError(
                f"Sample {index} frames contain NaN or Inf."
            )

    try:
        batched_frames = torch.stack(frames, dim=0)
    except RuntimeError as exc:
        raise ValueError(
            "Evaluation samples have inconsistent cached feature "
            "dimensions. Check the DINOv2 feature cache."
        ) from exc

    metadata_keys = (
        "annotation",
        "state_descriptions",
        "transition_description",
        "object",
        "action",
        "frame_indices",
        "image_paths",
    )

    for index, sample in enumerate(samples):
        missing = set(metadata_keys) - sample.keys()
        if missing:
            raise KeyError(
                f"Sample {index} is missing metadata fields: "
                f"{sorted(missing)}"
            )

    return {
        "frames": batched_frames,
        **{
            key: [sample[key] for sample in samples]
            for key in metadata_keys
        },
    }
