
import json

import pytest

from src.sostd.evaluation.pipeline import EvaluationPipeline


class FakeRunner:
    def __init__(self, config):
        self.config = config

    def run(self):
        predictions = [
            {
                "before": "The drawer is partially open.",
                "during": "The drawer opens further.",
                "after": "The drawer is fully open.",
                "transition": "The drawer progressively opens.",
            }
        ]

        return {
            "split": "validation",
            "num_samples": 1,
            "predictions": predictions,
            "references": [dict(predictions[0])],
            "metadata": [
                {
                    "object": "drawer",
                    "action": "open",
                    "frame_indices": (1, 2, 3),
                    "image_paths": {},
                }
            ],
        }


class FakeEvaluator:
    def evaluate(self, predictions, references):
        return {
            "num_samples": len(predictions),
            "stages": {
                stage: {
                    "caption": {
                        "bleu_1": 1.0,
                        "bleu_2": 1.0,
                        "bleu_3": 1.0,
                        "bleu_4": 1.0,
                        "rouge_l": 1.0,
                    },
                    "semantic": {"mean_similarity": 1.0},
                }
                for stage in ("before", "during", "after", "transition")
            },
            "temporal": {
                "temporal_score": 1.0,
                "stage_scores": {
                    stage: 1.0
                    for stage in ("before", "during", "after", "transition")
                },
            },
        }


class FakeErrorAnalyzer:
    def analyze(self, predictions, references):
        return {
            "num_samples": len(predictions),
            "similarity_threshold": 0.5,
            "num_errors": 0,
            "errors": [],
            "stage_summary": {
                stage: {
                    "num_samples": len(predictions),
                    "num_low_similarity": 0,
                    "low_similarity_rate": 0.0,
                    "mean_similarity": 1.0,
                }
                for stage in ("before", "during", "after", "transition")
            },
        }


class FakeReportGenerator:
    def generate(self, evaluation, error_analysis):
        return "# Test Evaluation Report"

    def save(self, report, output_path):
        from pathlib import Path

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report, encoding="utf-8")
        return path


class FakeVisualizer:
    def plot_stage_metrics(self, evaluation):
        return "stage-figure"

    def plot_temporal_alignment(self, evaluation):
        return "temporal-figure"

    def save(self, figure, output_path):
        from pathlib import Path

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(figure, encoding="utf-8")
        return path


@pytest.fixture
def config(tmp_path):
    class Config:
        output_dir = tmp_path / "evaluation"

    return Config()


@pytest.fixture
def pipeline(config):
    return EvaluationPipeline(
        config=config,
        runner_factory=FakeRunner,
        evaluator=FakeEvaluator(),
        error_analyzer=FakeErrorAnalyzer(),
        report_generator=FakeReportGenerator(),
        visualizer=FakeVisualizer(),
    )


def test_pipeline_returns_evaluation_results(pipeline):
    result = pipeline.run()

    assert result["num_samples"] == 1
    assert result["evaluation"]["temporal"]["temporal_score"] == 1.0
    assert result["error_analysis"]["num_errors"] == 0


def test_pipeline_preserves_predictions_and_references(pipeline):
    result = pipeline.run()

    assert result["predictions"][0]["before"] == (
        "The drawer is partially open."
    )
    assert result["references"][0]["transition"] == (
        "The drawer progressively opens."
    )


def test_pipeline_creates_all_artifacts(pipeline, config):
    result = pipeline.run()

    expected_files = {
        "results.json",
        "report.md",
        "stage_metrics.png",
        "temporal_alignment.png",
        "visual_comparison.html",
        "visual_comparison_assets",
    }

    actual_files = {
        path.name
        for path in config.output_dir.iterdir()
    }

    assert actual_files == expected_files

    # All file artifacts returned by the pipeline must exist.
    for path in result["artifacts"].values():
        assert path.is_file()

    assert (
        config.output_dir / "visual_comparison.html"
    ).is_file()

    assert (
        config.output_dir / "visual_comparison_assets"
    ).is_dir()


def test_results_json_contains_evaluation_data(pipeline, config):
    pipeline.run()

    data = json.loads(
        (config.output_dir / "results.json").read_text(
            encoding="utf-8"
        )
    )

    assert data["split"] == "validation"
    assert data["num_samples"] == 1
    assert data["evaluation"]["temporal"]["temporal_score"] == 1.0


def test_pipeline_creates_output_directory(pipeline, config):
    assert not config.output_dir.exists()

    pipeline.run()

    assert config.output_dir.is_dir()
