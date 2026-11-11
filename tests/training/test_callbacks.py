import pytest
import torch
import torch.nn as nn

from src.sostd.training.callbacks import (
    CheckpointManager,
    EarlyStopping,
)


@pytest.fixture
def model():
    return nn.Linear(10, 4)


@pytest.fixture
def optimizer(model):
    return torch.optim.AdamW(
        model.parameters(),
        lr=0.001,
    )


class TestCheckpointManager:

    def test_creates_checkpoint_directory(self, tmp_path):
        directory = tmp_path / "checkpoints"

        manager = CheckpointManager(directory)

        assert directory.exists()
        assert manager.best_path == directory / "best.pt"
        assert manager.latest_path == directory / "latest.pt"

    def test_save_best_checkpoint(self, tmp_path, model, optimizer):
        manager = CheckpointManager(tmp_path)

        path = manager.save_best(
            model=model,
            optimizer=optimizer,
            epoch=5,
            metric=0.85,
        )

        assert path.exists()
        assert path.name == "best.pt"

    def test_save_latest_checkpoint(self, tmp_path, model, optimizer):
        manager = CheckpointManager(tmp_path)

        path = manager.save_latest(
            model=model,
            optimizer=optimizer,
            epoch=5,
            metric=0.85,
        )

        assert path.exists()
        assert path.name == "latest.pt"

    def test_checkpoint_contains_training_state(
        self, tmp_path, model, optimizer
    ):
        manager = CheckpointManager(tmp_path)

        manager.save_best(
            model=model,
            optimizer=optimizer,
            epoch=10,
            metric=0.75,
            config={"lr": 0.001},
        )

        checkpoint = torch.load(
            manager.best_path,
            map_location="cpu",
            weights_only=False,
        )

        assert checkpoint["epoch"] == 10
        assert checkpoint["metric"] == pytest.approx(0.75)
        assert checkpoint["config"]["lr"] == pytest.approx(0.001)
        assert "model_state_dict" in checkpoint
        assert "optimizer_state_dict" in checkpoint

    def test_load_restores_model_weights(
        self, tmp_path, model, optimizer
    ):
        manager = CheckpointManager(tmp_path)

        manager.save_best(
            model=model,
            optimizer=optimizer,
            epoch=5,
        )

        expected_weights = {
            key: value.clone()
            for key, value in model.state_dict().items()
        }

        with torch.no_grad():
            for parameter in model.parameters():
                parameter.add_(10)

        CheckpointManager.load(
            manager.best_path,
            model=model,
            optimizer=optimizer,
        )

        for key, value in model.state_dict().items():
            assert torch.equal(value, expected_weights[key])

    def test_load_restores_optimizer_state(
        self, tmp_path, model, optimizer
    ):
        manager = CheckpointManager(tmp_path)

        inputs = torch.randn(4, 10)
        targets = torch.randint(0, 4, (4,))

        loss = nn.CrossEntropyLoss()(model(inputs), targets)
        loss.backward()
        optimizer.step()

        manager.save_latest(
            model=model,
            optimizer=optimizer,
            epoch=3,
        )

        expected_state = optimizer.state_dict()

        new_model = nn.Linear(10, 4)
        new_optimizer = torch.optim.AdamW(
            new_model.parameters(),
            lr=0.001,
        )

        CheckpointManager.load(
            manager.latest_path,
            new_model,
            new_optimizer,
        )

        assert new_optimizer.state_dict()["state"].keys() == (
            expected_state["state"].keys()
        )

    def test_load_returns_metadata(self, tmp_path, model):
        manager = CheckpointManager(tmp_path)

        manager.save_best(
            model=model,
            epoch=7,
            metric=0.92,
        )

        metadata = CheckpointManager.load(
            manager.best_path,
            model,
        )

        assert metadata["epoch"] == 7
        assert metadata["metric"] == pytest.approx(0.92)

    def test_load_missing_checkpoint_raises_error(
        self, tmp_path, model
    ):
        with pytest.raises(FileNotFoundError):
            CheckpointManager.load(
                tmp_path / "missing.pt",
                model,
            )

    def test_checkpoint_is_overwritten(
        self, tmp_path, model
    ):
        manager = CheckpointManager(tmp_path)

        manager.save_best(model, epoch=1)
        manager.save_best(model, epoch=2)

        checkpoint = CheckpointManager.load(
            manager.best_path,
            model,
        )

        assert checkpoint["epoch"] == 2

    def test_checkpoint_does_not_leave_temporary_file(
        self, tmp_path, model
    ):
        manager = CheckpointManager(tmp_path)

        manager.save_best(model)

        assert not (tmp_path / "best.pt.tmp").exists()

    def test_invalid_checkpoint_format_raises_error(
        self, tmp_path, model
    ):
        path = tmp_path / "invalid.pt"
        torch.save({"invalid": True}, path)

        with pytest.raises(ValueError, match="Invalid checkpoint"):
            CheckpointManager.load(path, model)


class TestEarlyStopping:

    def test_first_metric_is_improvement(self):
        callback = EarlyStopping(patience=3)

        assert callback.step(1.0) is False
        assert callback.best_score == 1.0
        assert callback.counter == 0

    def test_min_mode_improvement(self):
        callback = EarlyStopping(patience=3, mode="min")

        callback.step(1.0)

        assert callback.step(0.8) is False
        assert callback.best_score == 0.8

    def test_max_mode_improvement(self):
        callback = EarlyStopping(patience=3, mode="max")

        callback.step(0.5)

        assert callback.step(0.8) is False
        assert callback.best_score == 0.8

    def test_counter_increments_without_improvement(self):
        callback = EarlyStopping(patience=3)

        callback.step(1.0)
        callback.step(1.1)

        assert callback.counter == 1

    def test_counter_resets_after_improvement(self):
        callback = EarlyStopping(patience=3)

        callback.step(1.0)
        callback.step(1.1)
        callback.step(1.2)
        callback.step(0.8)

        assert callback.counter == 0

    def test_stops_after_patience(self):
        callback = EarlyStopping(patience=3)

        callback.step(1.0)

        assert callback.step(1.1) is False
        assert callback.step(1.2) is False
        assert callback.step(1.3) is True

        assert callback.early_stop is True

    def test_min_delta_is_respected(self):
        callback = EarlyStopping(
            patience=3,
            min_delta=0.1,
            mode="min",
        )

        callback.step(1.0)

        callback.step(0.95)

        assert callback.best_score == 1.0
        assert callback.counter == 1

        callback.step(0.85)

        assert callback.best_score == 0.85
        assert callback.counter == 0

    def test_nan_is_not_an_improvement(self):
        callback = EarlyStopping(patience=2)

        callback.step(1.0)

        assert callback.step(float("nan")) is False
        assert callback.counter == 1

        assert callback.step(float("nan")) is True

    def test_invalid_patience(self):
        with pytest.raises(ValueError, match="patience"):
            EarlyStopping(patience=0)

    def test_negative_min_delta(self):
        with pytest.raises(ValueError, match="min_delta"):
            EarlyStopping(min_delta=-0.1)

    def test_invalid_mode(self):
        with pytest.raises(ValueError, match="mode"):
            EarlyStopping(mode="invalid")

    def test_state_dict_restores_state(self):
        original = EarlyStopping(
            patience=3,
            min_delta=0.01,
            mode="min",
        )

        original.step(1.0)
        original.step(1.1)

        state = original.state_dict()

        restored = EarlyStopping(
            patience=3,
            min_delta=0.01,
            mode="min",
        )

        restored.load_state_dict(state)

        assert restored.best_score == original.best_score
        assert restored.counter == original.counter
        assert restored.early_stop == original.early_stop

    def test_state_dict_rejects_configuration_mismatch(self):
        original = EarlyStopping(patience=3)
        state = original.state_dict()

        restored = EarlyStopping(patience=5)

        with pytest.raises(ValueError, match="patience mismatch"):
            restored.load_state_dict(state)

    def test_stopping_remains_active(self):
        callback = EarlyStopping(patience=1)

        callback.step(1.0)
        assert callback.step(2.0) is True
        assert callback.step(0.5) is True
