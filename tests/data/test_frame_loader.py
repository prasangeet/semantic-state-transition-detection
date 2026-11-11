
from pathlib import Path

import pytest
from PIL import Image

from src.sostd.data.frame_loader import RGBFrameLoader


@pytest.fixture
def dataset_root(tmp_path: Path) -> Path:
    return tmp_path / "OSCaR"


@pytest.fixture
def frame_loader(dataset_root: Path) -> RGBFrameLoader:
    return RGBFrameLoader(dataset_root=dataset_root)


@pytest.fixture
def create_image(dataset_root: Path):
    def _create(
        relative_path: str,
        size: tuple[int, int] = (32, 32),
        mode: str = "RGB",
    ) -> Path:
        path = dataset_root / "data" / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new(mode, size).save(path)
        return path

    return _create


def test_repository_id(frame_loader):
    assert frame_loader.REPOSITORY_ID == "ali-vosoughi/oscar-dataset"


def test_initialization(frame_loader):
    assert frame_loader.token is None
    assert frame_loader.revision == "main"


def test_resolves_default_local_dataset_root():
    expected = Path(__file__).resolve().parents[2] / "data" / "OSCaR"

    loader = RGBFrameLoader()

    assert loader.dataset_root == expected.resolve()


def test_load_local_image(frame_loader, create_image):
    create_image(
        "object-state-data/P01_05_110/frame_23923.jpg"
    )

    image = frame_loader.load(
        "object-state-data/P01_05_110/frame_23923.jpg"
    )

    assert isinstance(image, Image.Image)
    assert image.mode == "RGB"
    assert image.size == (32, 32)


def test_load_accepts_data_prefixed_path(frame_loader, create_image):
    create_image(
        "object-state-data/P01_05_110/frame_23923.jpg"
    )

    image = frame_loader.load(
        "data/object-state-data/P01_05_110/frame_23923.jpg"
    )

    assert image.mode == "RGB"
    assert image.size == (32, 32)


def test_load_converts_image_to_rgb(frame_loader, create_image):
    create_image(
        "object-state-data/P01_05_110/frame_gray.jpg",
        mode="L",
    )

    image = frame_loader.load(
        "object-state-data/P01_05_110/frame_gray.jpg"
    )

    assert image.mode == "RGB"


@pytest.mark.parametrize(
    "path",
    [
        "",
        "/etc/passwd",
        "../frame.jpg",
        "object-state-data/../../frame.jpg",
        "other-directory/frame.jpg",
        "data/other-directory/frame.jpg",
        "object-state-data\\P01_05_110\\frame.jpg",
    ],
)
def test_load_rejects_invalid_paths(frame_loader, path):
    with pytest.raises(ValueError, match="Invalid repository"):
        frame_loader.load(path)


def test_load_raises_for_missing_image(frame_loader):
    with pytest.raises(FileNotFoundError, match="Local OSCaR image not found"):
        frame_loader.load(
            "object-state-data/P01_05_110/missing.jpg"
        )


def test_load_many_preserves_order(frame_loader, create_image):
    paths = [
        "object-state-data/P01_05_110/frame_23923.jpg",
        "object-state-data/P01_05_110/frame_23949.jpg",
        "object-state-data/P01_05_110/frame_23976.jpg",
    ]

    for path in paths:
        create_image(path)

    images = frame_loader.load_many(paths)

    assert len(images) == 3
    assert all(image.mode == "RGB" for image in images)
    assert all(image.size == (32, 32) for image in images)


def test_load_many_empty_list(frame_loader):
    assert frame_loader.load_many([]) == []
