
from __future__ import annotations

from dataclasses import replace

import pytest
import torch
from torch import nn

from src.sostd.evaluation.config import EvaluationConfig
from src.sostd.evaluation.evaluation_runner import EvaluationRunner


class FakeDataset:
    """Minimal stand-in for the temporal evaluation dataset."""

    def __init__(self, size: int = 3):
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return {
            "before": torch.rand(257, 384),
            "during": {
                2: torch.rand(257, 384),
            },
            "after": torch.rand(257, 384),
            "annotation": None,
            "state_descriptions": {
                "Frame_1": f"Before {index}",
                "Frame_2": f"During {index}",
                "Frame_3": f"After {index}",
            },
            "transition_description": f"Transition {index}",
            "object": "drawer",
            "action": "open",
            "frame_indices": {
                "before": 1,
                "during": [2],
                "after": 3,
            },
            "frame_paths": {
                "before": f"/dataset/sample_{index}/before.png",
                "during": {
                    2: f"/dataset/sample_{index}/during.png",
                },
                "after": f"/dataset/sample_{index}/after.png",
            },
        }


class FakeModel(nn.Module):
    """Minimal PyTorch model accepted by EvaluationRunner."""

    def __init__(self):
        super().__init__()
        self.dummy = nn.Parameter(torch.zeros(1))


class FakeModelLoader:
    def __init__(self, checkpoint, device):
        self.checkpoint = checkpoint
        self.device = device

    def load(self):
        return FakeModel()


class FakeInferenceRunner:
    def __init__(self, model, tokenizer, **kwargs):
        self.model = model
        self.tokenizer = tokenizer

    def run_batch(self, frames):
        return [
            {
                "before": "Predicted before",
                "during": "Predicted during",
                "after": "Predicted after",
                "transition": "Predicted transition",
            }
            for _ in range(frames.shape[0])
        ]


@pytest.fixture
def config(tmp_path):
    return EvaluationConfig(
        checkpoint=tmp_path / "best.pt",
        output_dir=tmp_path / "evaluation",
        split="validation",
        batch_size=2,
        num_workers=0,
        pin_memory=False,
        device="cpu",
        amp=False,
        limit=None,
    )


def make_runner(config, dataset_size=3):
    def dataset_builder(**kwargs):
        return FakeDataset(dataset_size), None

    return EvaluationRunner(
        config=config,
        dataset_builder=dataset_builder,
        model_loader_factory=FakeModelLoader,
        tokenizer_loader=lambda name: f"tokenizer:{name}",
        inference_runner_factory=FakeInferenceRunner,
    )


def test_run_collects_predictions_and_references(config):
    result = make_runner(config).run()

    assert result["num_samples"] == 3
    assert len(result["predictions"]) == 3
    assert len(result["references"]) == 3

    assert result["predictions"][0]["before"] == "Predicted before"
    assert result["references"][0]["before"] == "Before 0"
    assert result["references"][0]["transition"] == "Transition 0"


def test_run_preserves_metadata(config):
    result = make_runner(config).run()

    assert result["metadata"][0] == {
        "object": "drawer",
        "action": "open",
        "frame_indices": {
            "before": 1,
            "during": [2],
            "after": 3,
        },
        "image_paths": {
            "before": "/dataset/sample_0/before.png",
            "during": "/dataset/sample_0/during.png",
            "after": "/dataset/sample_0/after.png",
        },
    }


def test_run_preserves_image_paths_for_all_samples(config):
    result = make_runner(config).run()

    assert len(result["metadata"]) == 3

    for index, metadata in enumerate(result["metadata"]):
        assert metadata["image_paths"]["before"] == (
            f"/dataset/sample_{index}/before.png"
        )
        assert metadata["image_paths"]["during"] == (
            f"/dataset/sample_{index}/during.png"
        )
        assert metadata["image_paths"]["after"] == (
            f"/dataset/sample_{index}/after.png"
        )


def test_run_respects_sample_limit(config):
    limited_config = replace(config, limit=2)

    result = make_runner(limited_config).run()

    assert result["num_samples"] == 2
    assert len(result["metadata"]) == 2


def test_run_rejects_empty_dataset(config):
    runner = make_runner(config, dataset_size=0)

    with pytest.raises(ValueError, match="dataset is empty"):
        runner.run()


def test_load_tokenizer_uses_configured_name(config):
    loaded_names = []

    runner = EvaluationRunner(
        config=config,
        tokenizer_loader=lambda name: (
            loaded_names.append(name) or "tokenizer"
        ),
    )

    assert runner._load_tokenizer() == "tokenizer"
    assert loaded_names == [config.tokenizer_name]


def test_build_dataloader_uses_configured_batch_size(config):
    runner = make_runner(config)

    dataloader = runner._build_dataloader()

    assert dataloader.batch_size == 2
    assert dataloader.num_workers == 0
    assert dataloader.pin_memory is False


def test_build_dataloader_preserves_image_paths(config):
    runner = make_runner(config)

    dataloader = runner._build_dataloader()
    batch = next(iter(dataloader))

    assert len(batch["image_paths"]) == 2
    assert batch["image_paths"][0]["before"] == (
        "/dataset/sample_0/before.png"
    )
    assert batch["image_paths"][1]["during"] == (
        "/dataset/sample_1/during.png"
    )
