from pathlib import Path

import pytest

from src.sostd.evaluation.reporting.report_generator import ReportGenerator


@pytest.fixture
def generator():
    return ReportGenerator()


@pytest.fixture
def evaluation():
    return {
        "num_samples": 2,
        "stages": {
            stage: {
                "caption": {
                    "bleu_1": 0.8,
                    "bleu_2": 0.7,
                    "bleu_3": 0.6,
                    "bleu_4": 0.5,
                    "rouge_l": 0.75,
                },
                "semantic": {"mean_similarity": 0.9},
            }
            for stage in ("before", "during", "after", "transition")
        },
        "temporal": {
            "temporal_score": 0.85,
            "stage_scores": {
                "before": 0.9,
                "during": 0.8,
                "after": 0.85,
                "transition": 0.85,
            },
        },
    }


@pytest.fixture
def error_analysis():
    return {
        "num_samples": 2,
        "similarity_threshold": 0.5,
        "num_errors": 1,
        "errors": [
            {
                "sample_index": 1,
                "stage": "during",
                "prediction": "The box opens.",
                "reference": "The box remains closed.",
                "similarity": 0.2,
                "error_type": "low_semantic_similarity",
            }
        ],
        "stage_summary": {
            stage: {
                "num_samples": 2,
                "num_low_similarity": 1 if stage == "during" else 0,
                "low_similarity_rate": 0.5 if stage == "during" else 0.0,
                "mean_similarity": 0.6,
            }
            for stage in ("before", "during", "after", "transition")
        },
    }


def test_generates_markdown_report(generator, evaluation):
    report = generator.generate(evaluation)

    assert "# OSCaR-Lite Evaluation Report" in report
    assert "## Temporal Stage Metrics" in report
    assert "## Temporal Alignment" in report
    assert "Samples evaluated: 2" in report


def test_includes_all_temporal_stages(generator, evaluation):
    report = generator.generate(evaluation)

    for stage in ("Before", "During", "After", "Transition"):
        assert stage in report


def test_formats_metric_values(generator, evaluation):
    report = generator.generate(evaluation)

    assert "0.8000" in report
    assert "0.7500" in report
    assert "0.8500" in report


def test_includes_error_analysis(generator, evaluation, error_analysis):
    report = generator.generate(evaluation, error_analysis)

    assert "## Qualitative Error Analysis" in report
    assert "Cases for Manual Inspection" in report
    assert "The box opens." in report
    assert "The box remains closed." in report


def test_report_without_error_analysis(generator, evaluation):
    report = generator.generate(evaluation)

    assert "Qualitative Error Analysis" not in report


def test_rejects_non_dictionary_evaluation(generator):
    with pytest.raises(TypeError, match="dictionary"):
        generator.generate("invalid")


def test_rejects_missing_evaluation_fields(generator):
    with pytest.raises(ValueError, match="missing fields"):
        generator.generate({"num_samples": 2})


def test_rejects_missing_stage(generator, evaluation):
    del evaluation["stages"]["during"]

    with pytest.raises(ValueError, match="during"):
        generator.generate(evaluation)


def test_rejects_incomplete_temporal_results(generator, evaluation):
    del evaluation["temporal"]["stage_scores"]["after"]

    with pytest.raises(ValueError, match="after"):
        generator.generate(evaluation)


def test_saves_report(generator, tmp_path):
    output = tmp_path / "reports" / "evaluation.md"
    path = generator.save("# Test report", output)

    assert path == output
    assert path.exists()
    assert path.read_text(encoding="utf-8") == "# Test report"


def test_rejects_empty_report(generator, tmp_path):
    with pytest.raises(ValueError, match="non-empty"):
        generator.save("  ", tmp_path / "empty.md")