
#!/usr/bin/env python3

"""
Download the complete OSCaR dataset from Hugging Face.

Repository:
    ali-vosoughi/oscar-dataset

Destination:
    data/OSCaR/

Features:
    - Loads HF_TOKEN from the project-root .env file.
    - Supports existing Hugging Face authentication.
    - Downloads the complete dataset without file filtering.
    - Uses a local destination.
    - Uses multiple download workers.
    - Preserves downloaded files when interrupted.
    - Supports resuming incomplete downloads.
    - Provides useful error messages.

IMPORTANT:
    You must accept the OSCaR dataset access conditions
    on Hugging Face before downloading.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import snapshot_download


# ============================================================
# Project configuration
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

ENV_FILE = PROJECT_ROOT / ".env"

DATASET_ID = "ali-vosoughi/oscar-dataset"

DESTINATION = PROJECT_ROOT / "data" / "OSCaR"


# ============================================================
# Environment configuration
# ============================================================

def load_configuration() -> tuple[str | None, int]:

    # Load environment variables from the project root.
    # Existing shell environment variables take priority.
    load_dotenv(
        dotenv_path=ENV_FILE,
        override=False,
    )

    token = os.getenv("HF_TOKEN", "").strip() or None

    try:
        max_workers = int(
            os.getenv("HF_MAX_WORKERS", "4")
        )
    except ValueError:
        raise ValueError(
            "HF_MAX_WORKERS must be a valid integer."
        )

    if max_workers < 1:
        raise ValueError(
            "HF_MAX_WORKERS must be greater than zero."
        )

    return token, max_workers


# ============================================================
# Dataset download
# ============================================================

def download_dataset(
    token: str | None,
    max_workers: int,
) -> Path:

    print("=" * 65)
    print("OSCaR DATASET DOWNLOADER")
    print("=" * 65)

    print(f"Repository : {DATASET_ID}")
    print(f"Destination: {DESTINATION}")
    print(f"Workers    : {max_workers}")
    print(
        "Authentication: "
        + ("HF token configured" if token else "Using Hugging Face authentication")
    )

    print("=" * 65)

    # Create the destination directory.
    DESTINATION.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("\nStarting OSCaR dataset download...\n")

    # Download the complete dataset repository.
    #
    # No allow_patterns or ignore_patterns are used.
    #
    # Existing files are reused where possible.
    # Hugging Face maintains local download metadata
    # inside the destination directory.
    #
    # Authentication uses HF_TOKEN from .env when
    # available, otherwise the locally cached HF login.

    downloaded_path = snapshot_download(
        repo_id=DATASET_ID,
        repo_type="dataset",
        local_dir=str(DESTINATION),
        token=token,
        max_workers=max_workers,
    )

    return Path(downloaded_path)


# ============================================================
# Main
# ============================================================

def main() -> int:

    try:
        token, max_workers = load_configuration()

        downloaded_path = download_dataset(
            token=token,
            max_workers=max_workers,
        )

        print("\n" + "=" * 65)
        print("DOWNLOAD COMPLETED")
        print("=" * 65)

        print(f"\nDataset location:\n{downloaded_path}")

        print("\nDownloaded top-level entries:")

        for entry in sorted(downloaded_path.iterdir()):
            if entry.name == ".cache":
                continue

            entry_type = "DIR " if entry.is_dir() else "FILE"
            print(f"  [{entry_type}] {entry.name}")

        print("\nOSCaR dataset download completed successfully.")

        return 0

    except KeyboardInterrupt:
        print(
            "\n\nDownload interrupted by user.",
            file=sys.stderr,
        )

        print(
            "Run the same command again to continue "
            "without deleting the existing dataset.",
            file=sys.stderr,
        )

        return 130

    except Exception as error:
        print(
            f"\nDownload failed: {type(error).__name__}: {error}",
            file=sys.stderr,
        )

        print(
            "\nThe existing dataset directory has not been deleted.",
            file=sys.stderr,
        )

        print(
            "Check your Hugging Face authentication and confirm "
            "that you have accepted the OSCaR dataset conditions.",
            file=sys.stderr,
        )

        print(
            "Resolve the reported problem and rerun the downloader.",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
