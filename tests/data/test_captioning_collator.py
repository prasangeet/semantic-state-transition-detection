
from __future__ import annotations

from collections import UserDict

import pytest
import torch

from src.sostd.data.collate import (
    CaptioningCollator,
    temporal_collate_fn,
)


class FakeTokenizer:
    """Minimal tokenizer for testing caption collation."""

    pad_token_id = 0

    def __call__(
        self,
        texts,
        padding=True,
        truncation=False,
        max_length=None,
        return_tensors=None,
    ):
        encoded = []

        for text in texts:
            # Deterministic non-zero token IDs.
            tokens = [
                index + 1
                for index, _ in enumerate(text.split())
            ]

            if truncation and max_length is not None:
                tokens = tokens[:max_length]

            encoded.append(tokens)

        max_tokens = max(len(tokens) for tokens in encoded)

        input_ids = torch.full(
            (len(encoded), max_tokens),
            self.pad_token_id,
            dtype=torch.long,
        )

        for index, tokens in enumerate(encoded):
            input_ids[index, :len(tokens)] = torch.tensor(
                tokens,
                dtype=torch.long,
            )

        return {"input_ids": input_ids}


@pytest.fixture
def sample():
    frame_conversations = {
        "Frame_1": (
            {"from": "human", "value": "Describe state of salt"},
            {"from": "gpt", "value": "Salt is falling."},
        ),
        "Frame_2": (
            {"from": "human", "value": "Describe state of salt"},
            {"from": "gpt", "value": "Salt is falling densely."},
        ),
        "Frame_3": (
            {"from": "human", "value": "Describe state of salt"},
            {"from": "gpt", "value": "Salt has landed."},
        ),
    }

    transition_conversation = (
        {
            "from": "human",
            "value": "Describe state change of salt",
        },
        {
            "from": "gpt",
            "value": "Salt transitions from falling to settled.",
        },
    )

    return {
        "before": torch.zeros(3, 224, 224),
        "during": {
            70190: torch.ones(3, 224, 224),
        },
        "after": torch.full((3, 224, 224), 0.5),
        "annotation": object(),
        "frame_indices": {
            "before": 70172,
            "during": [70190],
            "after": 70209,
        },
        "state_descriptions": {
            "Frame_1": "Salt is falling.",
            "Frame_2": "Salt is falling densely.",
            "Frame_3": "Salt has landed.",
        },
        "transition_description": (
            "Salt transitions from falling to settled."
        ),
        "object": "salt",
        "action": "sprinkle salt",
        "frame_conversations": frame_conversations,
        "transition_conversation": transition_conversation,
    }


@pytest.fixture
def tokenizer():
    return FakeTokenizer()


@pytest.fixture
def captioning_collator(tokenizer):
    return CaptioningCollator(tokenizer)


# ---------------------------------------------------------------------
# temporal_collate_fn
# ---------------------------------------------------------------------


def test_collate_returns_expected_keys(sample):
    batch = temporal_collate_fn([sample])

    assert set(batch) == {
        "before",
        "during",
        "after",
        "annotation",
        "frame_indices",
        "state_descriptions",
        "transition_description",
        "object",
        "action",
        "frame_conversations",
        "transition_conversation",
    }


def test_collate_preserves_frame_tensors(sample):
    batch = temporal_collate_fn([sample])

    assert torch.equal(batch["before"][0], sample["before"])
    assert torch.equal(batch["after"][0], sample["after"])

    assert torch.equal(
        batch["during"][0][70190],
        sample["during"][70190],
    )


def test_collate_preserves_variable_length_during_frames(sample):
    second = dict(sample)

    second["during"] = {}

    second["frame_indices"] = {
        "before": 70172,
        "during": [],
        "after": 70209,
    }

    batch = temporal_collate_fn([sample, second])

    assert len(batch["during"]) == 2
    assert 70190 in batch["during"][0]
    assert batch["during"][1] == {}


def test_collate_preserves_annotations(sample):
    batch = temporal_collate_fn([sample])

    assert batch["annotation"][0] is sample["annotation"]


def test_collate_preserves_semantic_descriptions(sample):
    batch = temporal_collate_fn([sample])

    assert (
        batch["state_descriptions"][0]
        == sample["state_descriptions"]
    )

    assert (
        batch["transition_description"][0]
        == sample["transition_description"]
    )


def test_collate_preserves_object_and_action(sample):
    batch = temporal_collate_fn([sample])

    assert batch["object"] == ["salt"]
    assert batch["action"] == ["sprinkle salt"]


def test_collate_preserves_frame_conversations(sample):
    batch = temporal_collate_fn([sample])

    assert (
        batch["frame_conversations"][0]
        == sample["frame_conversations"]
    )

    assert (
        batch["frame_conversations"][0]["Frame_1"][1]["value"]
        == "Salt is falling."
    )


def test_collate_preserves_transition_conversation(sample):
    batch = temporal_collate_fn([sample])

    assert (
        batch["transition_conversation"][0]
        == sample["transition_conversation"]
    )

    assert (
        batch["transition_conversation"][0][1]["value"]
        == "Salt transitions from falling to settled."
    )


def test_collate_supports_multiple_samples(sample):
    second = dict(sample)
    second["object"] = "cabinet"
    second["action"] = "open cabinet"

    batch = temporal_collate_fn([sample, second])

    assert batch["object"] == ["salt", "cabinet"]

    assert batch["action"] == [
        "sprinkle salt",
        "open cabinet",
    ]

    assert len(batch["frame_conversations"]) == 2
    assert len(batch["transition_conversation"]) == 2


def test_collate_rejects_empty_batch():
    with pytest.raises(ValueError, match="empty batch"):
        temporal_collate_fn([])


# ---------------------------------------------------------------------
# CaptioningCollator: initialization
# ---------------------------------------------------------------------


def test_captioning_collator_initialization(tokenizer):
    collator = CaptioningCollator(tokenizer)

    assert collator.tokenizer is tokenizer
    assert collator.max_state_length is None
    assert collator.max_transition_length is None


@pytest.mark.parametrize(
    ("max_state_length", "max_transition_length"),
    [
        (0, None),
        (-1, None),
        (None, 0),
        (None, -1),
    ],
)
def test_captioning_collator_rejects_invalid_lengths(
    tokenizer,
    max_state_length,
    max_transition_length,
):
    with pytest.raises(ValueError, match="must be positive"):
        CaptioningCollator(
            tokenizer,
            max_state_length=max_state_length,
            max_transition_length=max_transition_length,
        )


# ---------------------------------------------------------------------
# CaptioningCollator: raw RGB inputs
# ---------------------------------------------------------------------


def test_captioning_collator_returns_expected_keys(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert set(batch) == {
        "frames",
        "state_labels",
        "state_mask",
        "transition_labels",
        "annotation",
        "frame_indices",
        "state_descriptions",
        "transition_description",
        "object",
        "action",
        "frame_conversations",
        "transition_conversation",
    }


def test_captioning_collator_stacks_raw_frames(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert batch["frames"].shape == (1, 3, 3, 224, 224)

    assert torch.equal(
        batch["frames"][0, 0],
        sample["before"],
    )

    assert torch.equal(
        batch["frames"][0, 1],
        sample["during"][70190],
    )

    assert torch.equal(
        batch["frames"][0, 2],
        sample["after"],
    )


def test_captioning_collator_preserves_temporal_order(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert torch.equal(
        batch["frames"][0, 0],
        torch.zeros(3, 224, 224),
    )

    assert torch.equal(
        batch["frames"][0, 1],
        torch.ones(3, 224, 224),
    )

    assert torch.equal(
        batch["frames"][0, 2],
        torch.full((3, 224, 224), 0.5),
    )


# ---------------------------------------------------------------------
# CaptioningCollator: cached visual features
# ---------------------------------------------------------------------


def test_captioning_collator_supports_cached_features(
    captioning_collator,
    sample,
):
    cached_sample = dict(sample)

    cached_sample["before"] = torch.randn(257, 1024)
    cached_sample["during"] = {
        70190: torch.randn(257, 1024),
    }
    cached_sample["after"] = torch.randn(257, 1024)

    batch = captioning_collator([cached_sample])

    assert batch["frames"].shape == (1, 3, 257, 1024)


def test_captioning_collator_preserves_cached_feature_values(
    captioning_collator,
    sample,
):
    cached_sample = dict(sample)

    before = torch.randn(257, 1024)
    during = torch.randn(257, 1024)
    after = torch.randn(257, 1024)

    cached_sample["before"] = before
    cached_sample["during"] = {70190: during}
    cached_sample["after"] = after

    batch = captioning_collator([cached_sample])

    assert torch.equal(batch["frames"][0, 0], before)
    assert torch.equal(batch["frames"][0, 1], during)
    assert torch.equal(batch["frames"][0, 2], after)


# ---------------------------------------------------------------------
# CaptioningCollator: state caption supervision
# ---------------------------------------------------------------------


def test_captioning_collator_builds_state_labels(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert batch["state_labels"].ndim == 3
    assert batch["state_labels"].shape[:2] == (1, 3)

    assert batch["state_mask"].shape == (1, 3)
    assert batch["state_mask"].all()


def test_captioning_collator_masks_missing_state_descriptions(
    captioning_collator,
    sample,
):
    modified = dict(sample)

    modified["state_descriptions"] = {
        "Frame_1": "Salt is falling.",
        "Frame_2": "",
        "Frame_3": None,
    }

    batch = captioning_collator([modified])

    assert batch["state_mask"].tolist() == [
        [True, False, False]
    ]

    assert torch.all(
        batch["state_labels"][0, 1:] == -100
    )


def test_captioning_collator_handles_all_missing_state_descriptions(
    captioning_collator,
    sample,
):
    modified = dict(sample)

    modified["state_descriptions"] = {
        "Frame_1": "",
        "Frame_2": None,
        "Frame_3": "",
    }

    batch = captioning_collator([modified])

    assert batch["state_mask"].shape == (1, 3)
    assert not batch["state_mask"].any()

    assert batch["state_labels"].shape == (1, 3, 1)
    assert torch.all(batch["state_labels"] == -100)


def test_captioning_collator_handles_missing_state_in_one_sample(
    captioning_collator,
    sample,
):
    second = dict(sample)

    second["state_descriptions"] = {
        "Frame_1": "A cabinet is closed.",
        "Frame_2": None,
        "Frame_3": "The cabinet is open.",
    }

    batch = captioning_collator([sample, second])

    assert batch["state_mask"].shape == (2, 3)

    assert batch["state_mask"][0].all()

    assert batch["state_mask"][1].tolist() == [
        True,
        False,
        True,
    ]

    assert torch.all(
        batch["state_labels"][1, 1] == -100
    )


def test_captioning_collator_rejects_non_string_state_description(
    captioning_collator,
    sample,
):
    modified = dict(sample)

    modified["state_descriptions"] = {
        "Frame_1": 123,
        "Frame_2": "Salt is falling.",
        "Frame_3": "Salt has landed.",
    }

    with pytest.raises(TypeError, match="must be a string"):
        captioning_collator([modified])


# ---------------------------------------------------------------------
# CaptioningCollator: transition supervision
# ---------------------------------------------------------------------


def test_captioning_collator_builds_transition_labels(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert batch["transition_labels"].ndim == 2
    assert batch["transition_labels"].shape[0] == 1

    assert torch.all(
        batch["transition_labels"] != -100
    )


def test_captioning_collator_rejects_empty_transition(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["transition_description"] = ""

    with pytest.raises(
        ValueError,
        match="non-empty transition description",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_non_string_transition(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["transition_description"] = None

    with pytest.raises(TypeError):
        captioning_collator([modified])


# ---------------------------------------------------------------------
# CaptioningCollator: padding and truncation
# ---------------------------------------------------------------------


def test_captioning_collator_masks_padding_tokens(
    captioning_collator,
    sample,
):
    second = dict(sample)

    second["state_descriptions"] = {
        "Frame_1": "Salt falls.",
        "Frame_2": "Salt falls.",
        "Frame_3": "Salt falls.",
    }

    batch = captioning_collator([sample, second])

    assert torch.any(
        batch["state_labels"] == -100
    )


def test_captioning_collator_respects_max_state_length(
    tokenizer,
    sample,
):
    collator = CaptioningCollator(
        tokenizer,
        max_state_length=2,
    )

    batch = collator([sample])

    assert batch["state_labels"].shape[-1] == 2


def test_captioning_collator_respects_max_transition_length(
    tokenizer,
    sample,
):
    collator = CaptioningCollator(
        tokenizer,
        max_transition_length=3,
    )

    batch = collator([sample])

    assert batch["transition_labels"].shape[-1] == 3


# ---------------------------------------------------------------------
# CaptioningCollator: validation
# ---------------------------------------------------------------------


def test_captioning_collator_rejects_empty_batch(
    captioning_collator,
):
    with pytest.raises(ValueError, match="empty batch"):
        captioning_collator([])


def test_captioning_collator_rejects_missing_during_frame(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["during"] = {}

    with pytest.raises(
        ValueError,
        match="exactly one during-frame",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_multiple_during_frames(
    captioning_collator,
    sample,
):
    modified = dict(sample)

    modified["during"] = {
        70190: torch.ones(3, 224, 224),
        70195: torch.ones(3, 224, 224),
    }

    with pytest.raises(
        ValueError,
        match="exactly one during-frame",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_invalid_frame_rank(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["before"] = torch.randn(3, 224)

    with pytest.raises(
        ValueError,
        match="feature shape",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_integer_frame_tensor(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["before"] = torch.ones(
        3,
        224,
        224,
        dtype=torch.long,
    )

    with pytest.raises(
        TypeError,
        match="floating-point dtype",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_non_finite_frame(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["before"] = torch.full(
        (3, 224, 224),
        float("nan"),
    )

    with pytest.raises(
        ValueError,
        match="non-finite",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_mismatched_frame_shapes(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    modified["after"] = torch.randn(3, 256, 256)

    with pytest.raises(
        ValueError,
        match="matching shapes",
    ):
        captioning_collator([modified])


def test_captioning_collator_rejects_mismatched_batch_shapes(
    captioning_collator,
    sample,
):
    second = dict(sample)

    second["before"] = torch.randn(3, 256, 256)
    second["during"] = {
        70190: torch.randn(3, 256, 256),
    }
    second["after"] = torch.randn(3, 256, 256)

    with pytest.raises(
        ValueError,
        match="identical visual input shapes",
    ):
        captioning_collator([sample, second])


# ---------------------------------------------------------------------
# CaptioningCollator: metadata and multiple samples
# ---------------------------------------------------------------------


def test_captioning_collator_preserves_metadata(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert batch["annotation"][0] is sample["annotation"]

    assert batch["frame_indices"][0] == sample["frame_indices"]

    assert (
        batch["state_descriptions"][0]
        == sample["state_descriptions"]
    )

    assert (
        batch["transition_description"][0]
        == sample["transition_description"]
    )

    assert batch["object"] == ["salt"]
    assert batch["action"] == ["sprinkle salt"]

    assert (
        batch["frame_conversations"][0]
        == sample["frame_conversations"]
    )

    assert (
        batch["transition_conversation"][0]
        == sample["transition_conversation"]
    )


def test_captioning_collator_supports_multiple_samples(
    captioning_collator,
    sample,
):
    second = dict(sample)

    second["object"] = "cabinet"
    second["action"] = "open cabinet"

    second["before"] = torch.full(
        (3, 224, 224),
        0.2,
    )

    batch = captioning_collator([sample, second])

    assert batch["frames"].shape == (2, 3, 3, 224, 224)

    assert batch["state_labels"].shape[:2] == (2, 3)

    assert batch["state_mask"].shape == (2, 3)

    assert batch["transition_labels"].shape[0] == 2

    assert batch["object"] == ["salt", "cabinet"]

    assert batch["action"] == [
        "sprinkle salt",
        "open cabinet",
    ]


def test_captioning_collator_preserves_state_mask_order(
    captioning_collator,
    sample,
):
    batch = captioning_collator([sample])

    assert batch["state_mask"].tolist() == [
        [True, True, True]
    ]


def test_captioning_collator_rejects_missing_metadata(
    captioning_collator,
    sample,
):
    modified = dict(sample)
    del modified["object"]

    with pytest.raises(KeyError, match="object"):
        captioning_collator([modified])





def test_captioning_collator_accepts_mapping_tokenizer_output(sample):
    """Accept mapping-like outputs, including Hugging Face BatchEncoding."""

    class MappingTokenizer(FakeTokenizer):
        def __call__(self, *args, **kwargs):
            return UserDict(super().__call__(*args, **kwargs))

    collator = CaptioningCollator(MappingTokenizer())
    batch = collator([sample])

    assert batch["state_labels"].shape[:2] == (1, 3)
    assert batch["transition_labels"].shape[0] == 1


def test_captioning_collator_accepts_plain_dict_tokenizer_output(sample):
    collator = CaptioningCollator(FakeTokenizer())
    batch = collator([sample])

    assert batch["state_labels"].shape[:2] == (1, 3)
    assert batch["transition_labels"].shape[0] == 1


def test_captioning_collator_rejects_tokenizer_output_without_input_ids(sample):
    class InvalidTokenizer:
        pad_token_id = 0

        def __call__(self, *args, **kwargs):
            return UserDict({"attention_mask": torch.ones(1, 2)})

    collator = CaptioningCollator(InvalidTokenizer())

    with pytest.raises(KeyError, match="mapping containing 'input_ids'"):
        collator([sample])


def test_captioning_collator_rejects_non_mapping_tokenizer_output(sample):
    class InvalidTokenizer:
        pad_token_id = 0

        def __call__(self, *args, **kwargs):
            return None

    collator = CaptioningCollator(InvalidTokenizer())

    with pytest.raises(TypeError, match="mapping containing 'input_ids'"):
        collator([sample])


def test_captioning_collator_rejects_non_2d_tokenizer_input_ids(sample):
    class InvalidShapeTokenizer:
        pad_token_id = 0

        def __call__(self, texts, **kwargs):
            return UserDict({
                "input_ids": torch.ones(len(texts), dtype=torch.long)
            })

    collator = CaptioningCollator(InvalidShapeTokenizer())

    with pytest.raises(ValueError, match="batch, sequence"):
        collator([sample])


def test_captioning_collator_rejects_wrong_tokenizer_batch_size(sample):
    class InvalidBatchTokenizer:
        pad_token_id = 0

        def __call__(self, texts, **kwargs):
            return UserDict({
                "input_ids": torch.ones(1, 2, dtype=torch.long)
            })

    collator = CaptioningCollator(InvalidBatchTokenizer())

    with pytest.raises(ValueError, match="unexpected batch size"):
        collator([sample, dict(sample)])
