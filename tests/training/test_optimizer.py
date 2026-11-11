import pytest
import torch
import torch.nn as nn

from src.sostd.training.optimizer import OptimizerFactory


class TestOptimizerFactory:

    @pytest.mark.parametrize(
        "name, expected_type",
        [
            ("adam", torch.optim.Adam),
            ("adamw", torch.optim.AdamW),
            ("sgd", torch.optim.SGD),
            ("rmsprop", torch.optim.RMSprop),
        ],
    )
    def test_create_supported_optimizers(self, name, expected_type):
        model = nn.Linear(10, 4)

        optimizer = OptimizerFactory.create(
            name,
            model.parameters(),
        )

        assert isinstance(optimizer, expected_type)

    def test_custom_learning_rate(self):
        model = nn.Linear(10, 4)

        optimizer = OptimizerFactory.create(
            "adamw",
            model.parameters(),
            lr=0.005,
        )

        assert optimizer.param_groups[0]["lr"] == pytest.approx(0.005)

    def test_default_learning_rate(self):
        model = nn.Linear(10, 4)

        optimizer = OptimizerFactory.create(
            "adam",
            model.parameters(),
        )

        assert optimizer.param_groups[0]["lr"] == pytest.approx(1e-3)

    def test_custom_optimizer_parameters(self):
        model = nn.Linear(10, 4)

        optimizer = OptimizerFactory.create(
            "adamw",
            model.parameters(),
            lr=0.001,
            weight_decay=1e-4,
        )

        assert optimizer.param_groups[0]["weight_decay"] == pytest.approx(1e-4)

    def test_unsupported_optimizer(self):
        model = nn.Linear(10, 4)

        with pytest.raises(ValueError, match="Unsupported optimizer"):
            OptimizerFactory.create(
                "unknown",
                model.parameters(),
            )

    @pytest.mark.parametrize("lr", [0, -0.001, -1])
    def test_invalid_learning_rate(self, lr):
        model = nn.Linear(10, 4)

        with pytest.raises(ValueError, match="positive"):
            OptimizerFactory.create(
                "adam",
                model.parameters(),
                lr=lr,
            )

    def test_optimizer_performs_parameter_update(self):
        model = nn.Linear(10, 4)

        optimizer = OptimizerFactory.create(
            "adamw",
            model.parameters(),
        )

        inputs = torch.randn(8, 10)
        targets = torch.randint(0, 4, (8,))

        criterion = nn.CrossEntropyLoss()

        before = model.weight.detach().clone()

        optimizer.zero_grad()

        loss = criterion(model(inputs), targets)
        loss.backward()

        optimizer.step()

        assert not torch.equal(before, model.weight.detach())
