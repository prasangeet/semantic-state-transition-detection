
import pytest
import torch

from src.sostd.models.components.visual_projection import VisualProjection


@pytest.fixture
def model():
    return VisualProjection(
        input_dim=1024,
        output_dim=768,
        dropout=0.0,
    )


# ---------------------------------------------------------
# V3 configuration
# ---------------------------------------------------------


def test_default_v3_configuration():
    model = VisualProjection()

    assert model.input_dim == 1024
    assert model.output_dim == 768
    assert model.projection.in_features == 1024
    assert model.projection.out_features == 768


def test_reports_input_dimension(model):
    assert model.get_input_dim() == 1024


def test_reports_output_dimension(model):
    assert model.get_output_dim() == 768


# ---------------------------------------------------------
# Output shapes
# ---------------------------------------------------------


def test_returns_expected_shape(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert output.shape == (2, 3, 32, 768)


def test_supports_single_frame(model):
    features = torch.randn(2, 1, 32, 1024)

    output = model(features)

    assert output.shape == (2, 1, 32, 768)


def test_supports_single_visual_token(model):
    features = torch.randn(2, 3, 1, 1024)

    output = model(features)

    assert output.shape == (2, 3, 1, 768)


def test_supports_different_batch_sizes(model):
    features = torch.randn(1, 3, 32, 1024)

    output = model(features)

    assert output.shape == (1, 3, 32, 768)


def test_supports_variable_token_counts(model):
    features = torch.randn(2, 3, 64, 1024)

    output = model(features)

    assert output.shape == (2, 3, 64, 768)


# ---------------------------------------------------------
# Numerical stability and precision
# ---------------------------------------------------------


def test_output_is_finite(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert torch.isfinite(output).all()


def test_output_uses_expected_dtype(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert output.dtype == torch.float32


def test_supports_half_precision_input(model):
    features = torch.randn(2, 3, 32, 1024).half()

    output = model(features)

    assert output.shape == (2, 3, 32, 768)
    assert output.dtype == torch.float32
    assert torch.isfinite(output).all()


# ---------------------------------------------------------
# Gradient propagation
# ---------------------------------------------------------


def test_supports_gradient_backpropagation(model):
    features = torch.randn(
        2, 3, 32, 1024,
        requires_grad=True,
    )

    output = model(features)
    output.square().mean().backward()

    assert features.grad is not None
    assert model.projection.weight.grad is not None
    assert model.norm.weight.grad is not None

    assert torch.isfinite(features.grad).all()
    assert torch.isfinite(model.projection.weight.grad).all()
    assert torch.isfinite(model.norm.weight.grad).all()


def test_projection_parameters_are_trainable(model):
    assert model.projection.weight.requires_grad
    assert model.projection.bias.requires_grad
    assert model.norm.weight.requires_grad
    assert model.norm.bias.requires_grad


def test_projection_has_expected_parameter_count(model):
    expected = (
        1024 * 768
        + 768
        + 1024
        + 1024
    )

    actual = sum(
        parameter.numel()
        for parameter in model.parameters()
    )

    assert actual == expected


# ---------------------------------------------------------
# Dropout behavior
# ---------------------------------------------------------


def test_dropout_respects_training_mode():
    model = VisualProjection(
        input_dim=1024,
        output_dim=768,
        dropout=0.5,
    )

    features = torch.randn(2, 3, 32, 1024)

    model.eval()
    output_eval = model(features)

    model.train()
    output_train = model(features)

    assert output_eval.shape == output_train.shape
    assert not torch.equal(output_eval, output_train)


def test_dropout_is_disabled_in_evaluation_mode():
    model = VisualProjection(
        input_dim=1024,
        output_dim=768,
        dropout=0.5,
    )

    features = torch.randn(2, 3, 32, 1024)

    model.eval()

    output1 = model(features)
    output2 = model(features)

    torch.testing.assert_close(output1, output2)


# ---------------------------------------------------------
# Input validation
# ---------------------------------------------------------


def test_rejects_invalid_input_dimensions(model):
    with pytest.raises(ValueError, match="Expected features"):
        model(torch.randn(2, 32, 1024))


def test_rejects_invalid_feature_dimension(model):
    with pytest.raises(
        ValueError,
        match="Expected input dimension",
    ):
        model(torch.randn(2, 3, 32, 768))


def test_rejects_non_floating_input(model):
    features = torch.randint(
        0,
        255,
        (2, 3, 32, 1024),
    )

    with pytest.raises(TypeError, match="floating-point"):
        model(features)


def test_rejects_zero_batch_size(model):
    with pytest.raises(
        ValueError,
        match="Batch size must be positive",
    ):
        model(torch.randn(0, 3, 32, 1024))


def test_rejects_zero_frames(model):
    with pytest.raises(
        ValueError,
        match="At least one frame",
    ):
        model(torch.randn(2, 0, 32, 1024))


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
        {"dropout": -0.1},
        {"dropout": 1.0},
    ],
)
def test_rejects_invalid_configuration(kwargs):
    with pytest.raises(ValueError):
        VisualProjection(**kwargs)
