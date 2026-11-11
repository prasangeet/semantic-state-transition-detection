
"""Generate Markdown reports from OSCaR-Lite evaluation results."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ReportGenerator:
    """Format evaluation results as a Markdown report."""

    STAGES = ("before", "during", "after", "transition")

    def generate(
        self,
        evaluation: dict[str, Any],
        error_analysis: dict[str, Any] | None = None,
    ) -> str:
        """Generate a Markdown report from evaluation outputs."""

        self._validate_evaluation(evaluation)

        lines = [
            "# OSCaR-Lite Evaluation Report",
            "",
            f"- Generated: {datetime.now(timezone.utc).isoformat()}",
            f"- Samples evaluated: {evaluation['num_samples']}",
            "",
            "## Temporal Stage Metrics",
            "",
            "| Stage | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | Semantic Similarity |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]

        for stage in self.STAGES:
            metrics = evaluation["stages"][stage]
            caption = metrics["caption"]
            semantic = metrics["semantic"]

            semantic_score = self._get_semantic_score(semantic)

            lines.append(
                f"| {stage.title()} "
                f"| {self._format_metric(caption, 'bleu_1')} "
                f"| {self._format_metric(caption, 'bleu_2')} "
                f"| {self._format_metric(caption, 'bleu_3')} "
                f"| {self._format_metric(caption, 'bleu_4')} "
                f"| {self._format_metric(caption, 'rouge_l')} "
                f"| {self._format_number(semantic_score)} |"
            )

        temporal = evaluation["temporal"]

        lines.extend([
            "",
            "## Temporal Alignment",
            "",
            f"- Overall temporal score: "
            f"{self._format_number(temporal['temporal_score'])}",
            "",
            "| Stage | Semantic Alignment |",
            "|---|---:|",
        ])

        for stage in self.STAGES:
            score = temporal["stage_scores"][stage]
            lines.append(
                f"| {stage.title()} | {self._format_number(score)} |"
            )

        if error_analysis is not None:
            self._append_error_analysis(lines, error_analysis)

        lines.extend([
            "",
            "## Interpretation Notes",
            "",
            "- BLEU and ROUGE-L measure lexical overlap with reference captions.",
            "- Semantic similarity measures embedding-based caption similarity.",
            "- Temporal alignment aggregates semantic similarity across the four stages.",
            "- Low-similarity cases are candidates for manual review, not confirmed factual errors.",
            "",
        ])

        return "\n".join(lines)

    def save(
        self,
        report: str,
        output_path: str | Path,
    ) -> Path:
        """Save a generated Markdown report."""

        if not isinstance(report, str) or not report.strip():
            raise ValueError("Report must be a non-empty string.")

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report, encoding="utf-8")

        return path

    def _append_error_analysis(
        self,
        lines: list[str],
        error_analysis: dict[str, Any],
    ) -> None:
        required = {
            "num_samples",
            "similarity_threshold",
            "num_errors",
            "errors",
            "stage_summary",
        }
        missing = required.difference(error_analysis)

        if missing:
            raise ValueError(
                f"Error analysis is missing fields: {sorted(missing)}"
            )

        lines.extend([
            "",
            "## Qualitative Error Analysis",
            "",
            f"- Similarity threshold: "
            f"{self._format_number(error_analysis['similarity_threshold'])}",
            f"- Low-similarity cases: {error_analysis['num_errors']}",
            "",
            "| Stage | Low-Similarity Cases | Rate | Mean Similarity |",
            "|---|---:|---:|---:|",
        ])

        for stage in self.STAGES:
            if stage not in error_analysis["stage_summary"]:
                raise ValueError(
                    f"Error analysis is missing stage '{stage}'."
                )

            summary = error_analysis["stage_summary"][stage]

            lines.append(
                f"| {stage.title()} "
                f"| {summary['num_low_similarity']} "
                f"| {self._format_number(summary['low_similarity_rate'])} "
                f"| {self._format_number(summary['mean_similarity'])} |"
            )

        if error_analysis["errors"]:
            lines.extend([
                "",
                "### Cases for Manual Inspection",
                "",
            ])

            for error in error_analysis["errors"]:
                lines.extend([
                    f"#### Sample {error['sample_index']} — "
                    f"{error['stage'].title()}",
                    "",
                    f"- Similarity: {self._format_number(error['similarity'])}",
                    f"- Prediction: {error['prediction']}",
                    f"- Reference: {error['reference']}",
                    "",
                ])

    def _validate_evaluation(self, evaluation: dict[str, Any]) -> None:
        if not isinstance(evaluation, dict):
            raise TypeError("Evaluation results must be a dictionary.")

        required = {"num_samples", "stages", "temporal"}
        missing = required.difference(evaluation)

        if missing:
            raise ValueError(
                f"Evaluation results are missing fields: {sorted(missing)}"
            )

        if (
            not isinstance(evaluation["num_samples"], int)
            or isinstance(evaluation["num_samples"], bool)
            or evaluation["num_samples"] <= 0
        ):
            raise ValueError("num_samples must be a positive integer.")

        if not isinstance(evaluation["stages"], dict):
            raise TypeError("Evaluation stages must be a dictionary.")

        if not isinstance(evaluation["temporal"], dict):
            raise TypeError("Temporal results must be a dictionary.")

        for stage in self.STAGES:
            if stage not in evaluation["stages"]:
                raise ValueError(
                    f"Evaluation results are missing stage '{stage}'."
                )

            metrics = evaluation["stages"][stage]

            if not isinstance(metrics, dict):
                raise TypeError(f"Metrics for stage '{stage}' must be a dictionary.")

            if "caption" not in metrics or "semantic" not in metrics:
                raise ValueError(
                    f"Stage '{stage}' must contain caption and semantic metrics."
                )

            self._get_semantic_score(metrics["semantic"])

        temporal = evaluation["temporal"]

        if "temporal_score" not in temporal or "stage_scores" not in temporal:
            raise ValueError("Temporal results are incomplete.")

        for stage in self.STAGES:
            if stage not in temporal["stage_scores"]:
                raise ValueError(
                    f"Temporal results are missing stage '{stage}'."
                )

    @staticmethod
    def _get_semantic_score(metrics: dict[str, Any]) -> float:
        """Read semantic similarity using either supported result key."""

        if "semantic_similarity" in metrics:
            return float(metrics["semantic_similarity"])

        if "mean_similarity" in metrics:
            return float(metrics["mean_similarity"])

        raise ValueError("Semantic metrics are missing their similarity score.")

    @staticmethod
    def _format_number(value: float) -> str:
        return f"{float(value):.4f}"

    def _format_metric(self, metrics: dict[str, Any], key: str) -> str:
        return self._format_number(metrics.get(key, 0.0))
