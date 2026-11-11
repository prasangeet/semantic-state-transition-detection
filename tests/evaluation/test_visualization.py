import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest
from matplotlib.figure import Figure

from src.sostd.evaluation.reporting.visualization import EvaluationVisualizer


@pytest.fixture
def visualizer():
    return EvaluationVisualizer()


@pytest.fixture
def evaluation():
    return {
        "stages": {
            stage: {
                "semantic": {"mean_similarity": 0.8},
                "caption": {"rouge_l": 0.7},
            }
            for stage in ("before", "during", "after", "transition")
        },
        "temporal": {
            "stage_scores": {
                "before": 0.9,
                "during": 0.8,
                "after": 0.85,
                "transition": 0.75,
            }
        },
    }


def test_plot_stage_metrics_returns_figure(visualizer, evaluation):
    figure = visualizer.plot_stage_metrics(evaluation)

    assert isinstance(figure, Figure)
    assert len(figure.axes) == 1
    assert len(figure.axes[0].patches) == 8

    plt.close(figure)


def test_plot_temporal_alignment_returns_figure(visualizer, evaluation):
    figure = visualizer.plot_temporal_alignment(evaluation)

    assert isinstance(figure, Figure)
    assert len(figure.axes) == 1
    assert len(figure.axes[0].patches) == 4

    plt.close(figure)


def test_stage_plot_contains_expected_labels(visualizer, evaluation):
    figure = visualizer.plot_stage_metrics(evaluation)
    axis = figure.axes[0]

    assert axis.get_title() == "Caption Quality Across Temporal Stages"
    assert [label.get_text() for label in axis.get_xticklabels()] == [
        "Before",
        "During",
        "After",
        "Transition",
    ]

    plt.close(figure)


def test_temporal_plot_contains_expected_labels(visualizer, evaluation):
    figure = visualizer.plot_temporal_alignment(evaluation)
    axis = figure.axes[0]

    assert axis.get_title() == "Temporal Stage Alignment"
    assert len(axis.texts) == 4

    plt.close(figure)


def test_save_creates_output_file(visualizer, evaluation, tmp_path):
    figure = visualizer.plot_temporal_alignment(evaluation)
    output = tmp_path / "charts" / "temporal.png"

    path = visualizer.save(figure, output)

    assert path == output
    assert path.exists()
    assert path.stat().st_size > 0

    plt.close(figure)


def test_save_rejects_invalid_figure(visualizer, tmp_path):
    with pytest.raises(TypeError, match="Matplotlib Figure"):
        visualizer.save("not a figure", tmp_path / "invalid.png")


def test_save_rejects_non_positive_dpi(visualizer, evaluation, tmp_path):
    figure = visualizer.plot_temporal_alignment(evaluation)

    with pytest.raises(ValueError, match="dpi must be positive"):
        visualizer.save(figure, tmp_path / "chart.png", dpi=0)

    plt.close(figure)


def test_rejects_missing_stage(visualizer, evaluation):
    del evaluation["stages"]["during"]

    with pytest.raises(ValueError, match="during"):
        visualizer.plot_stage_metrics(evaluation)


def test_rejects_missing_temporal_stage(visualizer, evaluation):
    del evaluation["temporal"]["stage_scores"]["after"]

    with pytest.raises(ValueError, match="after"):
        visualizer.plot_temporal_alignment(evaluation)


def test_rejects_non_dictionary_input(visualizer):
    with pytest.raises(TypeError, match="dictionary"):
        visualizer.plot_stage_metrics([])