
"""Visualization utilities for OSCaR-Lite evaluation results."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class EvaluationVisualizer:
    """Create visual summaries of evaluation metrics."""

    STAGES = ("before", "during", "after", "transition")

    @staticmethod
    def _get_semantic_score(metrics: dict[str, Any]) -> float:
        """Support both real semantic metrics and legacy result fixtures."""

        semantic = metrics["semantic"]

        if "semantic_similarity" in semantic:
            return float(semantic["semantic_similarity"])

        if "mean_similarity" in semantic:
            return float(semantic["mean_similarity"])

        raise ValueError(
            "Stage is missing mean semantic similarity."
        )

    def plot_stage_metrics(
        self,
        evaluation: dict[str, Any],
    ) -> Figure:
        """Plot semantic similarity and ROUGE-L across temporal stages."""

        self._validate_evaluation(evaluation)

        semantic_scores = [
            self._get_semantic_score(evaluation["stages"][stage])
            for stage in self.STAGES
        ]

        rouge_scores = [
            float(evaluation["stages"][stage]["caption"]["rouge_l"])
            for stage in self.STAGES
        ]

        positions = list(range(len(self.STAGES)))
        width = 0.35

        figure, axis = plt.subplots(figsize=(10, 5))

        axis.bar(
            [position - width / 2 for position in positions],
            semantic_scores,
            width,
            label="Semantic Similarity",
        )
        axis.bar(
            [position + width / 2 for position in positions],
            rouge_scores,
            width,
            label="ROUGE-L",
        )

        axis.set_title("Caption Quality Across Temporal Stages")
        axis.set_xlabel("Temporal Stage")
        axis.set_ylabel("Score")
        axis.set_xticks(positions)
        axis.set_xticklabels([stage.title() for stage in self.STAGES])
        axis.set_ylim(0.0, 1.0)
        axis.legend()
        axis.grid(axis="y", linestyle="--", alpha=0.3)

        figure.tight_layout()
        return figure

    def plot_temporal_alignment(
        self,
        evaluation: dict[str, Any],
    ) -> Figure:
        """Plot semantic alignment across temporal stages."""

        self._validate_evaluation(evaluation)

        scores = [
            float(evaluation["temporal"]["stage_scores"][stage])
            for stage in self.STAGES
        ]

        figure, axis = plt.subplots(figsize=(9, 5))

        bars = axis.bar(
            [stage.title() for stage in self.STAGES],
            scores,
        )

        axis.bar_label(bars, fmt="%.3f", padding=3)
        axis.set_title("Temporal Stage Alignment")
        axis.set_xlabel("Temporal Stage")
        axis.set_ylabel("Semantic Similarity")
        axis.set_ylim(-1.0, 1.0)
        axis.grid(axis="y", linestyle="--", alpha=0.3)

        figure.tight_layout()
        return figure

    def save(
        self,
        figure: Figure,
        output_path: str | Path,
        dpi: int = 300,
    ) -> Path:
        """Save a visualization to disk."""

        if not isinstance(figure, Figure):
            raise TypeError("figure must be a Matplotlib Figure.")

        if dpi <= 0:
            raise ValueError("dpi must be positive.")

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(path, dpi=dpi, bbox_inches="tight")
        return path

    def _validate_evaluation(self, evaluation: dict[str, Any]) -> None:
        """Validate the evaluation structure required by visualizations."""

        if not isinstance(evaluation, dict):
            raise TypeError("Evaluation results must be a dictionary.")

        if "stages" not in evaluation or "temporal" not in evaluation:
            raise ValueError(
                "Evaluation results must contain stages and temporal metrics."
            )

        for stage in self.STAGES:
            if stage not in evaluation["stages"]:
                raise ValueError(f"Missing stage metrics for '{stage}'.")

            metrics = evaluation["stages"][stage]

            if "semantic" not in metrics or "caption" not in metrics:
                raise ValueError(
                    f"Stage '{stage}' must contain semantic and caption metrics."
                )

            self._get_semantic_score(metrics)

            if "rouge_l" not in metrics["caption"]:
                raise ValueError(f"Stage '{stage}' is missing ROUGE-L.")

        if "stage_scores" not in evaluation["temporal"]:
            raise ValueError("Temporal results are missing stage_scores.")

        for stage in self.STAGES:
            if stage not in evaluation["temporal"]["stage_scores"]:
                raise ValueError(
                    f"Temporal results are missing stage '{stage}'."
                )
