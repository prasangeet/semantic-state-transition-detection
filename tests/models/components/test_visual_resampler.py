
import pytest
import torch

from src.sostd.models.components.visual_resampler import VisualResampler


@pytest.fixture
def model():
    return VisualResampler(
        input_dim=1024,
        output_dim=1024,
        num_queries=32,
        num_heads=16,
        dropout=0.0,
    )


# ---------------------------------------------------------
# V3 configuration
# ---------------------------------------------------------


def test_v3_default_configuration():
    model = VisualResampler()

    assert model.input_dim == 1024
    assert model.output_dim == 1024
    assert model.num_queries == 32
    assert model.num_heads == 16


def test_v3_attention_configuration():
    model = VisualResampler()

    assert model.cross_attention.embed_dim == 1024
    assert model.cross_attention.num_heads == 16


def test_reports_output_dimension(model):
    assert model.get_output_dim() == 1024


def test_reports_query_count(model):
    assert model.get_num_queries() == 32


# ---------------------------------------------------------
# Output shapes
# ---------------------------------------------------------


def test_returns_expected_shape(model):
    features = torch.randn(2, 3, 257, 1024)

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)


def test_supports_single_frame(model):
    features = torch.randn(2, 1, 257, 1024)

    output = model(features)

    assert output.shape == (2, 1, 32, 1024)


def test_supports_variable_token_counts(model):
    features = torch.randn(2, 3, 64, 1024)

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)


def test_supports_single_visual_token(model):
    features = torch.randn(2, 3, 1, 1024)

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)


def test_supports_different_batch_sizes(model):
    features = torch.randn(1, 3, 257, 1024)

    output = model(features)

    assert output.shape == (1, 3, 32, 1024)


def test_supports_different_input_and_output_dimensions():
    model = VisualResampler(
        input_dim=768,
        output_dim=1024,
        num_queries=32,
        num_heads=16,
    )

    features = torch.randn(2, 3, 257, 768)

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)


def test_uses_identity_projection_when_dimensions_match(model):
    assert isinstance(model.input_projection, torch.nn.Identity)


def test_uses_linear_projection_when_dimensions_differ():
    model = VisualResampler(
        input_dim=768,
        output_dim=1024,
        num_queries=32,
        num_heads=16,
    )

    assert isinstance(model.input_projection, torch.nn.Linear)


# ---------------------------------------------------------
# Numerical stability
# ---------------------------------------------------------


def test_output_is_finite(model):
    features = torch.randn(2, 3, 64, 1024)

    output = model(features)

    assert torch.isfinite(output).all()


def test_output_is_float32_for_float32_input(model):
    features = torch.randn(2, 3, 64, 1024)

    output = model(features)

    assert output.dtype == torch.float32


# ---------------------------------------------------------
# Gradient propagation
# ---------------------------------------------------------


def test_supports_gradient_backpropagation(model):
    features = torch.randn(
        2, 3, 64, 1024,
        requires_grad=True,
    )

    output = model(features)
    loss = output.square().mean()
    loss.backward()

    assert features.grad is not None
    assert torch.isfinite(features.grad).all()

    assert model.query_tokens.grad is not None
    assert torch.isfinite(model.query_tokens.grad).all()


def test_query_tokens_are_trainable(model):
    assert model.query_tokens.requires_grad


def test_query_tokens_are_shared_across_frames(model):
    assert model.query_tokens.shape == (1, 1, 32, 1024)


def test_attention_parameters_receive_gradients(model):
    features = torch.randn(2, 3, 64, 1024)

    model(features).square().mean().backward()

    grad = model.cross_attention.in_proj_weight.grad

    assert grad is not None
    assert torch.isfinite(grad).all()


def test_feed_forward_receives_gradients(model):
    features = torch.randn(2, 3, 64, 1024)

    model(features).square().mean().backward()

    grad = model.feed_forward[0].weight.grad

    assert grad is not None
    assert torch.isfinite(grad).all()


def test_layer_norm_parameters_receive_gradients(model):
    features = torch.randn(2, 3, 64, 1024)

    model(features).square().mean().backward()

    assert model.norm1.weight.grad is not None
    assert model.norm2.weight.grad is not None


# ---------------------------------------------------------
# Frame independence
# ---------------------------------------------------------


def test_resampling_is_independent_across_frames(model):
    model.eval()

    features = torch.randn(1, 3, 64, 1024)

    with torch.no_grad():
        original_output = model(features)

        modified_features = features.clone()
        modified_features[:, 1] += 10.0

        modified_output = model(modified_features)

    # Modifying frame 1 must not affect frames 0 and 2.
    torch.testing.assert_close(
        original_output[:, 0],
        modified_output[:, 0],
    )

    torch.testing.assert_close(
        original_output[:, 2],
        modified_output[:, 2],
    )

    # The modified frame should produce a different representation.
    assert not torch.allclose(
        original_output[:, 1],
        modified_output[:, 1],
    )


# ---------------------------------------------------------
# Input validation
# ---------------------------------------------------------


def test_rejects_invalid_input_dimensions(model):
    with pytest.raises(ValueError, match="Expected features"):
        model(torch.randn(2, 257, 1024))


def test_rejects_non_floating_input(model):
    features = torch.randint(
        0,
        255,
        (2, 3, 64, 1024),
    )

    with pytest.raises(TypeError, match="floating-point"):
        model(features)


def test_rejects_invalid_feature_dimension(model):
    features = torch.randn(2, 3, 64, 768)

    with pytest.raises(
        ValueError,
        match="Expected input dimension",
    ):
        model(features)


def test_rejects_zero_batch_size(model):
    with pytest.raises(ValueError, match="Batch size"):
        model(torch.randn(0, 3, 64, 1024))


def test_rejects_zero_frames(model):
    with pytest.raises(ValueError, match="At least one frame"):
        model(torch.randn(2, 0, 64, 1024))


def test_rejects_zero_visual_tokens(model):
    with pytest.raises(
        ValueError,
        match="At least one visual token",
    ):
        model(torch.randn(2, 3, 0, 1024))


# ---------------------------------------------------------
# Configuration validation
# ---------------------------------------------------------


@pytest.mark.parametrize(
    "kwargs",
    [
        {"input_dim": 0},
        {"input_dim": -1},
        {"output_dim": 0},
        {"output_dim": -1},
        {"num_queries": 0},
        {"num_heads": 0},
        {"output_dim": 1023, "num_heads": 16},
        {"dropout": -0.1},
        {"dropout": 1.0},
    ],
)
def test_rejects_invalid_configuration(kwargs):
    with pytest.raises(ValueError):
        VisualResampler(**kwargs)
