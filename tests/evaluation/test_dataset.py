
from __future__ import annotations

from unittest.mock import MagicMock

import pytest
import torch

from src.sostd.evaluation.dataset import (
    EvaluationDataset,
    evaluation_collate,
)


FEATURE_SHAPE = (257, 384)


class MockTemporalDataset:
    """Minimal stand-in for TemporalDataset."""

    def __init__(self, samples: list[dict]) -> None:
        self.samples = samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int) -> dict:
        return self.samples[index]


def make_features(
    value: float = 0.0,
    shape: tuple[int, int] = FEATURE_SHAPE,
) -> torch.Tensor:
    return torch.full(shape, value, dtype=torch.float32)


def make_sample(
    during: dict[int, torch.Tensor] | None = None,
    feature_shape: tuple[int, int] = FEATURE_SHAPE,
) -> dict:
    if during is None:
        during = {20: make_features(0.2, feature_shape)}

    annotation = MagicMock()
    annotation.clip_id = "test_clip_001"

    return {
        "before": make_features(0.1, feature_shape),
        "during": during,
        "after": make_features(0.3, feature_shape),
        "annotation": annotation,
        "state_descriptions": {
            "Frame_1": "The drawer is closed.",
            "Frame_2": "The drawer is partially open.",
            "Frame_3": "The drawer is fully open.",
        },
        "transition_description": "The drawer gradually opens.",
        "object": "drawer",
        "action": "open drawer",
        "frame_indices": {
            "before": 10,
            "during": list(during.keys()),
            "after": 40,
        },
        "frame_paths": {
            "before": "/dataset/test_clip_001/frame_10.png",
            "during": {
                frame_index: (
                    f"/dataset/test_clip_001/frame_{frame_index}.png"
                )
                for frame_index in during
            },
            "after": "/dataset/test_clip_001/frame_40.png",
        },
    }


@pytest.fixture
def evaluation_dataset():
    return EvaluationDataset(
        MockTemporalDataset([
            make_sample(),
            make_sample(),
        ])
    )


def test_dataset_length(evaluation_dataset):
    assert len(evaluation_dataset) == 2


def test_dataset_frame_order(evaluation_dataset):
    sample = evaluation_dataset[0]

    assert sample["frames"].shape == (3, *FEATURE_SHAPE)
    assert torch.allclose(sample["frames"][0], make_features(0.1))
    assert torch.allclose(sample["frames"][1], make_features(0.2))
    assert torch.allclose(sample["frames"][2], make_features(0.3))


def test_selects_first_during_frame():
    sample = make_sample(
        during={
            30: make_features(0.3),
            20: make_features(0.2),
        }
    )

    dataset = EvaluationDataset(MockTemporalDataset([sample]))
    result = dataset[0]

    assert torch.allclose(result["frames"][1], make_features(0.2))


def test_selects_matching_during_image_path():
    sample = make_sample(
        during={
            30: make_features(0.3),
            20: make_features(0.2),
        }
    )

    dataset = EvaluationDataset(MockTemporalDataset([sample]))
    result = dataset[0]

    assert result["image_paths"]["during"] == (
        "/dataset/test_clip_001/frame_20.png"
    )


def test_preserves_all_image_paths(evaluation_dataset):
    sample = evaluation_dataset[0]

    assert sample["image_paths"] == {
        "before": "/dataset/test_clip_001/frame_10.png",
        "during": "/dataset/test_clip_001/frame_20.png",
        "after": "/dataset/test_clip_001/frame_40.png",
    }


def test_rejects_empty_during_frames():
    dataset = EvaluationDataset(
        MockTemporalDataset([make_sample(during={})])
    )

    with pytest.raises(ValueError, match="during frame"):
        dataset[0]


def test_preserves_ground_truth(evaluation_dataset):
    sample = evaluation_dataset[0]

    assert sample["state_descriptions"] == {
        "Frame_1": "The drawer is closed.",
        "Frame_2": "The drawer is partially open.",
        "Frame_3": "The drawer is fully open.",
    }
    assert sample["transition_description"] == (
        "The drawer gradually opens."
    )


def test_preserves_metadata(evaluation_dataset):
    sample = evaluation_dataset[0]

    assert sample["object"] == "drawer"
    assert sample["action"] == "open drawer"
    assert sample["frame_indices"] == {
        "before": 10,
        "during": [20],
        "after": 40,
    }
    assert sample["annotation"].clip_id == "test_clip_001"


def test_rejects_non_tensor_features():
    sample = make_sample()
    sample["before"] = [
        [0.0] * FEATURE_SHAPE[1]
        for _ in range(FEATURE_SHAPE[0])
    ]

    dataset = EvaluationDataset(MockTemporalDataset([sample]))

    with pytest.raises(TypeError, match="before"):
        dataset[0]


def test_rejects_invalid_feature_dimensions():
    sample = make_sample()
    sample["before"] = torch.zeros(384)

    dataset = EvaluationDataset(MockTemporalDataset([sample]))

    with pytest.raises(ValueError, match="before"):
        dataset[0]


def test_rejects_inconsistent_temporal_feature_dimensions():
    sample = make_sample()
    sample["after"] = torch.zeros(256, 384)

    dataset = EvaluationDataset(MockTemporalDataset([sample]))

    with pytest.raises(ValueError, match="dimensions must match"):
        dataset[0]


def test_collate_batch():
    dataset = EvaluationDataset(
        MockTemporalDataset([
            make_sample(),
            make_sample(),
        ])
    )

    batch = evaluation_collate([
        dataset[0],
        dataset[1],
    ])

    assert batch["frames"].shape == (2, 3, *FEATURE_SHAPE)
    assert batch["frames"].dtype == torch.float32


def test_collate_preserves_annotations():
    dataset = EvaluationDataset(
        MockTemporalDataset([make_sample()])
    )

    batch = evaluation_collate([dataset[0]])

    assert len(batch["annotation"]) == 1
    assert batch["annotation"][0].clip_id == "test_clip_001"
    assert batch["state_descriptions"][0]["Frame_1"] == (
        "The drawer is closed."
    )
    assert batch["transition_description"][0] == (
        "The drawer gradually opens."
    )


def test_collate_preserves_image_paths():
    dataset = EvaluationDataset(
        MockTemporalDataset([
            make_sample(),
            make_sample(),
        ])
    )

    batch = evaluation_collate([
        dataset[0],
        dataset[1],
    ])

    assert len(batch["image_paths"]) == 2
    assert batch["image_paths"][0]["before"].endswith("frame_10.png")
    assert batch["image_paths"][0]["during"].endswith("frame_20.png")
    assert batch["image_paths"][0]["after"].endswith("frame_40.png")


def test_collate_rejects_empty_batch():
    with pytest.raises(ValueError, match="empty"):
        evaluation_collate([])


def test_collate_rejects_inconsistent_dimensions():
    first = make_sample(feature_shape=(257, 384))
    second = make_sample(feature_shape=(256, 384))

    first_dataset = EvaluationDataset(
        MockTemporalDataset([first])
    )
    first_item = first_dataset[0]

    second_item = {
        "frames": torch.stack([
            second["before"],
            second["during"][20],
            second["after"],
        ]),
        **{
            key: second[key]
            for key in (
                "annotation",
                "state_descriptions",
                "transition_description",
                "object",
                "action",
                "frame_indices",
                "frame_paths",
            )
        },
        "image_paths": {
            "before": second["frame_paths"]["before"],
            "during": second["frame_paths"]["during"][20],
            "after": second["frame_paths"]["after"],
        },
    }

    with pytest.raises(
        ValueError,
        match="inconsistent cached feature",
    ):
        evaluation_collate([first_item, second_item])


def test_collate_rejects_invalid_sample_shape():
    sample = make_sample()
    sample["frames"] = torch.zeros(3, 384)

    with pytest.raises(ValueError, match="feature shape"):
        evaluation_collate([sample])
