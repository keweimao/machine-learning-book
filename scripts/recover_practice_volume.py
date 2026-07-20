#!/usr/bin/env python3
"""Recover and organize the historical hands-on book materials.

The organized 2026 archive is the canonical source because its copies match
the KeenSee publication tree while excluding rendered HTML and checkpoints.
This script copies the selected source notebooks and data, converts notebooks
to non-executing QMD chapters, and creates a theory-aligned practice scaffold.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = Path("/Users/wk77/Documents/git/book/oldbook_organized/web-source")
PRACTICE = ROOT / "practice"

LABS = [
    ("setup", "setup.ipynb", "Python and Jupyter Setup", "toolkit"),
    ("python-intro", "python/python_intro.ipynb", "Python Programming Primer", "toolkit"),
    ("python-io", "python/python_io.ipynb", "Python Input and Output", "toolkit"),
    ("python-selection", "python/python_selection.ipynb", "Python Selection", "toolkit"),
    ("python-random", "python/python_random.ipynb", "Python Randomness", "toolkit"),
    ("python-loops", "python/python_loop.ipynb", "Python Repetition", "toolkit"),
    ("python-file-processing", "python/python_data_files.ipynb", "Python File Processing", "toolkit"),
    ("python-data-types", "python/python_data_types.ipynb", "Python Data Types", "02"),
    ("python-data-structures", "python/python_data_structures.ipynb", "Python Data Structures", "02"),
    ("python-data-structures-assignment", "problems/python_data_structure.ipynb", "Python Data Structures Assignment", "02"),
    ("data-initialization-assignment", "problems/python_data_init.ipynb", "Data, Vectors, and Cosine Assignment", "03"),
    ("probability-linearity", "demo/data_prob_linear.ipynb", "Probability and Linearity in Data", "04"),
    ("data-preprocessing", "python/python_data_preprocessing.ipynb", "Python Data Preprocessing", "06"),
    ("outliers", "demo/demo_outliers.ipynb", "Outliers versus the Normal", "06"),
    ("classification-patterns-assignment", "problems/assignment_2_final.ipynb", "Classification Patterns and Evaluation Assignment", "09"),
    ("clustering", "demo/python_clustering.ipynb", "Text and Cluster Analysis", "10"),
    ("text-vectorization", "demo/python_text_vector.ipynb", "Text Vectorization", "11"),
    ("text-vectorization-assignment", "problems/python_text_vector.ipynb", "Text Vectorization Programming Assignment", "11"),
    ("integrated-learning-assignment", "problems/data_learning.ipynb", "Integrated Data Learning Assignment", "11"),
    ("sqlite-assignment", "problems/python_sqlite.ipynb", "SQLite and Data Retrieval Assignment", "12"),
    ("sqlite", "sql/sqlite.ipynb", "SQLite Practice", "12"),
    ("sqlite-python", "sql/sqlite_python.ipynb", "SQLite with Python", "12"),
    ("association-rules", "demo/python_association_rule_mining.ipynb", "Association Rule Mining", "14"),
    ("data-mining-project", "problems/data_mining_project.ipynb", "Data Mining Project", "16"),
    ("reinforcement-learning-extension", "research/rl_taxi.ipynb", "Reinforcement Learning Extension", "16"),
]

LAB_TITLES = {slug: title for slug, _source, title, _chapter in LABS}


def lab_link(slug: str, prefix: str = "labs/") -> str:
    """Return a cross-format link to a recovered lab landing section."""
    return f"[{LAB_TITLES[slug]}]({prefix}{slug}.qmd#sec-lab-{slug})"

DATA = [
    ("demo/data/adult.data", "adult.data"),
    ("demo/data/cars.txt", "cars.txt"),
    ("demo/data/phones.csv", "phones.csv"),
    ("demo/data/spam.csv", "spam.csv"),
    ("demo/yelp_reviews.csv", "yelp_reviews.csv"),
    ("demo/groceries/groceries_modified.csv", "groceries/groceries_modified.csv"),
    ("python/data/Yelp_Usefulness_Practice.csv", "Yelp_Usefulness_Practice.csv"),
    ("python/data/students.csv", "students.csv"),
    ("problems/data/CCSubset.csv", "CCSubset.csv"),
    ("problems/data/Yelp_Usefulness_Assignment2_1.csv", "Yelp_Usefulness_Assignment2_1.csv"),
    ("problems/data/Yelp_Usefulness_Assignment2_2.csv", "Yelp_Usefulness_Assignment2_2.csv"),
    ("problems/data/Yelp_Usefulness_Assignment2_3.csv", "Yelp_Usefulness_Assignment2_3.csv"),
    ("problems/mydatabase.db", "mydatabase.db"),
]

FIGURES = [
    ("figures/drexel_vpn1.png", "drexel_vpn1.png"),
    ("figures/drexel_vpn3.png", "drexel_vpn3.png"),
    ("figures/right.png", "right.png"),
    ("figures/jupyter_hub.png", "jupyter_hub.png"),
    ("figures/jupyter1.png", "jupyter1.png"),
    ("figures/jupyter2.png", "jupyter2.png"),
    ("figures/book_stack.jpg", "book_stack.jpg"),
    ("figures/wait_line.jpg", "wait_line.jpg"),
    ("figures/served.jpg", "served.jpg"),
    ("figures/train.jpg", "train.jpg"),
    ("figures/outliers/summer.jpg", "outliers/summer.jpg"),
    ("models/figures/nn_sigmoid.png", "nn_sigmoid.png"),
    ("research/figures/demo_state.png", "research/demo_state.png"),
    ("research/figures/soccer_game.jpg", "research/soccer_game.jpg"),
    ("research/figures/taxi.png", "research/taxi.png"),
    ("research/figures/cab2.png", "research/cab2.png"),
    ("research/figures/0_south.png", "research/0_south.png"),
    ("research/figures/8_dropoff.png", "research/8_dropoff.png"),
    ("research/figures/7_north.png", "research/7_north.png"),
    ("sql/figures/sqlite3.png", "sqlite/sqlite3.png"),
    ("sql/figures/sqlite_open.png", "sqlite/sqlite_open.png"),
    ("figures/python_data/typewrite.jpg", "python_data/typewrite.jpg"),
    ("figures/python_data/text.png", "python_data/text.png"),
    ("figures/python_data/radish.png", "python_data/radish.png"),
]

CHAPTER_NAMES = {
    "01": "From Data to Information and Meaning",
    "02": "Data Types and Representations",
    "03": "Vectors, Matrices, and Geometric Thinking",
    "04": "Probability and Statistical Thinking",
    "05": "Information, Entropy, and Divergence",
    "06": "Data Preparation and Feature Engineering",
    "07": "Classification",
    "08": "Multiclass and Structured Decisions",
    "09": "Numeric Prediction and Regression",
    "10": "Clustering and Organization",
    "11": "Text and Human Language",
    "12": "Search and Retrieval",
    "13": "Graphs and Structural Analysis",
    "14": "Evaluation and Experimentation",
    "15": "Generalization, Model Selection, and Fit",
    "16": "Scaling, Deployment, and Responsible Use",
}

CHAPTER_FILES = {
    p.name[:2]: p for p in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.qmd"))
}

LAB_DESCRIPTIONS = {
    "setup": "Install and verify the Python/Jupyter environment used by the recovered activities.",
    "python-intro": "Practice expressions, variables, functions, and a reproducible notebook workflow.",
    "python-io": "Read input, format output, and practice small interactive programs.",
    "python-selection": "Use conditions to encode branching decisions.",
    "python-random": "Generate and interpret pseudo-random outcomes.",
    "python-loops": "Use repetition to process collections and numerical sequences.",
    "python-file-processing": "Read and transform text and structured files.",
    "python-data-types": "Represent numeric, textual, Boolean, and composite values in Python.",
    "python-data-structures": "Work with lists, tuples, sets, and dictionaries as computational representations.",
    "python-data-structures-assignment": "Apply foundational Python structures in a graded problem set.",
    "data-initialization-assignment": "Construct arrays and vectors, compute descriptive quantities, and implement cosine-based comparisons.",
    "probability-linearity": "Explore probability patterns and train linear classifiers on idealized and imperfect data.",
    "data-preprocessing": "Load tabular data, inspect quality, transform values, and detect candidate outliers.",
    "outliers": "Compare global and contextual outliers using international-call and demographic examples.",
    "classification-patterns-assignment": "Apply predictive models, pattern evaluation, and association analysis to prepared data.",
    "clustering": "Vectorize Yelp review text and build a topic-oriented k-means clustering workflow.",
    "text-vectorization": "Tokenize text and construct document vectors step by step.",
    "text-vectorization-assignment": "Implement reusable text-vectorization functions over a document collection.",
    "integrated-learning-assignment": "Connect rank-frequency behavior, text vectorization, and linear/nonlinear classification.",
    "sqlite-assignment": "Create and query a SQLite database while connecting storage choices to retrieval tasks.",
    "sqlite": "Practice relational storage and SQL operations with SQLite.",
    "sqlite-python": "Connect Python programs to a SQLite database.",
    "association-rules": "Prepare transaction data and evaluate association rules with support, confidence, and lift.",
    "data-mining-project": "Design a complete project from problem statement through data, method, evaluation, and communication.",
    "reinforcement-learning-extension": "Explore a sequential-decision extension using the Taxi environment.",
}

SECTION_LABS = {
    "01": [(r"data|generaliz", ["data-mining-project"])],
    "02": [
        (r"datum|numerical|categorical", ["python-data-types"]),
        (r"data|sets|vectors", ["python-data-structures", "python-data-structures-assignment", "data-initialization-assignment"]),
    ],
    "03": [
        (r"matrix|sum of squares|magnitude|distance|angle", ["data-initialization-assignment"]),
        (r"kernel|optimization", ["integrated-learning-assignment"]),
        (r"graph", ["reinforcement-learning-extension"]),
    ],
    "04": [
        (r"probability|joint|independent|dependent|distribution|estimat|mle", ["probability-linearity"]),
        (r"bayes", ["integrated-learning-assignment"]),
    ],
    "05": [
        (r"entropy|information|idf|divergence", ["integrated-learning-assignment"]),
    ],
    "06": [
        (r"quality|missing|noisy|scaling|normalization|encoding|feature|pipeline|leakage", ["data-preprocessing"]),
        (r"quality|missing|noisy", ["outliers"]),
    ],
    "07": [
        (r"nearest|distance|centroid", ["data-initialization-assignment"]),
        (r"linear|perceptron", ["probability-linearity", "integrated-learning-assignment"]),
        (r"non-linear|kernel|neural|support vector", ["integrated-learning-assignment"]),
    ],
    "08": [
        (r".", ["classification-patterns-assignment", "integrated-learning-assignment"]),
    ],
    "09": [
        (r"outcome|linear regression|loss|diagnostic|uncertainty", ["outliers", "classification-patterns-assignment"]),
        (r"regularization|nonlinear", ["classification-patterns-assignment"]),
    ],
    "10": [(r".", ["clustering"])],
    "11": [
        (r"vectorization|tokenization|weighting", ["text-vectorization", "text-vectorization-assignment"]),
        (r"similarity", ["data-initialization-assignment", "text-vectorization"]),
        (r"zipf|feature selection", ["integrated-learning-assignment"]),
        (r"classification|bayes", ["integrated-learning-assignment"]),
    ],
    "12": [
        (r"indexing|matching|paradigm", ["sqlite", "sqlite-python", "sqlite-assignment"]),
        (r"ranking|pagerank|filtering", ["integrated-learning-assignment"]),
    ],
    "14": [
        (r"precision|recall|sensitivity|specificity|kappa|averaging|error|correlation", ["classification-patterns-assignment"]),
        (r"rank", ["integrated-learning-assignment", "association-rules"]),
        (r"experiment|efficiency", ["data-mining-project"]),
    ],
    "15": [(r".", ["classification-patterns-assignment", "data-mining-project"])],
    "16": [
        (r"compute|batch|stream|pipeline|deployment|monitoring", ["data-mining-project"]),
        (r"responsible|human|misuse|privacy|energy", ["data-mining-project", "reinforcement-learning-extension"]),
    ],
}


def slugify(value: str) -> str:
    value = re.sub(r"\{[^}]*\}", "", value)
    value = re.sub(r"[`*_]", "", value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "section"


def theory_sections(chapter: str) -> list[tuple[int, str, str]]:
    sections: list[tuple[int, str, str]] = []
    seen: dict[str, int] = {}
    for line in CHAPTER_FILES[chapter].read_text(errors="ignore").splitlines():
        match = re.match(r"^(##|###)\s+(.+?)(?:\s+\{[^}]*\})?\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        title = re.sub(r"\s+\{[^}]*\}\s*$", "", match.group(2)).strip()
        if re.search(r"^(summary|questions?|exercises?|final observation)", title, re.I):
            continue
        base = slugify(title)
        seen[base] = seen.get(base, 0) + 1
        suffix = f"-{seen[base]}" if seen[base] > 1 else ""
        sections.append((level, title, f"sec-pr-{chapter}-{base}{suffix}"))
    return sections


def copy_sources() -> list[dict[str, str]]:
    notebook_dir = PRACTICE / "notebooks"
    lab_dir = PRACTICE / "labs"
    data_dir = PRACTICE / "data"
    figure_dir = PRACTICE / "figures"
    notebook_dir.mkdir(parents=True, exist_ok=True)
    lab_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    figure_dir.mkdir(parents=True, exist_ok=True)

    provenance: list[dict[str, str]] = []
    for slug, relative, title, chapter in LABS:
        source = ARCHIVE / relative
        notebook = notebook_dir / f"{slug}.ipynb"
        qmd = lab_dir / f"{slug}.qmd"
        shutil.copy2(source, notebook)
        subprocess.run(
            ["quarto", "convert", str(source), "--output", str(qmd)],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        normalize_lab(qmd, slug, title, relative)
        provenance.append(
            {
                "slug": slug,
                "title": title,
                "practice_chapter": chapter,
                "source": str(source),
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "notebook": str(notebook.relative_to(ROOT)),
                "qmd": str(qmd.relative_to(ROOT)),
            }
        )

    for relative, destination in DATA:
        source = ARCHIVE / relative
        target = data_dir / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for relative, destination in FIGURES:
        source = ARCHIVE / relative
        target = figure_dir / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return provenance


def normalize_lab(path: Path, slug: str, title: str, source_relative: str) -> None:
    text = path.read_text(errors="ignore")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        text = text[end + 4 :].lstrip("\n")
    historical_links = {
        "http://keensee.com/pdp/demo/python_text_vector.html": "text-vectorization.qmd#sec-lab-text-vectorization",
        "http://keensee.com/pdp/python/python_data_preprocessing.html": "data-preprocessing.qmd#sec-lab-data-preprocessing",
        "http://keensee.com/pdp/python/python_data_structures.html": "python-data-structures.qmd#sec-lab-python-data-structures",
    }
    for old_url, new_target in historical_links.items():
        text = re.sub(
            rf"\[([^]]+)\]\({re.escape(old_url)}\)",
            rf"[\1]({new_target})",
            text,
        )
        text = text.replace(old_url, new_target)
    text = text.replace("![SQLite](https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg)\n", "")
    text = text.replace("![Python](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)\n", "")
    text = text.replace("[SQLite](sqlite.html)", "[SQLite Practice](sqlite.qmd#sec-lab-sqlite)")
    replacements = {
        "./data/Yelp_Usefulness_Practice.csv": "../data/Yelp_Usefulness_Practice.csv",
        "./data/Yelp_Usefulness_Assignment2_1.csv": "../data/Yelp_Usefulness_Assignment2_1.csv",
        "./data/Yelp_Usefulness_Assignment2_2.csv": "../data/Yelp_Usefulness_Assignment2_2.csv",
        "./data/Yelp_Usefulness_Assignment2_3.csv": "../data/Yelp_Usefulness_Assignment2_3.csv",
        "data/CCSubset.csv": "../data/CCSubset.csv",
        "data/adult.data": "../data/adult.data",
        "data/cars.txt": "../data/cars.txt",
        "data/phones.csv": "../data/phones.csv",
        "data/spam.csv": "../data/spam.csv",
        "yelp_reviews.csv": "../data/yelp_reviews.csv",
        "./groceries/groceries_modified.csv": "../data/groceries/groceries_modified.csv",
        "../models/figures/nn_sigmoid.png": "../figures/nn_sigmoid.png",
        '"mydatabase.db"': '"../data/mydatabase.db"',
        '"students.csv"': '"../data/students.csv"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    if slug == "setup":
        text = re.sub(r'(?<=src=")figures/', "../figures/", text)
        text = re.sub(r'(?<=\]\()figures/', "../figures/", text)
    if slug == "reinforcement-learning-extension":
        text = text.replace('src="figures/', 'src="../figures/research/')
    if slug == "sqlite":
        text = text.replace('src="figures/', 'src="../figures/sqlite/')
    header = f'''---
execute:
  enabled: false
---

# {title} {{#ch-lab-{slug} .unnumbered}}

## Recovered activity {{#sec-lab-{slug}}}

::: {{.callout-note title="Historical source and execution note"}}
This activity was recovered from `{source_relative}`. Its code is preserved but
is not executed during the public book build, so readers can inspect it without
requiring legacy package versions. Download the [source notebook](../notebooks/{slug}.ipynb)
to run and modernize it interactively.
:::

'''
    path.write_text(header + text.lstrip())


def labs_for_chapter(chapter: str) -> list[tuple[str, str]]:
    return [(slug, title) for slug, _, title, mapped in LABS if mapped == chapter]


def labs_for_section(chapter: str, title: str) -> list[str]:
    result: list[str] = []
    for pattern, slugs in SECTION_LABS.get(chapter, []):
        if re.search(pattern, title, re.I):
            for slug in slugs:
                if slug not in result:
                    result.append(slug)
    return result


def write_practice_chapters(legacy_search: str) -> None:
    PRACTICE.mkdir(parents=True, exist_ok=True)
    (PRACTICE / "index.qmd").write_text(
        '''---
number-sections: false
---

# Practice and Projects {#ch-practice .unnumbered}

This volume turns the conceptual development in Volume I into observable,
testable work. It is intentionally placed after the theory chapters so readers
can follow the conceptual narrative continuously, while every substantive
theory section provides a direct route here.

## How to use this volume

- **Read-first path:** finish a theory section, then follow its *Put it into
  practice* link to the aligned activity or development scaffold.
- **Build-first path:** start from an activity, use its *Theory connection* to
  revisit the underlying model, and return with a concrete question.
- **Course path:** combine selected activities into short labs, assignments,
  and a final project without changing the theory sequence.

Recovered activities preserve their original wording and code wherever
possible. They are rendered without execution until dependencies, datasets,
and expected outputs have been modernized and tested. Sections marked as
development scaffolds make the missing practical coverage explicit rather than
hiding it.
'''
    )
    (PRACTICE / "00-toolkit.qmd").write_text(
        '''---
number-sections: false
---

# Computational Toolkit {#ch-practice-toolkit .unnumbered}

The book's practice volume uses Python and Jupyter-compatible notebooks. These
recovered primers are optional for readers who already have a working Python
environment.

## Environment setup {#sec-pr-toolkit-setup}

Continue with [Python and Jupyter Setup](labs/setup.qmd#sec-lab-setup).

## Python programming primer {#sec-pr-toolkit-python}

Continue with [Python Programming Primer](labs/python-intro.qmd#sec-lab-python-intro).

## Control flow, randomness, and input/output {#sec-pr-toolkit-control-flow}

Continue with [Python Input and Output](labs/python-io.qmd#sec-lab-python-io),
[Python Selection](labs/python-selection.qmd#sec-lab-python-selection),
[Python Randomness](labs/python-random.qmd#sec-lab-python-random), and
[Python Repetition](labs/python-loops.qmd#sec-lab-python-loops).

## File processing {#sec-pr-toolkit-files}

Continue with [Python File Processing](labs/python-file-processing.qmd#sec-lab-python-file-processing).

## Core data types and structures {#sec-pr-toolkit-data}

Continue with [Python Data Types](labs/python-data-types.qmd#sec-lab-python-data-types),
[Python Data Structures](labs/python-data-structures.qmd#sec-lab-python-data-structures), and
[Python Data Structures Assignment](labs/python-data-structures-assignment.qmd#sec-lab-python-data-structures-assignment).
'''
    )

    for chapter, name in CHAPTER_NAMES.items():
        theory_file = CHAPTER_FILES[chapter]
        theory_ref = f"[Volume I, Chapter {int(chapter)}](../chapters/{theory_file.name})"
        lines = [
            "---",
            "number-sections: false",
            "---",
            "",
            f"# Practice {int(chapter)}: {name} {{#ch-practice-{chapter} .unnumbered}}",
            "",
            f"**Theory connection:** {theory_ref}",
            "",
            "Use this chapter as the practical companion to the corresponding theory chapter.",
            "Recovered activities are linked where a strong match exists; other sections are",
            "explicit development scaffolds for the next writing cycle.",
            "",
        ]
        sections = theory_sections(chapter)
        for level, title, section_id in sections:
            hashes = "#" * level
            lines.extend([f"{hashes} {title} {{#{section_id}}}", ""])
            matched_labs = labs_for_section(chapter, title)
            if matched_labs:
                links = " and ".join(lab_link(slug) for slug in matched_labs)
                lines.extend(
                    [
                        f"Recovered starting point: {links}.",
                        "",
                        "Use the recovered material as evidence and raw material; revise package calls,",
                        "expected outputs, and assessment criteria before assigning it in a current course.",
                        "",
                    ]
                )
            else:
                lines.extend(
                    [
                        "::: {.callout-note title=\"Practice development scaffold\"}",
                        f"Create an activity that makes **{title}** observable through a calculation,",
                        "small implementation, visualization, diagnostic, or written interpretation.",
                        "Include a reproducible input, a checkable result, and one reflection question.",
                        "::: ",
                        "",
                    ]
                )
        if chapter == "12" and legacy_search:
            lines.extend(
                [
                    "## Recovered retrieval questions and exercise {#sec-pr-12-recovered-exercise}",
                    "",
                    legacy_search.strip(),
                    "",
                ]
            )
        (PRACTICE / f"{chapter}-{slugify(name)}.qmd").write_text("\n".join(lines).rstrip() + "\n")


def move_search_exercises() -> str:
    path = CHAPTER_FILES["12"]
    text = path.read_text()
    marker = "\n## Questions\n"
    if marker not in text:
        return ""
    body, recovered = text.split(marker, 1)
    recovered = "## Recovered questions\n" + recovered
    recovered = recovered.replace("## Exercise {#exercise .unnumbered}", "## Recovered retrieval calculation")
    path.write_text(body.rstrip() + "\n")
    return recovered


def restore_search_footnotes(recovered: str) -> str:
    """Keep chapter footnote definitions with the theory that cites them."""
    match = re.search(r"(?m)^\[\^ch12-1\]:", recovered)
    if not match:
        return recovered
    activity = recovered[: match.start()].rstrip()
    footnotes = recovered[match.start() :].strip()
    theory_path = CHAPTER_FILES["12"]
    theory = theory_path.read_text().rstrip()
    if "[^ch12-1]:" not in theory:
        theory_path.write_text(theory + "\n\n" + footnotes + "\n")
    return activity


def main() -> None:
    if not ARCHIVE.is_dir():
        raise SystemExit(f"Archive not found: {ARCHIVE}")
    legacy_search = move_search_exercises()
    existing_search = PRACTICE / "12-search-and-retrieval.qmd"
    if not legacy_search and existing_search.exists():
        existing = existing_search.read_text(errors="ignore")
        marker = "## Recovered retrieval questions and exercise"
        if marker in existing:
            legacy_search = existing.split(marker, 1)[1]
            legacy_search = re.sub(r"^\s*\{#sec-pr-12-recovered-exercise\}\s*", "", legacy_search)
    legacy_search = restore_search_footnotes(legacy_search)
    provenance = copy_sources()
    write_practice_chapters(legacy_search)
    manifest = {
        "canonical_archive": str(ARCHIVE),
        "selection_policy": "latest corrected, non-checkpoint source; rendered HTML excluded",
        "labs": provenance,
        "data": [
            {
                "source": str(ARCHIVE / source),
                "destination": str((PRACTICE / "data" / destination).relative_to(ROOT)),
            }
            for source, destination in DATA
        ],
        "figures": [
            {
                "source": str(ARCHIVE / source),
                "destination": str((PRACTICE / "figures" / destination).relative_to(ROOT)),
            }
            for source, destination in FIGURES
        ],
    }
    (PRACTICE / "PROVENANCE.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Recovered {len(provenance)} labs and {len(DATA)} data files into {PRACTICE}")


if __name__ == "__main__":
    main()
