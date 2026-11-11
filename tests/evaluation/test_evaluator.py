import pytest

from src.sostd.evaluation.evaluator import Evaluator


class MockCaptionMetrics:
    def compute(self, predictions, references):
        return {"mean_rouge": 1.0}


class MockSemanticMetrics:
    def compute(self, predictions, references):
        return {
            "mean_similarity": (
                sum(p == r for p, r in zip(predictions, references))
                / len(predictions)
            )
        }


class MockTemporalMetrics:
    def compute(self, predictions, references):
        return {"temporal_score": 0.75}


@pytest.fixture
def evaluator():
    semantic = MockSemanticMetrics()

    return Evaluator(
        caption_metrics=MockCaptionMetrics(),
        semantic_metrics=semantic,
        temporal_metrics=MockTemporalMetrics(),
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
            "transition": "The box changes from closed to open.",
        },
    ]
    references = [dict(item) for item in predictions]

    return predictions, references


def test_evaluate_returns_all_stages(evaluator, samples):
    predictions, references = samples

    result = evaluator.evaluate(predictions, references)

    assert result["num_samples"] == 2
    assert set(result["stages"]) == {
        "before",
        "during",
        "after",
        "transition",
    }


def test_evaluate_returns_caption_and_semantic_metrics(evaluator, samples):
    predictions, references = samples

    result = evaluator.evaluate(predictions, references)

    for stage in evaluator.STAGES:
        assert result["stages"][stage]["caption"] == {"mean_rouge": 1.0}
        assert result["stages"][stage]["semantic"]["mean_similarity"] == 1.0


def test_evaluate_returns_temporal_metrics(evaluator, samples):
    predictions, references = samples

    result = evaluator.evaluate(predictions, references)

    assert result["temporal"] == {"temporal_score": 0.75}


def test_rejects_empty_inputs(evaluator):
    with pytest.raises(ValueError, match="cannot be empty"):
        evaluator.evaluate([], [])


def test_rejects_mismatched_lengths(evaluator, samples):
    predictions, references = samples

    with pytest.raises(ValueError, match="equal lengths"):
        evaluator.evaluate(predictions, references[:1])


def test_rejects_non_list_inputs(evaluator):
    with pytest.raises(TypeError, match="must be lists"):
        evaluator.evaluate({}, {})


def test_rejects_non_dictionary_samples(evaluator):
    with pytest.raises(TypeError, match="must be a dictionary"):
        evaluator.evaluate(["invalid"], ["invalid"])


@pytest.mark.parametrize(
    "stage",
    ["before", "during", "after", "transition"],
)
def test_rejects_missing_stage(evaluator, samples, stage):
    predictions, references = samples
    del predictions[0][stage]

    with pytest.raises(ValueError, match=stage):
        evaluator.evaluate(predictions, references)


def test_default_metrics_are_created(monkeypatch):
    import src.sostd.evaluation.evaluator as evaluator_module

    class MockCaptionMetrics:
        pass

    class MockSemanticMetrics:
        pass

    class MockTemporalMetrics:
        def __init__(self, semantic_metrics=None):
            self.semantic_metrics = semantic_metrics

    monkeypatch.setattr(
        evaluator_module,
        "CaptionMetrics",
        MockCaptionMetrics,
    )
    monkeypatch.setattr(
        evaluator_module,
        "SemanticMetrics",
        MockSemanticMetrics,
    )
    monkeypatch.setattr(
        evaluator_module,
        "TemporalMetrics",
        MockTemporalMetrics,
    )

    evaluator = evaluator_module.Evaluator()

    assert isinstance(evaluator.caption_metrics, MockCaptionMetrics)
    assert isinstance(evaluator.semantic_metrics, MockSemanticMetrics)
    assert isinstance(evaluator.temporal_metrics, MockTemporalMetrics)
    assert evaluator.temporal_metrics.semantic_metrics is evaluator.semantic_metrics