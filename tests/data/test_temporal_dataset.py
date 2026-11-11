
from unittest.mock import Mock

import pytest
import torch
from PIL import Image

from src.sostd.data.annotation_parser import (
    OSCaRAnnotationParser,
)
from src.sostd.data.frame_loader import RGBFrameLoader
from src.sostd.data.temporal_dataset import TemporalDataset
from src.sostd.data.temporal_sample_builder import (
    TemporalSample,
    TemporalSampleBuilder,
)


@pytest.fixture
def annotation():
    parser = OSCaRAnnotationParser()

    clip_id = "P01_05_110"

    records = []

    for key, frame in [
        ("Frame_1", 23923),
        ("Frame_2", 23949),
        ("Frame_3", 23976),
        ("State_change_caption", None),
    ]:
        filename = (
            "state_change.jpg"
            if frame is None
            else f"frame_{frame}.jpg"
        )

        records.append({
            "image_path": (
                f"object-state-data/{clip_id}/{filename}"
            ),
            "caption_key": key,
            "caption_path": f"state-change-json/{clip_id}.json",
            "qa_path": f"question-answers-clean/{clip_id}.json",
            "conversation_path": (
                f"conversation-clean/{clip_id}.json"
            ),
            "object": "drawer",
            "action_narration": "open drawer",
        })

    frame_annotations = [
        parser.parse_record(record)
        for record in records
    ]

    state_change_json = {
        "Frame_1": "Drawer partially open.",
        "Frame_2": "Drawer further open.",
        "Frame_3": "Drawer fully extended.",
        "State_change_caption": (
            "The drawer progressively opens."
        ),
    }

    return parser.build_clip_annotation(
        frame_annotations,
        state_change_json,
    )


@pytest.fixture
def sample(annotation):
    return TemporalSampleBuilder.build_sample(annotation)


@pytest.fixture
def frame_loader():
    loader = Mock(spec=RGBFrameLoader)
    loader.load.return_value = Image.new("RGB", (32, 32))
    return loader


@pytest.fixture
def dataset(sample, frame_loader):
    return TemporalDataset([sample], frame_loader)


def test_dataset_length(dataset):
    assert len(dataset) == 1


def test_dataset_returns_expected_keys(dataset):
    item = dataset[0]

    assert set(item.keys()) == {
        "before",
        "during",
        "after",
        "annotation",
        "frame_indices",
        "frame_paths",
        "state_descriptions",
        "transition_description",
        "object",
        "action",
        "frame_conversations",
        "transition_conversation",
    }


def test_dataset_converts_frames_to_tensors(dataset):
    item = dataset[0]

    assert isinstance(item["before"], torch.Tensor)
    assert isinstance(item["after"], torch.Tensor)

    assert item["before"].shape == (3, 32, 32)
    assert item["after"].shape == (3, 32, 32)


def test_dataset_preserves_during_frames(dataset):
    item = dataset[0]

    assert list(item["during"].keys()) == [23949]

    assert all(
        isinstance(frame, torch.Tensor)
        for frame in item["during"].values()
    )


def test_dataset_preserves_annotation(dataset, sample):
    item = dataset[0]

    assert item["annotation"] is sample.annotation
    assert item["annotation"].object_name == "drawer"
    assert item["annotation"].action_narration == "open drawer"


def test_dataset_preserves_frame_indices(dataset):
    item = dataset[0]

    assert item["frame_indices"] == {
        "before": 23923,
        "during": [23949],
        "after": 23976,
    }


def test_dataset_preserves_frame_paths(dataset, sample):
    item = dataset[0]

    assert item["frame_paths"] == {
        "before": str(sample.before_frame_path),
        "during": {
            frame_idx: str(path)
            for frame_idx, path in sample.during_frames.items()
        },
        "after": str(sample.after_frame_path),
    }


def test_dataset_frame_paths_match_frame_indices(dataset):
    item = dataset[0]

    assert item["frame_paths"]["during"].keys() == (
        item["during"].keys()
    )

    assert item["frame_paths"]["before"]
    assert item["frame_paths"]["after"]


def test_dataset_exposes_state_descriptions(dataset):
    item = dataset[0]

    assert item["state_descriptions"] == {
        "Frame_1": "Drawer partially open.",
        "Frame_2": "Drawer further open.",
        "Frame_3": "Drawer fully extended.",
    }


def test_dataset_exposes_transition_description(dataset):
    item = dataset[0]

    assert item["transition_description"] == (
        "The drawer progressively opens."
    )


def test_dataset_exposes_object_and_action(dataset):
    item = dataset[0]

    assert item["object"] == "drawer"
    assert item["action"] == "open drawer"


def test_dataset_metadata_is_independent(dataset):
    first = dataset[0]
    first["state_descriptions"]["Frame_1"] = "Modified"

    second = dataset[0]

    assert second["state_descriptions"]["Frame_1"] == (
        "Drawer partially open."
    )


def test_dataset_loads_all_required_frames(
    dataset,
    frame_loader,
):
    dataset[0]

    assert frame_loader.load.call_count == 3


def test_dataset_supports_multiple_samples(
    sample,
    frame_loader,
):
    dataset = TemporalDataset(
        [sample, sample],
        frame_loader,
    )

    assert len(dataset) == 2
    assert dataset[0]["annotation"] is sample.annotation
    assert dataset[1]["annotation"] is sample.annotation


@pytest.mark.parametrize("index", [-1, 1, 5])
def test_dataset_rejects_invalid_index(dataset, index):
    with pytest.raises(IndexError):
        dataset[index]


def test_dataset_handles_empty_during_frames(
    annotation,
    frame_loader,
):
    sample = TemporalSample(
        annotation=annotation,
        before_frame_idx=23923,
        before_frame_path=(
            "object-state-data/P01_05_110/frame_23923.jpg"
        ),
        during_frames={},
        after_frame_idx=23976,
        after_frame_path=(
            "object-state-data/P01_05_110/frame_23976.jpg"
        ),
    )

    dataset = TemporalDataset([sample], frame_loader)

    item = dataset[0]

    assert item["during"] == {}
    assert item["frame_indices"]["during"] == []
    assert item["frame_paths"]["during"] == {}
