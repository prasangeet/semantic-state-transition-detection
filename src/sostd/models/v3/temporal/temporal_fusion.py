
from __future__ import annotations

import torch
import torch.nn as nn


class SpatioTemporalBlock(nn.Module):
    """
    Factorized spatiotemporal Transformer block.

    Applies spatial attention independently to each frame,
    followed by temporal attention independently to each
    spatial-token position.

    Input:
        (B, T, N, D)

    Output:
        (B, T, N, D)
    """

    def __init__(
        self,
        hidden_dim: int,
        num_heads: int,
        dropout: float,
    ) -> None:
        super().__init__()

        self.spatial_norm = nn.LayerNorm(hidden_dim)
        self.temporal_norm = nn.LayerNorm(hidden_dim)

        self.spatial_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True,
        )

        self.temporal_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True,
        )

        self.spatial_ffn_norm = nn.LayerNorm(hidden_dim)
        self.temporal_ffn_norm = nn.LayerNorm(hidden_dim)

        self.spatial_ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 4, hidden_dim),
            nn.Dropout(dropout),
        )

        self.temporal_ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 4),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 4, hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, T, N, D)

        Returns:
            (B, T, N, D)
        """

        batch_size, num_frames, num_tokens, hidden_dim = x.shape

        # Spatial attention:
        # Each frame independently attends to its visual tokens.

        spatial = x.reshape(
            batch_size * num_frames,
            num_tokens,
            hidden_dim,
        )

        normalized = self.spatial_norm(spatial)

        attended, _ = self.spatial_attention(
            normalized,
            normalized,
            normalized,
            need_weights=False,
        )

        spatial = spatial + attended

        spatial = spatial + self.spatial_ffn(
            self.spatial_ffn_norm(spatial)
        )

        x = spatial.reshape(
            batch_size,
            num_frames,
            num_tokens,
            hidden_dim,
        )

        # Temporal attention:
        # Each spatial-token position attends across frames.

        temporal = x.permute(
            0, 2, 1, 3
        ).reshape(
            batch_size * num_tokens,
            num_frames,
            hidden_dim,
        )

        normalized = self.temporal_norm(temporal)

        attended, _ = self.temporal_attention(
            normalized,
            normalized,
            normalized,
            need_weights=False,
        )

        temporal = temporal + attended

        temporal = temporal + self.temporal_ffn(
            self.temporal_ffn_norm(temporal)
        )

        x = temporal.reshape(
            batch_size,
            num_tokens,
            num_frames,
            hidden_dim,
        ).permute(
            0, 2, 1, 3
        )

        return x


class TemporalFusion(nn.Module):
    """
    Factorized spatiotemporal feature fusion for DINOv2-Large.

    Spatial attention models relationships between visual
    regions within each frame.

    Temporal attention models feature evolution across frames.

    V3 defaults:
        input_dim: 1024
        hidden_dim: 1024
        num_heads: 16
        num_layers: 4
        max_frames: 3

    Input:
        (B, T, N, 1024)

    Output:
        (B, T, N, 1024)
    """

    def __init__(
        self,
        input_dim: int = 1024,
        hidden_dim: int = 1024,
        num_heads: int = 16,
        num_layers: int = 4,
        max_frames: int = 3,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()

        if input_dim < 1 or hidden_dim < 1:
            raise ValueError(
                "Feature dimensions must be positive."
            )

        if num_heads < 1 or hidden_dim % num_heads != 0:
            raise ValueError(
                "hidden_dim must be divisible by num_heads."
            )

        if num_layers < 1:
            raise ValueError(
                "num_layers must be at least 1."
            )

        if max_frames < 1:
            raise ValueError(
                "max_frames must be at least 1."
            )

        if not 0.0 <= dropout < 1.0:
            raise ValueError(
                "dropout must be in [0, 1)."
            )

        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.num_layers = num_layers
        self.max_frames = max_frames

        self.input_projection = nn.Linear(
            input_dim,
            hidden_dim,
        )

        self.temporal_embedding = nn.Parameter(
            torch.randn(
                1,
                max_frames,
                1,
                hidden_dim,
            ) * 0.02
        )

        self.blocks = nn.ModuleList([
            SpatioTemporalBlock(
                hidden_dim=hidden_dim,
                num_heads=num_heads,
                dropout=dropout,
            )
            for _ in range(num_layers)
        ])

        self.output_norm = nn.LayerNorm(hidden_dim)

    def forward(
        self,
        features: torch.Tensor,
    ) -> torch.Tensor:
        """
        Fuse spatial and temporal information.

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
            raise TypeError(
                "Features must be floating-point tensors."
            )

        batch_size, num_frames, num_tokens, feature_dim = (
            features.shape
        )

        if batch_size < 1:
            raise ValueError(
                "Batch size must be positive."
            )

        if num_frames < 1:
            raise ValueError(
                "At least one temporal frame is required."
            )

        if num_frames > self.max_frames:
            raise ValueError(
                f"Received {num_frames} frames; "
                f"maximum supported is {self.max_frames}."
            )

        if num_tokens < 1:
            raise ValueError(
                "At least one spatial token is required."
            )

        if feature_dim != self.input_dim:
            raise ValueError(
                f"Expected input dimension {self.input_dim}, "
                f"got {feature_dim}."
            )

        # Keep fusion in FP32 for numerical stability.
        with torch.autocast(
            device_type=features.device.type,
            enabled=False,
        ):
            features = features.float()

            x = self.input_projection(features)

            x = x + self.temporal_embedding[:, :num_frames]

            for block in self.blocks:
                x = block(x)

            return self.output_norm(x)
