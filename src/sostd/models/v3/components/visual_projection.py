
from __future__ import annotations

import torch
import torch.nn as nn


class VisualProjection(nn.Module):
    """
    Project visual representations into the language model
    embedding space.

    V4 configuration:
        input_dim: 1024 (DINOv2-Large / temporal features)
        output_dim: 768 (FLAN-T5-Base)

    Input:
        (B, Q, input_dim)

    Output:
        (B, Q, output_dim)
    """

    def __init__(
        self,
        input_dim: int = 1024,
        output_dim: int = 768,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or output_dim < 1:
            raise ValueError(
                "Feature dimensions must be positive."
            )

        if not 0.0 <= dropout < 1.0:
            raise ValueError(
                "dropout must be in [0, 1)."
            )

        self.input_dim = input_dim
        self.output_dim = output_dim

        self.norm = nn.LayerNorm(input_dim)
        self.projection = nn.Linear(input_dim, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        features: torch.Tensor,
    ) -> torch.Tensor:

        if not isinstance(features, torch.Tensor):
            raise TypeError(
                "features must be a torch.Tensor."
            )

        if features.ndim != 3:
            raise ValueError(
                "Expected features with shape (B, Q, D)."
            )

        if not features.is_floating_point():
            raise TypeError(
                "Features must be floating-point tensors."
            )

        batch_size, num_queries, feature_dim = features.shape

        if batch_size < 1 or num_queries < 1:
            raise ValueError(
                "Batch size and query count must be positive."
            )

        if feature_dim != self.input_dim:
            raise ValueError(
                f"Expected input dimension {self.input_dim}, "
                f"received {feature_dim}."
            )

        if features.device != self.projection.weight.device:
            raise ValueError(
                "Input features and projection parameters "
                "must be on the same device."
            )

        features = features.to(
            dtype=self.projection.weight.dtype
        )

        features = self.norm(features)
        features = self.projection(features)
        features = self.dropout(features)

        return features

    def get_input_dim(self) -> int:
        return self.input_dim

    def get_output_dim(self) -> int:
        return self.output_dim
