
from __future__ import annotations

import pytest
import torch
import torch.nn as nn

from src.sostd.evaluation.inference import InferenceRunner


FEATURE_SHAPE = (257, 384)


class MockModel(nn.Module):
    def __init__(self, output=None):
        super().__init__()
        self.output = output
        self.received_frames = None
        self.generation_kwargs = None

    def generate(self, frames, **kwargs):
        self.received_frames = frames
        self.generation_kwargs = kwargs

        if isinstance(self.output, Exception):
            raise self.output

        if self.output is not None:
            return self.output

        batch_size = frames.shape[0]

        return {
            "state_tokens": torch.ones(
                batch_size, 3, 5, dtype=torch.long,
                device=frames.device,
            ),
            "transition_tokens": torch.ones(
                batch_size, 5, dtype=torch.long,
                device=frames.device,
            ),
        }


class MockTokenizer:
    def __init__(self):
        self.received_tokens = []

    def batch_decode(
        self,
        sequences,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    ):
        self.received_tokens.append(sequences.clone())

        return [
            f"caption_{index}"
            for index in range(len(sequences))
        ]


@pytest.fixture
def runner_components():
    model = MockModel()
    tokenizer = MockTokenizer()

    runner = InferenceRunner(
        model=model,
        tokenizer=tokenizer,
        device="cpu",
        amp=False,
    )

    return runner, model, tokenizer


def make_features(
    batch_size=2,
    num_frames=3,
    num_tokens=257,
    feature_dim=384,
):
    return torch.randn(
        batch_size,
        num_frames,
        num_tokens,
        feature_dim,
    )


def test_generate_batch(runner_components):
    runner, model, tokenizer = runner_components
    frames = make_features(batch_size=2)

    results = runner.run_batch(frames)

    assert len(results) == 2

    assert results[0] == {
        "before": "caption_0",
        "during": "caption_1",
        "after": "caption_2",
        "transition": "caption_0",
    }

    assert results[1] == {
        "before": "caption_3",
        "during": "caption_4",
        "after": "caption_5",
        "transition": "caption_1",
    }

    assert model.received_frames.shape == (2, 3, 257, 384)
    assert len(tokenizer.received_tokens) == 2



def test_generation_arguments(runner_components):
    runner, model, _ = runner_components

    runner.max_state_tokens = 48
    runner.max_transition_tokens = 80
    runner.num_beams = 2
    runner.repetition_penalty = 1.15
    runner.no_repeat_ngram_size = 3
    runner.length_penalty = 1.0

    runner.run_batch(make_features(batch_size=1))

    assert model.generation_kwargs == {
        "max_state_tokens": 48,
        "max_transition_tokens": 80,
        "num_beams": 2,
        "repetition_penalty": 1.15,
        "no_repeat_ngram_size": 3,
        "length_penalty": 1.0,
        "do_sample": False,
        "early_stopping": True,
    }



@pytest.mark.parametrize(
    "frames",
    [
        torch.randn(3, 257, 384),
        torch.randn(2, 2, 257, 384),
        torch.randn(2, 3, 0, 384),
        torch.randn(2, 3, 257, 0),
    ],
)
def test_invalid_frame_shapes(runner_components, frames):
    runner, _, _ = runner_components

    with pytest.raises(ValueError):
        runner.run_batch(frames)


def test_integer_frames(runner_components):
    runner, _, _ = runner_components

    frames = torch.ones(2, 3, 257, 384, dtype=torch.long)

    with pytest.raises(TypeError, match="floating-point"):
        runner.run_batch(frames)


def test_non_finite_frames(runner_components):
    runner, _, _ = runner_components

    frames = make_features(batch_size=1)
    frames[0, 0, 0, 0] = float("nan")

    with pytest.raises(ValueError, match="non-finite"):
        runner.run_batch(frames)


def test_feature_values_outside_rgb_range_are_accepted(
    runner_components,
):
    runner, _, _ = runner_components

    # Cached DINOv2 features are embeddings, not RGB pixels.
    frames = torch.full((1, 3, 257, 384), 12.5)

    results = runner.run_batch(frames)

    assert len(results) == 1


def test_missing_generation_output(runner_components):
    runner, model, _ = runner_components

    model.output = {
        "state_tokens": torch.ones(1, 3, 5, dtype=torch.long),
    }

    with pytest.raises(KeyError, match="transition_tokens"):
        runner.run_batch(make_features(batch_size=1))


def test_invalid_state_token_shape(runner_components):
    runner, model, _ = runner_components

    model.output = {
        "state_tokens": torch.ones(1, 5, dtype=torch.long),
        "transition_tokens": torch.ones(1, 5, dtype=torch.long),
    }

    with pytest.raises(ValueError, match="state_tokens"):
        runner.run_batch(make_features(batch_size=1))


def test_invalid_transition_token_shape(runner_components):
    runner, model, _ = runner_components

    model.output = {
        "state_tokens": torch.ones(1, 3, 5, dtype=torch.long),
        "transition_tokens": torch.ones(
            1, 3, 5, dtype=torch.long
        ),
    }

    with pytest.raises(ValueError, match="transition_tokens"):
        runner.run_batch(make_features(batch_size=1))


def test_model_generation_must_return_dictionary(
    runner_components,
):
    runner, model, _ = runner_components
    model.output = ["invalid output"]

    with pytest.raises(TypeError, match="dictionary"):
        runner.run_batch(make_features(batch_size=1))


def test_model_generation_receives_cached_features(
    runner_components,
):
    runner, model, _ = runner_components
    frames = make_features(batch_size=1)

    runner.run_batch(frames)

    assert model.received_frames is not None
    assert model.received_frames.shape == (1, 3, 257, 384)
    assert torch.equal(model.received_frames, frames)


def test_model_is_in_evaluation_mode(runner_components):
    runner, model, _ = runner_components

    assert not model.training


def test_rejects_non_tensor_frames(runner_components):
    runner, _, _ = runner_components

    with pytest.raises(TypeError, match="torch.Tensor"):
        runner.run_batch([1, 2, 3])


def test_rejects_empty_batch(runner_components):
    runner, _, _ = runner_components

    with pytest.raises(ValueError, match="at least one"):
        runner.run_batch(torch.empty(0, 3, 257, 384))


def test_rejects_wrong_number_of_frames(runner_components):
    runner, _, _ = runner_components

    with pytest.raises(ValueError, match="exactly three"):
        runner.run_batch(torch.randn(1, 2, 257, 384))


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"max_state_tokens": 0}, "max_state_tokens"),
        ({"max_transition_tokens": 0}, "max_transition_tokens"),
        ({"num_beams": 0}, "num_beams"),
    ],
)
def test_invalid_configuration(kwargs, message):
    with pytest.raises(ValueError, match=message):
        InferenceRunner(
            model=MockModel(),
            tokenizer=MockTokenizer(),
            device="cpu",
            **kwargs,
        )


def test_decode_rejects_non_tensor_tokens(runner_components):
    runner, model, _ = runner_components

    model.output = {
        "state_tokens": [[1, 2, 3]],
        "transition_tokens": torch.ones(1, 5, dtype=torch.long),
    }

    with pytest.raises(TypeError, match="state_tokens"):
        runner.run_batch(make_features(batch_size=1))


def test_transition_batch_size_mismatch(runner_components):
    runner, model, _ = runner_components

    model.output = {
        "state_tokens": torch.ones(2, 3, 5, dtype=torch.long),
        "transition_tokens": torch.ones(1, 5, dtype=torch.long),
    }

    with pytest.raises(ValueError, match="input batch size"):
        runner.run_batch(make_features(batch_size=2))
