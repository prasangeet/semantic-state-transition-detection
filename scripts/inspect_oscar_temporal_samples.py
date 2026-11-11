
from __future__ import annotations

from src.sostd.data.load_dataset import DatasetLoader


def main():
    loader = DatasetLoader(streaming=True)
    dataset = loader.load()

    target_clip = "P01_05_110"

    print(f"\nInspecting OSCaR clip: {target_clip}")
    print("=" * 80)

    matching_records = []

    for record in dataset["validation"]:
        image_path = record.get("image_path", "")

        if f"/{target_clip}/" in image_path:
            matching_records.append(record)

    print(f"\nTotal records found: {len(matching_records)}")

    for index, record in enumerate(matching_records, start=1):
        print(f"\n--- Record {index} ---")

        print(f"Image       : {record.get('image_path')}")
        print(f"Caption key : {record.get('caption_key')}")
        print(f"Caption path: {record.get('caption_path')}")
        print(f"QA path     : {record.get('qa_path')}")
        print(f"Object      : {record.get('object')}")
        print(f"Action      : {record.get('action_narration')}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
