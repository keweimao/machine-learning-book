#!/usr/bin/env python3
"""Add idempotent end-of-section links from Volume I to Volume II."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted((ROOT / "chapters").glob("[0-9][0-9]-*.qmd"))
START = "<!-- practice-link:start -->"
END = "<!-- practice-link:end -->"


def slugify(value: str) -> str:
    value = re.sub(r"\{[^}]*\}", "", value)
    value = re.sub(r"[`*_]", "", value).lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "section"


def strip_existing(text: str) -> str:
    # Remove both valid blocks and fragments produced by the original
    # same-boundary insertion bug (for example ``<!`` followed later by
    # ``-- practice-link:start -->``).
    text = re.sub(
        r"(?ms)^(?:[<! -]*\n)*[<! -]*practice-link:start -->\n.*?^<!-- practice-link:end -->\n?",
        "",
        text,
    )
    text = re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", text, flags=re.S)
    return text


def main() -> None:
    total = 0
    for path in CHAPTERS:
        chapter = path.name[:2]
        practice_files = sorted((ROOT / "practice").glob(f"{chapter}-*.qmd"))
        if len(practice_files) != 1:
            raise RuntimeError(f"Expected one practice chapter for {chapter}, found {practice_files}")
        practice_file = practice_files[0]
        text = strip_existing(path.read_text())
        matches = list(re.finditer(r"^(##|###)\s+(.+?)(?:\s+\{[^}]*\})?\s*$", text, re.M))
        seen: dict[str, int] = {}
        inserts: list[tuple[int, int, str]] = []
        for index, match in enumerate(matches):
            level = len(match.group(1))
            title = re.sub(r"\s+\{[^}]*\}\s*$", "", match.group(2)).strip()
            if re.search(r"^(summary|questions?|exercises?|final observation)", title, re.I):
                continue
            base = slugify(title)
            seen[base] = seen.get(base, 0) + 1
            suffix = f"-{seen[base]}" if seen[base] > 1 else ""
            target = f"sec-pr-{chapter}-{base}{suffix}"
            end = len(text)
            for later in matches[index + 1 :]:
                if len(later.group(1)) <= level:
                    end = later.start()
                    break
            block = f'''\n{START}
::: {{.callout-tip collapse="true" title="Put it into practice"}}
Continue with [the corresponding practice activity](../practice/{practice_file.name}#{target})
to turn **{title}** into a calculation,
implementation, visualization, diagnostic, or interpretation task.
:::
{END}
'''
            inserts.append((end, level, block))
        # Group links that share a boundary so no later insertion can split an
        # earlier marker. Put the deeper section link before its parent link.
        grouped: dict[int, list[tuple[int, str]]] = {}
        for position, level, block in inserts:
            grouped.setdefault(position, []).append((level, block))
        for position in sorted(grouped, reverse=True):
            combined = "\n".join(block for _, block in sorted(grouped[position], reverse=True))
            text = text[:position].rstrip() + "\n" + combined + "\n" + text[position:].lstrip("\n")
        path.write_text(text.rstrip() + "\n")
        total += len(inserts)
    print(f"Added {total} theory-to-practice section links")


if __name__ == "__main__":
    main()
