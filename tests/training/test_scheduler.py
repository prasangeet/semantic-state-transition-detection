import pytest
import torch
import torch.nn as nn

from src.sostd.training.scheduler import SchedulerFactory


@pytest.fixture
def optimizer():
    model = nn.Linear(10, 4)

    return torch.optim.AdamW(
        model.parameters(),
        lr=0.001,
    )


class TestSchedulerFactory:

    @pytest.mark.parametrize(
        "name, expected_type, kwargs",
        [
            (
                "step",
                torch.optim.lr_scheduler.StepLR,
                {"step_size": 5},
            ),
            (
                "cosine",
                torch.optim.lr_scheduler.CosineAnnealingLR,
                {"T_max": 10},
            ),
            (
                "plateau",
                torch.optim.lr_scheduler.ReduceLROnPlateau,
                {},
            ),
            (
                "exponential",
                torch.optim.lr_scheduler.ExponentialLR,
                {"gamma": 0.9},
            ),
        ],
    )
    def test_create_supported_schedulers(
        self,
        optimizer,
        name,
        expected_type,
        kwargs,
    ):
        scheduler = SchedulerFactory.create(
            name,
            optimizer,
            **kwargs,
        )

        assert isinstance(scheduler, expected_type)

    def test_unsupported_scheduler(self, optimizer):
        with pytest.raises(ValueError, match="Unsupported scheduler"):
            SchedulerFactory.create("unknown", optimizer)

    def test_invalid_step_size(self, optimizer):
        with pytest.raises(ValueError, match="step_size"):
            SchedulerFactory.create(
                "step",
                optimizer,
                step_size=0,
            )

    def test_invalid_cosine_tmax(self, optimizer):
        with pytest.raises(ValueError, match="T_max"):
            SchedulerFactory.create(
                "cosine",
                optimizer,
                T_max=-1,
            )

    def test_invalid_exponential_gamma(self, optimizer):
        with pytest.raises(ValueError, match="gamma"):
            SchedulerFactory.create(
                "exponential",
                optimizer,
                gamma=1.5,
            )

    def test_invalid_plateau_factor(self, optimizer):
        with pytest.raises(ValueError, match="factor"):
            SchedulerFactory.create(
                "plateau",
                optimizer,
                factor=1.0,
            )

    def test_negative_plateau_patience(self, optimizer):
        with pytest.raises(ValueError, match="patience"):
            SchedulerFactory.create(
                "plateau",
                optimizer,
                patience=-1,
            )

    def test_step_scheduler_updates_learning_rate(self, optimizer):
        scheduler = SchedulerFactory.create(
            "step",
            optimizer,
            step_size=1,
            gamma=0.1,
        )

        initial_lr = optimizer.param_groups[0]["lr"]

        scheduler.step()

        updated_lr = optimizer.param_groups[0]["lr"]

        assert updated_lr == pytest.approx(initial_lr * 0.1)

    def test_cosine_scheduler_updates_learning_rate(self, optimizer):
        scheduler = SchedulerFactory.create(
            "cosine",
            optimizer,
            T_max=2,
        )

        initial_lr = optimizer.param_groups[0]["lr"]

        scheduler.step()

        assert optimizer.param_groups[0]["lr"] < initial_lr

    def test_plateau_scheduler_accepts_validation_metric(self, optimizer):
        scheduler = SchedulerFactory.create(
            "plateau",
            optimizer,
            patience=0,
            factor=0.1,
        )

        scheduler.step(1.0)
        scheduler.step(2.0)

        assert optimizer.param_groups[0]["lr"] < 0.001
