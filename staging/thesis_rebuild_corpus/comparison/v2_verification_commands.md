## V2 Verification Commands

Status: synthesis control document  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This file defines the canonical verification commands and hygiene checks for the V2 thesis shell.

It exists so the rebuild does not rely on memory for compile and review steps.

### Primary Build Command

Run from:

- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/v2`

Command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Use after any meaningful edit to:

1. chapter files under `v2/sections/`
2. the V2 preamble
3. bibliography-affecting content
4. figures, tables, or labels

### Canonical Output

Expected build artifact:

- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/v2/main.pdf`

### Build Interpretation

Treat as blocking:

1. LaTeX compile errors
2. undefined control sequences
3. missing input files
4. broken bibliography runs
5. unresolved citations or references that change argument readability materially

Treat as non-blocking but worth monitoring:

1. small overfull or underfull boxes
2. formatting warnings that do not break readability

### Text-Hygiene Checks

Run from repo root when needed:

```bash
rg -n "TODO|TBD|FIXME|XXX" v2
```

Purpose:

1. detect unresolved placeholders
2. catch accidental workflow residue in submission-facing text

### Citation / Reference Sweep

Run from repo root when needed:

```bash
rg -n "\\\\cite\\{|TODO-CITE|TODO-LINK" v2 sections bibliography.bib REFERENCE_MAPPING.md
```

Purpose:

1. inspect citation usage in V2
2. catch leftover citation placeholders
3. cross-check where source resolution may still be incomplete

### Lexicon Safety Check

Run from repo root when needed:

```bash
rg -n "ORSTE|DSTE" v2 sections
```

Purpose:

1. catch forbidden legacy terminology
2. preserve DTSE naming consistency required by `THESIS_OS.md`

### V2 Shell Inventory

Run from repo root when needed:

```bash
rg --files v2/sections
```

Purpose:

1. confirm which V2 chapter files currently exist
2. avoid accidental edits to V1 files when the work should happen in `v2/`

### Final Rule

No section should be treated as stable after patching until the primary V2 build command has been run and checked.
