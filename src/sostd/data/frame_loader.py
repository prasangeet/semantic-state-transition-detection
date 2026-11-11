
from __future__ import annotations

from pathlib import Path, PurePosixPath

from PIL import Image


class RGBFrameLoader:
    """Lazily loads RGB frames from the local OSCaR dataset."""

    REPOSITORY_ID = "ali-vosoughi/oscar-dataset"
    DATA_DIRECTORY = "data"

    def __init__(
        self,
        token: str | None = None,
        revision: str = "main",
        dataset_root: str | Path | None = None,
    ) -> None:
        # Retained for compatibility with existing callers.
        self.token = token
        self.revision = revision

        project_root = Path(__file__).resolve().parents[3]

        self.dataset_root = (
            Path(dataset_root).expanduser().resolve()
            if dataset_root is not None
            else project_root / "data" / "OSCaR"
        )

        self.image_root = (
            self.dataset_root / "data" / "object-state-data"
        ).resolve()

    def _resolve_repository_path(self, repository_path: str) -> Path:
        """Resolve a manifest image path inside the local image directory."""

        if not isinstance(repository_path, str) or not repository_path:
            raise ValueError(
                f"Invalid repository image path: {repository_path!r}"
            )

        path = PurePosixPath(repository_path)

        if (
            path.is_absolute()
            or "\\" in repository_path
            or ".." in path.parts
            or not path.parts
        ):
            raise ValueError(
                f"Invalid repository image path: {repository_path!r}"
            )

        parts = path.parts

        # Accept both:
        # object-state-data/clip/frame.jpg
        # data/object-state-data/clip/frame.jpg
        if parts[0] == self.DATA_DIRECTORY:
            parts = parts[1:]

        if not parts or parts[0] != "object-state-data":
            raise ValueError(
                f"Invalid repository image path: {repository_path!r}"
            )

        local_path = (self.image_root / Path(*parts[1:])).resolve()

        if not local_path.is_relative_to(self.image_root):
            raise ValueError(
                f"Invalid repository image path: {repository_path!r}"
            )

        return local_path

    def load(self, repository_path: str) -> Image.Image:
        """Load a local OSCaR image and return it as RGB."""

        local_path = self._resolve_repository_path(repository_path)

        if not local_path.is_file():
            raise FileNotFoundError(
                f"Local OSCaR image not found: {local_path}"
            )

        with Image.open(local_path) as image:
            return image.convert("RGB")

    def load_many(
        self,
        repository_paths: list[str],
    ) -> list[Image.Image]:
        """Load multiple local images while preserving their order."""

        return [
            self.load(repository_path)
            for repository_path in repository_paths
        ]
