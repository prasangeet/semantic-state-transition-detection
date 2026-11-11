from __future__ import annotations

import pytest
import torch

from src.sostd.evaluation.metrics.semantic_metrics import SemanticMetrics


class MockSentenceEncoder:
    def __init__(self):
        self.training = True

        self.embeddings = {
            "the red ball moves": [1.0, 0.0, 0.0],
            "a red ball is moving": [1.0, 0.0, 0.0],
            "the blue cube stops": [0.0, 1.0, 0.0],
            "the object changes position": [0.0, 0.0, 1.0],
        }

    def eval(self):
        self.training = False
        return self

    def encode(
        self,
        sentences,
        batch_size,
        convert_to_tensor,
        normalize_embeddings,
        show_progress_bar,
    ):
        vectors = [
            self.embeddings[sentence]
            for sentence in sentences
        ]

        return torch.tensor(vectors, dtype=torch.float32)


@pytest.fixture
def semantic_metrics():
    return SemanticMetrics(
        device="cpu",
        model=MockSentenceEncoder(),
    )


def test_initialization(semantic_metrics):
    assert semantic_metrics.model.training is False


def test_identical_semantic_embeddings(semantic_metrics):
    results = semantic_metrics.compute(
        ["the red ball moves"],
        ["the red ball moves"],
    )

    assert results["semantic_similarity"] == pytest.approx(1.0)
    assert results["semantic_similarity_std"] == pytest.approx(0.0)


def test_equivalent_semantic_embeddings(semantic_metrics):
    results = semantic_metrics.compute(
        ["the red ball moves"],
        ["a red ball is moving"],
    )

    assert results["semantic_similarity"] == pytest.approx(1.0)


def test_unrelated_semantic_embeddings(semantic_metrics):
    results = semantic_metrics.compute(
        ["the red ball moves"],
        ["the blue cube stops"],
    )

    assert results["semantic_similarity"] == pytest.approx(0.0)


def test_multiple_caption_pairs(semantic_metrics):
    results = semantic_metrics.compute(
        [
            "the red ball moves",
            "the blue cube stops",
        ],
        [
            "a red ball is moving",
            "the blue cube stops",
        ],
    )

    assert results["semantic_similarity"] == pytest.approx(1.0)
    assert len(results["per_sample_similarity"]) == 2


def test_mismatched_lengths(semantic_metrics):
    with pytest.raises(ValueError, match="equal lengths"):
        semantic_metrics.compute(
            ["the red ball moves"],
            [
                "the red ball moves",
                "the blue cube stops",
            ],
        )


def test_empty_inputs(semantic_metrics):
    with pytest.raises(ValueError, match="At least one"):
        semantic_metrics.compute([], [])


def test_invalid_prediction_type(semantic_metrics):
    with pytest.raises(TypeError, match="predictions"):
        semantic_metrics.compute(
            "the red ball moves",
            ["the red ball moves"],
        )


def test_invalid_caption_element(semantic_metrics):
    with pytest.raises(TypeError, match="strings"):
        semantic_metrics.compute(
            [None],
            ["the red ball moves"],
        )


def test_invalid_batch_size(semantic_metrics):
    with pytest.raises(ValueError, match="batch_size"):
        semantic_metrics.compute(
            ["the red ball moves"],
            ["the red ball moves"],
            batch_size=0,
        )


def test_embedding_shape_mismatch():
    class InvalidEncoder(MockSentenceEncoder):
        def encode(self, sentences, **kwargs):
            if sentences[0] == "the red ball moves":
                return torch.tensor([[1.0, 0.0]])
            return torch.tensor([[1.0, 0.0, 0.0]])

    metrics = SemanticMetrics(
        device="cpu",
        model=InvalidEncoder(),
    )

    with pytest.raises(ValueError, match="shapes"):
        metrics.compute(
            ["the red ball moves"],
            ["the blue cube stops"],
        )