from __future__ import annotations

import pytest

from src.sostd.evaluation.metrics.caption_metrics import CaptionMetrics


def test_identical_captions():
    captions = [
        "The red object moves forward",
        "A blue sphere is stationary",
    ]

    results = CaptionMetrics.compute(captions, captions)

    assert results["bleu_1"] == pytest.approx(1.0)
    assert results["bleu_2"] == pytest.approx(1.0)
    assert results["bleu_3"] == pytest.approx(1.0)
    assert results["bleu_4"] == pytest.approx(1.0)
    assert results["rouge_l"] == pytest.approx(1.0)


def test_completely_different_captions():
    predictions = ["A red sphere moves"]
    references = ["The blue cube stops"]

    results = CaptionMetrics.compute(
        predictions,
        references,
    )

    assert results["bleu_1"] == 0.0
    assert results["bleu_4"] == 0.0
    assert results["rouge_l"] == 0.0


def test_partial_caption_overlap():
    predictions = ["The red object moves forward"]
    references = ["The red object moves backward"]

    results = CaptionMetrics.compute(
        predictions,
        references,
    )

    assert 0.0 < results["bleu_1"] < 1.0
    assert 0.0 < results["rouge_l"] < 1.0


def test_case_insensitive_comparison():
    results = CaptionMetrics.compute(
        ["THE RED OBJECT MOVES"],
        ["the red object moves"],
    )

    assert results["bleu_1"] == pytest.approx(1.0)
    assert results["rouge_l"] == pytest.approx(1.0)


def test_empty_prediction():
    results = CaptionMetrics.compute(
        [""],
        ["The object moves"],
    )

    assert results["bleu_1"] == 0.0
    assert results["rouge_l"] == 0.0


def test_empty_reference():
    results = CaptionMetrics.compute(
        ["The object moves"],
        [""],
    )

    assert results["bleu_1"] == 0.0
    assert results["rouge_l"] == 0.0


def test_multiple_caption_pairs():
    predictions = [
        "The object moves forward",
        "The object stops",
        "The sphere changes position",
    ]

    references = [
        "The object moves forward",
        "The object stops",
        "The sphere changes position",
    ]

    results = CaptionMetrics.compute(
        predictions,
        references,
    )

    assert len(results) == 5
    assert all(value == pytest.approx(1.0) for value in results.values())


def test_mismatched_lengths():
    with pytest.raises(ValueError, match="equal lengths"):
        CaptionMetrics.compute(
            ["The object moves"],
            ["The object moves", "The object stops"],
        )


def test_empty_dataset():
    with pytest.raises(ValueError, match="At least one"):
        CaptionMetrics.compute([], [])


def test_invalid_prediction_type():
    with pytest.raises(TypeError, match="strings"):
        CaptionMetrics.compute(
            [None],
            ["The object moves"],
        )


def test_invalid_input_container():
    with pytest.raises(TypeError, match="predictions"):
        CaptionMetrics.compute(
            "The object moves",
            ["The object moves"],
        )