import pytest
import torch
import torch.nn as nn

from src.sostd.training.losses import (
    LossFactory,
    compute_class_weights,
)


class TestLossFactory:

    @pytest.mark.parametrize(
        "name, expected_type",
        [
            ("cross_entropy", nn.CrossEntropyLoss),
            ("bce", nn.BCEWithLogitsLoss),
            ("mse", nn.MSELoss),
            ("l1", nn.L1Loss),
            ("smooth_l1", nn.SmoothL1Loss),
        ],
    )
    def test_create_supported_losses(self, name, expected_type):
        criterion = LossFactory.create(name)

        assert isinstance(criterion, expected_type)

    def test_unsupported_loss_raises_error(self):
        with pytest.raises(ValueError, match="Unsupported loss"):
            LossFactory.create("unknown")

    def test_cross_entropy_computes_loss(self):
        criterion = LossFactory.create("cross_entropy")

        logits = torch.randn(4, 4)
        targets = torch.tensor([0, 1, 2, 3])

        loss = criterion(logits, targets)

        assert loss.ndim == 0
        assert torch.isfinite(loss)
        assert loss.item() > 0

    def test_loss_factory_accepts_kwargs(self):
        criterion = LossFactory.create(
            "cross_entropy",
            label_smoothing=0.1,
        )

        assert isinstance(criterion, nn.CrossEntropyLoss)
        assert criterion.label_smoothing == pytest.approx(0.1)


class TestClassWeights:

    def test_balanced_classes(self):
        labels = torch.tensor([0, 0, 1, 1, 2, 2])

        weights = compute_class_weights(labels, 3)

        assert weights.shape == (3,)
        assert torch.allclose(weights, torch.ones(3))

    def test_imbalanced_classes(self):
        labels = torch.tensor([0, 0, 0, 1, 2])

        weights = compute_class_weights(labels, 3)

        assert weights[0] < weights[1]
        assert weights[0] < weights[2]
        assert weights.mean().item() == pytest.approx(1.0)

    def test_missing_class_raises_error(self):
        labels = torch.tensor([0, 0, 1, 1])

        with pytest.raises(ValueError, match="no samples"):
            compute_class_weights(labels, 3)

    def test_empty_labels_raises_error(self):
        labels = torch.tensor([], dtype=torch.long)

        with pytest.raises(ValueError, match="no samples"):
            compute_class_weights(labels, 3)
