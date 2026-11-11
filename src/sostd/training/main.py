
from __future__ import annotations

from src.sostd.data.build_dataset import build_temporal_dataset
from src.sostd.data.label_analyzer import AnnotationLabelAnalyzer


def main() -> None:
    """Inspect the OSCaR temporal dataset."""

    print("=" * 65)
    print("Semantic Object State Transition Detection")
    print("OSCaR Dataset Pipeline")
    print("=" * 65)

    # 1. Build temporal dataset from OSCaR validation annotations.
    dataset, build_result = build_temporal_dataset(
        split="validation",
    )

    annotations = [
        sample.annotation
        for sample in build_result.samples
    ]

    print("\nDataset Construction Completed")
    print("-" * 65)
    print(f"Clips encountered: {build_result.clips_seen}")
    print(f"Temporal samples built: {build_result.clips_built}")
    print(f"Dataset length: {len(dataset)}")

    # 2. Display a sample annotation.
    if annotations:
        sample = build_result.samples[0]
        annotation = sample.annotation

        print("\nSample OSCaR Annotation")
        print("-" * 65)
        print(f"Clip ID: {annotation.clip_id}")
        print(f"Object: {annotation.object_name}")
        print(f"Action: {annotation.action_narration}")

        print("\nTemporal Frames")
        print(f"Before: {sample.before_frame_idx}")
        print(f"During: {list(sample.during_frames.keys())}")
        print(f"After: {sample.after_frame_idx}")

        print("\nFrame Descriptions")

        for frame, description in annotation.state_descriptions.items():
            print(f"{frame}: {description}")

        print("\nTransition Description")
        print(annotation.transition_description)

    # 3. Analyze semantic annotations.
    statistics = AnnotationLabelAnalyzer.analyze(annotations)
    AnnotationLabelAnalyzer.display(statistics)

    print("\nDataset inspection completed.")
    print(
        "Note: OSCaR temporal training data construction is "
        "not yet implemented."
    )


if __name__ == "__main__":
    main()
