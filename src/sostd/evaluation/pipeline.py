
"""End-to-end OSCaR-Lite evaluation pipeline."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from src.sostd.evaluation.config import EvaluationConfig
from src.sostd.evaluation.evaluation_runner import EvaluationRunner
from src.sostd.evaluation.evaluator import Evaluator
from src.sostd.evaluation.qualitative.error_analysis import ErrorAnalyzer
from src.sostd.evaluation.reporting.report_generator import ReportGenerator
from src.sostd.evaluation.reporting.visualization import EvaluationVisualizer
from src.sostd.evaluation.reporting.visual_comparison_report import (
    VisualComparisonReportGenerator,
)


class EvaluationPipeline:
    """Run inference, evaluate captions, and save evaluation artifacts."""

    def __init__(
        self,
        config: EvaluationConfig,
        runner_factory: Callable[..., Any] = EvaluationRunner,
        evaluator: Evaluator | None = None,
        error_analyzer: ErrorAnalyzer | None = None,
        report_generator: ReportGenerator | None = None,
        visualizer: EvaluationVisualizer | None = None,
        visual_comparison_generator: (
            VisualComparisonReportGenerator | None
        ) = None,
    ) -> None:
        self.config = config
        self.runner_factory = runner_factory
        self.evaluator = evaluator or Evaluator()

        self.error_analyzer = error_analyzer or ErrorAnalyzer(
            semantic_metrics=self.evaluator.semantic_metrics
        )

        self.report_generator = report_generator or ReportGenerator()
        self.visualizer = visualizer or EvaluationVisualizer()

        self.visual_comparison_generator = (
            visual_comparison_generator
            or VisualComparisonReportGenerator()
        )

    def run(self) -> dict[str, Any]:
        """Execute evaluation and persist all generated artifacts."""

        runner = self.runner_factory(config=self.config)
        inference_results = runner.run()

        self._validate_inference_results(inference_results)

        predictions = inference_results["predictions"]
        references = inference_results["references"]
        metadata = inference_results["metadata"]

        evaluation = self.evaluator.evaluate(
            predictions,
            references,
        )

        error_analysis = self.error_analyzer.analyze(
            predictions,
            references,
        )

        report = self.report_generator.generate(
            evaluation,
            error_analysis,
        )

        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        results = {
            "split": inference_results["split"],
            "num_samples": inference_results["num_samples"],
            "predictions": predictions,
            "references": references,
            "metadata": metadata,
            "evaluation": evaluation,
            "error_analysis": error_analysis,
        }

        # Save structured evaluation results.
        results_path = output_dir / "results.json"
        results_path.write_text(
            json.dumps(
                results,
                indent=2,
                ensure_ascii=False,
                default=str,
            ),
            encoding="utf-8",
        )

        # Save the existing Markdown evaluation report.
        report_path = self.report_generator.save(
            report,
            output_dir / "report.md",
        )

        # Generate the existing aggregate stage metrics chart.
        stage_figure = self.visualizer.plot_stage_metrics(evaluation)

        try:
            stage_chart_path = self.visualizer.save(
                stage_figure,
                output_dir / "stage_metrics.png",
            )
        finally:
            self._close_figure(stage_figure)

        # Generate the existing temporal alignment chart.
        temporal_figure = self.visualizer.plot_temporal_alignment(
            evaluation
        )

        try:
            temporal_chart_path = self.visualizer.save(
                temporal_figure,
                output_dir / "temporal_alignment.png",
            )
        finally:
            self._close_figure(temporal_figure)

        # Generate the sample-level visual comparison report.
        visual_comparison_path = (
            self.visual_comparison_generator.generate(
                predictions=predictions,
                references=references,
                metadata=metadata,
                output_dir=output_dir,
            )
        )

        return {
            **results,
            "artifacts": {
                "results": results_path,
                "report": report_path,
                "stage_metrics_chart": stage_chart_path,
                "temporal_alignment_chart": temporal_chart_path,
                "visual_comparison": visual_comparison_path,
            },
        }

    @staticmethod
    def _validate_inference_results(
        results: dict[str, Any],
    ) -> None:
        """Validate the inference runner output before evaluation."""

        if not isinstance(results, dict):
            raise TypeError("Inference results must be a dictionary.")

        required = {
            "split",
            "num_samples",
            "predictions",
            "references",
            "metadata",
        }

        missing = required.difference(results)

        if missing:
            raise ValueError(
                f"Inference results are missing fields: {sorted(missing)}"
            )

        predictions = results["predictions"]
        references = results["references"]
        metadata = results["metadata"]
        num_samples = results["num_samples"]

        if not isinstance(predictions, list):
            raise TypeError("Inference predictions must be a list.")

        if not isinstance(references, list):
            raise TypeError("Inference references must be a list.")

        if not isinstance(metadata, list):
            raise TypeError("Inference metadata must be a list.")

        if not isinstance(num_samples, int) or isinstance(num_samples, bool):
            raise TypeError("num_samples must be an integer.")

        if num_samples <= 0:
            raise ValueError("num_samples must be positive.")

        if len(predictions) != num_samples:
            raise ValueError(
                "Prediction count does not match num_samples."
            )

        if len(references) != num_samples:
            raise ValueError(
                "Reference count does not match num_samples."
            )

        if len(metadata) != num_samples:
            raise ValueError(
                "Metadata count does not match num_samples."
            )

    @staticmethod
    def _close_figure(figure: Any) -> None:
        """Close actual Matplotlib figures without affecting test doubles."""

        if isinstance(figure, Figure):
            plt.close(figure)
