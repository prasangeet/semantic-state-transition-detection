
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable

import torch


FRAME_ORDER = ("Frame_1", "Frame_2", "Frame_3")
IGNORE_INDEX = -100

METADATA_KEYS = (
    "annotation",
    "frame_indices",
    "state_descriptions",
    "transition_description",
    "object",
    "action",
    "frame_conversations",
    "transition_conversation",
)


def temporal_collate_fn(
    batch: list[dict[str, Any]],
) -> dict[str, Any]:
    """Collate temporal samples while preserving variable-length fields."""

    if not batch:
        raise ValueError("Cannot collate an empty batch.")

    required_keys = (
        "before",
        "during",
        "after",
        *METADATA_KEYS,
    )

    for index, sample in enumerate(batch):
        if not isinstance(sample, dict):
            raise TypeError(f"Sample {index} must be a dictionary.")

        for key in required_keys:
            if key not in sample:
                raise KeyError(
                    f"Sample {index} is missing required key: {key}"
                )

    return {
        key: [sample[key] for sample in batch]
        for key in (
            "before",
            "during",
            "after",
            *METADATA_KEYS,
        )
    }


class CaptioningCollator:
    """Collate OSCaR temporal samples for V3 and V4 training.

    Visual input:
      - Raw RGB: (C, H, W)
      - Cached features: (N, D)

    Output visual tensor:
      - Raw RGB: (B, 3, C, H, W)
      - Cached features: (B, 3, N, D)

    Object classification is optional. When object_to_idx is omitted,
    the output remains compatible with the original V3 collator.
    """

    def __init__(
        self,
        tokenizer: Callable[..., Any],
        max_state_length: int | None = None,
        max_transition_length: int | None = None,
        object_to_idx: Mapping[str, int] | None = None,
    ) -> None:
        if not callable(tokenizer):
            raise TypeError("tokenizer must be callable.")

        self.tokenizer = tokenizer
        self.max_state_length = max_state_length
        self.max_transition_length = max_transition_length

        for name, length in (
            ("max_state_length", max_state_length),
            ("max_transition_length", max_transition_length),
        ):
            if length is not None and length <= 0:
                raise ValueError(f"{name} must be positive.")

        self.object_to_idx: dict[str, int] | None = None

        if object_to_idx is not None:
            if not isinstance(object_to_idx, Mapping):
                raise TypeError("object_to_idx must be a mapping.")

            if not object_to_idx:
                raise ValueError("object_to_idx cannot be empty.")

            normalized_mapping: dict[str, int] = {}

            for label, index in object_to_idx.items():
                if not isinstance(label, str) or not label.strip():
                    raise ValueError(
                        "Object vocabulary labels must be non-empty strings."
                    )

                if isinstance(index, bool) or not isinstance(index, int):
                    raise TypeError(
                        f"Class index for {label!r} must be an integer."
                    )

                if index < 0:
                    raise ValueError(
                        f"Class index for {label!r} cannot be negative."
                    )

                normalized_label = label.strip()

                if normalized_label in normalized_mapping:
                    raise ValueError(
                        f"Duplicate normalized object label: "
                        f"{normalized_label!r}."
                    )

                normalized_mapping[normalized_label] = index

            indices = sorted(normalized_mapping.values())

            if indices != list(range(len(indices))):
                raise ValueError(
                    "Object class indices must be contiguous, "
                    "unique, and start at zero."
                )

            self.object_to_idx = normalized_mapping

    def _tokenize(
        self,
        texts: list[str],
        max_length: int | None,
    ) -> torch.Tensor:
        """Tokenize text and convert padding IDs to the ignore index."""

        if not texts:
            raise ValueError("Cannot tokenize an empty list of captions.")

        encoded = self.tokenizer(
            texts,
            padding=True,
            truncation=max_length is not None,
            max_length=max_length,
            return_tensors="pt",
        )

        if not isinstance(encoded, Mapping):
            raise TypeError(
                "Tokenizer output must be a mapping containing 'input_ids'; "
                f"received {type(encoded).__name__}."
            )

        if "input_ids" not in encoded:
            raise KeyError(
                "Tokenizer output must be a mapping containing 'input_ids'."
            )

        input_ids = encoded["input_ids"]

        if not isinstance(input_ids, torch.Tensor):
            input_ids = torch.as_tensor(input_ids)

        if input_ids.ndim != 2:
            raise ValueError(
                "Tokenizer input_ids must have shape (batch, sequence); "
                f"received {tuple(input_ids.shape)}."
            )

        if input_ids.shape[0] != len(texts):
            raise ValueError(
                "Tokenizer returned an unexpected batch size: "
                f"expected {len(texts)}, received {input_ids.shape[0]}."
            )

        labels = input_ids.clone().long()
        pad_token_id = getattr(self.tokenizer, "pad_token_id", None)

        if pad_token_id is not None:
            labels[labels == int(pad_token_id)] = IGNORE_INDEX

        return labels

    @staticmethod
    def _validate_frame(
        frame: Any,
        frame_name: str,
    ) -> torch.Tensor:
        """Validate one raw RGB frame or cached feature tensor."""

        if not isinstance(frame, torch.Tensor):
            raise TypeError(
                f"frames must be tensors; {frame_name} is "
                f"{type(frame).__name__}."
            )

        if frame.ndim not in (2, 3):
            raise ValueError(
                f"Invalid feature shape for {frame_name}: expected "
                "(N, D) cached features or (C, H, W) RGB frames; "
                f"received {tuple(frame.shape)}."
            )

        if not frame.is_floating_point():
            raise TypeError(
                f"{frame_name} must have a floating-point dtype; "
                f"received {frame.dtype}."
            )

        if not torch.isfinite(frame).all():
            raise ValueError(
                f"{frame_name} contains non-finite values."
            )

        return frame

    def _build_frame_sequence(
        self,
        sample: dict[str, Any],
    ) -> torch.Tensor:
        """Return the ordered before, during, after frame tensor."""

        for key in ("before", "during", "after"):
            if key not in sample:
                raise KeyError(f"Sample is missing required key: {key}")

        during = sample["during"]

        if not isinstance(during, dict):
            raise TypeError(
                "'during' must be a dictionary of frame tensors."
            )

        if len(during) != 1:
            raise ValueError(
                "OSCaR captioning requires exactly one during-frame "
                f"per sample; received {len(during)}."
            )

        during_frame = next(iter(during.values()))

        frames = [
            self._validate_frame(sample["before"], "before"),
            self._validate_frame(during_frame, "during"),
            self._validate_frame(sample["after"], "after"),
        ]

        reference_shape = frames[0].shape
        reference_dtype = frames[0].dtype
        reference_rank = frames[0].ndim

        for frame_name, frame in zip(("during", "after"), frames[1:]):
            if frame.ndim != reference_rank:
                raise ValueError(
                    "All temporal inputs must use the same feature shape "
                    "representation (all cached features or all RGB frames). "
                    f"before has {reference_rank} dimensions, "
                    f"{frame_name} has {frame.ndim} dimensions."
                )

            if frame.shape != reference_shape:
                raise ValueError(
                    "All three temporal inputs must have matching shapes. "
                    f"before has {tuple(reference_shape)}, "
                    f"{frame_name} has {tuple(frame.shape)}."
                )

            if frame.dtype != reference_dtype:
                raise ValueError(
                    "All three temporal inputs must have matching dtypes. "
                    f"before has {reference_dtype}, "
                    f"{frame_name} has {frame.dtype}."
                )

        return torch.stack(frames, dim=0)

    def _build_state_labels(
        self,
        batch: list[dict[str, Any]],
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Build state captions and a (B, 3) validity mask."""

        batch_size = len(batch)

        state_mask = torch.zeros(
            (batch_size, len(FRAME_ORDER)),
            dtype=torch.bool,
        )

        targets: list[str] = []
        positions: list[tuple[int, int]] = []

        for batch_index, sample in enumerate(batch):
            if "state_descriptions" not in sample:
                raise KeyError(
                    "Sample is missing required key: state_descriptions"
                )

            descriptions = sample["state_descriptions"]

            if not isinstance(descriptions, dict):
                raise TypeError(
                    "'state_descriptions' must be a dictionary."
                )

            for frame_index, frame_key in enumerate(FRAME_ORDER):
                description = descriptions.get(frame_key)

                if description is None:
                    continue

                if not isinstance(description, str):
                    raise TypeError(
                        f"State description for {frame_key} must be a string."
                    )

                description = description.strip()

                if not description:
                    continue

                state_mask[batch_index, frame_index] = True
                targets.append(description)
                positions.append((batch_index, frame_index))

        if not targets:
            return (
                torch.full(
                    (batch_size, len(FRAME_ORDER), 1),
                    IGNORE_INDEX,
                    dtype=torch.long,
                ),
                state_mask,
            )

        tokenized = self._tokenize(
            targets,
            self.max_state_length,
        )

        state_labels = torch.full(
            (
                batch_size,
                len(FRAME_ORDER),
                tokenized.shape[1],
            ),
            IGNORE_INDEX,
            dtype=torch.long,
        )

        for target_index, (batch_index, frame_index) in enumerate(positions):
            state_labels[batch_index, frame_index] = tokenized[target_index]

        return state_labels, state_mask

    def _build_transition_labels(
        self,
        batch: list[dict[str, Any]],
    ) -> torch.Tensor:
        """Build one transition caption per video."""

        targets: list[str] = []

        for sample in batch:
            if "transition_description" not in sample:
                raise KeyError(
                    "Sample is missing required key: transition_description"
                )

            transition = sample["transition_description"]

            if not isinstance(transition, str):
                raise TypeError(
                    "Transition description must be a string."
                )

            transition = transition.strip()

            if not transition:
                raise ValueError(
                    "Every sample must have a non-empty "
                    "transition description."
                )

            targets.append(transition)

        return self._tokenize(
            targets,
            self.max_transition_length,
        )

    def _build_object_labels(
        self,
        batch: list[dict[str, Any]],
    ) -> torch.Tensor:
        """Build clip-level object class IDs.

        Labels absent from the training vocabulary receive IGNORE_INDEX.
        """

        if self.object_to_idx is None:
            raise RuntimeError(
                "Object vocabulary is required to build object labels."
            )

        labels: list[int] = []

        for sample_index, sample in enumerate(batch):
            label = sample.get("object")

            if not isinstance(label, str) or not label.strip():
                labels.append(IGNORE_INDEX)
                continue

            labels.append(
                self.object_to_idx.get(
                    label.strip(),
                    IGNORE_INDEX,
                )
            )

        return torch.tensor(labels, dtype=torch.long)

    def __call__(
        self,
        batch: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Collate visual inputs, caption labels, and optional object labels."""

        if not batch:
            raise ValueError("Cannot collate an empty batch.")

        for index, sample in enumerate(batch):
            if not isinstance(sample, dict):
                raise TypeError(
                    f"Sample {index} must be a dictionary."
                )

            for key in METADATA_KEYS:
                if key not in sample:
                    raise KeyError(
                        f"Sample {index} is missing required key: {key}"
                    )

        frame_sequences = [
            self._build_frame_sequence(sample)
            for sample in batch
        ]

        reference_shape = frame_sequences[0].shape
        reference_dtype = frame_sequences[0].dtype

        for sample_index, frames in enumerate(frame_sequences[1:], start=1):
            if frames.shape != reference_shape:
                raise ValueError(
                    "All samples in a batch must have identical visual "
                    "input shapes. "
                    f"Sample 0 has {tuple(reference_shape)}, "
                    f"sample {sample_index} has {tuple(frames.shape)}."
                )

            if frames.dtype != reference_dtype:
                raise ValueError(
                    "All samples in a batch must have identical "
                    "visual input dtypes."
                )

        visual_batch = torch.stack(frame_sequences, dim=0)

        state_labels, state_mask = self._build_state_labels(batch)
        transition_labels = self._build_transition_labels(batch)

        result: dict[str, Any] = {
            "frames": visual_batch,
            "state_labels": state_labels,
            "state_mask": state_mask,
            "transition_labels": transition_labels,
        }

        # Preserve all original metadata for both V3 and V4.
        for key in METADATA_KEYS:
            result[key] = [sample[key] for sample in batch]

        # V4-only output. V3 receives no additional keys.
        if self.object_to_idx is not None:
            result["object_labels"] = self._build_object_labels(batch)

        return result
