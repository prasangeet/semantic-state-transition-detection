
from __future__ import annotations

from typing import Literal

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import Dinov2Model


class DINOv2Encoder(nn.Module):
    """
    DINOv2 visual feature extractor.

    Supports:
        - DINOv2-Small: 384-dimensional features
        - DINOv2-Base:   768-dimensional features

    The backbone is frozen by default. Fine-tuning can be enabled
    explicitly when sufficient training resources are available.

    Input:
        images: (B, 3, H, W), RGB, floating point, range [0, 1]

    Output:
        features: (B, 257, hidden_size)
                  Token 0: CLS token
                  Tokens 1-256: patch tokens
    """

    MODEL_VARIANTS = {
        "small": {
            "model_name": "facebook/dinov2-small",
            "hidden_size": 384,
        },
        "base": {
            "model_name": "facebook/dinov2-base",
            "hidden_size": 768,
        },
    }

    IMAGE_SIZE = 224

    IMAGE_MEAN = (0.485, 0.456, 0.406)
    IMAGE_STD = (0.229, 0.224, 0.225)

    def __init__(
        self,
        variant: Literal["small", "base"] = "base",
        pretrained: bool = True,
        freeze_backbone: bool = True,
        image_size: int = IMAGE_SIZE,
    ) -> None:
        super().__init__()

        if variant not in self.MODEL_VARIANTS:
            raise ValueError(
                f"Unsupported DINOv2 variant: {variant}. "
                f"Choose from {list(self.MODEL_VARIANTS)}."
            )

        if image_size <= 0:
            raise ValueError("image_size must be positive.")

        self.variant = variant
        self.image_size = image_size
        self.freeze_backbone = freeze_backbone

        variant_config = self.MODEL_VARIANTS[variant]

        model_name = variant_config["model_name"]

        if pretrained:
            self.backbone = Dinov2Model.from_pretrained(model_name)
        else:
            from transformers import Dinov2Config

            config = Dinov2Config.from_pretrained(model_name)
            self.backbone = Dinov2Model(config)

        self.hidden_size = self.backbone.config.hidden_size
        self.patch_size = self.backbone.config.patch_size

        if self.hidden_size != variant_config["hidden_size"]:
            raise RuntimeError(
                f"Unexpected hidden size for {variant}: "
                f"{self.hidden_size}."
            )

        self.num_patches_per_side = image_size // self.patch_size

        if image_size % self.patch_size != 0:
            raise ValueError(
                f"image_size ({image_size}) must be divisible "
                f"by patch_size ({self.patch_size})."
            )

        self.num_patches = self.num_patches_per_side**2
        self.num_tokens = self.num_patches + 1

        self._configure_backbone()

        self.register_buffer(
            "image_mean",
            torch.tensor(self.IMAGE_MEAN).view(1, 3, 1, 1),
        )

        self.register_buffer(
            "image_std",
            torch.tensor(self.IMAGE_STD).view(1, 3, 1, 1),
        )

    def _configure_backbone(self) -> None:
        """Configure backbone gradients and training behavior."""

        self.backbone.requires_grad_(not self.freeze_backbone)

        if self.freeze_backbone:
            self.backbone.eval()

    def train(self, mode: bool = True) -> DINOv2Encoder:
        """
        Update module training mode.

        A frozen backbone always remains in evaluation mode.
        A trainable backbone follows the parent module's mode.
        """

        super().train(mode)

        if self.freeze_backbone:
            self.backbone.eval()

        return self

    def preprocess(self, images: torch.Tensor) -> torch.Tensor:
        """Resize and normalize input images."""

        if images.ndim != 4:
            raise ValueError(
                f"Expected (B, 3, H, W), got {tuple(images.shape)}."
            )

        if images.shape[1] != 3:
            raise ValueError(
                f"Expected 3 RGB channels, got {images.shape[1]}."
            )

        if not images.is_floating_point():
            raise TypeError("Images must be floating-point tensors.")

        images = images.to(
            device=self.image_mean.device,
            dtype=self.image_mean.dtype,
        )

        images = F.interpolate(
            images,
            size=(self.image_size, self.image_size),
            mode="bicubic",
            align_corners=False,
        )

        images = (images - self.image_mean) / self.image_std

        return images

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        """
        Extract CLS and patch-level visual representations.

        Args:
            images: RGB tensor of shape (B, 3, H, W).

        Returns:
            Visual tokens of shape (B, num_tokens, hidden_size).
        """

        images = self.preprocess(images)

        if self.freeze_backbone:
            with torch.no_grad():
                outputs = self.backbone(
                    pixel_values=images,
                    return_dict=True,
                )
        else:
            outputs = self.backbone(
                pixel_values=images,
                return_dict=True,
            )

        features = outputs.last_hidden_state

        if features.shape[1] != self.num_tokens:
            raise RuntimeError(
                f"Expected {self.num_tokens} tokens, "
                f"received {features.shape[1]}."
            )

        return features

    def get_output_dim(self) -> int:
        """Return the visual feature dimension."""
        return self.hidden_size

    def get_num_tokens(self) -> int:
        """Return the number of visual tokens."""
        return self.num_tokens
