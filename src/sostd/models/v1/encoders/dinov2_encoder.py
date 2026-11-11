
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import Dinov2Model


class DINOv2Encoder(nn.Module):
    """Frozen DINOv2-Small visual feature extractor."""

    MODEL_NAME = "facebook/dinov2-small"

    IMAGE_SIZE = 224
    HIDDEN_SIZE = 384

    IMAGE_MEAN = (0.485, 0.456, 0.406)
    IMAGE_STD = (0.229, 0.224, 0.225)

    def __init__(self) -> None:
        super().__init__()

        self.backbone = Dinov2Model.from_pretrained(
            self.MODEL_NAME
        )

        self.backbone.requires_grad_(False)
        self.backbone.eval()

        self.register_buffer(
            "image_mean",
            torch.tensor(self.IMAGE_MEAN).view(1, 3, 1, 1),
        )

        self.register_buffer(
            "image_std",
            torch.tensor(self.IMAGE_STD).view(1, 3, 1, 1),
        )

    def train(self, mode: bool = True):
        """Keep the frozen backbone in evaluation mode."""
        super().train(mode)
        self.backbone.eval()
        return self

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        """
        Extract visual tokens.

        Args:
            images: RGB tensor of shape (B, 3, H, W),
                    with values in [0, 1].

        Returns:
            Tensor of shape (B, 257, 384).
            Token 0 is the CLS token; remaining tokens
            represent image patches.
        """

        if images.ndim != 4:
            raise ValueError(
                f"Expected images with shape (B, 3, H, W), "
                f"got {tuple(images.shape)}."
            )

        if images.shape[1] != 3:
            raise ValueError("Expected three RGB channels.")

        if not images.is_floating_point():
            raise TypeError("Images must be floating-point tensors.")

        images = images.to(
            device=self.image_mean.device,
            dtype=self.image_mean.dtype,
        )

        images = F.interpolate(
            images,
            size=(self.IMAGE_SIZE, self.IMAGE_SIZE),
            mode="bilinear",
            align_corners=False,
        )

        images = (images - self.image_mean) / self.image_std

        with torch.no_grad():
            outputs = self.backbone(
                pixel_values=images,
                return_dict=True,
            )

        return outputs.last_hidden_state
