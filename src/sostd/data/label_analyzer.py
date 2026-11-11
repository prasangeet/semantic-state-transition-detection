
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from src.sostd.data.annotation_parser import OSCaRClipAnnotation


@dataclass(slots=True)
class AnnotationLabelStatistics:
    total_annotations: int

    object_names: Counter[str]
    action_narrations: Counter[str]
    action_terms: Counter[str]
    action_combinations: Counter[tuple[str, ...]]

    state_descriptions: Counter[str]
    transition_descriptions: Counter[str]


class AnnotationLabelAnalyzer:
    """Analyze semantic annotations in OSCaR clip annotations."""

    @staticmethod
    def analyze(
        annotations: list[OSCaRClipAnnotation],
    ) -> AnnotationLabelStatistics:

        object_names: Counter[str] = Counter()
        action_narrations: Counter[str] = Counter()
        action_terms: Counter[str] = Counter()
        action_combinations: Counter[tuple[str, ...]] = Counter()

        state_descriptions: Counter[str] = Counter()
        transition_descriptions: Counter[str] = Counter()

        for annotation in annotations:
            object_name = annotation.object_name

            if object_name and object_name.strip():
                object_names[object_name] += 1

            action = annotation.action_narration

            if action and action.strip():
                action_narrations[action] += 1

                terms = tuple(action.split())

                if terms:
                    action_terms.update(terms)
                    action_combinations[terms] += 1

            for description in annotation.state_descriptions.values():
                if description and description.strip():
                    state_descriptions[description] += 1

            transition = annotation.transition_description

            if transition and transition.strip():
                transition_descriptions[transition] += 1

        return AnnotationLabelStatistics(
            total_annotations=len(annotations),
            object_names=object_names,
            action_narrations=action_narrations,
            action_terms=action_terms,
            action_combinations=action_combinations,
            state_descriptions=state_descriptions,
            transition_descriptions=transition_descriptions,
        )

    @staticmethod
    def display(statistics: AnnotationLabelStatistics) -> None:
        """Print a readable semantic annotation report."""

        print("\nOSCaR SEMANTIC ANNOTATION ANALYSIS")
        print("=" * 65)

        print(f"Total clip annotations: {statistics.total_annotations}")

        sections = [
            ("Object names", statistics.object_names),
            ("Action narrations", statistics.action_narrations),
            ("Action terms", statistics.action_terms),
            ("Action combinations", statistics.action_combinations),
            ("Frame-state descriptions", statistics.state_descriptions),
            ("Transition descriptions", statistics.transition_descriptions),
        ]

        for title, counter in sections:
            print(f"\n{title}")
            print("-" * 65)

            if not counter:
                print("No annotations found.")
                continue

            for label, count in counter.most_common():
                print(f"{str(label):50} {count:>5}")
