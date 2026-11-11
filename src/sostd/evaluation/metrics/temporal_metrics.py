
"""Temporal-stage alignment metrics for OSCaR-Lite predictions."""

from __future__ import annotations

from typing import Any

from src.sostd.evaluation.metrics.semantic_metrics import SemanticMetrics


class TemporalMetrics:
    """Evaluate caption alignment across ordered temporal stages."""

    STAGES = ("before", "during", "after", "transition")

    def __init__(self, semantic_metrics: SemanticMetrics | None = None) -> None:
        self.semantic_metrics = semantic_metrics or SemanticMetrics()

    @staticmethod
    def _get_similarity_score(result: dict[str, Any]) -> float:
        """Read the aggregate score from supported semantic metric outputs."""

        if "semantic_similarity" in result:
            return float(result["semantic_similarity"])

        if "mean_similarity" in result:
            return float(result["mean_similarity"])

        raise KeyError(
            "Semantic metric result must contain either "
            "'semantic_similarity' or 'mean_similarity'."
        )

    def compute(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str]],
    ) -> dict[str, Any]:
        """Compute per-stage semantic alignment and aggregate temporal score."""

        if not isinstance(predictions, list) or not isinstance(references, list):
            raise TypeError("Predictions and references must be lists.")

        if len(predictions) != len(references):
            raise ValueError("Predictions and references must have equal lengths.")

        if not predictions:
            raise ValueError("Predictions and references cannot be empty.")

        for collection_name, collection in (
            ("predictions", predictions),
            ("references", references),
        ):
            for index, item in enumerate(collection):
                if not isinstance(item, dict):
                    raise TypeError(
                        f"{collection_name}[{index}] must be a dictionary."
                    )

                for stage in self.STAGES:
                    value = item.get(stage)
                    if not isinstance(value, str) or not value.strip():
                        raise ValueError(
                            f"{collection_name}[{index}]['{stage}'] "
                            "must be a non-empty string."
                        )

        stage_results: dict[str, dict[str, Any]] = {}

        for stage in self.STAGES:
            stage_predictions = [item[stage] for item in predictions]
            stage_references = [item[stage] for item in references]

            stage_results[stage] = self.semantic_metrics.compute(
                stage_predictions,
                stage_references,
            )

        stage_scores = {
            stage: self._get_similarity_score(result)
            for stage, result in stage_results.items()
        }

        temporal_score = sum(stage_scores.values()) / len(self.STAGES)

        return {
            "temporal_score": temporal_score,
            "stage_scores": stage_scores,
            "stage_details": stage_results,
            "num_samples": len(predictions),
        }
