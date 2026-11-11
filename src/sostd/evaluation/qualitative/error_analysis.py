
"""Qualitative error analysis for OSCaR-Lite caption predictions."""

from __future__ import annotations

from typing import Any

from src.sostd.evaluation.metrics.semantic_metrics import SemanticMetrics


class ErrorAnalyzer:
    """Identify low-similarity predictions for manual inspection."""

    STAGES = ("before", "during", "after", "transition")

    def __init__(
        self,
        semantic_metrics: SemanticMetrics | None = None,
        similarity_threshold: float = 0.5,
    ) -> None:
        if not isinstance(similarity_threshold, (int, float)):
            raise TypeError("similarity_threshold must be numeric.")

        if not 0.0 <= similarity_threshold <= 1.0:
            raise ValueError("similarity_threshold must be between 0 and 1.")

        self.semantic_metrics = semantic_metrics or SemanticMetrics()
        self.similarity_threshold = float(similarity_threshold)

    @staticmethod
    def _extract_scores(
        result: dict[str, Any],
    ) -> tuple[float, list[float], float]:
        """Extract scores and their valid lower bound from metric output."""

        if "semantic_similarity" in result:
            mean_similarity = result["semantic_similarity"]
            similarities = result.get("per_sample_similarity")
            lower_bound = -1.0
        else:
            mean_similarity = result.get("mean_similarity")
            similarities = result.get("similarities")
            lower_bound = 0.0

        if not isinstance(mean_similarity, (int, float)):
            raise KeyError(
                "Semantic metrics must return 'semantic_similarity' "
                "or 'mean_similarity'."
            )

        if not isinstance(similarities, list):
            raise KeyError(
                "Semantic metrics must return 'per_sample_similarity' "
                "or 'similarities'."
            )

        return float(mean_similarity), similarities, lower_bound

    def analyze(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str]],
    ) -> dict[str, Any]:
        """Find predictions below the configured similarity threshold."""

        self._validate_inputs(predictions, references)

        errors: list[dict[str, Any]] = []
        stage_summary: dict[str, dict[str, Any]] = {}

        for stage in self.STAGES:
            stage_predictions = [item[stage] for item in predictions]
            stage_references = [item[stage] for item in references]

            result = self.semantic_metrics.compute(
                stage_predictions,
                stage_references,
            )

            mean_similarity, similarities, lower_bound = (
                self._extract_scores(result)
            )

            if len(similarities) != len(predictions):
                raise ValueError(
                    f"Semantic metrics returned an invalid number of "
                    f"similarities for stage '{stage}'."
                )

            if not lower_bound <= mean_similarity <= 1.0:
                raise ValueError(
                    f"Mean similarity must be between "
                    f"{lower_bound:g} and 1."
                )

            stage_errors = 0

            for index, similarity in enumerate(similarities):
                if not isinstance(similarity, (int, float)):
                    raise TypeError("Similarity scores must be numeric.")

                score = float(similarity)

                if not lower_bound <= score <= 1.0:
                    raise ValueError(
                        f"Similarity scores must be between "
                        f"{lower_bound:g} and 1."
                    )

                if score < self.similarity_threshold:
                    stage_errors += 1
                    errors.append(
                        {
                            "sample_index": index,
                            "stage": stage,
                            "prediction": stage_predictions[index],
                            "reference": stage_references[index],
                            "similarity": score,
                            "error_type": "low_semantic_similarity",
                        }
                    )

            stage_summary[stage] = {
                "num_samples": len(predictions),
                "num_low_similarity": stage_errors,
                "low_similarity_rate": stage_errors / len(predictions),
                "mean_similarity": mean_similarity,
            }

        return {
            "num_samples": len(predictions),
            "similarity_threshold": self.similarity_threshold,
            "num_errors": len(errors),
            "errors": errors,
            "stage_summary": stage_summary,
        }

    def _validate_inputs(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str]],
    ) -> None:
        if not isinstance(predictions, list) or not isinstance(references, list):
            raise TypeError("Predictions and references must be lists.")

        if len(predictions) != len(references):
            raise ValueError(
                "Predictions and references must have equal lengths."
            )

        if not predictions:
            raise ValueError(
                "Predictions and references cannot be empty."
            )

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
