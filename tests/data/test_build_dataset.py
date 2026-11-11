
from unittest.mock import Mock, patch

import pytest

from src.sostd.data.build_dataset import (
    TemporalDatasetBuildResult,
    build_temporal_dataset,
)
from src.sostd.data.temporal_dataset import TemporalDataset


@pytest.fixture
def validation_records():
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

    return records


@pytest.fixture
def state_change_json():
    return {
        "Frame_1": "Drawer partially open.",
        "Frame_2": "Drawer further open.",
        "Frame_3": "Drawer fully extended.",
        "State_change_caption": (
            "The drawer progressively opens."
        ),
    }


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_temporal_dataset(
    mock_loader_class,
    mock_frame_loader_class,
    validation_records,
    state_change_json,
):
    loader = mock_loader_class.return_value
    loader.hf_token = "test-token"
    loader.load.return_value = None
    loader.get_split.return_value = validation_records
    loader.load_original_annotations.return_value = state_change_json

    frame_loader = mock_frame_loader_class.return_value

    dataset, result = build_temporal_dataset()

    assert isinstance(dataset, TemporalDataset)
    assert isinstance(result, TemporalDatasetBuildResult)

    assert len(dataset) == 1
    assert result.clips_seen == 1
    assert result.clips_built == 1
    assert len(result.samples) == 1

    loader.load.assert_called_once()
    loader.get_split.assert_called_once_with("validation")

    loader.load_original_annotations.assert_called_once_with(
        "P01_05_110.json",
        annotation_type="state-change-json",
    )

    mock_frame_loader_class.assert_called_once_with(
        token="test-token"
    )

    assert dataset.frame_loader is frame_loader


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_temporal_dataset_accepts_val_alias(
    mock_loader_class,
    mock_frame_loader_class,
    validation_records,
    state_change_json,
):
    loader = mock_loader_class.return_value
    loader.hf_token = "test-token"
    loader.get_split.return_value = validation_records
    loader.load_original_annotations.return_value = state_change_json

    dataset, result = build_temporal_dataset(split="val")

    loader.get_split.assert_called_once_with("validation")
    assert len(dataset) == 1
    assert result.clips_built == 1


@pytest.mark.parametrize("split", ["test", "invalid"])
def test_build_temporal_dataset_rejects_unsupported_splits(split):
    with pytest.raises(ValueError, match="Unsupported split"):
        build_temporal_dataset(split=split)


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_temporal_dataset_groups_records_by_clip(
    mock_loader_class,
    mock_frame_loader_class,
    validation_records,
    state_change_json,
):
    second_clip_records = []

    for record in validation_records:
        copied = dict(record)
        copied["image_path"] = copied["image_path"].replace(
            "P01_05_110",
            "P01_05_111",
        )
        copied["caption_path"] = copied["caption_path"].replace(
            "P01_05_110",
            "P01_05_111",
        )
        copied["qa_path"] = copied["qa_path"].replace(
            "P01_05_110",
            "P01_05_111",
        )
        copied["conversation_path"] = copied[
            "conversation_path"
        ].replace("P01_05_110", "P01_05_111")

        second_clip_records.append(copied)

    loader = mock_loader_class.return_value
    loader.hf_token = "test-token"
    loader.get_split.return_value = (
        validation_records + second_clip_records
    )
    loader.load_original_annotations.return_value = state_change_json

    dataset, result = build_temporal_dataset()

    assert len(dataset) == 2
    assert result.clips_seen == 2
    assert result.clips_built == 2

    assert loader.load_original_annotations.call_count == 2



@pytest.fixture
def training_records_and_metadata():
    clip_id = "P01_109_402"

    examples = [
        ("frame_70172.jpg", "Frame_1", "Salt is falling."),
        ("frame_70190.jpg", "Frame_2", "Salt is falling densely."),
        ("frame_70209.jpg", "Frame_3", "Salt has landed."),
        (
            "state_change.jpg",
            "State_change_caption",
            "Salt transitions from falling to settled.",
        ),
    ]

    records = []
    metadata = []

    for filename, caption_key, description in examples:
        image_path = (
            f"object-state-data/{clip_id}/{filename}"
        )

        records.append({
            "image": image_path,
            "conversations": [
                {
                    "from": "human",
                    "value": "<image>\nDescribe state of salt",
                },
                {
                    "from": "gpt",
                    "value": description,
                },
                {
                    "from": "human",
                    "value": "What is happening?",
                },
                {
                    "from": "gpt",
                    "value": "Salt is being sprinkled.",
                },
            ],
        })

        metadata.append({
            "image_path": image_path,
            "caption_key": caption_key,
            "caption_path": f"state-change-json/{clip_id}.json",
            "qa_path": f"question-answers-clean/{clip_id}.json",
            "conversation_path": f"conversation-clean/{clip_id}.json",
            "object": "salt",
            "action_narration": "sprinkle salt",
        })

    return records, metadata


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_training_temporal_dataset(
    mock_loader_class,
    mock_frame_loader_class,
    training_records_and_metadata,
):
    records, metadata = training_records_and_metadata

    loader = mock_loader_class.return_value
    loader.hf_token = "test-token"
    loader.load.return_value = None
    loader.get_split.return_value = records
    loader.load_metadata.return_value = metadata

    dataset, result = build_temporal_dataset(split="train")

    assert isinstance(dataset, TemporalDataset)
    assert isinstance(result, TemporalDatasetBuildResult)

    assert len(dataset) == 1
    assert result.clips_seen == 1
    assert result.clips_built == 1

    loader.load.assert_called_once()
    loader.get_split.assert_called_once_with("train")
    loader.load_metadata.assert_called_once()

    mock_frame_loader_class.assert_called_once_with(
        token="test-token"
    )

    annotation = result.samples[0].annotation

    assert annotation.clip_id == "P01_109_402"
    assert annotation.object_name == "salt"
    assert annotation.action_narration == "sprinkle salt"

    assert annotation.transition_description == (
        "Salt transitions from falling to settled."
    )

    assert len(annotation.transition_conversation) == 4


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_training_dataset_rejects_missing_metadata(
    mock_loader_class,
    mock_frame_loader_class,
    training_records_and_metadata,
):
    records, metadata = training_records_and_metadata

    loader = mock_loader_class.return_value
    loader.load.return_value = None
    loader.get_split.return_value = records
    loader.load_metadata.return_value = metadata[:-1]

    with pytest.raises(
        ValueError,
        match="Training metadata not found",
    ):
        build_temporal_dataset(split="train")


@patch("src.sostd.data.build_dataset.RGBFrameLoader")
@patch("src.sostd.data.build_dataset.DatasetLoader")
def test_build_training_dataset_rejects_duplicate_metadata(
    mock_loader_class,
    mock_frame_loader_class,
    training_records_and_metadata,
):
    records, metadata = training_records_and_metadata

    loader = mock_loader_class.return_value
    loader.load.return_value = None
    loader.get_split.return_value = records
    loader.load_metadata.return_value = metadata + [metadata[0]]

    with pytest.raises(
        ValueError,
        match="Duplicate image path",
    ):
        build_temporal_dataset(split="train")
