#!/usr/bin/env python3
"""Build the Onocoy Intelligence Dossier PDF from its markdown source.

Usage:
    python3 scripts/build_onocoy_intelligence_dossier.py

Requires: pandoc, pdflatex (both expected in PATH via texlive-full).
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MD_SOURCE = REPO_ROOT / "output" / "md" / "Onocoy_Intelligence_Dossier.md"
PDF_OUTPUT = REPO_ROOT / "output" / "pdf" / "Onocoy_Intelligence_Dossier.pdf"


def main() -> None:
    if not MD_SOURCE.exists():
        print(f"ERROR: source not found: {MD_SOURCE}", file=sys.stderr)
        sys.exit(1)

    PDF_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(MD_SOURCE),
        "-o", str(PDF_OUTPUT),
        "--pdf-engine=pdflatex",
        "-V", "geometry:margin=2.5cm",
        "-V", "fontsize=11pt",
        "-V", "mainfont=Times",
        "-V", "linkcolor=black",
        "-V", "urlcolor=blue",
        "--highlight-style=tango",
    ]

    print(f"Building: {MD_SOURCE.name} -> {PDF_OUTPUT.name}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("pandoc stderr:", result.stderr, file=sys.stderr)
        sys.exit(result.returncode)

    size_kb = PDF_OUTPUT.stat().st_size / 1024
    print(f"Done: {PDF_OUTPUT} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
