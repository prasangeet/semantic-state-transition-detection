
"""Orchestration of OSCaR-Lite evaluation metrics.

Supports partially missing frame-level ground-truth captions.
V3 and V4 share the same evaluation interface.
"""

from __future__ import annotations

from typing import Any

from src.sostd.evaluation.metrics.caption_metrics import CaptionMetrics
from src.sostd.evaluation.metrics.semantic_metrics import SemanticMetrics
from src.sostd.evaluation.metrics.temporal_metrics import TemporalMetrics


class Evaluator:
    """Compute caption, semantic, and temporal evaluation metrics."""

    STAGES = ("before", "during", "after", "transition")
    FRAME_STAGES = ("before", "during", "after")

    def __init__(
        self,
        caption_metrics: CaptionMetrics | None = None,
        semantic_metrics: SemanticMetrics | None = None,
        temporal_metrics: TemporalMetrics | None = None,
    ) -> None:
        self.caption_metrics = caption_metrics or CaptionMetrics()
        self.semantic_metrics = semantic_metrics or SemanticMetrics()
        self.temporal_metrics = temporal_metrics or TemporalMetrics(
            semantic_metrics=self.semantic_metrics
        )

    @staticmethod
    def _valid_caption(value: Any) -> bool:
        """Check whether a caption is usable for metric computation."""

        return isinstance(value, str) and bool(value.strip())

    def evaluate(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str | None]],
    ) -> dict[str, Any]:
        """Evaluate predictions using available ground-truth references.

        Each stage is evaluated independently using only samples with
        valid ground truth for that stage.

        Temporal metrics use only samples with all four references.
        Missing references are never replaced with fabricated captions.
        """

        self._validate_inputs(predictions, references)

        stage_results: dict[str, dict[str, Any]] = {}
        valid_indices: dict[str, list[int]] = {}

        # ---------------------------------------------------------
        # Independent stage metrics
        # ---------------------------------------------------------

        for stage in self.STAGES:
            indices = [
                index
                for index, reference in enumerate(references)
                if self._valid_caption(reference.get(stage))
            ]

            valid_indices[stage] = indices

            stage_predictions = [
                predictions[index][stage]
                for index in indices
            ]

            stage_references = [
                references[index][stage].strip()
                for index in indices
            ]

            if not indices:
                stage_results[stage] = {
                    "caption": None,
                    "semantic": None,
                    "num_samples": 0,
                    "num_missing": len(predictions),
                    "coverage": 0.0,
                    "status": "skipped_no_valid_references",
                }
                continue

            stage_results[stage] = {
                "caption": self.caption_metrics.compute(
                    stage_predictions,
                    stage_references,
                ),
                "semantic": self.semantic_metrics.compute(
                    stage_predictions,
                    stage_references,
                ),
                "num_samples": len(indices),
                "num_missing": len(predictions) - len(indices),
                "coverage": len(indices) / len(predictions),
                "status": "computed",
            }

        # ---------------------------------------------------------
        # Temporal metrics
        # ---------------------------------------------------------

        complete_indices = [
            index
            for index, reference in enumerate(references)
            if all(
                self._valid_caption(reference.get(stage))
                for stage in self.STAGES
            )
        ]

        if complete_indices:
            temporal_predictions = [
                predictions[index]
                for index in complete_indices
            ]

            temporal_references = [
                references[index]
                for index in complete_indices
            ]

            temporal_result = self.temporal_metrics.compute(
                temporal_predictions,
                temporal_references,
            )

            temporal_status = "computed"

        else:
            temporal_result = None
            temporal_status = "skipped_no_complete_references"

        return {
            "num_samples": len(predictions),
            "stages": stage_results,
            "temporal": temporal_result,
            "reference_coverage": {
                stage: {
                    "valid": len(valid_indices[stage]),
                    "missing": (
                        len(predictions) - len(valid_indices[stage])
                    ),
                    "fraction": (
                        len(valid_indices[stage]) / len(predictions)
                    ),
                }
                for stage in self.STAGES
            },
            "temporal_coverage": {
                "valid": len(complete_indices),
                "missing": len(predictions) - len(complete_indices),
                "fraction": len(complete_indices) / len(predictions),
                "status": temporal_status,
            },
        }

    def _validate_inputs(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str | None]],
    ) -> None:
        """Validate predictions and references without rejecting missing
        frame references.
        """

        if not isinstance(predictions, list) or not isinstance(
            references, list
        ):
            raise TypeError(
                "Predictions and references must be lists."
            )

        if len(predictions) != len(references):
            raise ValueError(
                "Predictions and references must have equal lengths."
            )

        if not predictions:
            raise ValueError(
                "Predictions and references cannot be empty."
            )

        for index, prediction in enumerate(predictions):
            if not isinstance(prediction, dict):
                raise TypeError(
                    f"predictions[{index}] must be a dictionary."
                )

            for stage in self.STAGES:
                value = prediction.get(stage)

                if not self._valid_caption(value):
                    raise ValueError(
                        f"predictions[{index}]['{stage}'] "
                        "must be a non-empty string."
                    )

        for index, reference in enumerate(references):
            if not isinstance(reference, dict):
                raise TypeError(
                    f"references[{index}] must be a dictionary."
                )

            # A transition reference is required for every sample.
            transition = reference.get("transition")

            if not self._valid_caption(transition):
                raise ValueError(
                    f"references[{index}]['transition'] "
                    "must be a non-empty string."
                )

            # Frame references may be None or empty.
            for stage in self.FRAME_STAGES:
                value = reference.get(stage)

                if value is not None and not isinstance(value, str):
                    raise TypeError(
                        f"references[{index}]['{stage}'] must be "
                        "a string or None."
                    )
