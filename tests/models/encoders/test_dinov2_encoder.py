
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import torch
import torch.nn as nn

from src.sostd.models.encoders.dinov2_encoder import DINOv2Encoder


class DummyBlock(nn.Module):
    """Lightweight transformer-block substitute for testing."""

    def __init__(self):
        super().__init__()
        self.scale = nn.Parameter(torch.ones(()))
        self.bias = nn.Parameter(torch.zeros(()))

    def forward(self, hidden_states):
        return hidden_states * self.scale + self.bias


class DummyBackbone(nn.Module):
    """Lightweight mock of the Hugging Face DINOv2-Large backbone."""

    def __init__(self):
        super().__init__()

        self.config = SimpleNamespace(
            hidden_size=1024,
            patch_size=14,
        )

        self.projection = nn.Linear(3, 1024)
        self.embeddings = nn.Identity()

        self.encoder = nn.Module()
        self.encoder.layer = nn.ModuleList(
            [DummyBlock() for _ in range(24)]
        )

        self.layernorm = nn.LayerNorm(1024)

    def forward(self, pixel_values, return_dict=True):
        batch_size = pixel_values.shape[0]

        pooled = pixel_values.mean(dim=(2, 3))
        features = self.projection(pooled)

        tokens = features.unsqueeze(1).expand(
            batch_size, 257, 1024
        )

        tokens = self.embeddings(tokens)

        for layer in self.encoder.layer:
            tokens = layer(tokens)

        tokens = self.layernorm(tokens)

        return SimpleNamespace(last_hidden_state=tokens)


@pytest.fixture
def mock_backbone():
    backbone = DummyBackbone()

    with patch(
        "src.sostd.models.encoders.dinov2_encoder.Dinov2Model.from_pretrained",
        return_value=backbone,
    ) as mock:
        yield backbone, mock


@pytest.fixture
def encoder(mock_backbone):
    return DINOv2Encoder()


# ---------------------------------------------------------
# Architecture and output
# ---------------------------------------------------------


def test_encoder_returns_expected_shape(encoder):
    images = torch.rand(2, 3, 224, 224)

    features = encoder(images)

    assert features.shape == (2, 257, 1024)


def test_encoder_supports_different_image_sizes(encoder):
    images = torch.rand(2, 3, 128, 160)

    features = encoder(images)

    assert features.shape == (2, 257, 1024)


def test_encoder_reports_correct_output_dimension(encoder):
    assert encoder.get_output_dim() == 1024


def test_encoder_reports_correct_token_count(encoder):
    assert encoder.get_num_tokens() == 257


def test_encoder_uses_dinov2_large(mock_backbone):
    _, mock = mock_backbone

    DINOv2Encoder()

    mock.assert_called_once_with("facebook/dinov2-large")


def test_encoder_uses_pretrained_weights_by_default(mock_backbone):
    _, mock = mock_backbone

    DINOv2Encoder()

    mock.assert_called_once()


def test_encoder_supports_custom_image_size(mock_backbone):
    model = DINOv2Encoder(image_size=280)

    assert model.get_num_tokens() == 401


# ---------------------------------------------------------
# Frozen mode
# ---------------------------------------------------------


def test_encoder_freezes_backbone_by_default(encoder):
    assert all(
        not parameter.requires_grad
        for parameter in encoder.backbone.parameters()
    )


def test_encoder_keeps_backbone_in_eval_mode(encoder):
    encoder.train()

    assert encoder.training
    assert not encoder.backbone.training


def test_encoder_returns_no_grad_features(encoder):
    images = torch.rand(
        2, 3, 224, 224,
        requires_grad=True,
    )

    features = encoder(images)

    assert not features.requires_grad


def test_frozen_encoder_has_zero_trainable_parameters(encoder):
    assert encoder.get_num_trainable_parameters() == 0


# ---------------------------------------------------------
# Selective fine-tuning
# ---------------------------------------------------------


@pytest.fixture
def selective_encoder(mock_backbone):
    return DINOv2Encoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=4,
    )


def test_selectively_unfreezes_last_four_layers(selective_encoder):
    layers = selective_encoder.encoder_layers

    assert len(layers) == 24

    for layer in layers[:-4]:
        assert all(
            not parameter.requires_grad
            for parameter in layer.parameters()
        )

    for layer in layers[-4:]:
        assert all(
            parameter.requires_grad
            for parameter in layer.parameters()
        )


def test_selective_finetuning_keeps_embeddings_frozen(
    selective_encoder,
):
    assert all(
        not parameter.requires_grad
        for parameter in selective_encoder.backbone.embeddings.parameters()
    )


def test_selective_finetuning_keeps_layernorm_frozen(
    selective_encoder,
):
    assert all(
        not parameter.requires_grad
        for parameter in selective_encoder.backbone.layernorm.parameters()
    )


def test_selective_finetuning_returns_grad_enabled_features(
    selective_encoder,
):
    images = torch.rand(2, 3, 224, 224)

    features = selective_encoder(images)

    assert features.requires_grad


def test_selective_finetuning_propagates_gradients(
    selective_encoder,
):
    images = torch.rand(2, 3, 224, 224)

    features = selective_encoder(images)
    features.mean().backward()

    layers = selective_encoder.encoder_layers

    assert layers[-1].scale.grad is not None
    assert torch.isfinite(layers[-1].scale.grad)

    assert layers[-1].bias.grad is not None

    assert layers[0].scale.grad is None
    assert layers[0].bias.grad is None


def test_selective_finetuning_keeps_earlier_layers_in_eval_mode(
    selective_encoder,
):
    selective_encoder.train()

    layers = selective_encoder.encoder_layers

    assert all(
        not layer.training
        for layer in layers[:-4]
    )

    assert all(
        layer.training
        for layer in layers[-4:]
    )


def test_selective_finetuning_keeps_embeddings_and_layernorm_in_eval(
    selective_encoder,
):
    selective_encoder.train()

    assert not selective_encoder.backbone.embeddings.training
    assert not selective_encoder.backbone.layernorm.training


def test_selective_finetuning_reports_trainable_parameters(
    selective_encoder,
):
    expected = sum(
        parameter.numel()
        for layer in selective_encoder.encoder_layers[-4:]
        for parameter in layer.parameters()
    )

    assert (
        selective_encoder.get_num_trainable_parameters()
        == expected
    )


# ---------------------------------------------------------
# Full fine-tuning
# ---------------------------------------------------------


@pytest.fixture
def fully_trainable_encoder(mock_backbone):
    return DINOv2Encoder(
        freeze_backbone=False,
    )


def test_full_finetuning_unfreezes_entire_backbone(
    fully_trainable_encoder,
):
    assert all(
        parameter.requires_grad
        for parameter in fully_trainable_encoder.backbone.parameters()
    )


def test_full_finetuning_returns_grad_enabled_features(
    fully_trainable_encoder,
):
    images = torch.rand(2, 3, 224, 224)

    features = fully_trainable_encoder(images)

    assert features.requires_grad


def test_full_finetuning_propagates_gradients(
    fully_trainable_encoder,
):
    images = torch.rand(2, 3, 224, 224)

    features = fully_trainable_encoder(images)
    features.mean().backward()

    assert (
        fully_trainable_encoder.encoder_layers[0].scale.grad
        is not None
    )

    assert (
        fully_trainable_encoder.encoder_layers[-1].scale.grad
        is not None
    )


def test_full_finetuning_reports_all_parameters(
    fully_trainable_encoder,
):
    assert (
        fully_trainable_encoder.get_num_trainable_parameters()
        == fully_trainable_encoder.get_num_parameters()
    )


# ---------------------------------------------------------
# Input validation
# ---------------------------------------------------------


@pytest.mark.parametrize(
    "images",
    [
        torch.rand(3, 224, 224),
        torch.rand(2, 1, 224, 224),
        torch.rand(2, 4, 224, 224),
    ],
)
def test_encoder_rejects_invalid_shapes(encoder, images):
    with pytest.raises(ValueError):
        encoder(images)


def test_encoder_rejects_integer_images(encoder):
    images = torch.randint(
        0,
        255,
        (2, 3, 224, 224),
        dtype=torch.uint8,
    )

    with pytest.raises(TypeError):
        encoder(images)


def test_encoder_rejects_zero_batch_size(encoder):
    images = torch.rand(0, 3, 224, 224)

    with pytest.raises(ValueError, match="Batch size"):
        encoder(images)


@pytest.mark.parametrize(
    "image_size",
    [0, -14, 225],
)
def test_encoder_rejects_invalid_image_size(image_size):
    with pytest.raises(ValueError):
        DINOv2Encoder(image_size=image_size)


@pytest.mark.parametrize(
    "unfreeze_last_n_layers",
    [-1, 25],
)
def test_encoder_rejects_invalid_unfreeze_count(
    unfreeze_last_n_layers,
):
    with pytest.raises(ValueError):
        DINOv2Encoder(
            unfreeze_last_n_layers=unfreeze_last_n_layers
        )


def test_encoder_rejects_non_integer_unfreeze_count():
    with pytest.raises(TypeError):
        DINOv2Encoder(
            unfreeze_last_n_layers=4.5
        )


def test_encoder_rejects_conflicting_finetuning_configuration():
    with pytest.raises(ValueError):
        DINOv2Encoder(
            freeze_backbone=False,
            unfreeze_last_n_layers=4,
        )
