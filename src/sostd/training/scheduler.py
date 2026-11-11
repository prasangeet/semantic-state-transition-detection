from __future__ import annotations

import torch


class SchedulerFactory:
    """Factory for PyTorch learning-rate schedulers."""

    @staticmethod
    def create(
        name: str,
        optimizer: torch.optim.Optimizer,
        **kwargs,
    ):
        schedulers = {
            "step": torch.optim.lr_scheduler.StepLR,
            "cosine": torch.optim.lr_scheduler.CosineAnnealingLR,
            "plateau": torch.optim.lr_scheduler.ReduceLROnPlateau,
            "exponential": torch.optim.lr_scheduler.ExponentialLR,
        }

        name = name.lower()

        if name not in schedulers:
            raise ValueError(
                f"Unsupported scheduler: {name}. "
                f"Available: {list(schedulers.keys())}"
            )

        if name == "step":
            if kwargs.get("step_size", 0) <= 0:
                raise ValueError("step_size must be positive.")

        elif name == "cosine":
            if kwargs.get("T_max", 0) <= 0:
                raise ValueError("T_max must be positive.")

        elif name == "exponential":
            gamma = kwargs.get("gamma", 0.0)

            if not 0.0 < gamma <= 1.0:
                raise ValueError("gamma must be in (0, 1].")

        elif name == "plateau":
            factor = kwargs.get("factor", 0.1)

            if not 0.0 < factor < 1.0:
                raise ValueError("factor must be in (0, 1).")

            if kwargs.get("patience", 10) < 0:
                raise ValueError("patience cannot be negative.")

        return schedulers[name](optimizer, **kwargs)
