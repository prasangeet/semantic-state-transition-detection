import pytest

from src.sostd.evaluation.metrics.temporal_metrics import TemporalMetrics


class MockSemanticMetrics:
    def compute(self, predictions, references):
        score = sum(
            1.0 if prediction == reference else 0.0
            for prediction, reference in zip(predictions, references)
        ) / len(predictions)

        return {
            "mean_similarity": score,
            "std_similarity": 0.0,
            "similarities": [
                1.0 if prediction == reference else 0.0
                for prediction, reference in zip(predictions, references)
            ],
        }


@pytest.fixture
def metric():
    return TemporalMetrics(semantic_metrics=MockSemanticMetrics())


@pytest.fixture
def sample_predictions():
    return [
        {
            "before": "The object is upright.",
            "during": "The object begins falling.",
            "after": "The object lies on the ground.",
            "transition": "The object falls onto the ground.",
        },
        {
            "before": "The box is closed.",
            "during": "The box opens.",
            "after": "The box is open.",
            "transition": "The box changes from closed to open.",
        },
    ]


def test_perfect_temporal_alignment(metric, sample_predictions):
    result = metric.compute(sample_predictions, sample_predictions)

    assert result["temporal_score"] == pytest.approx(1.0)
    assert result["num_samples"] == 2

    for stage in ("before", "during", "after", "transition"):
        assert result["stage_scores"][stage] == pytest.approx(1.0)


def test_stage_scores_are_computed_independently(
    metric,
    sample_predictions,
):
    references = [dict(item) for item in sample_predictions]
    references[0]["during"] = "A different description."

    result = metric.compute(sample_predictions, references)

    assert result["stage_scores"]["before"] == pytest.approx(1.0)
    assert result["stage_scores"]["during"] == pytest.approx(0.5)
    assert result["stage_scores"]["after"] == pytest.approx(1.0)
    assert result["stage_scores"]["transition"] == pytest.approx(1.0)

    assert result["temporal_score"] == pytest.approx(0.875)


def test_returns_stage_details(metric, sample_predictions):
    result = metric.compute(sample_predictions, sample_predictions)

    assert set(result["stage_details"]) == {
        "before",
        "during",
        "after",
        "transition",
    }

    assert result["stage_details"]["before"]["mean_similarity"] == 1.0


def test_rejects_empty_predictions(metric):
    with pytest.raises(ValueError, match="cannot be empty"):
        metric.compute([], [])


def test_rejects_mismatched_lengths(metric, sample_predictions):
    with pytest.raises(ValueError, match="equal lengths"):
        metric.compute(sample_predictions, sample_predictions[:1])


def test_rejects_non_list_inputs(metric):
    with pytest.raises(TypeError, match="must be lists"):
        metric.compute({}, {})


def test_rejects_non_dictionary_sample(metric):
    with pytest.raises(TypeError, match="must be a dictionary"):
        metric.compute(["invalid"], ["invalid"])


@pytest.mark.parametrize("stage", ["before", "during", "after", "transition"])
def test_rejects_missing_stage(metric, sample_predictions, stage):
    predictions = [dict(item) for item in sample_predictions]
    del predictions[0][stage]

    with pytest.raises(ValueError, match=stage):
        metric.compute(predictions, sample_predictions)


@pytest.mark.parametrize("invalid_value", ["", "   ", None, 123])
def test_rejects_invalid_stage_caption(
    metric,
    sample_predictions,
    invalid_value,
):
    predictions = [dict(item) for item in sample_predictions]
    predictions[0]["before"] = invalid_value

    with pytest.raises(ValueError, match="before"):
        metric.compute(predictions, sample_predictions)