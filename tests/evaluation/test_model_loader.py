
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
import torch

from src.sostd.evaluation.model_loader import ModelLoader


@pytest.fixture
def checkpoint_file(tmp_path):
    path = tmp_path / "best.pt"
    path.touch()
    return path


@pytest.fixture
def state_dict():
    return {
        "weight": torch.tensor([1.0, 2.0]),
        "bias": torch.tensor([0.5]),
    }


def test_missing_checkpoint(tmp_path):
    loader = ModelLoader(
        checkpoint=tmp_path / "missing.pt",
        device="cpu",
    )

    with pytest.raises(FileNotFoundError):
        loader.load()


def test_checkpoint_must_be_dictionary(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    with patch.object(
        loader,
        "_load_checkpoint",
        return_value=[],
    ):
        with pytest.raises(TypeError, match="dictionary"):
            loader.load()


def test_extract_state_dict_from_model_state_dict(
    checkpoint_file,
    state_dict,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    extracted = loader._extract_state_dict(
        {"model_state_dict": state_dict}
    )

    assert extracted.keys() == state_dict.keys()


@pytest.mark.parametrize(
    "key",
    ["state_dict", "model"],
)
def test_extract_supported_checkpoint_keys(
    checkpoint_file,
    state_dict,
    key,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    extracted = loader._extract_state_dict(
        {key: state_dict}
    )

    assert extracted.keys() == state_dict.keys()


def test_extract_raw_state_dict(
    checkpoint_file,
    state_dict,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    extracted = loader._extract_state_dict(state_dict)

    assert extracted.keys() == state_dict.keys()


def test_extract_state_dict_removes_module_prefix(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    extracted = loader._extract_state_dict(
        {
            "state_dict": {
                "module.weight": torch.tensor([1.0]),
            }
        }
    )

    assert "weight" in extracted
    assert "module.weight" not in extracted


def test_missing_state_dict_raises_error(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    with pytest.raises(KeyError, match="model weights"):
        loader._extract_state_dict(
            {"epoch": 25, "optimizer_state_dict": {}}
        )


def test_empty_state_dict_raises_error(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    with pytest.raises(ValueError, match="empty"):
        loader._extract_state_dict(
            {"state_dict": {}}
        )


def test_non_tensor_state_dict_raises_error(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    with pytest.raises(TypeError, match="non-tensor"):
        loader._extract_state_dict(
            {"state_dict": {"weight": "invalid"}}
        )


def test_load_model(
    checkpoint_file,
    state_dict,
):
    loader = ModelLoader(checkpoint_file, device="cpu")

    mock_model = MagicMock()
    mock_model.load_state_dict.return_value = None

    with (
        patch.object(
            loader,
            "_load_checkpoint",
            return_value={"model_state_dict": state_dict},
        ),
        patch(
            "src.sostd.evaluation.model_loader.OSCaRLite",
            return_value=mock_model,
        ),
    ):
        model = loader.load()

    assert model is mock_model
    mock_model.load_state_dict.assert_called_once_with(
        state_dict,
        strict=True,
    )
    mock_model.to.assert_called_once_with(torch.device("cpu"))
    mock_model.eval.assert_called_once()


def test_cuda_unavailable(
    checkpoint_file,
):
    loader = ModelLoader(checkpoint_file, device="cuda")

    with patch(
        "src.sostd.evaluation.model_loader.torch.cuda.is_available",
        return_value=False,
    ):
        with pytest.raises(RuntimeError, match="CUDA"):
            loader.load()
