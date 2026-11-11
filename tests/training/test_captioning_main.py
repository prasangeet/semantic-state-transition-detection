
from __future__ import annotations

import json

from pathlib import Path
from types import SimpleNamespace

import pytest
import torch
import torch.nn as nn

from src.sostd.training import captioning_main


class FakeDataset:
    def __len__(self):
        return 4

    def __getitem__(self, index):
        return index


class FakeTokenizer:
    @classmethod
    def from_pretrained(cls, name):
        return cls()


class FakeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.adapter = nn.Linear(2, 2)


class FakeTrainer:
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = Path(checkpoint_dir)
        self.best_metric = 0.5
        self.history = []

    @classmethod
    def from_config(cls, model, config, checkpoint_dir):
        return cls(checkpoint_dir)

    def resume(self, model):
        return 1

    def fit(self, model, train_loader, validation_loader, epochs):
        self.history = [{"epoch": 1}]
        return self.history


@pytest.fixture
def config(tmp_path):
    return {
        "model": {
            "tokenizer_name": "test-tokenizer",
        },
        "data": {
            "batch_size": 1,
            "num_workers": 0,
            "max_state_length": 32,
            "max_transition_length": 32,
        },
        "optimizer": {
            "name": "adamw",
            "lr": 0.0001,
        },
        "scheduler": {},
        "engine": {
            "device": "cpu",
            "amp": False,
        },
        "training": {
            "epochs": 2,
            "checkpoint_dir": str(tmp_path / "checkpoints"),
            "resume": False,
            "seed": 42,
        },
    }


def install_fakes(monkeypatch, config):
    def fake_build_temporal_dataset(split):
        return (
            FakeDataset(),
            SimpleNamespace(
                clips_built=4,
                clips_seen=4,
            ),
        )

    monkeypatch.setattr(
        captioning_main,
        "build_temporal_dataset",
        fake_build_temporal_dataset,
    )

    monkeypatch.setattr(
        captioning_main,
        "AutoTokenizer",
        FakeTokenizer,
    )

    monkeypatch.setattr(
        captioning_main,
        "CaptioningCollator",
        lambda **kwargs: lambda batch: batch,
    )

    monkeypatch.setattr(
        captioning_main,
        "OSCaRLite",
        FakeModel,
    )

    monkeypatch.setattr(
        captioning_main,
        "CaptioningTrainer",
        FakeTrainer,
    )


def test_load_config(tmp_path):
    path = tmp_path / "config.json"
    expected = {"training": {"epochs": 5}}

    path.write_text(
        json.dumps(expected),
        encoding="utf-8",
    )

    assert captioning_main.load_config(path) == expected


def test_load_config_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        captioning_main.load_config(tmp_path / "missing.json")


def test_load_config_rejects_non_object(tmp_path):
    path = tmp_path / "config.json"
    path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        captioning_main.load_config(path)


def test_run_training_constructs_pipeline(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)

    trainer = captioning_main.run_training(config)

    assert isinstance(trainer, FakeTrainer)
    assert len(trainer.history) == 1


def test_run_training_rejects_invalid_epochs(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)
    config["training"]["epochs"] = 0

    with pytest.raises(ValueError):
        captioning_main.run_training(config)


def test_run_training_rejects_invalid_batch_size(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)
    config["data"]["batch_size"] = 0

    with pytest.raises(ValueError):
        captioning_main.run_training(config)


def test_run_training_falls_back_to_cpu(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)

    monkeypatch.setattr(
        torch.cuda,
        "is_available",
        lambda: False,
    )

    config["engine"]["device"] = "cuda"
    config["engine"]["amp"] = True

    trainer = captioning_main.run_training(config)

    assert trainer is not None
    assert config["engine"]["device"] == "cpu"
    assert config["engine"]["amp"] is False


def test_resume_requires_existing_checkpoint(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)

    with pytest.raises(FileNotFoundError):
        captioning_main.run_training(
            config,
            resume=True,
        )


def test_resume_uses_existing_checkpoint(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)

    checkpoint_dir = Path(
        config["training"]["checkpoint_dir"]
    )
    checkpoint_dir.mkdir(parents=True)
    (checkpoint_dir / "latest.pt").touch()

    trainer = captioning_main.run_training(
        config,
        resume=True,
    )

    assert trainer is not None


def test_explicit_resume_overrides_config(
    config,
    monkeypatch,
):
    install_fakes(monkeypatch, config)

    config["training"]["resume"] = True

    trainer = captioning_main.run_training(
        config,
        resume=False,
    )

    assert trainer is not None
