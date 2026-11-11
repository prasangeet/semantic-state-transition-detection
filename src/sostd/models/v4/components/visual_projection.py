from __future__ import annotations

import torch
import torch.nn as nn


class VisualProjection(nn.Module):
    """
    Project visual representations into the language model
    embedding space.

    Supports:
        (B, Q, D)    - temporally aggregated features
        (B, T, Q, D) - per-frame visual features

    V4 configuration:
        input_dim: 1024
        output_dim: 768

    Outputs:
        (B, Q, output_dim)
        (B, T, Q, output_dim)
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
                "Dropout must be in [0, 1)."
            )

        self.input_dim = input_dim
        self.output_dim = output_dim

        self.norm = nn.LayerNorm(input_dim)

        self.projection = nn.Linear(
            input_dim,
            output_dim,
        )

        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        features: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            features:
                (B, Q, D) or (B, T, Q, D)

        Returns:
            Projected features:
                (B, Q, output_dim) or
                (B, T, Q, output_dim)
        """

        if not isinstance(features, torch.Tensor):
            raise TypeError(
                "Features must be a torch.Tensor."
            )

        if features.ndim not in (3, 4):
            raise ValueError(
                "Expected features with shape "
                "(B, Q, D) or (B, T, Q, D), "
                f"received {tuple(features.shape)}."
            )

        if not features.is_floating_point():
            raise TypeError(
                "Features must be floating-point tensors."
            )

        if any(size < 1 for size in features.shape[:-1]):
            raise ValueError(
                "Batch, temporal and query dimensions "
                "must be positive."
            )

        feature_dim = features.shape[-1]

        if feature_dim != self.input_dim:
            raise ValueError(
                f"Expected input dimension {self.input_dim}, "
                f"received {feature_dim}."
            )

        if not torch.isfinite(features).all():
            raise ValueError(
                "Features contain non-finite values."
            )

        # Match the projection parameter dtype.
        features = features.to(
            dtype=self.projection.weight.dtype
        )

        # LayerNorm and Linear operate on the final dimension,
        # preserving all leading dimensions automatically.
        features = self.norm(features)
        features = self.projection(features)
        features = self.dropout(features)

        return features

    def get_input_dim(self) -> int:
        return self.input_dim

    def get_output_dim(self) -> int:
        return self.output_dim