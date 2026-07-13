#!/usr/bin/env python3
"""Insert rendered legacy figure assets into a converted Quarto chapter.

Run this immediately after ``render_legacy_tikz.py`` for one chapter. It
replaces labeled empty HTML figures first, then replaces the remaining empty
margin-figure placeholders in source order. Legacy Pandoc figure links are
normalized to native Quarto cross-references.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QMD = {
    "02": "02-data-representations.qmd",
    "03": "03-vectors-matrices-geometry.qmd",
    "04": "04-probability-statistics.qmd",
    "05": "05-information-entropy.qmd",
    "07": "07-classification.qmd",
    "10": "10-clustering.qmd",
    "11": "11-text-language.qmd",
    "12": "12-search-retrieval.qmd",
    "14": "14-evaluation.qmd",
}


def qmd_id(original_label: str, fallback: str) -> str:
    return original_label.replace(":", "-") if original_label else fallback


def clean_caption(value: str) -> str:
    value = value.replace("\\#", "#")
    value = re.sub(r"Figure\s+fig[-:][A-Za-z0-9_:-]+", "the referenced figure", value)
    return " ".join(value.split())


def plain_alt(value: str) -> str:
    value = re.sub(r"\$([^$]+)\$", r"\1", value)
    value = re.sub(r"\\[A-Za-z]+", "", value)
    value = value.replace("{", "").replace("}", "").replace('"', "'")
    return " ".join(value.split())


def figure_markdown(item: dict[str, str]) -> str:
    identifier = qmd_id(item["original_label"], item["quarto_label"])
    caption = clean_caption(item["caption"])
    alt = plain_alt(caption)
    return f'![{caption}](../{item["asset"]}){{#{identifier} fig-alt="{alt}" width="70%"}}'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter", choices=sorted(QMD))
    args = parser.parse_args()
    chapter_path = ROOT / "chapters" / QMD[args.chapter]
    manifest = json.loads((ROOT / "planning" / "FIGURE_RENDER_MANIFEST.json").read_text())
    items = [item for item in manifest if item["chapter"] == args.chapter and item["status"] == "rendered"]
    if not items:
        raise SystemExit(f"No rendered manifest entries for Chapter {args.chapter}")

    text = chapter_path.read_text()
    remaining: list[dict[str, str]] = []
    for item in items:
        identifier = qmd_id(item["original_label"], item["quarto_label"])
        html_pattern = re.compile(rf'<figure\s+id="{re.escape(identifier)}"[^>]*>.*?</figure>', re.S)
        text, count = html_pattern.subn(lambda _: figure_markdown(item), text, count=1)
        if not count:
            remaining.append(item)

    empty_pattern = re.compile(r"::: ?marginfigure\s*\n(?:\[\]\{[^}]+\}\s*\n)?:::")
    empty_count = len(empty_pattern.findall(text))
    if empty_count != len(remaining):
        raise SystemExit(
            f"Chapter {args.chapter}: {len(remaining)} rendered figures remain but {empty_count} empty placeholders were found; refusing an unsafe rewrite"
        )
    iterator = iter(remaining)
    text = empty_pattern.sub(lambda _: figure_markdown(next(iterator)), text)

    # Normalize the two common Pandoc legacy-reference forms to @fig-id.
    text = re.sub(
        r"Figure\s* ?\[\\?\[?([^\]]+)\\?\]?\]\(#[^)]+\)\{reference-type=\"ref\"\s*reference=\"([^\"]+)\"\}",
        lambda match: "@" + match.group(2),
        text,
    )
    text = re.sub(
        r"Figure\s* ?\[[0-9.]+\]\(#[^)]+\)\{reference-type=\"ref\"\s*reference=\"([^\"]+)\"\}",
        lambda match: "@" + match.group(1),
        text,
    )
    chapter_path.write_text(text)
    print(f"Restored {len(items)} figures in {chapter_path}")


if __name__ == "__main__":
    main()
