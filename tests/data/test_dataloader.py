
from unittest.mock import Mock, patch

import pytest
import torch
from torch.utils.data import DataLoader, Dataset

from src.sostd.data.dataloader import create_temporal_dataloader


class DummyTemporalDataset(Dataset):
    def __init__(self, size=4):
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return {
            "before": torch.zeros(3, 8, 8),
            "during": {},
            "after": torch.ones(3, 8, 8),
            "annotation": f"annotation-{index}",
            "frame_indices": {
                "before": index,
                "during": [],
                "after": index + 2,
            },
            "state_descriptions": {
                "Frame_1": "Before state",
                "Frame_2": "During state",
                "Frame_3": "After state",
            },
            "transition_description": "An object changes state.",
            "object": "drawer",
            "action": "open drawer",
            "frame_conversations": {
                "Frame_1": (),
                "Frame_2": (),
                "Frame_3": (),
            },
            "transition_conversation": (),
        }


@pytest.fixture
def dataset_and_report():
    return DummyTemporalDataset(), {"clips_built": 4}


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_returns_dataloader_and_report(
    mock_build,
    dataset_and_report,
):
    dataset, report = dataset_and_report
    mock_build.return_value = (dataset, report)

    dataloader, returned_report = create_temporal_dataloader()

    assert isinstance(dataloader, DataLoader)
    assert returned_report is report
    mock_build.assert_called_once_with(split="validation")


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_passes_split(mock_build, dataset_and_report):
    mock_build.return_value = dataset_and_report

    create_temporal_dataloader(split="val")

    mock_build.assert_called_once_with(split="val")


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"batch_size": 0}, "batch_size must be at least 1"),
        ({"batch_size": -1}, "batch_size must be at least 1"),
        ({"num_workers": -1}, "num_workers cannot be negative"),
    ],
)
def test_create_dataloader_rejects_invalid_arguments(kwargs, message):
    with pytest.raises(ValueError, match=message):
        create_temporal_dataloader(**kwargs)


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_respects_batch_size(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader(batch_size=2)

    assert dataloader.batch_size == 2
    assert len(list(dataloader)) == 2


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_uses_temporal_collator(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader(batch_size=2)

    batch = next(iter(dataloader))

    assert set(batch) == {
        "before",
        "during",
        "after",
        "annotation",
        "frame_indices",
        "state_descriptions",
        "transition_description",
        "object",
        "action",
        "frame_conversations",
        "transition_conversation",
    }

    assert len(batch["before"]) == 2
    assert len(batch["transition_description"]) == 2


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_supports_pin_memory(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader(pin_memory=True)

    assert dataloader.pin_memory is True


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_supports_worker_configuration(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader(num_workers=1)

    assert dataloader.num_workers == 1
    assert dataloader.persistent_workers is True


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_does_not_shuffle_by_default(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader()

    assert dataloader.sampler.__class__.__name__ == "SequentialSampler"


@patch("src.sostd.data.dataloader.build_temporal_dataset")
def test_create_dataloader_supports_shuffle(
    mock_build,
    dataset_and_report,
):
    mock_build.return_value = dataset_and_report

    dataloader, _ = create_temporal_dataloader(shuffle=True)

    assert dataloader.sampler.__class__.__name__ == "RandomSampler"
