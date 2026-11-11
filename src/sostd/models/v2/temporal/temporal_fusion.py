
from __future__ import annotations

import torch
import torch.nn as nn


class TemporalFusion(nn.Module):
    """
    Transformer-based temporal feature fusion.

    Processes each spatial token across the temporal dimension.

    Input:
        (B, T, N, input_dim)

    Output:
        (B, T, N, hidden_dim)
    """

    def __init__(
        self,
        input_dim: int = 768,
        hidden_dim: int = 512,
        num_heads: int = 8,
        num_layers: int = 3,
        max_frames: int = 3,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or hidden_dim < 1:
            raise ValueError("Feature dimensions must be positive.")

        if num_heads < 1 or hidden_dim % num_heads != 0:
            raise ValueError(
                "hidden_dim must be divisible by num_heads."
            )

        if num_layers < 1:
            raise ValueError("num_layers must be at least 1.")

        if max_frames < 1:
            raise ValueError("max_frames must be at least 1.")

        if not 0.0 <= dropout < 1.0:
            raise ValueError("dropout must be in [0, 1).")

        self.input_projection = nn.Linear(input_dim, hidden_dim)

        self.temporal_embedding = nn.Parameter(
            torch.randn(1, max_frames, 1, hidden_dim) * 0.02
        )

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim * 4,
            dropout=dropout,
            batch_first=True,
            norm_first=True,
            activation="gelu",
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers,
            enable_nested_tensor=False,
        )

        self.norm = nn.LayerNorm(hidden_dim)
        self.max_frames = max_frames

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """
        Fuse temporal information for each spatial token.

        Args:
            features: (B, T, N, input_dim)

        Returns:
            Fused features: (B, T, N, hidden_dim)
        """

        if features.ndim != 4:
            raise ValueError(
                "Expected features with shape (B, T, N, D)."
            )

        if not features.is_floating_point():
            raise TypeError("Features must be floating-point tensors.")

        if features.shape[0] < 1:
            raise ValueError("Batch size must be positive.")

        if features.shape[1] < 1:
            raise ValueError("At least one temporal frame is required.")

        if features.shape[1] > self.max_frames:
            raise ValueError(
                f"Received {features.shape[1]} frames; "
                f"maximum supported is {self.max_frames}."
            )

        if features.shape[2] < 1:
            raise ValueError("At least one spatial token is required.")

        if features.shape[-1] != self.input_projection.in_features:
            raise ValueError(
                f"Expected input dimension "
                f"{self.input_projection.in_features}, "
                f"got {features.shape[-1]}."
            )

        # Keep temporal fusion in FP32 for numerical stability.
        with torch.autocast(
            device_type=features.device.type,
            enabled=False,
        ):
            features = features.float()

            projected = self.input_projection(features)

            projected = projected + self.temporal_embedding[
                :, :features.shape[1]
            ]

            batch_size, num_frames, num_tokens, hidden_dim = (
                projected.shape
            )

            # Each spatial token gets its own temporal sequence.
            temporal_sequence = projected.permute(
                0, 2, 1, 3
            ).reshape(
                batch_size * num_tokens,
                num_frames,
                hidden_dim,
            )

            fused = self.transformer(temporal_sequence)

            fused = fused.reshape(
                batch_size,
                num_tokens,
                num_frames,
                hidden_dim,
            ).permute(0, 2, 1, 3)

            return self.norm(fused)
