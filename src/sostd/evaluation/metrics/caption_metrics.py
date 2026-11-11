from __future__ import annotations

import math
import re
from collections import Counter


class CaptionMetrics:
    """Compute BLEU and ROUGE-L caption evaluation metrics."""

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        if not isinstance(text, str):
            raise TypeError("Captions must be strings.")

        return re.findall(r"\b\w+\b", text.lower())

    @staticmethod
    def _ngrams(
        tokens: list[str],
        n: int,
    ) -> Counter:
        return Counter(
            tuple(tokens[index:index + n])
            for index in range(len(tokens) - n + 1)
        )

    @staticmethod
    def _lcs_length(
        first: list[str],
        second: list[str],
    ) -> int:
        """Calculate longest common subsequence length."""

        previous = [0] * (len(second) + 1)

        for token_a in first:
            current = [0] * (len(second) + 1)

            for j, token_b in enumerate(second, start=1):
                if token_a == token_b:
                    current[j] = previous[j - 1] + 1
                else:
                    current[j] = max(
                        previous[j],
                        current[j - 1],
                    )

            previous = current

        return previous[-1]

    @classmethod
    def _corpus_bleu(
        cls,
        predictions: list[list[str]],
        references: list[list[str]],
        max_order: int,
    ) -> float:
        """Calculate corpus BLEU with clipped n-gram precision."""

        clipped_counts = [0] * max_order
        total_counts = [0] * max_order

        prediction_length = 0
        reference_length = 0

        for prediction, reference in zip(
            predictions,
            references,
            strict=True,
        ):
            prediction_length += len(prediction)
            reference_length += len(reference)

            for order in range(1, max_order + 1):
                prediction_ngrams = cls._ngrams(
                    prediction,
                    order,
                )
                reference_ngrams = cls._ngrams(
                    reference,
                    order,
                )

                clipped_counts[order - 1] += sum(
                    min(count, reference_ngrams[ngram])
                    for ngram, count in prediction_ngrams.items()
                )

                total_counts[order - 1] += sum(
                    prediction_ngrams.values()
                )

        if prediction_length == 0 or reference_length == 0:
            return 0.0

        precisions = []

        for clipped, total in zip(
            clipped_counts,
            total_counts,
            strict=True,
        ):
            if total == 0 or clipped == 0:
                return 0.0

            precisions.append(clipped / total)

        brevity_penalty = min(
            1.0,
            math.exp(
                1.0 - reference_length / prediction_length
            ),
        )

        geometric_mean = math.exp(
            sum(math.log(value) for value in precisions)
            / max_order
        )

        return brevity_penalty * geometric_mean

    @classmethod
    def _rouge_l(
        cls,
        prediction: list[str],
        reference: list[str],
    ) -> float:
        """Calculate ROUGE-L F1 for one caption pair."""

        if not prediction or not reference:
            return 0.0

        lcs = cls._lcs_length(prediction, reference)

        precision = lcs / len(prediction)
        recall = lcs / len(reference)

        if precision + recall == 0:
            return 0.0

        return (
            2 * precision * recall
            / (precision + recall)
        )

    @classmethod
    def compute(
        cls,
        predictions: list[str],
        references: list[str],
    ) -> dict[str, float]:
        """
        Compute corpus BLEU-1 through BLEU-4 and mean ROUGE-L.

        Each prediction must correspond to exactly one reference.
        """
        if not isinstance(predictions, list):
            raise TypeError("predictions must be a list.")

        if not isinstance(references, list):
            raise TypeError("references must be a list.")

        if not predictions:
            raise ValueError("At least one caption pair is required.")

        if len(predictions) != len(references):
            raise ValueError(
                "Predictions and references must have equal lengths."
            )

        tokenized_predictions = [
            cls._tokenize(text)
            for text in predictions
        ]

        tokenized_references = [
            cls._tokenize(text)
            for text in references
        ]

        results = {}

        for order in range(1, 5):
            results[f"bleu_{order}"] = cls._corpus_bleu(
                tokenized_predictions,
                tokenized_references,
                max_order=order,
            )

        rouge_scores = [
            cls._rouge_l(prediction, reference)
            for prediction, reference in zip(
                tokenized_predictions,
                tokenized_references,
                strict=True,
            )
        ]

        results["rouge_l"] = sum(rouge_scores) / len(rouge_scores)

        return results