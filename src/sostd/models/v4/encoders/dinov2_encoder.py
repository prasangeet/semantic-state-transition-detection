
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F

from transformers import Dinov2Model


class DINOv2Encoder(nn.Module):
    """
    DINOv2-Large visual feature extractor.

    Supports three training configurations:

        1. Frozen:
           freeze_backbone=True, unfreeze_last_n_layers=0

        2. Selective fine-tuning:
           freeze_backbone=True, unfreeze_last_n_layers=4

        3. Full fine-tuning:
           freeze_backbone=False, unfreeze_last_n_layers=0

    Architecture:
        Model: facebook/dinov2-large
        Hidden dimension: 1024
        Transformer layers: 24
        Patch size: 14

    Input:
        images: (B, 3, H, W), RGB, floating point, range [0, 1]

    Output:
        features: (B, 257, 1024)
            Token 0: CLS token
            Tokens 1-256: patch tokens
    """

    MODEL_NAME = "facebook/dinov2-large"

    HIDDEN_SIZE = 1024
    NUM_LAYERS = 24
    PATCH_SIZE = 14

    IMAGE_SIZE = 224

    IMAGE_MEAN = (0.485, 0.456, 0.406)
    IMAGE_STD = (0.229, 0.224, 0.225)

    def __init__(
        self,
        pretrained: bool = True,
        freeze_backbone: bool = True,
        unfreeze_last_n_layers: int = 0,
        image_size: int = IMAGE_SIZE,
    ) -> None:
        super().__init__()

        if image_size <= 0:
            raise ValueError("image_size must be positive.")

        if image_size % self.PATCH_SIZE != 0:
            raise ValueError(
                f"image_size ({image_size}) must be divisible "
                f"by patch_size ({self.PATCH_SIZE})."
            )

        if not isinstance(unfreeze_last_n_layers, int):
            raise TypeError(
                "unfreeze_last_n_layers must be an integer."
            )

        if not 0 <= unfreeze_last_n_layers <= self.NUM_LAYERS:
            raise ValueError(
                f"unfreeze_last_n_layers must be between "
                f"0 and {self.NUM_LAYERS}."
            )

        if not freeze_backbone and unfreeze_last_n_layers > 0:
            raise ValueError(
                "unfreeze_last_n_layers must be 0 when "
                "freeze_backbone=False. Full fine-tuning already "
                "unfreezes the entire backbone."
            )

        self.image_size = image_size
        self.freeze_backbone = freeze_backbone
        self.unfreeze_last_n_layers = unfreeze_last_n_layers

        self.is_fully_frozen = (
            freeze_backbone and unfreeze_last_n_layers == 0
        )

        self.is_selectively_finetuned = (
            freeze_backbone and unfreeze_last_n_layers > 0
        )

        if pretrained:
            self.backbone = Dinov2Model.from_pretrained(
                self.MODEL_NAME
            )
        else:
            from transformers import Dinov2Config

            config = Dinov2Config.from_pretrained(
                self.MODEL_NAME
            )

            self.backbone = Dinov2Model(config)

        self.hidden_size = self.backbone.config.hidden_size
        self.patch_size = self.backbone.config.patch_size

        if self.hidden_size != self.HIDDEN_SIZE:
            raise RuntimeError(
                f"Expected hidden size {self.HIDDEN_SIZE}, "
                f"received {self.hidden_size}."
            )

        if self.patch_size != self.PATCH_SIZE:
            raise RuntimeError(
                f"Expected patch size {self.PATCH_SIZE}, "
                f"received {self.patch_size}."
            )

        self.encoder_layers = self.backbone.encoder.layer
        self.num_layers = len(self.encoder_layers)

        if self.num_layers != self.NUM_LAYERS:
            raise RuntimeError(
                f"Expected {self.NUM_LAYERS} transformer layers, "
                f"received {self.num_layers}."
            )

        self.num_patches_per_side = image_size // self.patch_size
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
        """Configure frozen and trainable backbone parameters."""

        if not self.freeze_backbone:
            self.backbone.requires_grad_(True)
            return

        # Freeze the complete backbone first.
        self.backbone.requires_grad_(False)

        # Selectively unfreeze the final transformer blocks.
        if self.unfreeze_last_n_layers > 0:
            for layer in self.encoder_layers[-self.unfreeze_last_n_layers:]:
                layer.requires_grad_(True)

        self._configure_training_modes()

    def _configure_training_modes(self) -> None:
        """
        Keep frozen components in evaluation mode.

        In selective fine-tuning mode:
            - Embeddings remain in evaluation mode.
            - Earlier transformer blocks remain in evaluation mode.
            - Final selected blocks follow the parent training mode.
            - Final layer normalization remains in evaluation mode.
        """

        if self.is_fully_frozen:
            self.backbone.eval()
            return

        if self.is_selectively_finetuned:
            self.backbone.embeddings.eval()

            for layer in self.encoder_layers[
                :-self.unfreeze_last_n_layers
            ]:
                layer.eval()

            self.backbone.layernorm.eval()

    def train(self, mode: bool = True) -> DINOv2Encoder:
        """
        Update training mode without enabling training behavior
        in frozen components.
        """

        super().train(mode)

        self._configure_training_modes()

        return self

    def preprocess(self, images: torch.Tensor) -> torch.Tensor:
        """Resize and normalize input images."""

        if images.ndim != 4:
            raise ValueError(
                f"Expected (B, 3, H, W), got {tuple(images.shape)}."
            )

        if images.shape[0] == 0:
            raise ValueError("Batch size must be greater than zero.")

        if images.shape[1] != 3:
            raise ValueError(
                f"Expected 3 RGB channels, got {images.shape[1]}."
            )

        if not images.is_floating_point():
            raise TypeError(
                "Images must be floating-point tensors."
            )

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
            Visual tokens of shape (B, num_tokens, 1024).
        """

        images = self.preprocess(images)

        if self.is_fully_frozen:
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

        if features.shape[2] != self.hidden_size:
            raise RuntimeError(
                f"Expected hidden dimension {self.hidden_size}, "
                f"received {features.shape[2]}."
            )

        return features

    def get_output_dim(self) -> int:
        """Return the visual feature dimension."""
        return self.hidden_size

    def get_num_tokens(self) -> int:
        """Return the number of visual tokens."""
        return self.num_tokens

    def get_num_trainable_parameters(self) -> int:
        """Return the number of trainable backbone parameters."""
        return sum(
            parameter.numel()
            for parameter in self.backbone.parameters()
            if parameter.requires_grad
        )

    def get_num_parameters(self) -> int:
        """Return the total number of backbone parameters."""
        return sum(
            parameter.numel()
            for parameter in self.backbone.parameters()
        )
