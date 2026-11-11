
from types import SimpleNamespace

import pytest
import torch
import torch.nn as nn
import torch.nn.functional as F

from src.sostd.models.oscar_lite import OSCaRLite


# ---------------------------------------------------------
# Dummy components
# ---------------------------------------------------------


class DummyEncoder(nn.Module):
    def __init__(self, hidden_size=1024, num_tokens=17):
        super().__init__()

        self.hidden_size = hidden_size
        self.num_tokens = num_tokens
        self.projection = nn.Linear(3, hidden_size)

    def forward(self, images):
        batch_size = images.shape[0]

        pooled = images.mean(dim=(-2, -1))
        features = self.projection(pooled)

        return features.unsqueeze(1).expand(
            batch_size,
            self.num_tokens,
            self.hidden_size,
        )


class DummyTemporalFusion(nn.Module):
    def __init__(self, input_dim=1024, hidden_dim=1024):
        super().__init__()

        self.input_projection = nn.Linear(input_dim, hidden_dim)
        self.norm = nn.LayerNorm(hidden_dim)

    def forward(self, features):
        return self.norm(self.input_projection(features))


class DummyResampler(nn.Module):
    def __init__(
        self,
        input_dim=1024,
        output_dim=1024,
        num_queries=32,
    ):
        super().__init__()

        self.input_projection = (
            nn.Identity()
            if input_dim == output_dim
            else nn.Linear(input_dim, output_dim)
        )

        self.query_tokens = nn.Parameter(
            torch.randn(1, 1, num_queries, output_dim)
        )

        self.output_dim = output_dim

    def forward(self, features):
        batch_size, num_frames, _, _ = features.shape

        projected = self.input_projection(features)

        pooled = projected.mean(dim=2, keepdim=True)

        return pooled.expand(
            batch_size,
            num_frames,
            self.query_tokens.shape[2],
            self.output_dim,
        ) + self.query_tokens


class DummyProjection(nn.Module):
    def __init__(self, input_dim=1024, output_dim=768):
        super().__init__()

        self.input_dim = input_dim
        self.output_dim = output_dim

        self.norm = nn.LayerNorm(input_dim)
        self.projection = nn.Linear(input_dim, output_dim)

    def forward(self, features):
        return self.projection(self.norm(features))


class DummyLanguageDecoder(nn.Module):
    def __init__(self, hidden_dim=768, vocab_size=100):
        super().__init__()

        self.hidden_dim = hidden_dim
        self.vocab_size = vocab_size

        self.projection = nn.Linear(hidden_dim, vocab_size)

        self.forward_calls = []
        self.generate_calls = []

    def forward(self, embeddings, labels):
        self.forward_calls.append({
            "embeddings": embeddings,
            "labels": labels,
        })

        if embeddings.ndim == 4:
            batch_size, num_frames, num_tokens, hidden_dim = (
                embeddings.shape
            )
            embeddings = embeddings.reshape(
                batch_size,
                num_frames * num_tokens,
                hidden_dim,
            )

        context = embeddings.mean(dim=1)
        logits = self.projection(context)

        logits = logits.unsqueeze(1).expand(
            -1,
            labels.shape[1],
            -1,
        )

        loss = logits.mean()

        return SimpleNamespace(
            loss=loss,
            logits=logits,
        )

    def generate(
        self,
        embeddings,
        max_new_tokens=64,
        **kwargs,
    ):
        self.generate_calls.append({
            "embeddings": embeddings,
            "max_new_tokens": max_new_tokens,
            "kwargs": kwargs,
        })

        return torch.ones(
            embeddings.shape[0],
            max_new_tokens,
            dtype=torch.long,
            device=embeddings.device,
        )


# ---------------------------------------------------------
# Fixtures
# ---------------------------------------------------------


@pytest.fixture
def decoder():
    return DummyLanguageDecoder()


@pytest.fixture
def model(decoder):
    return OSCaRLite(
        encoder=DummyEncoder(),
        temporal_fusion=DummyTemporalFusion(),
        visual_resampler=DummyResampler(),
        visual_projection=DummyProjection(),
        language_decoder=decoder,
    )


@pytest.fixture
def frames():
    return torch.rand(2, 3, 3, 224, 224)


@pytest.fixture
def cached_features():
    return torch.randn(2, 3, 257, 1024)


# ---------------------------------------------------------
# Initialization and architecture
# ---------------------------------------------------------


def test_initializes_all_components(model):
    assert model.encoder is not None
    assert model.temporal_fusion is not None
    assert model.visual_resampler is not None
    assert model.visual_projection is not None
    assert model.language_decoder is not None


def test_v3_dimensions(model):
    assert model._get_encoder_dimension(model.encoder) == 1024
    assert model._get_temporal_output_dimension(
        model.temporal_fusion
    ) == 1024
    assert model._get_resampler_output_dimension(
        model.visual_resampler
    ) == 1024
    assert model._get_decoder_dimension(
        model.language_decoder
    ) == 768


def test_visual_dimension_matches_decoder(model):
    assert model.visual_dim == 768


def test_rejects_invalid_max_frames(decoder):
    with pytest.raises(ValueError, match="max_frames"):
        OSCaRLite(
            encoder=DummyEncoder(),
            temporal_fusion=DummyTemporalFusion(),
            visual_resampler=DummyResampler(),
            visual_projection=DummyProjection(),
            language_decoder=decoder,
            max_frames=0,
        )


def test_rejects_invalid_temporal_head_configuration(decoder):
    with pytest.raises(ValueError, match="divisible"):
        OSCaRLite(
            encoder=DummyEncoder(),
            temporal_fusion=DummyTemporalFusion(),
            visual_resampler=DummyResampler(),
            visual_projection=DummyProjection(),
            language_decoder=decoder,
            temporal_hidden_dim=1024,
            temporal_num_heads=15,
        )


# ---------------------------------------------------------
# Visual encoding: raw RGB frames
# ---------------------------------------------------------


def test_encode_visual_returns_v3_shape(model, frames):
    embeddings = model.encode_visual(frames)

    assert embeddings.shape == (2, 3, 32, 768)


def test_encode_visual_flattens_frames_for_encoder(model, frames):
    model.encode_visual(frames)

    assert model.encoder.projection.weight.shape == (1024, 3)


def test_encode_visual_preserves_batch_and_frame_dimensions(
    model,
    frames,
):
    embeddings = model.encode_visual(frames)

    assert embeddings.shape[:2] == (2, 3)


def test_encode_visual_supports_single_frame(model):
    frames = torch.rand(2, 1, 3, 224, 224)

    embeddings = model.encode_visual(frames)

    assert embeddings.shape == (2, 1, 32, 768)


def test_encode_visual_supports_single_batch(model):
    frames = torch.rand(1, 3, 3, 224, 224)

    embeddings = model.encode_visual(frames)

    assert embeddings.shape == (1, 3, 32, 768)


# ---------------------------------------------------------
# Visual encoding: cached features
# ---------------------------------------------------------


def test_encode_visual_accepts_cached_v3_features(
    model,
    cached_features,
):
    embeddings = model.encode_visual(cached_features)

    assert embeddings.shape == (2, 3, 32, 768)


def test_cached_features_preserve_gradients(model, cached_features):
    cached_features.requires_grad_(True)

    embeddings = model.encode_visual(cached_features)
    embeddings.mean().backward()

    assert cached_features.grad is not None
    assert torch.isfinite(cached_features.grad).all()


def test_rejects_wrong_cached_feature_dimension(model):
    features = torch.randn(2, 3, 257, 768)

    with pytest.raises(ValueError, match="cached feature dimension"):
        model.encode_visual(features)


def test_rejects_integer_cached_features(model):
    features = torch.randint(0, 255, (2, 3, 257, 1024))

    with pytest.raises(TypeError, match="floating-point"):
        model.encode_visual(features)


# ---------------------------------------------------------
# Training forward pass
# ---------------------------------------------------------


def test_forward_without_labels_returns_visual_embeddings(
    model,
    frames,
):
    output = model(frames)

    assert output["state_output"] is None
    assert output["transition_output"] is None
    assert output["visual_embeddings"].shape == (2, 3, 32, 768)


def test_forward_supports_state_labels(model, frames, decoder):
    state_labels = torch.randint(0, 100, (2, 3, 20))

    output = model(
        frames,
        state_labels=state_labels,
    )

    assert output["state_output"] is not None
    assert output["transition_output"] is None
    assert len(decoder.forward_calls) == 1

    call = decoder.forward_calls[0]

    assert call["embeddings"].shape == (6, 32, 768)
    assert call["labels"].shape == (6, 20)


def test_forward_supports_transition_labels(model, frames, decoder):
    transition_labels = torch.randint(0, 100, (2, 30))

    output = model(
        frames,
        transition_labels=transition_labels,
    )

    assert output["state_output"] is None
    assert output["transition_output"] is not None
    assert len(decoder.forward_calls) == 1

    call = decoder.forward_calls[0]

    assert call["embeddings"].shape == (2, 3, 32, 768)
    assert call["labels"].shape == (2, 30)


def test_forward_supports_both_tasks(model, frames, decoder):
    state_labels = torch.randint(0, 100, (2, 3, 20))
    transition_labels = torch.randint(0, 100, (2, 30))

    output = model(
        frames,
        state_labels=state_labels,
        transition_labels=transition_labels,
    )

    assert output["state_output"] is not None
    assert output["transition_output"] is not None
    assert len(decoder.forward_calls) == 2


def test_forward_state_labels_are_frame_specific(
    model,
    frames,
    decoder,
):
    state_labels = torch.randint(0, 100, (2, 3, 20))

    model(frames, state_labels=state_labels)

    call = decoder.forward_calls[0]

    assert call["labels"].shape[0] == 2 * 3


def test_state_mask_selects_only_valid_frames(
    model,
    frames,
    decoder,
):
    state_labels = torch.randint(0, 100, (2, 3, 20))

    state_mask = torch.tensor([
        [True, False, True],
        [False, True, False],
    ])

    model(
        frames,
        state_labels=state_labels,
        state_mask=state_mask,
    )

    call = decoder.forward_calls[0]

    assert call["embeddings"].shape == (3, 32, 768)
    assert call["labels"].shape == (3, 20)


def test_automatically_skips_fully_masked_state_rows(
    model,
    frames,
    decoder,
):
    state_labels = torch.full((2, 3, 20), -100)

    output = model(
        frames,
        state_labels=state_labels,
    )

    assert output["state_output"] is None
    assert len(decoder.forward_calls) == 0


def test_state_mask_can_skip_all_state_rows(model, frames, decoder):
    state_labels = torch.randint(0, 100, (2, 3, 20))
    state_mask = torch.zeros(2, 3, dtype=torch.bool)

    output = model(
        frames,
        state_labels=state_labels,
        state_mask=state_mask,
    )

    assert output["state_output"] is None
    assert len(decoder.forward_calls) == 0


def test_rejects_state_mask_without_state_labels(model, frames):
    with pytest.raises(ValueError, match="state_mask"):
        model(
            frames,
            state_mask=torch.ones(2, 3, dtype=torch.bool),
        )


def test_rejects_invalid_state_mask_shape(model, frames):
    labels = torch.randint(0, 100, (2, 3, 20))
    mask = torch.ones(2, 2, dtype=torch.bool)

    with pytest.raises(ValueError, match="state_mask"):
        model(
            frames,
            state_labels=labels,
            state_mask=mask,
        )


def test_rejects_valid_state_mask_for_fully_masked_caption(
    model,
    frames,
):
    labels = torch.full((2, 3, 20), -100)
    mask = torch.ones(2, 3, dtype=torch.bool)

    with pytest.raises(ValueError, match="non-masked token"):
        model(
            frames,
            state_labels=labels,
            state_mask=mask,
        )


# ---------------------------------------------------------
# Gradient propagation
# ---------------------------------------------------------


def test_transition_loss_backpropagates_to_visual_encoder(
    model,
    frames,
):
    labels = torch.randint(0, 100, (2, 20))

    output = model(
        frames,
        transition_labels=labels,
    )

    output["transition_output"].loss.backward()

    assert model.encoder.projection.weight.grad is not None
    assert model.temporal_fusion.input_projection.weight.grad is not None
    assert model.visual_resampler.query_tokens.grad is not None
    assert model.visual_projection.projection.weight.grad is not None

    assert torch.isfinite(
        model.encoder.projection.weight.grad
    ).all()


def test_state_loss_backpropagates_to_visual_encoder(
    model,
    frames,
):
    labels = torch.randint(0, 100, (2, 3, 20))

    output = model(
        frames,
        state_labels=labels,
    )

    output["state_output"].loss.backward()

    assert model.encoder.projection.weight.grad is not None
    assert model.temporal_fusion.input_projection.weight.grad is not None
    assert model.visual_resampler.query_tokens.grad is not None
    assert model.visual_projection.projection.weight.grad is not None


def test_visual_embeddings_remain_connected_to_computation_graph(
    model,
    frames,
):
    output = model(frames)

    assert output["visual_embeddings"].requires_grad
    assert output["visual_embeddings"].grad_fn is not None


# ---------------------------------------------------------
# Generation
# ---------------------------------------------------------


def test_generate_returns_both_tasks(model, frames):
    output = model.generate(frames)

    assert output["state_tokens"].shape == (2, 3, 64)
    assert output["transition_tokens"].shape == (2, 96)


def test_generate_uses_separate_sequence_lengths(
    model,
    frames,
    decoder,
):
    model.generate(
        frames,
        max_state_tokens=32,
        max_transition_tokens=80,
    )

    assert decoder.generate_calls[0]["max_new_tokens"] == 32
    assert decoder.generate_calls[1]["max_new_tokens"] == 80


def test_generate_passes_all_frames_to_transition_decoder(
    model,
    frames,
    decoder,
):
    model.generate(frames)

    transition_call = decoder.generate_calls[1]

    assert transition_call["embeddings"].shape == (2, 3, 32, 768)


def test_generate_passes_individual_frames_to_state_decoder(
    model,
    frames,
    decoder,
):
    model.generate(frames)

    state_call = decoder.generate_calls[0]

    assert state_call["embeddings"].shape == (6, 32, 768)


def test_generate_passes_generation_options(
    model,
    frames,
    decoder,
):
    model.generate(
        frames,
        num_beams=4,
        do_sample=False,
    )

    assert decoder.generate_calls[0]["kwargs"]["num_beams"] == 4
    assert decoder.generate_calls[1]["kwargs"]["do_sample"] is False


def test_generate_runs_without_gradient_tracking(model, frames):
    output = model.generate(frames)

    assert not output["state_tokens"].requires_grad
    assert not output["transition_tokens"].requires_grad


# ---------------------------------------------------------
# Input validation
# ---------------------------------------------------------


def test_rejects_invalid_frame_dimensions(model):
    with pytest.raises(ValueError, match="Expected frames shaped"):
        model(torch.rand(2, 3, 224))


def test_rejects_zero_batch_size(model):
    with pytest.raises(ValueError, match="Batch size"):
        model(torch.rand(0, 3, 3, 224, 224))


def test_rejects_zero_frames(model):
    with pytest.raises(ValueError, match="frames"):
        model(torch.rand(2, 0, 3, 224, 224))


def test_rejects_too_many_frames(model):
    with pytest.raises(ValueError, match="maximum supported"):
        model(torch.rand(2, 4, 3, 224, 224))


def test_rejects_non_rgb_frames(model):
    with pytest.raises(ValueError, match="RGB"):
        model(torch.rand(2, 3, 1, 224, 224))


def test_rejects_zero_height(model):
    with pytest.raises(ValueError, match="RGB"):
        model(torch.rand(2, 3, 3, 0, 224))


def test_rejects_zero_width(model):
    with pytest.raises(ValueError, match="RGB"):
        model(torch.rand(2, 3, 3, 224, 0))


def test_rejects_invalid_state_label_dimensions(model, frames):
    labels = torch.randint(0, 100, (2, 20))

    with pytest.raises(ValueError, match="state_labels"):
        model(frames, state_labels=labels)


def test_rejects_mismatched_state_label_frames(model, frames):
    labels = torch.randint(0, 100, (2, 2, 20))

    with pytest.raises(ValueError, match="State labels"):
        model(frames, state_labels=labels)


def test_rejects_empty_state_label_sequence(model, frames):
    labels = torch.empty(2, 3, 0, dtype=torch.long)

    with pytest.raises(ValueError, match="non-empty sequence"):
        model(frames, state_labels=labels)


def test_rejects_invalid_transition_label_dimensions(model, frames):
    labels = torch.randint(0, 100, (2, 3, 20))

    with pytest.raises(ValueError, match="transition_labels"):
        model(frames, transition_labels=labels)


def test_rejects_mismatched_transition_batch(model, frames):
    labels = torch.randint(0, 100, (3, 20))

    with pytest.raises(ValueError, match="Transition labels"):
        model(frames, transition_labels=labels)


def test_rejects_empty_transition_label_sequence(model, frames):
    labels = torch.empty(2, 0, dtype=torch.long)

    with pytest.raises(ValueError, match="non-empty sequence"):
        model(frames, transition_labels=labels)


def test_rejects_fully_masked_transition_labels(model, frames):
    labels = torch.full((2, 20), -100)

    with pytest.raises(ValueError, match="non-masked token"):
        model(frames, transition_labels=labels)


@pytest.mark.parametrize(
    "state_length, transition_length",
    [
        (0, 96),
        (64, 0),
        (-1, 96),
        (64, -1),
    ],
)
def test_rejects_invalid_generation_lengths(
    model,
    frames,
    state_length,
    transition_length,
):
    with pytest.raises(ValueError, match="Generation lengths"):
        model.generate(
            frames,
            max_state_tokens=state_length,
            max_transition_tokens=transition_length,
        )
