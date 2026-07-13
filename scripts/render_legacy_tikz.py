#!/usr/bin/env python3
"""Render active legacy TikZ figure environments to SVG assets.

The original manuscript embeds many figures directly in LaTeX. Pandoc
preserved their captions during migration but could not preserve the TikZ
drawing commands. This script extracts each active figure containing TikZ,
compiles it in a minimal standalone document, and writes a web-ready SVG.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_ROOT = Path("/Users/wk77/Documents/git/book/print")

CHAPTERS = {
    "01": ("datainfo.tex", "chapter01"),
    "02": ("numbers.tex", "chapter02"),
    "03": ("matrix.tex", "chapter03"),
    "04": ("probability.tex", "chapter04"),
    "05": ("info.tex", "chapter05"),
    "07": ("binary.tex", "chapter07"),
    "10": ("organization.tex", "chapter10"),
    "11": ("text.tex", "chapter11"),
    "12": ("search.tex", "chapter12"),
    "14": ("eval.tex", "chapter14"),
}

PREAMBLE = r"""\documentclass[border=8pt,varwidth=24cm]{standalone}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage[dvipsnames]{xcolor}
\def\pgfsysdriver{pgfsys-dvisvgm.def}
\usepackage{tikz}
\usetikzlibrary{patterns,arrows,matrix,chains,arrows.meta,decorations.pathreplacing,positioning,scopes}
\usepackage{amsmath}
\usepackage{pgfplots}
\usepackage{tabularx}
\usepackage{SIunits}
\usepackage{units}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator*{\argmax}{arg\,max}
\newcommand{\R}{\mathbb{R}}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\tikzset{basic/.style={draw,fill=white,text badly centered,minimum width=3em}}
\tikzset{input/.style={basic,circle}}
\tikzset{weights/.style={basic,rectangle,minimum width=2em}}
\tikzset{functions/.style={basic,circle,fill=white}}
\newcommand{\stepsymbol}{\draw[thick] (0.5em,0.5em) -- (0,0.5em) -- (0,-0.5em) -- (-0.5em,-0.5em) (0em,0.5em) -- (0em,-0.5em) (0.5em,0em) -- (-0.5em,0em);}
\pgfmathdeclarefunction{gauss}{2}{\pgfmathparse{1/(#2*sqrt(2*pi))*exp(-((x-#1)^2)/(2*#2^2))}}
\begin{document}
"""


def active_source(path: Path) -> str:
    """Drop fully commented lines while retaining active LaTeX."""
    return "\n".join(line for line in path.read_text(errors="ignore").splitlines() if not line.lstrip().startswith("%"))


def expand_local_inputs(source: str) -> str:
    """Expand legacy figure snippets referenced with ``\\input``.

    A few search/retrieval diagrams live in ``print/tfigs`` rather than
    directly in the chapter.  Expanding them here lets the same renderer
    preserve those figures without altering the historical source tree.
    """
    pattern = re.compile(r"\\input\{([^}]+)\}")

    def replace(match: re.Match[str]) -> str:
        relative = Path(match.group(1))
        candidate = LEGACY_ROOT / relative
        if not candidate.suffix:
            candidate = candidate.with_suffix(".tex")
        if not candidate.is_file():
            return match.group(0)
        return active_source(candidate)

    return pattern.sub(replace, source)


def extract_environments(source: str) -> list[tuple[str, str]]:
    token = re.compile(r"\\(begin|end)\{(marginfigure|figure\*?)\}")
    stack: list[tuple[str, int, int]] = []
    result: list[tuple[str, str]] = []
    for match in token.finditer(source):
        kind, env = match.group(1), match.group(2)
        if kind == "begin":
            stack.append((env, match.start(), match.end()))
        elif stack and stack[-1][0] == env:
            _, start, content_start = stack.pop()
            if not stack:
                result.append((env, source[content_start : match.start()]))
    return result


def remove_command(text: str, command: str) -> str:
    """Remove every command plus its balanced braced argument."""
    marker = "\\" + command
    while True:
        start = text.find(marker)
        if start < 0:
            return text
        brace = text.find("{", start + len(marker))
        if brace < 0:
            return text
        depth = 0
        end = brace
        while end < len(text):
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1
        text = text[:start] + text[end:]


def plain_caption(block: str) -> str:
    start = block.find("\\caption")
    if start < 0:
        return "Legacy manuscript figure"
    brace = block.find("{", start)
    depth = 0
    end = brace
    while end < len(block):
        if block[end] == "{":
            depth += 1
        elif block[end] == "}":
            depth -= 1
            if depth == 0:
                break
        end += 1
    caption = block[brace + 1 : end]
    caption = re.sub(r"\\ref\{([^}]+)\}", r"\1", caption)
    caption = re.sub(r"\\(?:it|textit)\s*\{([^}]*)\}", r"\1", caption)
    caption = caption.replace("\\#", "#").replace("~", " ")
    return " ".join(caption.split())


def slug_label(label: str, chapter: str, index: int) -> str:
    if label:
        label = label.replace(":", "-").replace("_", "-")
        return re.sub(r"[^A-Za-z0-9-]+", "-", label).strip("-")
    return f"fig-ch{chapter}-legacy-{index:02d}"


def render_chapter(chapter: str) -> list[dict[str, str]]:
    tex_name, asset_dir = CHAPTERS[chapter]
    source_path = LEGACY_ROOT / "chapters" / tex_name
    out_dir = ROOT / "assets" / "figures" / asset_dir
    work_dir = ROOT / "tmp" / "legacy-tikz" / asset_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, str]] = []
    used_slugs: set[str] = set()
    source = expand_local_inputs(active_source(source_path))
    for index, (_, block) in enumerate(extract_environments(source), start=1):
        if "\\begin{tikzpicture}" not in block:
            continue
        label_match = re.search(r"\\label\{([^}]+)\}", block)
        original_label = label_match.group(1) if label_match else ""
        slug = slug_label(original_label, chapter, index)
        base_slug = slug
        duplicate = 2
        while slug in used_slugs:
            slug = f"{base_slug}-{duplicate}"
            duplicate += 1
        used_slugs.add(slug)
        clean = remove_command(remove_command(block, "caption"), "label")
        clean = re.sub(r"^\s*\[[^]]+\]\s*", "", clean)
        clean = clean.replace("\\centering", "")
        document = PREAMBLE + clean + "\n\\end{document}\n"
        tex_path = work_dir / f"{slug}.tex"
        dvi_path = work_dir / f"{slug}.dvi"
        svg_path = out_dir / f"{slug}.svg"
        pdf_path = out_dir / f"{slug}.pdf"
        tex_path.write_text(document)

        compile_result = subprocess.run(
            ["/Library/TeX/texbin/latex", "-halt-on-error", "-interaction=nonstopmode", f"-output-directory={work_dir}", str(tex_path)],
            cwd=LEGACY_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        status = "rendered"
        detail = ""
        if compile_result.returncode:
            status = "compile-failed"
            detail = "\n".join(compile_result.stdout.splitlines()[-12:])
        else:
            convert_result = subprocess.run(
                ["/Library/TeX/texbin/dvisvgm", "--page=1", f"--output={svg_path}", str(dvi_path)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if convert_result.returncode:
                status = "convert-failed"
                detail = "\n".join(convert_result.stdout.splitlines()[-12:])
            else:
                print_tex_path = work_dir / f"{slug}-print.tex"
                print_tex_path.write_text(document.replace("\\def\\pgfsysdriver{pgfsys-dvisvgm.def}\n", ""))
                pdf_result = subprocess.run(
                    [
                        "/Library/TeX/texbin/pdflatex",
                        "-halt-on-error",
                        "-interaction=nonstopmode",
                        f"-output-directory={work_dir}",
                        str(print_tex_path),
                    ],
                    cwd=LEGACY_ROOT,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                )
                if pdf_result.returncode:
                    status = "pdf-convert-failed"
                    detail = "\n".join(pdf_result.stdout.splitlines()[-12:])
                else:
                    shutil.copyfile(work_dir / f"{slug}-print.pdf", pdf_path)

        manifest.append(
            {
                "chapter": chapter,
                "source": str(source_path),
                "original_label": original_label,
                "quarto_label": slug,
                "caption": plain_caption(block),
                "asset": str(svg_path.relative_to(ROOT)),
                "print_asset": str(pdf_path.relative_to(ROOT)),
                "status": status,
                "detail": detail,
            }
        )
        print(f"Chapter {chapter} {slug}: {status}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapters", nargs="*", choices=sorted(CHAPTERS), default=sorted(CHAPTERS))
    args = parser.parse_args()
    manifest: list[dict[str, str]] = []
    for chapter in args.chapters:
        manifest.extend(render_chapter(chapter))
    manifest_path = ROOT / "planning" / "FIGURE_RENDER_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
