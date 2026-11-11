import pytest
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset

from src.sostd.training.callbacks import EarlyStopping
from src.sostd.training.trainer import Trainer


@pytest.fixture
def datasets():
    torch.manual_seed(42)

    train_x = torch.randn(32, 10)
    train_y = torch.randint(0, 4, (32,))

    val_x = torch.randn(16, 10)
    val_y = torch.randint(0, 4, (16,))

    train_loader = DataLoader(
        TensorDataset(train_x, train_y),
        batch_size=8,
        shuffle=False,
    )

    val_loader = DataLoader(
        TensorDataset(val_x, val_y),
        batch_size=8,
    )

    return train_loader, val_loader


@pytest.fixture
def trainer_factory(datasets, tmp_path):

    def create(
        epochs=2,
        monitor="val_loss",
        mode="min",
        scheduler=None,
        early_stopping=None,
        checkpoint_dir=None,
    ):
        train_loader, val_loader = datasets

        model = nn.Linear(10, 4)

        optimizer = torch.optim.AdamW(
            model.parameters(),
            lr=0.001,
        )

        return Trainer(
            model=model,
            train_loader=train_loader,
            val_loader=val_loader,
            criterion=nn.CrossEntropyLoss(),
            optimizer=optimizer,
            scheduler=scheduler,
            device="cpu",
            epochs=epochs,
            checkpoint_dir=checkpoint_dir or tmp_path,
            early_stopping=early_stopping,
            monitor=monitor,
            mode=mode,
            config={"experiment": "test"},
        )

    return create


class TestTrainerInitialization:

    def test_initialization(self, trainer_factory):
        trainer = trainer_factory()

        assert trainer.epochs == 2
        assert trainer.monitor == "val_loss"
        assert trainer.mode == "min"
        assert trainer.start_epoch == 0
        assert trainer.best_metric is None
        assert trainer.history == []

    def test_invalid_epochs(self, trainer_factory):
        with pytest.raises(ValueError, match="epochs"):
            trainer_factory(epochs=0)

    def test_invalid_monitor(self, trainer_factory):
        with pytest.raises(ValueError, match="Unsupported monitor"):
            trainer_factory(monitor="invalid_metric")

    def test_invalid_mode(self, trainer_factory):
        with pytest.raises(ValueError, match="mode"):
            trainer_factory(mode="invalid")

    def test_early_stopping_mode_mismatch(self, trainer_factory):
        early_stopping = EarlyStopping(
            patience=3,
            mode="max",
        )

        with pytest.raises(ValueError, match="must match"):
            trainer_factory(
                mode="min",
                early_stopping=early_stopping,
            )


class TestTrainerFit:

    def test_training_completes(self, trainer_factory):
        trainer = trainer_factory(epochs=2)

        history = trainer.fit()

        assert len(history) == 2

    def test_history_contains_expected_metrics(self, trainer_factory):
        trainer = trainer_factory()

        history = trainer.fit()

        expected_keys = {
            "epoch",
            "train_loss",
            "train_accuracy",
            "val_loss",
            "val_accuracy",
            "learning_rate",
            "monitored_metric",
        }

        for record in history:
            assert expected_keys.issubset(record.keys())

    def test_epoch_numbers_are_correct(self, trainer_factory):
        trainer = trainer_factory(epochs=3)

        history = trainer.fit()

        assert [item["epoch"] for item in history] == [1, 2, 3]

    def test_metrics_are_finite(self, trainer_factory):
        trainer = trainer_factory()

        history = trainer.fit()

        for record in history:
            for key in (
                "train_loss",
                "train_accuracy",
                "val_loss",
                "val_accuracy",
                "learning_rate",
            ):
                assert torch.isfinite(
                    torch.tensor(record[key])
                )

    def test_best_checkpoint_is_saved(self, trainer_factory, tmp_path):
        trainer = trainer_factory()

        trainer.fit()

        assert trainer.checkpoints.best_path.exists()

    def test_latest_checkpoint_is_saved(self, trainer_factory, tmp_path):
        trainer = trainer_factory()

        trainer.fit()

        assert trainer.checkpoints.latest_path.exists()

    def test_best_metric_is_updated(self, trainer_factory):
        trainer = trainer_factory()

        trainer.fit()

        assert trainer.best_metric is not None
        assert trainer.best_metric > 0

    def test_training_history_is_preserved(self, trainer_factory):
        trainer = trainer_factory()

        trainer.fit()

        assert len(trainer.history) == 2

    def test_fit_rejects_completed_training(self, trainer_factory):
        trainer = trainer_factory(epochs=1)

        trainer.fit()

        with pytest.raises(ValueError, match="already completed"):
            trainer.fit()


class TestTrainerScheduling:

    def test_step_scheduler(self, trainer_factory):
        trainer = trainer_factory(epochs=2)

        trainer.scheduler = torch.optim.lr_scheduler.StepLR(
            trainer.optimizer,
            step_size=1,
            gamma=0.5,
        )

        history = trainer.fit()

        assert len(history) == 2
        assert history[1]["learning_rate"] < history[0]["learning_rate"]

    def test_plateau_scheduler(self, trainer_factory):
        trainer = trainer_factory(epochs=2)

        trainer.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            trainer.optimizer,
            patience=1,
        )

        history = trainer.fit()

        assert len(history) == 2

    def test_no_scheduler(self, trainer_factory):
        trainer = trainer_factory(epochs=2)

        assert trainer.scheduler is None

        history = trainer.fit()

        assert len(history) == 2


class TestTrainerEarlyStopping:

    def test_early_stopping_is_supported(self, trainer_factory):
        early_stopping = EarlyStopping(
            patience=2,
            mode="min",
        )

        trainer = trainer_factory(
            epochs=3,
            early_stopping=early_stopping,
        )

        history = trainer.fit()

        assert len(history) <= 3

    def test_early_stopping_state_is_saved(
        self, trainer_factory, tmp_path
    ):
        early_stopping = EarlyStopping(
            patience=3,
            mode="min",
        )

        trainer = trainer_factory(
            early_stopping=early_stopping,
        )

        trainer.fit()

        checkpoint = torch.load(
            trainer.checkpoints.latest_path,
            map_location="cpu",
            weights_only=False,
        )

        assert checkpoint["config"]["early_stopping"] is not None


class TestTrainerResume:

    def test_resume_returns_next_epoch(self, trainer_factory, tmp_path):
        checkpoint_dir = tmp_path / "resume"

        trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
        )

        trainer.fit()

        new_trainer = trainer_factory(
            epochs=5,
            checkpoint_dir=checkpoint_dir,
        )

        next_epoch = new_trainer.resume()

        assert next_epoch == 3

    def test_resume_restores_history(self, trainer_factory, tmp_path):
        checkpoint_dir = tmp_path / "history"

        trainer = trainer_factory(
            epochs=2,
            checkpoint_dir=checkpoint_dir,
        )

        trainer.fit()

        new_trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
        )

        new_trainer.resume()

        assert len(new_trainer.history) == 2

    def test_resume_restores_best_metric(self, trainer_factory, tmp_path):
        checkpoint_dir = tmp_path / "best"

        trainer = trainer_factory(
            epochs=2,
            checkpoint_dir=checkpoint_dir,
        )

        trainer.fit()

        expected_best = trainer.best_metric

        new_trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
        )

        new_trainer.resume()

        assert new_trainer.best_metric == pytest.approx(expected_best)

    def test_resume_continues_training(self, trainer_factory, tmp_path):
        checkpoint_dir = tmp_path / "continue"

        trainer = trainer_factory(
            epochs=2,
            checkpoint_dir=checkpoint_dir,
        )

        trainer.fit()

        new_trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
        )

        new_trainer.resume()
        history = new_trainer.fit()

        assert len(history) == 3
        assert history[-1]["epoch"] == 3

    def test_resume_missing_checkpoint(self, trainer_factory, tmp_path):
        trainer = trainer_factory(
            checkpoint_dir=tmp_path / "missing",
        )

        with pytest.raises(FileNotFoundError):
            trainer.resume()

    def test_resume_restores_early_stopping_state(
        self, trainer_factory, tmp_path
    ):
        checkpoint_dir = tmp_path / "early"

        early_stopping = EarlyStopping(
            patience=3,
            mode="min",
        )

        trainer = trainer_factory(
            epochs=2,
            checkpoint_dir=checkpoint_dir,
            early_stopping=early_stopping,
        )

        trainer.fit()

        expected_state = early_stopping.state_dict()

        restored_stopping = EarlyStopping(
            patience=3,
            mode="min",
        )

        new_trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
            early_stopping=restored_stopping,
        )

        new_trainer.resume()

        assert restored_stopping.state_dict() == expected_state

    def test_resume_rejects_monitor_mismatch(
        self, trainer_factory, tmp_path
    ):
        checkpoint_dir = tmp_path / "monitor"

        trainer = trainer_factory(
            epochs=2,
            checkpoint_dir=checkpoint_dir,
            monitor="val_loss",
        )

        trainer.fit()

        new_trainer = trainer_factory(
            epochs=3,
            checkpoint_dir=checkpoint_dir,
            monitor="val_accuracy",
            mode="max",
        )

        with pytest.raises(ValueError, match="monitoring configuration"):
            new_trainer.resume()
