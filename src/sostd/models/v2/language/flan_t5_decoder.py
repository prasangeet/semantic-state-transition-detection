
from __future__ import annotations

from typing import Any

import torch
import torch.nn as nn
from transformers import T5ForConditionalGeneration


class FlanT5Decoder(nn.Module):
    """
    Language decoder conditioned on visual embeddings.

    Supports FLAN-T5-Small and FLAN-T5-Base.

    The decoder accepts either:
        (B, T, K, D): temporal visual tokens
        (B, S, D): flattened visual sequence

    Visual embeddings must have the same final dimension as
    the selected T5 model's d_model.

    Default:
        google/flan-t5-base (d_model=768)
    """

    MODEL_VARIANTS = {
        "small": "google/flan-t5-small",
        "base": "google/flan-t5-base",
    }

    MODEL_NAME = MODEL_VARIANTS["base"]

    def __init__(
        self,
        model_name: str = MODEL_NAME,
        freeze_backbone: bool = True,
        model: nn.Module | None = None,
    ) -> None:
        super().__init__()

        self.backbone = (
            model
            if model is not None
            else T5ForConditionalGeneration.from_pretrained(model_name)
        )

        self.hidden_dim = self.backbone.config.d_model
        self.freeze_backbone = freeze_backbone

        self.backbone.requires_grad_(not freeze_backbone)

        if freeze_backbone:
            self.backbone.eval()

    def train(self, mode: bool = True) -> FlanT5Decoder:
        """Keep a frozen decoder in evaluation mode."""

        super().train(mode)

        if self.freeze_backbone:
            self.backbone.eval()

        return self

    def _prepare_visual_inputs(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Validate and flatten visual embeddings.

        Returns:
            embeddings: (B, S, D)
            attention_mask: (B, S)
        """

        if not isinstance(visual_embeddings, torch.Tensor):
            raise TypeError("visual_embeddings must be a torch.Tensor.")

        if visual_embeddings.ndim == 4:
            batch_size, num_frames, num_tokens, hidden_dim = (
                visual_embeddings.shape
            )

            if num_frames < 1 or num_tokens < 1:
                raise ValueError(
                    "Visual embeddings must contain at least "
                    "one frame and one token."
                )

            embeddings = visual_embeddings.reshape(
                batch_size,
                num_frames * num_tokens,
                hidden_dim,
            )

            expected_mask_shape = (
                batch_size,
                num_frames,
                num_tokens,
            )

            if attention_mask is not None:
                if attention_mask.shape == expected_mask_shape:
                    attention_mask = attention_mask.reshape(
                        batch_size,
                        num_frames * num_tokens,
                    )

                elif attention_mask.shape != (
                    batch_size,
                    num_frames * num_tokens,
                ):
                    raise ValueError(
                        "Attention mask must have shape "
                        f"{expected_mask_shape} or "
                        f"{(batch_size, num_frames * num_tokens)}."
                    )

        elif visual_embeddings.ndim == 3:
            batch_size, sequence_length, hidden_dim = (
                visual_embeddings.shape
            )

            if sequence_length < 1:
                raise ValueError(
                    "Visual embeddings must contain at least one token."
                )

            embeddings = visual_embeddings

            if attention_mask is not None and attention_mask.shape != (
                batch_size,
                sequence_length,
            ):
                raise ValueError(
                    "Attention mask must match the visual sequence shape."
                )

        else:
            raise ValueError(
                "Expected visual embeddings with shape "
                "(B, T, K, D) or (B, S, D), "
                f"got {tuple(visual_embeddings.shape)}."
            )

        if hidden_dim != self.hidden_dim:
            raise ValueError(
                f"Decoder expects embedding dimension "
                f"{self.hidden_dim}, but received {hidden_dim}. "
                "Check the visual projection dimension."
            )

        if not embeddings.is_floating_point():
            raise TypeError("Visual embeddings must be floating-point.")

        if attention_mask is None:
            attention_mask = torch.ones(
                embeddings.shape[:2],
                dtype=torch.long,
                device=embeddings.device,
            )
        else:
            attention_mask = attention_mask.to(
                device=embeddings.device,
            )

        return embeddings, attention_mask

    def forward(
        self,
        visual_embeddings: torch.Tensor,
        labels: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
    ) -> Any:
        """
        Teacher-forced training.

        T5 executes in FP32 while allowing gradients to propagate
        through the decoder into the visual embeddings.
        """

        if labels.ndim != 2:
            raise ValueError("Labels must have shape (B, L).")

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        if labels.shape[0] != embeddings.shape[0]:
            raise ValueError(
                "Visual embeddings and labels must have matching "
                "batch dimensions."
            )

        labels = labels.to(device=embeddings.device)

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            outputs = self.backbone(
                inputs_embeds=embeddings.float(),
                attention_mask=attention_mask,
                labels=labels,
                return_dict=True,
            )

        return outputs

    @torch.no_grad()
    def generate(
        self,
        visual_embeddings: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
        max_new_tokens: int = 96,
        **generation_kwargs: Any,
    ) -> torch.Tensor:
        """
        Autoregressively generate a description conditioned
        on visual embeddings.
        """

        if max_new_tokens < 1:
            raise ValueError("max_new_tokens must be at least 1.")

        if "inputs_embeds" in generation_kwargs:
            raise ValueError("Do not pass inputs_embeds in generation_kwargs.")

        if "attention_mask" in generation_kwargs:
            raise ValueError("Pass attention_mask through the explicit argument.")

        if "max_new_tokens" in generation_kwargs:
            raise ValueError("Pass max_new_tokens through the explicit argument.")

        embeddings, attention_mask = self._prepare_visual_inputs(
            visual_embeddings,
            attention_mask,
        )

        with torch.autocast(
            device_type=embeddings.device.type,
            enabled=False,
        ):
            generated_ids = self.backbone.generate(
                inputs_embeds=embeddings.float(),
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                **generation_kwargs,
            )

        return generated_ids
