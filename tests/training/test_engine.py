import pytest
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset, Dataset

from src.sostd.training.engine import TrainingEngine


@pytest.fixture
def engine():
    return TrainingEngine(device="cpu")


@pytest.fixture
def model():
    return nn.Linear(10, 4)


@pytest.fixture
def criterion():
    return nn.CrossEntropyLoss()


@pytest.fixture
def optimizer(model):
    return torch.optim.AdamW(
        model.parameters(),
        lr=0.01,
    )


@pytest.fixture
def dataloader():
    inputs = torch.randn(32, 10)
    targets = torch.randint(0, 4, (32,))

    return DataLoader(
        TensorDataset(inputs, targets),
        batch_size=8,
    )


class DictDataset(Dataset):
    """Dataset returning dictionary batches."""

    def __len__(self):
        return 16

    def __getitem__(self, index):
        return {
            "inputs": torch.randn(10),
            "targets": torch.tensor(index % 4),
        }


class InvalidDataset(Dataset):

    def __len__(self):
        return 4

    def __getitem__(self, index):
        return torch.randn(10)


class SequenceModel(nn.Module):
    """Simple model producing frame-wise predictions."""

    def __init__(self):
        super().__init__()
        self.classifier = nn.Linear(10, 4)

    def forward(self, x):
        return self.classifier(x)


class NonFiniteLoss(nn.Module):

    def forward(self, logits, targets):
        return torch.tensor(
            float("nan"),
            device=logits.device,
            requires_grad=True,
        )


class TestTrainingEngine:

    def test_engine_initialization(self):
        engine = TrainingEngine(device="cpu")

        assert engine.device == torch.device("cpu")
        assert engine.amp is False
        assert engine.scaler is not None

    def test_invalid_gradient_clipping(self):
        with pytest.raises(ValueError, match="grad_clip"):
            TrainingEngine(grad_clip=0)

    def test_training_runs_successfully(
        self, engine, model, dataloader, criterion, optimizer
    ):
        metrics = engine.train_one_epoch(
            model,
            dataloader,
            criterion,
            optimizer,
        )

        assert "loss" in metrics
        assert "accuracy" in metrics
        assert "samples" in metrics

        assert metrics["loss"] > 0
        assert 0 <= metrics["accuracy"] <= 1
        assert metrics["samples"] == 32

    def test_training_updates_model_parameters(
        self, engine, model, dataloader, criterion, optimizer
    ):
        before = model.weight.detach().clone()

        engine.train_one_epoch(
            model,
            dataloader,
            criterion,
            optimizer,
        )

        assert not torch.equal(before, model.weight)

    def test_validation_runs_successfully(
        self, engine, model, dataloader, criterion
    ):
        metrics = engine.validate(
            model,
            dataloader,
            criterion,
        )

        assert metrics["loss"] > 0
        assert 0 <= metrics["accuracy"] <= 1
        assert metrics["samples"] == 32

    def test_validation_does_not_update_parameters(
        self, engine, model, dataloader, criterion
    ):
        before = model.weight.detach().clone()

        engine.validate(
            model,
            dataloader,
            criterion,
        )

        assert torch.equal(before, model.weight)

    def test_temporal_classification(
        self, engine, criterion
    ):
        model = SequenceModel()

        inputs = torch.randn(4, 8, 10)
        targets = torch.randint(0, 4, (4, 8))

        loader = DataLoader(
            TensorDataset(inputs, targets),
            batch_size=2,
        )

        metrics = engine.validate(
            model,
            loader,
            criterion,
        )

        assert metrics["samples"] == 32
        assert metrics["loss"] > 0

    def test_dictionary_batch(
        self, engine, model, criterion
    ):
        loader = DataLoader(
            DictDataset(),
            batch_size=4,
        )

        metrics = engine.validate(
            model,
            loader,
            criterion,
        )

        assert metrics["samples"] == 16

    def test_empty_dataloader_raises_error(
        self, engine, model, criterion
    ):
        dataset = TensorDataset(
            torch.empty(0, 10),
            torch.empty(0, dtype=torch.long),
        )

        loader = DataLoader(dataset, batch_size=4)

        with pytest.raises(ValueError, match="no samples"):
            engine.validate(model, loader, criterion)

    def test_invalid_batch_raises_error(
        self, engine, model, criterion
    ):
        loader = DataLoader(
            InvalidDataset(),
            batch_size=2,
        )

        with pytest.raises(ValueError, match="Batch must be"):
            engine.validate(model, loader, criterion)

    def test_incompatible_shapes_raise_error(self, engine):
        logits = torch.randn(4, 4)
        targets = torch.randint(0, 4, (4, 8))

        with pytest.raises(ValueError, match="incompatible"):
            engine._prepare_predictions(logits, targets)

    def test_invalid_logits_dimensions_raise_error(self, engine):
        logits = torch.randn(4, 8, 16, 4)
        targets = torch.randint(0, 4, (4, 8, 16))

        with pytest.raises(ValueError, match="2D or 3D"):
            engine._prepare_predictions(logits, targets)

    def test_single_class_output_raises_error(self, engine):
        logits = torch.randn(4, 1)
        targets = torch.zeros(4, dtype=torch.long)

        with pytest.raises(ValueError, match="two output classes"):
            engine._prepare_predictions(logits, targets)

    def test_non_finite_loss_raises_error(
        self, engine, model, dataloader, optimizer
    ):
        with pytest.raises(FloatingPointError, match="Non-finite loss"):
            engine.train_one_epoch(
                model,
                dataloader,
                NonFiniteLoss(),
                optimizer,
            )

    def test_gradient_clipping(
        self, model, dataloader, criterion, optimizer
    ):
        engine = TrainingEngine(
            device="cpu",
            grad_clip=0.5,
        )

        metrics = engine.train_one_epoch(
            model,
            dataloader,
            criterion,
            optimizer,
        )

        assert torch.isfinite(torch.tensor(metrics["loss"]))

    def test_cpu_amp_is_disabled(
        self, model, dataloader, criterion
    ):
        engine = TrainingEngine(
            device="cpu",
            amp=True,
        )

        assert engine.amp is False

        metrics = engine.validate(
            model,
            dataloader,
            criterion,
        )

        assert metrics["samples"] == 32

    def test_model_is_set_to_eval_during_validation(
        self, engine, model, dataloader, criterion
    ):
        model.train()

        engine.validate(
            model,
            dataloader,
            criterion,
        )

        assert model.training is False

    def test_model_is_set_to_train_during_training(
        self, engine, model, dataloader, criterion, optimizer
    ):
        model.eval()

        engine.train_one_epoch(
            model,
            dataloader,
            criterion,
            optimizer,
        )

        assert model.training is True
