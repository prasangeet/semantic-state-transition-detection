
"""Generate a representative interactive HTML visual comparison report."""

from __future__ import annotations

import html
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any


class VisualComparisonReportGenerator:
    """Create a compact side-by-side image and caption comparison report."""

    STAGES = ("before", "during", "after", "transition")
    IMAGE_STAGES = ("before", "during", "after")
    DEFAULT_MAX_SAMPLES = 24
    IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

    def __init__(
        self,
        max_samples: int = DEFAULT_MAX_SAMPLES,
        image_root: str | Path = "data/OSCaR/data",
    ) -> None:
        if max_samples <= 0:
            raise ValueError("max_samples must be positive.")

        self.max_samples = max_samples
        self.image_root = Path(image_root).expanduser()

    def generate(
        self,
        predictions: list[dict[str, str]],
        references: list[dict[str, str]],
        metadata: list[dict[str, Any]],
        output_dir: str | Path,
    ) -> Path:
        """Generate the HTML report and return its path."""

        if not (
            len(predictions) == len(references) == len(metadata)
        ):
            raise ValueError(
                "Predictions, references and metadata must have "
                "the same number of samples."
            )

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        assets_dir = output_dir / "visual_comparison_assets"
        assets_dir.mkdir(parents=True, exist_ok=True)

        selected_indices = self._select_representative_samples(
            metadata,
            self.max_samples,
        )

        cards = []

        for index in selected_indices:
            prediction = predictions[index]
            reference = references[index]
            sample_metadata = metadata[index]

            images_html = self._render_images(
                index,
                sample_metadata.get("image_paths", {}),
                assets_dir,
            )

            captions_html = self._render_captions(
                prediction,
                reference,
            )

            object_name = html.escape(
                str(sample_metadata.get("object", "Unknown"))
            )
            action = html.escape(
                str(sample_metadata.get("action", "Unknown"))
            )

            cards.append(
                f"""
                <article class="sample-card"
                         data-object="{object_name.lower()}"
                         data-action="{action.lower()}">

                    <div class="sample-header">
                        <div>
                            <h2>Sample {index + 1:03d}</h2>
                            <p class="metadata">
                                Object: {object_name}
                                &nbsp;·&nbsp;
                                Action: {action}
                            </p>
                        </div>
                    </div>

                    {images_html}

                    {captions_html}
                </article>
                """
            )

        document = self._build_document(
            cards=cards,
            total_samples=len(predictions),
            displayed_samples=len(selected_indices),
        )

        report_path = output_dir / "visual_comparison.html"
        report_path.write_text(document, encoding="utf-8")

        return report_path

    @staticmethod
    def _select_representative_samples(
        metadata: list[dict[str, Any]],
        max_samples: int,
    ) -> list[int]:
        """Select diverse examples deterministically.

        First select one sample for each distinct object/action pair,
        preserving dataset order. If more examples are needed, fill
        the remaining slots with evenly distributed samples.
        """

        total = len(metadata)
        limit = min(total, max_samples)

        if limit == total:
            return list(range(total))

        selected = []
        seen_pairs = set()

        for index, sample in enumerate(metadata):
            object_name = str(sample.get("object", "Unknown")).lower()
            action = str(sample.get("action", "Unknown")).lower()

            pair = (object_name, action)

            if pair not in seen_pairs:
                selected.append(index)
                seen_pairs.add(pair)

                if len(selected) == limit:
                    return selected

        selected_set = set(selected)
        remaining = [
            index
            for index in range(total)
            if index not in selected_set
        ]

        slots = limit - len(selected)

        if slots > 0 and remaining:
            if slots >= len(remaining):
                selected.extend(remaining)
            else:
                step = len(remaining) / slots

                for position in range(slots):
                    candidate = remaining[int(position * step)]
                    selected.append(candidate)

        return sorted(selected)

    def _resolve_image_path(
        self,
        source: str | Path | None,
    ) -> Path | None:
        """Resolve an image path against the OSCaR image directory."""

        if not source:
            return None

        source_path = Path(source).expanduser()

        if source_path.is_absolute():
            candidates = [source_path]
        else:
            candidates = [
                source_path,
                Path.cwd() / source_path,
                self.image_root / source_path,
            ]

        for candidate in candidates:
            if candidate.is_file():
                return candidate.resolve()

        return None

    def _copy_image(
        self,
        source: str | Path | None,
        sample_index: int,
        stage: str,
        assets_dir: Path,
    ) -> str | None:
        """Copy a source image into the report assets directory."""

        source_path = self._resolve_image_path(source)

        if source_path is None:
            return None

        suffix = source_path.suffix.lower()

        if suffix not in self.IMAGE_EXTENSIONS:
            return None

        filename = (
            f"sample_{sample_index + 1:04d}_{stage}{suffix}"
        )

        destination = assets_dir / filename

        shutil.copy2(source_path, destination)

        return f"visual_comparison_assets/{filename}"

    def _render_images(
        self,
        sample_index: int,
        image_paths: dict[str, Any],
        assets_dir: Path,
    ) -> str:
        """Render the before, during and after source images."""

        image_sections = []

        for stage in self.IMAGE_STAGES:
            image_path = self._copy_image(
                image_paths.get(stage),
                sample_index,
                stage,
                assets_dir,
            )

            if image_path:
                image_content = (
                    f'<img src="{html.escape(image_path, quote=True)}" '
                    f'alt="{stage.title()} frame" loading="lazy">'
                )
            else:
                image_content = (
                    '<div class="image-missing">'
                    'Image unavailable'
                    '</div>'
                )

            image_sections.append(
                f"""
                <div class="frame">
                    {image_content}
                    <div class="frame-label">{stage.title()}</div>
                </div>
                """
            )

        return (
            '<div class="image-grid">'
            + "".join(image_sections)
            + "</div>"
        )

    def _render_captions(
        self,
        prediction: dict[str, str],
        reference: dict[str, str],
    ) -> str:
        """Render predicted and reference captions side by side."""

        sections = []

        for stage in self.STAGES:
            predicted_text = html.escape(
                str(prediction.get(stage, "Not available"))
            )

            reference_text = html.escape(
                str(reference.get(stage, "Not available"))
            )

            sections.append(
                f"""
                <div class="caption-stage">
                    <h3>{stage.title()}</h3>

                    <div class="caption-comparison">
                        <div class="caption prediction">
                            <span class="caption-label">
                                Prediction
                            </span>
                            <p>{predicted_text}</p>
                        </div>

                        <div class="caption reference">
                            <span class="caption-label">
                                Reference
                            </span>
                            <p>{reference_text}</p>
                        </div>
                    </div>
                </div>
                """
            )

        return (
            '<div class="caption-section">'
            '<h3 class="section-title">Caption comparison</h3>'
            + "".join(sections)
            + "</div>"
        )

    @staticmethod
    def _build_document(
        cards: list[str],
        total_samples: int,
        displayed_samples: int,
    ) -> str:
        """Build the complete HTML document."""

        cards_html = "\n".join(cards)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OSCaR-Lite Visual Comparison</title>

<style>
:root {{
    color-scheme: light;
    --background: #f4f6f9;
    --surface: #ffffff;
    --text: #202938;
    --muted: #687386;
    --border: #e1e6ed;
}}

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    background: var(--background);
    color: var(--text);
    font-family: Inter, system-ui, sans-serif;
    line-height: 1.55;
}}

.container {{
    max-width: 1200px;
    margin: auto;
    padding: 32px 20px;
}}

.page-header {{
    margin-bottom: 28px;
}}

.page-header h1 {{
    margin: 0;
    font-size: 30px;
}}

.subtitle {{
    color: var(--muted);
    margin-top: 6px;
}}

.report-stats {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 16px;
}}

.stat {{
    background: white;
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 12px 16px;
}}

.stat strong {{
    display: block;
    font-size: 20px;
}}

.stat span {{
    color: var(--muted);
    font-size: 12px;
}}

.toolbar {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin: 22px 0;
}}

.toolbar input {{
    flex: 1;
    min-width: 220px;
    padding: 12px 14px;
    border: 1px solid var(--border);
    border-radius: 9px;
    font-size: 14px;
}}

.counter {{
    color: var(--muted);
    font-size: 14px;
    align-self: center;
}}

.sample-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 3px 12px rgba(20, 30, 50, 0.04);
}}

.sample-header {{
    margin-bottom: 18px;
}}

.sample-header h2 {{
    margin: 0;
    font-size: 20px;
}}

.metadata {{
    color: var(--muted);
    font-size: 13px;
    margin: 4px 0 0;
}}

.image-grid {{
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
}}

.frame {{
    min-width: 0;
}}

.frame img {{
    display: block;
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: contain;
    background: #eef1f5;
    border-radius: 9px;
    border: 1px solid var(--border);
}}

.frame-label {{
    text-align: center;
    font-weight: 650;
    margin-top: 8px;
}}

.image-missing {{
    aspect-ratio: 4 / 3;
    display: grid;
    place-items: center;
    color: var(--muted);
    background: #eef1f5;
    border-radius: 9px;
}}

.caption-section {{
    margin-top: 28px;
}}

.section-title {{
    font-size: 18px;
    margin-bottom: 16px;
}}

.caption-stage {{
    margin-bottom: 20px;
}}

.caption-stage h3 {{
    font-size: 15px;
    margin: 0 0 9px;
}}

.caption-comparison {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}}

.caption {{
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 14px;
    min-width: 0;
}}

.prediction {{
    background: #f0f5ff;
}}

.reference {{
    background: #f2f8f3;
}}

.caption-label {{
    font-size: 11px;
    text-transform: uppercase;
    font-weight: 750;
    letter-spacing: .06em;
    color: var(--muted);
}}

.caption p {{
    margin: 8px 0 0;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    font-size: 14px;
}}

.empty-state {{
    display: none;
    text-align: center;
    color: var(--muted);
    padding: 40px;
}}

@media (max-width: 700px) {{
    .image-grid {{
        grid-template-columns: 1fr;
    }}

    .caption-comparison {{
        grid-template-columns: 1fr;
    }}

    .sample-card {{
        padding: 16px;
    }}
}}
</style>
</head>

<body>
<div class="container">

    <header class="page-header">
        <h1>OSCaR-Lite Visual Comparison</h1>

        <p class="subtitle">
            Representative predicted versus reference captions
            from the OSCaR validation evaluation.
        </p>

        <div class="report-stats">
            <div class="stat">
                <strong>{total_samples}</strong>
                <span>Total evaluation samples</span>
            </div>

            <div class="stat">
                <strong>{displayed_samples}</strong>
                <span>Visual examples displayed</span>
            </div>
        </div>
    </header>

    <div class="toolbar">
        <input
            id="search"
            type="search"
            placeholder="Search displayed samples by object or action..."
            aria-label="Search samples"
        >

        <span class="counter" id="counter">
            {displayed_samples} samples
        </span>
    </div>

    <main id="samples">
        {cards_html}
    </main>

    <div class="empty-state" id="empty-state">
        No matching samples found.
    </div>

</div>

<script>
const search = document.getElementById("search");
const cards = [...document.querySelectorAll(".sample-card")];
const counter = document.getElementById("counter");
const emptyState = document.getElementById("empty-state");

function filterSamples() {{
    const query = search.value.trim().toLowerCase();
    let visible = 0;

    for (const card of cards) {{
        const searchableText =
            card.dataset.object + " " +
            card.dataset.action + " " +
            card.textContent.toLowerCase();

        const matches = searchableText.includes(query);

        card.hidden = !matches;

        if (matches) visible++;
    }}

    counter.textContent = `${{visible}} / ${{cards.length}} samples`;
    emptyState.style.display = visible === 0 ? "block" : "none";
}}

search.addEventListener("input", filterSamples);
</script>

</body>
</html>
"""
