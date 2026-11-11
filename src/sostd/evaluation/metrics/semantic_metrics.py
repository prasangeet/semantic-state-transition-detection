
"""Semantic similarity metrics for generated captions."""

from __future__ import annotations

from typing import Any

import torch
import torch.nn.functional as F


class SemanticMetrics:
    """Evaluate semantic similarity between generated captions and references."""

    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL,
        device: str | torch.device = "cpu",
        model: Any | None = None,
    ) -> None:
        self.device = torch.device(device)

        if self.device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA was requested but is unavailable.")

        if model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise ImportError(
                    "Install sentence-transformers to use SemanticMetrics."
                ) from exc

            model = SentenceTransformer(
                model_name,
                device=str(self.device),
            )

        self.model = model
        self.model.eval()

    @staticmethod
    def _validate_inputs(
        predictions: list[str],
        references: list[str],
    ) -> None:
        if not isinstance(predictions, list):
            raise TypeError("predictions must be a list.")

        if not isinstance(references, list):
            raise TypeError("references must be a list.")

        if not predictions:
            raise ValueError("At least one caption pair is required.")

        if len(predictions) != len(references):
            raise ValueError(
                "Predictions and references must have equal lengths."
            )

        if not all(isinstance(text, str) for text in predictions):
            raise TypeError("All predictions must be strings.")

        if not all(isinstance(text, str) for text in references):
            raise TypeError("All references must be strings.")

    @torch.inference_mode()
    def compute(
        self,
        predictions: list[str],
        references: list[str],
        batch_size: int = 32,
    ) -> dict[str, Any]:
        """Compute pairwise cosine similarity and aggregate statistics."""

        self._validate_inputs(predictions, references)

        if batch_size < 1:
            raise ValueError("batch_size must be positive.")

        prediction_embeddings = self.model.encode(
            predictions,
            batch_size=batch_size,
            convert_to_tensor=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        reference_embeddings = self.model.encode(
            references,
            batch_size=batch_size,
            convert_to_tensor=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        if prediction_embeddings.shape != reference_embeddings.shape:
            raise ValueError(
                "Prediction and reference embedding shapes do not match."
            )

        similarities = F.cosine_similarity(
            prediction_embeddings,
            reference_embeddings,
            dim=-1,
        ).detach().float().cpu()

        return {
            "semantic_similarity": similarities.mean().item(),
            "semantic_similarity_std": similarities.std(
                unbiased=False
            ).item(),
            "per_sample_similarity": similarities.tolist(),
        }
