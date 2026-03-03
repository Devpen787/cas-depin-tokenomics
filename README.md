# DePIN Tokenomics Under Stress

This repository contains the source material, rebuild history, and final LaTeX manuscript for the CAS Blockchain transfer thesis **DePIN Tokenomics Under Stress: A Comparative Stress Evaluation Using the Onocoy Network as an Anchor Case**.

The canonical final manuscript lives in [`v2/`](./v2), not in the legacy root `main.tex` workflow.

## Repository Layout

### Final manuscript
- [`v2/main.tex`](./v2/main.tex): canonical thesis shell
- [`v2/sections/`](./v2/sections): accepted Chapters 1–8 and appendix
- [`v2/main.pdf`](./v2/main.pdf): current compiled thesis PDF when built locally

### Legacy source reservoir
- [`sections/`](./sections): earlier chapter reservoirs and source drafts used during the rebuild
- root [`main.tex`](./main.tex) and [`preamble.tex`](./preamble.tex): legacy manuscript shell retained for source lineage, not the final public thesis target

### Rebuild and audit trail
- [`staging/thesis_rebuild_corpus/`](./staging/thesis_rebuild_corpus): comparison material, handoff notes, decision logs, and full-pass audits used during the V2 rebuild
- [`THESIS_OS.md`](./THESIS_OS.md): project architecture, lexicon, and workflow guardrails
- [`REFERENCE_MAPPING.md`](./REFERENCE_MAPPING.md): citation-control and source-tracking file

### Tooling and data support
- [`scripts/`](./scripts): figure generation and helper scripts
- [`bibliography.bib`](./bibliography.bib): master bibliography database
- [`references/`](./references): local reference archive and extraction files

## Building the Final Thesis

Build from the `v2/` directory:

```bash
cd v2
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

If `biber` is available and you want a fully fresh rebuild:

```bash
cd v2
latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final output is:

- [`v2/main.pdf`](./v2/main.pdf)

## Notes for Readers

- The `v2/` manuscript is the submission-grade thesis.
- The root-level draft files and author-specific section reservoirs are retained for transparency and lineage.
- The `staging/` directory contains rebuild-control artifacts and is useful for process audit, not for reading the thesis itself.

## Notes for Reuse

- This repository contains both original thesis material and third-party reference materials.
- Rights and reuse conditions should be reviewed before republishing or redistributing repository contents, especially inside [`references/`](./references).
