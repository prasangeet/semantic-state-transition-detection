import torch.nn as nn
import torch
from types import SimpleNamespace
from src.sostd.training.captioning_engine import CaptioningEngine


def test_progress_bar_reports_running_captioning_losses(monkeypatch):
    updates = []
    descriptions = []

    class FakeProgress:
        def __init__(self, iterable, **kwargs):
            self.iterable = iterable
            descriptions.append(kwargs["desc"])

        def __iter__(self):
            return iter(self.iterable)

        def set_postfix(self, **kwargs):
            updates.append(kwargs)

    class TinyCaptioningModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.weight = nn.Parameter(torch.tensor(1.0))

        def forward(
            self,
            frames,
            state_labels,
            transition_labels,
            state_mask,
        ):
            return {
                "state_output": SimpleNamespace(
                    loss=self.weight.square()
                ),
                "transition_output": SimpleNamespace(
                    loss=(self.weight - 2).square()
                ),
            }

    monkeypatch.setattr(
        "src.sostd.training.captioning_engine.tqdm",
        FakeProgress,
    )

    engine = CaptioningEngine(device="cpu")

    model = TinyCaptioningModel()

    batch = {
        "frames": torch.rand(1, 3, 3, 8, 8),
        "state_labels": torch.tensor(
            [[[1, 2], [3, 4], [5, 6]]]
        ),
        "state_mask": torch.tensor([[True, True, True]]),
        "transition_labels": torch.tensor([[1, 2]]),
    }

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=1e-3,
    )

    engine.train_one_epoch(
        model=model,
        dataloader=[batch],
        optimizer=optimizer,
    )

    assert descriptions == ["Training"]
    assert len(updates) == 1

    assert set(updates[0]) == {
        "loss",
        "state_loss",
        "transition_loss",
    }

    assert engine.validate(
        model=model,
        dataloader=[batch],
    )["batches"] == 1

    assert descriptions[-1] == "Validation"
