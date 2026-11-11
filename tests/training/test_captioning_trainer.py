from __future__ import annotations

from pathlib import Path

import pytest
import torch
import torch.nn as nn

from src.sostd.training.callbacks import CheckpointManager, EarlyStopping
from src.sostd.training.captioning_trainer import CaptioningTrainer


class FakeEngine:
    def __init__(self, train_losses=None, validation_losses=None):
        self.train_losses = list(train_losses or [1.0])
        self.validation_losses = list(validation_losses or [0.8])
        self.train_calls = 0
        self.validation_calls = 0
        self.scaler = torch.amp.GradScaler("cuda", enabled=False)
        self.device = torch.device("cpu")
        self.amp = False

    def train_one_epoch(self, model, dataloader, optimizer):
        index = min(self.train_calls, len(self.train_losses) - 1)
        loss = self.train_losses[index]
        self.train_calls += 1
        optimizer.step()
        return {
            "loss": loss,
            "state_loss": loss,
            "transition_loss": loss,
            "state_tokens": 10,
            "transition_tokens": 10,
            "samples": 1,
            "batches": 1,
        }

    def validate(self, model, dataloader):
        index = min(self.validation_calls, len(self.validation_losses) - 1)
        loss = self.validation_losses[index]
        self.validation_calls += 1
        return {
            "loss": loss,
            "state_loss": loss * 0.5,
            "transition_loss": loss * 0.5,
            "state_tokens": 10,
            "transition_tokens": 10,
            "samples": 1,
            "batches": 1,
        }


class FakeLoader:
    pass


def create_trainer(
    tmp_path: Path,
    validation_losses=None,
    early_stopping=None,
):
    model = nn.Linear(2, 1)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    scheduler = torch.optim.lr_scheduler.StepLR(
        optimizer, step_size=1, gamma=0.5
    )
    engine = FakeEngine(validation_losses=validation_losses)
    trainer = CaptioningTrainer(
        engine=engine,
        optimizer=optimizer,
        scheduler=scheduler,
        checkpoint_manager=CheckpointManager(tmp_path / "checkpoints"),
        early_stopping=early_stopping,
        config={"optimizer": {"name": "adamw"}},
    )
    return model, trainer


def test_initialization(tmp_path):
    _, trainer = create_trainer(tmp_path)
    assert trainer.start_epoch == 0
    assert trainer.best_metric == float("inf")
    assert trainer.history == []
    assert trainer.stopped_early is False


def test_fit_saves_latest_and_best(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.8, 0.6])
    history = trainer.fit(model, FakeLoader(), FakeLoader(), epochs=2)
    manager = trainer.checkpoint_manager

    assert len(history) == 2
    assert manager.latest_path.exists()
    assert manager.best_path.exists()

    latest = torch.load(
        manager.latest_path, map_location="cpu", weights_only=False
    )
    assert latest["epoch"] == 2
    assert latest["metric"] == pytest.approx(0.6)


def test_best_checkpoint_only_updates_on_improvement(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.5, 0.8])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=2)

    best = torch.load(
        trainer.checkpoint_manager.best_path,
        map_location="cpu",
        weights_only=False,
    )
    latest = torch.load(
        trainer.checkpoint_manager.latest_path,
        map_location="cpu",
        weights_only=False,
    )
    assert best["epoch"] == 1
    assert best["metric"] == pytest.approx(0.5)
    assert latest["epoch"] == 2


def test_resume_restores_epoch_and_training_metadata(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.8])
    trainer.early_stopping = EarlyStopping(patience=4)
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(tmp_path)
    resumed_trainer.early_stopping = EarlyStopping(patience=4)
    next_epoch = resumed_trainer.resume(resumed_model)

    assert next_epoch == 1
    assert resumed_trainer.start_epoch == 1
    assert resumed_trainer.best_metric == pytest.approx(0.8)
    assert len(resumed_trainer.history) == 1
    assert resumed_trainer.early_stopping.best_score == pytest.approx(0.8)


def test_resume_restores_optimizer_scheduler_and_model(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.8])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(tmp_path)
    resumed_trainer.resume(resumed_model)

    for original, restored in zip(model.parameters(), resumed_model.parameters()):
        assert torch.allclose(original, restored)

    assert resumed_trainer.optimizer.param_groups[0]["lr"] == pytest.approx(
        trainer.optimizer.param_groups[0]["lr"]
    )
    assert resumed_trainer.scheduler.last_epoch == trainer.scheduler.last_epoch


def test_resume_from_explicit_checkpoint(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.8])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(tmp_path)
    next_epoch = resumed_trainer.resume(
        resumed_model,
        checkpoint_path=trainer.checkpoint_manager.best_path,
    )
    assert next_epoch == 1


def test_resume_rejects_missing_checkpoint(tmp_path):
    model, trainer = create_trainer(tmp_path)
    with pytest.raises(FileNotFoundError):
        trainer.resume(model)


def test_resume_rejects_early_stopping_mismatch(tmp_path):
    model, trainer = create_trainer(tmp_path)
    trainer.early_stopping = EarlyStopping(patience=3)
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(tmp_path)
    with pytest.raises(ValueError):
        resumed_trainer.resume(resumed_model)


def test_resume_rejects_incompatible_early_stopping_config(tmp_path):
    model, trainer = create_trainer(tmp_path)
    trainer.early_stopping = EarlyStopping(patience=3)
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(tmp_path)
    resumed_trainer.early_stopping = EarlyStopping(patience=5)
    with pytest.raises(ValueError):
        resumed_trainer.resume(resumed_model)


def test_early_stopping_state_is_saved(tmp_path):
    model, trainer = create_trainer(
        tmp_path,
        validation_losses=[0.5, 0.6, 0.7],
        early_stopping=EarlyStopping(patience=2),
    )
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=5)

    assert trainer.stopped_early is True
    assert trainer.start_epoch == 3
    latest = torch.load(
        trainer.checkpoint_manager.latest_path,
        map_location="cpu",
        weights_only=False,
    )
    assert latest["config"]["stopped_early"] is True
    assert latest["config"]["early_stopping"]["counter"] == 2


def test_fit_rejects_invalid_epochs(tmp_path):
    model, trainer = create_trainer(tmp_path)
    with pytest.raises(ValueError):
        trainer.fit(model, FakeLoader(), FakeLoader(), epochs=0)


def test_fit_rejects_non_finite_validation_loss(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[float("nan")])
    with pytest.raises(FloatingPointError):
        trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)


def test_fit_rejects_training_after_completion(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.5])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)
    with pytest.raises(ValueError):
        trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)


def test_checkpoint_contains_training_history(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.7])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)
    checkpoint = torch.load(
        trainer.checkpoint_manager.latest_path,
        map_location="cpu",
        weights_only=False,
    )
    assert len(checkpoint["config"]["history"]) == 1
    assert checkpoint["config"]["best_metric"] == pytest.approx(0.7)
    assert "user_config" in checkpoint["config"]


def test_fit_rejects_non_finite_train_loss(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.5])
    trainer.engine.train_losses = [float("inf")]
    with pytest.raises((FloatingPointError, ValueError)):
        trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)


def test_fit_can_continue_after_checkpoint_resume(tmp_path):
    model, trainer = create_trainer(tmp_path, validation_losses=[0.8])
    trainer.fit(model, FakeLoader(), FakeLoader(), epochs=1)

    resumed_model, resumed_trainer = create_trainer(
        tmp_path, validation_losses=[0.6]
    )
    resumed_trainer.resume(resumed_model)
    history = resumed_trainer.fit(
        resumed_model, FakeLoader(), FakeLoader(), epochs=2
    )

    assert resumed_trainer.start_epoch == 2
    assert len(history) == 2
    assert history[-1]["epoch"] == 2
