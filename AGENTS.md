# Codex & Antigravity Agent Configuration

You are assisting with a master's level thesis on DePIN Tokenomics. 

**CRITICAL:** Before taking any action, you MUST read the `THESIS_OS.md` file located in the root of this repository. 

The `THESIS_OS.md` file contains:
1. The "Golden Thread" (the core argument of the thesis)
2. The exact terminology (e.g., we use DTSE, not ORSTE)
3. The citation and LaTeX tagging workflows (`% TODO-CITE:`)
4. The mapping of theoretical concepts to simulation code parameters.

Always ensure your output aligns with the architecture and SOPs defined in `THESIS_OS.md`.

## Cursor Cloud specific instructions

### Project overview

This is a LaTeX thesis repository (no web app, no Node.js, no pip dependencies). The two "products" are:

1. **Thesis PDF** — compiled from `main.tex` via `latexmk -pdf main.tex`.
2. **Knowledge-skill graph tooling** — Python 3 stdlib-only scripts in `scripts/` validated by CI sanity checks.

### System dependencies

The VM snapshot includes `texlive-full`, `latexmk`, and `biber` (installed via `apt`). Python 3 and Git are pre-installed.

### Key commands

| Task | Command |
|---|---|
| Build PDF | `latexmk -pdf main.tex` |
| Clean build artefacts | `latexmk -C` |
| Validate graph structure | `python3 scripts/knowledge_skill_graph.py --validate` |
| Validate graph policy | `python3 scripts/knowledge_skill_graph.py --validate-policy` |
| Run all CI sanity checks | See `.github/workflows/graph-policy-sanity.yml` for the full list |

### Gotchas

- **Sanity scripts require a clean git working tree.** `sanity_graph_policy.sh` and `sanity_no_writes.sh` will refuse to run if `git status --porcelain` is non-empty. Commit or stash changes before running them.
- **`regression_task_routes.sh` snapshot mismatches on feature branches.** The `graph_source_version` pin in `.agent/knowledge-skill-graph.json` won't match HEAD on non-main branches, producing a `WARNING` line that causes snapshot diffs. This is expected; the actual task routes are correct.
- **No `biber` step in `.latexmkrc`.** The config only sets `$pdflatex` and `$pdf_mode = 1`. `latexmk` auto-detects `biber` from the `.bcf` file, so bibliography resolution works automatically.
- **All Python scripts use only the standard library** — no `pip install` is ever needed.