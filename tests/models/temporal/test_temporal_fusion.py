
import pytest
import torch

from src.sostd.models.temporal.temporal_fusion import TemporalFusion


@pytest.fixture
def model():
    return TemporalFusion(
        input_dim=1024,
        hidden_dim=1024,
        num_heads=16,
        num_layers=1,
        max_frames=3,
        dropout=0.0,
    )


# ---------------------------------------------------------
# V3 configuration
# ---------------------------------------------------------


def test_v3_default_configuration():
    model = TemporalFusion()

    assert model.input_dim == 1024
    assert model.hidden_dim == 1024
    assert model.num_heads == 16
    assert model.num_layers == 4
    assert model.max_frames == 3


def test_v3_attention_dimensions():
    model = TemporalFusion()

    for block in model.blocks:
        assert block.spatial_attention.embed_dim == 1024
        assert block.temporal_attention.embed_dim == 1024
        assert block.spatial_attention.num_heads == 16
        assert block.temporal_attention.num_heads == 16


# ---------------------------------------------------------
# Output shapes
# ---------------------------------------------------------


def test_returns_expected_shape(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)


def test_supports_single_frame(model):
    features = torch.randn(2, 1, 32, 1024)

    output = model(features)

    assert output.shape == (2, 1, 32, 1024)


def test_supports_variable_token_counts(model):
    features = torch.randn(2, 3, 64, 1024)

    output = model(features)

    assert output.shape == (2, 3, 64, 1024)


def test_supports_different_batch_sizes(model):
    features = torch.randn(1, 3, 32, 1024)

    output = model(features)

    assert output.shape == (1, 3, 32, 1024)


def test_supports_original_dinov2_token_count(model):
    features = torch.randn(1, 3, 257, 1024)

    output = model(features)

    assert output.shape == (1, 3, 257, 1024)


# ---------------------------------------------------------
# Numerical stability and precision
# ---------------------------------------------------------


def test_output_is_finite(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert torch.isfinite(output).all()


def test_output_is_float32(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)

    assert output.dtype == torch.float32


def test_supports_half_precision_input(model):
    features = torch.randn(2, 3, 32, 1024).half()

    output = model(features)

    assert output.shape == (2, 3, 32, 1024)
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
    loss = output.square().mean()
    loss.backward()

    assert features.grad is not None
    assert model.input_projection.weight.grad is not None
    assert model.temporal_embedding.grad is not None

    assert torch.isfinite(features.grad).all()
    assert torch.isfinite(
        model.input_projection.weight.grad
    ).all()
    assert torch.isfinite(model.temporal_embedding.grad).all()


def test_spatial_attention_receives_gradients(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)
    output.square().mean().backward()

    for layer_idx, block in enumerate(model.blocks):
        grad = block.spatial_attention.in_proj_weight.grad

        assert grad is not None, (
            f"Spatial attention in block {layer_idx} "
            "did not receive gradients."
        )

        assert torch.isfinite(grad).all()


def test_temporal_attention_receives_gradients(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)
    output.square().mean().backward()

    for layer_idx, block in enumerate(model.blocks):
        grad = block.temporal_attention.in_proj_weight.grad

        assert grad is not None, (
            f"Temporal attention in block {layer_idx} "
            "did not receive gradients."
        )

        assert torch.isfinite(grad).all()


def test_spatial_ffn_receives_gradients(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)
    output.square().mean().backward()

    for layer_idx, block in enumerate(model.blocks):
        grad = block.spatial_ffn[0].weight.grad

        assert grad is not None, (
            f"Spatial FFN in block {layer_idx} "
            "did not receive gradients."
        )

        assert torch.isfinite(grad).all()


def test_temporal_ffn_receives_gradients(model):
    features = torch.randn(2, 3, 32, 1024)

    output = model(features)
    output.square().mean().backward()

    for layer_idx, block in enumerate(model.blocks):
        grad = block.temporal_ffn[0].weight.grad

        assert grad is not None, (
            f"Temporal FFN in block {layer_idx} "
            "did not receive gradients."
        )

        assert torch.isfinite(grad).all()


def test_temporal_embedding_is_trainable(model):
    assert model.temporal_embedding.requires_grad


def test_all_parameters_are_trainable(model):
    for name, parameter in model.named_parameters():
        assert parameter.requires_grad, (
            f"Parameter {name} is unexpectedly frozen."
        )


# ---------------------------------------------------------
# Temporal and spatial behavior
# ---------------------------------------------------------


def test_single_frame_temporal_attention_is_valid(model):
    features = torch.randn(2, 1, 32, 1024)

    output = model(features)

    assert output.shape == (2, 1, 32, 1024)
    assert torch.isfinite(output).all()


def test_temporal_embedding_changes_with_frame_position(model):
    assert model.temporal_embedding.shape == (1, 3, 1, 1024)

    assert not torch.equal(
        model.temporal_embedding[:, 0],
        model.temporal_embedding[:, 1],
    )


# ---------------------------------------------------------
# Automatic mixed precision
# ---------------------------------------------------------


@pytest.mark.parametrize("device", ["cpu", "cuda"])
def test_amp_produces_finite_gradients(device):
    if device == "cuda" and not torch.cuda.is_available():
        pytest.skip("CUDA is not available.")

    model = TemporalFusion(
        input_dim=1024,
        hidden_dim=1024,
        num_heads=16,
        num_layers=1,
        max_frames=3,
        dropout=0.0,
    ).to(device)

    features = torch.randn(
        1, 3, 16, 1024,
        device=device,
        requires_grad=True,
    )

    with torch.autocast(
        device_type=device,
        dtype=torch.float16,
        enabled=(device == "cuda"),
    ):
        output = model(features)
        loss = output.square().mean()

    assert torch.isfinite(output).all()
    assert torch.isfinite(loss)
    assert output.dtype == torch.float32

    loss.backward()

    assert features.grad is not None
    assert model.temporal_embedding.grad is not None

    assert torch.isfinite(features.grad).all()
    assert torch.isfinite(model.temporal_embedding.grad).all()

    for name, parameter in model.named_parameters():
        if parameter.grad is not None:
            assert torch.isfinite(parameter.grad).all(), (
                f"Non-finite gradient in {name}"
            )


# ---------------------------------------------------------
# Input validation
# ---------------------------------------------------------


def test_rejects_invalid_input_dimensions(model):
    with pytest.raises(ValueError, match="Expected features"):
        model(torch.randn(2, 32, 1024))


def test_rejects_non_floating_input(model):
    features = torch.randint(
        0, 255,
        (2, 3, 32, 1024),
    )

    with pytest.raises(TypeError, match="floating-point"):
        model(features)


def test_rejects_invalid_feature_dimension(model):
    features = torch.randn(2, 3, 32, 768)

    with pytest.raises(
        ValueError,
        match="Expected input dimension",
    ):
        model(features)


def test_rejects_too_many_frames(model):
    features = torch.randn(2, 4, 32, 1024)

    with pytest.raises(
        ValueError,
        match="maximum supported",
    ):
        model(features)


def test_rejects_zero_batch_size(model):
    features = torch.randn(0, 3, 32, 1024)

    with pytest.raises(
        ValueError,
        match="Batch size must be positive",
    ):
        model(features)


def test_rejects_zero_frames(model):
    features = torch.randn(2, 0, 32, 1024)

    with pytest.raises(
        ValueError,
        match="At least one temporal frame",
    ):
        model(features)


def test_rejects_zero_visual_tokens(model):
    features = torch.randn(2, 3, 0, 1024)

    with pytest.raises(
        ValueError,
        match="At least one spatial token",
    ):
        model(features)


# ---------------------------------------------------------
# Configuration validation
# ---------------------------------------------------------


@pytest.mark.parametrize(
    "kwargs",
    [
        {"input_dim": 0},
        {"input_dim": -1},
        {"hidden_dim": 0},
        {"hidden_dim": 255, "num_heads": 4},
        {"num_heads": 0},
        {"num_layers": 0},
        {"max_frames": 0},
        {"dropout": -0.1},
        {"dropout": 1.0},
    ],
)
def test_rejects_invalid_configuration(kwargs):
    with pytest.raises(ValueError):
        TemporalFusion(**kwargs)
