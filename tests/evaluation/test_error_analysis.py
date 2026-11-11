import pytest

from src.sostd.evaluation.qualitative.error_analysis import ErrorAnalyzer


class MockSemanticMetrics:
    def compute(self, predictions, references):
        similarities = [
            1.0 if prediction == reference else 0.2
            for prediction, reference in zip(predictions, references)
        ]

        return {
            "mean_similarity": sum(similarities) / len(similarities),
            "similarities": similarities,
        }


@pytest.fixture
def analyzer():
    return ErrorAnalyzer(
        semantic_metrics=MockSemanticMetrics(),
        similarity_threshold=0.5,
    )


@pytest.fixture
def samples():
    predictions = [
        {
            "before": "The object is upright.",
            "during": "The object starts falling.",
            "after": "The object is on the ground.",
            "transition": "The object falls.",
        },
        {
            "before": "The box is closed.",
            "during": "The box opens.",
            "after": "The box is open.",
            "transition": "The box changes state.",
        },
    ]

    references = [
        dict(item) for item in predictions
    ]
    references[1]["during"] = "The box remains closed."

    return predictions, references


def test_finds_low_similarity_captions(analyzer, samples):
    predictions, references = samples

    result = analyzer.analyze(predictions, references)

    assert result["num_errors"] == 1
    assert result["errors"][0]["sample_index"] == 1
    assert result["errors"][0]["stage"] == "during"
    assert result["errors"][0]["similarity"] == pytest.approx(0.2)


def test_returns_stage_summary(analyzer, samples):
    predictions, references = samples

    result = analyzer.analyze(predictions, references)

    assert set(result["stage_summary"]) == {
        "before",
        "during",
        "after",
        "transition",
    }
    assert result["stage_summary"]["during"]["num_low_similarity"] == 1
    assert result["stage_summary"]["during"]["low_similarity_rate"] == 0.5
    assert result["stage_summary"]["before"]["low_similarity_rate"] == 0.0


def test_returns_threshold_and_sample_count(analyzer, samples):
    predictions, references = samples

    result = analyzer.analyze(predictions, references)

    assert result["similarity_threshold"] == 0.5
    assert result["num_samples"] == 2


def test_no_errors_for_matching_captions(analyzer):
    samples = [
        {
            "before": "A",
            "during": "B",
            "after": "C",
            "transition": "D",
        }
    ]

    result = analyzer.analyze(samples, samples)

    assert result["num_errors"] == 0
    assert result["errors"] == []


def test_rejects_invalid_threshold():
    with pytest.raises(ValueError, match="between 0 and 1"):
        ErrorAnalyzer(similarity_threshold=1.5)


def test_rejects_non_numeric_threshold():
    with pytest.raises(TypeError, match="must be numeric"):
        ErrorAnalyzer(similarity_threshold="0.5")


def test_rejects_empty_inputs(analyzer):
    with pytest.raises(ValueError, match="cannot be empty"):
        analyzer.analyze([], [])


def test_rejects_mismatched_lengths(analyzer, samples):
    predictions, references = samples

    with pytest.raises(ValueError, match="equal lengths"):
        analyzer.analyze(predictions, references[:1])


def test_rejects_missing_stage(analyzer, samples):
    predictions, references = samples
    del predictions[0]["during"]

    with pytest.raises(ValueError, match="during"):
        analyzer.analyze(predictions, references)


def test_rejects_invalid_similarity_scores():
    class InvalidSemanticMetrics:
        def compute(self, predictions, references):
            return {
                "mean_similarity": 1.0,
                "similarities": [1.5],
            }

    analyzer = ErrorAnalyzer(
        semantic_metrics=InvalidSemanticMetrics(),
    )
    sample = [{
        "before": "A",
        "during": "B",
        "after": "C",
        "transition": "D",
    }]

    with pytest.raises(ValueError, match="between 0 and 1"):
        analyzer.analyze(sample, sample)