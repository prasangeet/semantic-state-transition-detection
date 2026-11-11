
from types import SimpleNamespace

import pytest
import torch
import torch.nn as nn

from src.sostd.models.language.flan_t5_decoder import FlanT5Decoder


class DummyStack(nn.Module):
    def __init__(self, hidden_dim=512, num_layers=4):
        super().__init__()

        self.block = nn.ModuleList([
            nn.Linear(hidden_dim, hidden_dim)
            for _ in range(num_layers)
        ])


class DummyT5(nn.Module):
    def __init__(
        self,
        hidden_dim=512,
        vocab_size=100,
        num_layers=4,
    ):
        super().__init__()

        self.config = SimpleNamespace(d_model=hidden_dim)

        self.encoder = DummyStack(hidden_dim, num_layers)
        self.decoder = DummyStack(hidden_dim, num_layers)

        self.projection = nn.Linear(hidden_dim, vocab_size)

        self.forward_args = None
        self.generate_args = None
        self.generate_grad_enabled = None

    def forward(
        self,
        inputs_embeds,
        attention_mask,
        labels,
        return_dict=True,
    ):
        self.forward_args = {
            "inputs_embeds": inputs_embeds,
            "attention_mask": attention_mask,
            "labels": labels,
            "return_dict": return_dict,
        }

        context = inputs_embeds.mean(dim=1, keepdim=True)
        context = context.expand(-1, labels.shape[1], -1)

        logits = self.projection(context)

        return SimpleNamespace(
            loss=logits.mean(),
            logits=logits,
        )

    def generate(
        self,
        inputs_embeds,
        attention_mask,
        max_new_tokens,
        **kwargs,
    ):
        self.generate_args = {
            "inputs_embeds": inputs_embeds,
            "attention_mask": attention_mask,
            "max_new_tokens": max_new_tokens,
            **kwargs,
        }

        self.generate_grad_enabled = torch.is_grad_enabled()

        return torch.ones(
            inputs_embeds.shape[0],
            max_new_tokens,
            dtype=torch.long,
            device=inputs_embeds.device,
        )


@pytest.fixture
def backbone():
    return DummyT5()


@pytest.fixture
def model(backbone):
    return FlanT5Decoder(
        freeze_backbone=False,
        model=backbone,
    )


# ---------------------------------------------------------
# Forward and output
# ---------------------------------------------------------


def test_returns_expected_training_output(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    output = model(embeddings, labels)

    assert output.loss is not None
    assert output.logits.shape == (2, 20, 100)


def test_flattens_temporal_dimensions(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    model(embeddings, labels)

    passed = model.backbone.forward_args["inputs_embeds"]

    assert passed.shape == (2, 24, 512)


def test_accepts_flattened_visual_embeddings(model):
    embeddings = torch.randn(2, 24, 512)
    labels = torch.randint(0, 100, (2, 20))

    output = model(embeddings, labels)

    assert output.loss is not None
    assert model.backbone.forward_args["inputs_embeds"].shape == (
        2, 24, 512
    )


def test_output_uses_fp32_embeddings(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    output = model(embeddings, labels)

    assert model.backbone.forward_args["inputs_embeds"].dtype == torch.float32
    assert output.loss is not None


# ---------------------------------------------------------
# Attention masks
# ---------------------------------------------------------


def test_creates_default_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    model(embeddings, labels)

    mask = model.backbone.forward_args["attention_mask"]

    assert mask.shape == (2, 24)
    assert torch.all(mask == 1)


def test_accepts_temporal_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))
    mask = torch.ones(2, 3, 8, dtype=torch.long)

    model(embeddings, labels, attention_mask=mask)

    passed_mask = model.backbone.forward_args["attention_mask"]

    assert passed_mask.shape == (2, 24)


def test_accepts_flattened_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))
    mask = torch.ones(2, 24, dtype=torch.long)

    model(embeddings, labels, attention_mask=mask)

    passed_mask = model.backbone.forward_args["attention_mask"]

    assert torch.equal(passed_mask, mask)


def test_preserves_padding_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    mask = torch.ones(2, 3, 8, dtype=torch.long)
    mask[:, :, -2:] = 0

    model(embeddings, labels, attention_mask=mask)

    passed_mask = model.backbone.forward_args["attention_mask"]

    assert torch.equal(passed_mask, mask.reshape(2, 24))


def test_converts_boolean_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    mask = torch.ones(2, 3, 8, dtype=torch.bool)

    model(embeddings, labels, attention_mask=mask)

    passed_mask = model.backbone.forward_args["attention_mask"]

    assert passed_mask.dtype == torch.long
    assert torch.all(passed_mask == 1)


def test_rejects_invalid_attention_mask_shape(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 10))
    mask = torch.ones(2, 10)

    with pytest.raises(ValueError, match="Attention mask"):
        model(embeddings, labels, attention_mask=mask)


def test_rejects_non_binary_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    mask = torch.ones(2, 3, 8)
    mask[:, :, 0] = 0.5

    with pytest.raises(ValueError, match="only 0 and 1"):
        model(embeddings, labels, attention_mask=mask)


def test_rejects_non_finite_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    mask = torch.ones(2, 3, 8)
    mask[0, 0, 0] = float("nan")

    with pytest.raises(ValueError, match="finite values"):
        model(embeddings, labels, attention_mask=mask)


def test_rejects_fully_masked_visual_sequence(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 20))

    mask = torch.ones(2, 3, 8, dtype=torch.long)
    mask[1] = 0

    with pytest.raises(
        ValueError,
        match="at least one unmasked token",
    ):
        model(embeddings, labels, attention_mask=mask)


# ---------------------------------------------------------
# Gradient propagation
# ---------------------------------------------------------


def test_supports_gradient_backpropagation(model):
    embeddings = torch.randn(
        2, 3, 8, 512,
        requires_grad=True,
    )
    labels = torch.randint(0, 100, (2, 20))

    output = model(embeddings, labels)
    output.loss.backward()

    assert embeddings.grad is not None
    assert model.backbone.projection.weight.grad is not None

    assert torch.isfinite(embeddings.grad).all()
    assert torch.isfinite(
        model.backbone.projection.weight.grad
    ).all()


def test_forward_preserves_finite_gradients_under_autocast(model):
    embeddings = torch.randn(
        2, 3, 8, 512,
        requires_grad=True,
    )
    labels = torch.randint(0, 100, (2, 20))

    with torch.autocast(
        device_type="cpu",
        dtype=torch.bfloat16,
    ):
        output = model(embeddings, labels)

    output.loss.backward()

    assert embeddings.grad is not None
    assert torch.isfinite(embeddings.grad).all()


def test_forward_disables_outer_autocast(model):
    embeddings = torch.randn(
        2, 3, 8, 512,
        requires_grad=True,
    )
    labels = torch.randint(0, 100, (2, 20))

    with torch.autocast(
        device_type="cpu",
        dtype=torch.bfloat16,
    ):
        model(embeddings, labels)

    passed = model.backbone.forward_args["inputs_embeds"]

    assert passed.dtype == torch.float32


# ---------------------------------------------------------
# Backbone freezing and fine-tuning
# ---------------------------------------------------------


def test_freezes_backbone_by_default(backbone):
    model = FlanT5Decoder(model=backbone)

    assert all(
        not parameter.requires_grad
        for parameter in model.backbone.parameters()
    )


def test_keeps_frozen_backbone_in_eval_mode(backbone):
    model = FlanT5Decoder(model=backbone)

    model.train()

    assert model.training
    assert not model.backbone.training


def test_can_unfreeze_backbone(backbone):
    model = FlanT5Decoder(
        freeze_backbone=False,
        model=backbone,
    )

    assert all(
        parameter.requires_grad
        for parameter in model.backbone.parameters()
    )


def test_selectively_unfreezes_final_encoder_blocks(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    blocks = model.backbone.encoder.block

    for block in blocks[:-2]:
        assert all(not p.requires_grad for p in block.parameters())

    for block in blocks[-2:]:
        assert all(p.requires_grad for p in block.parameters())


def test_selectively_unfreezes_final_decoder_blocks(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    blocks = model.backbone.decoder.block

    for block in blocks[:-2]:
        assert all(not p.requires_grad for p in block.parameters())

    for block in blocks[-2:]:
        assert all(p.requires_grad for p in block.parameters())


def test_selective_unfreezing_keeps_other_parameters_frozen(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    assert not any(
        p.requires_grad
        for p in model.backbone.projection.parameters()
    )


def test_selective_unfreezing_keeps_early_blocks_frozen(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=1,
        model=backbone,
    )

    assert all(
        not p.requires_grad
        for p in model.backbone.encoder.block[0].parameters()
    )

    assert all(
        not p.requires_grad
        for p in model.backbone.decoder.block[0].parameters()
    )


def test_selective_unfreezing_preserves_trainable_blocks_in_train_mode(
    backbone,
):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    model.train()

    assert not model.backbone.training

    for block in model.backbone.encoder.block[:-2]:
        assert not block.training

    for block in model.backbone.decoder.block[:-2]:
        assert not block.training

    for block in model.backbone.encoder.block[-2:]:
        assert block.training

    for block in model.backbone.decoder.block[-2:]:
        assert block.training


def test_selective_unfreezing_returns_to_eval_mode(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    model.eval()

    for block in model.backbone.encoder.block:
        assert not block.training

    for block in model.backbone.decoder.block:
        assert not block.training


def test_reports_parameter_counts(backbone):
    model = FlanT5Decoder(
        freeze_backbone=True,
        unfreeze_last_n_layers=2,
        model=backbone,
    )

    total = sum(p.numel() for p in model.parameters())

    trainable = sum(
        p.numel()
        for p in model.parameters()
        if p.requires_grad
    )

    assert model.get_total_parameters() == total
    assert model.get_trainable_parameters() == trainable
    assert 0 < trainable < total


def test_rejects_negative_unfreeze_layers(backbone):
    with pytest.raises(ValueError, match="unfreeze_last_n_layers"):
        FlanT5Decoder(
            unfreeze_last_n_layers=-1,
            model=backbone,
        )


def test_rejects_too_many_unfreeze_layers(backbone):
    with pytest.raises(ValueError, match="exceeds the number"):
        FlanT5Decoder(
            unfreeze_last_n_layers=5,
            model=backbone,
        )


# ---------------------------------------------------------
# Generation
# ---------------------------------------------------------


def test_generate_returns_token_ids(model):
    embeddings = torch.randn(2, 3, 8, 512)

    generated = model.generate(
        embeddings,
        max_new_tokens=32,
    )

    assert generated.shape == (2, 32)
    assert generated.dtype == torch.long


def test_generate_flattens_visual_embeddings(model):
    embeddings = torch.randn(2, 3, 8, 512)

    model.generate(embeddings)

    passed = model.backbone.generate_args["inputs_embeds"]

    assert passed.shape == (2, 24, 512)


def test_generate_passes_generation_options(model):
    embeddings = torch.randn(2, 3, 8, 512)

    model.generate(
        embeddings,
        max_new_tokens=40,
        num_beams=4,
    )

    args = model.backbone.generate_args

    assert args["max_new_tokens"] == 40
    assert args["num_beams"] == 4


def test_generate_disables_gradient_tracking(model):
    embeddings = torch.randn(
        2, 3, 8, 512,
        requires_grad=True,
    )

    model.generate(embeddings)

    assert model.backbone.generate_grad_enabled is False


def test_generate_disables_outer_autocast(model):
    embeddings = torch.randn(2, 3, 8, 512)

    with torch.autocast(
        device_type="cpu",
        dtype=torch.bfloat16,
    ):
        model.generate(embeddings)

    passed = model.backbone.generate_args["inputs_embeds"]

    assert passed.dtype == torch.float32


def test_generate_disables_gradient_tracking_under_autocast(model):
    embeddings = torch.randn(2, 3, 8, 512)

    with torch.autocast(
        device_type="cpu",
        dtype=torch.bfloat16,
    ):
        model.generate(embeddings)

    assert model.backbone.generate_grad_enabled is False


def test_generate_accepts_explicit_attention_mask(model):
    embeddings = torch.randn(2, 3, 8, 512)

    mask = torch.ones(2, 3, 8, dtype=torch.long)
    mask[:, :, -2:] = 0

    model.generate(
        embeddings,
        attention_mask=mask,
    )

    passed = model.backbone.generate_args["attention_mask"]

    assert torch.equal(passed, mask.reshape(2, 24))


def test_generate_accepts_explicit_max_new_tokens(model):
    embeddings = torch.randn(2, 3, 8, 512)

    model.generate(
        embeddings,
        max_new_tokens=64,
    )

    assert model.backbone.generate_args["max_new_tokens"] == 64


def test_generate_rejects_reserved_inputs_embeds(model):
    embeddings = torch.randn(2, 3, 8, 512)

    with pytest.raises(ValueError, match="inputs_embeds"):
        model.generate(
            embeddings,
            **{"inputs_embeds": embeddings},
        )


def test_generate_rejects_invalid_generation_length(model):
    embeddings = torch.randn(2, 3, 8, 512)

    with pytest.raises(ValueError, match="max_new_tokens"):
        model.generate(embeddings, max_new_tokens=0)


# ---------------------------------------------------------
# Invalid inputs
# ---------------------------------------------------------


def test_rejects_invalid_visual_dimensions(model):
    with pytest.raises(
        ValueError,
        match="Expected visual embeddings",
    ):
        model(
            torch.randn(2, 512),
            torch.randint(0, 100, (2, 10)),
        )


def test_rejects_wrong_embedding_dimension(model):
    embeddings = torch.randn(2, 3, 8, 256)
    labels = torch.randint(0, 100, (2, 10))

    with pytest.raises(
        ValueError,
        match="Decoder expects embedding dimension",
    ):
        model(embeddings, labels)


def test_rejects_wrong_label_dimensions(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (2, 10, 1))

    with pytest.raises(ValueError, match="Labels must have shape"):
        model(embeddings, labels)


def test_rejects_empty_labels(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.empty(2, 0, dtype=torch.long)

    with pytest.raises(
        ValueError,
        match="non-empty batch and sequence",
    ):
        model(embeddings, labels)


def test_rejects_zero_label_batch(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.empty(0, 10, dtype=torch.long)

    with pytest.raises(
        ValueError,
        match="non-empty batch and sequence",
    ):
        model(embeddings, labels)


def test_rejects_mismatched_batch_sizes(model):
    embeddings = torch.randn(2, 3, 8, 512)
    labels = torch.randint(0, 100, (3, 10))

    with pytest.raises(
        ValueError,
        match="matching batch dimensions",
    ):
        model(embeddings, labels)


def test_rejects_zero_visual_frames(model):
    embeddings = torch.randn(2, 0, 8, 512)
    labels = torch.randint(0, 100, (2, 10))

    with pytest.raises(
        ValueError,
        match="at least one frame and one token",
    ):
        model(embeddings, labels)


def test_rejects_zero_visual_tokens(model):
    embeddings = torch.randn(2, 3, 0, 512)
    labels = torch.randint(0, 100, (2, 10))

    with pytest.raises(
        ValueError,
        match="at least one frame and one token",
    ):
        model(embeddings, labels)


def test_rejects_zero_visual_batch(model):
    embeddings = torch.randn(0, 3, 8, 512)
    labels = torch.randint(0, 100, (1, 10))

    with pytest.raises(
        ValueError,
        match="Batch size must be positive",
    ):
        model(embeddings, labels)


def test_rejects_non_floating_visual_embeddings(model):
    embeddings = torch.randint(
        0,
        255,
        (2, 3, 8, 512),
    )
    labels = torch.randint(0, 100, (2, 10))

    with pytest.raises(TypeError, match="floating-point"):
        model(embeddings, labels)


def test_rejects_full_and_selective_finetuning_combination(backbone):
    with pytest.raises(
        ValueError,
        match="cannot be combined",
    ):
        FlanT5Decoder(
            freeze_backbone=False,
            unfreeze_last_n_layers=2,
            model=backbone,
        )