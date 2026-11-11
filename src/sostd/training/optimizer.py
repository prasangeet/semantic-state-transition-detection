from __future__ import annotations

import torch
import torch.nn as nn


class OptimizerFactory:
    """Factory for PyTorch optimizers."""

    @staticmethod
    def create(
        name: str,
        parameters,
        lr: float = 1e-3,
        **kwargs,
    ) -> torch.optim.Optimizer:

        if lr <= 0:
            raise ValueError("Learning rate must be positive.")

        optimizers = {
            "adam": torch.optim.Adam,
            "adamw": torch.optim.AdamW,
            "sgd": torch.optim.SGD,
            "rmsprop": torch.optim.RMSprop,
        }

        name = name.lower()

        if name not in optimizers:
            raise ValueError(
                f"Unsupported optimizer: {name}. "
                f"Available: {list(optimizers.keys())}"
            )

        return optimizers[name](
            parameters,
            lr=lr,
            **kwargs,
        )
