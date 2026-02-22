# Agent Knowledge-Skill Graph for the Thesis

This document defines a practical, thesis-specific implementation of a knowledge-skill graph so agents can pick the right capabilities for each task.

## Why this pattern

Recent agent research and production patterns converge on a few useful ideas:

- **Composable skill libraries** improve reliability and reuse (skills become explicit, testable units).
- **Graph-based routing** helps with tool/skill selection when tasks have dependencies.
- **Memory + verification loops** reduce drift by forcing checks against source knowledge.

For this thesis, the same idea is useful because we already have stable source files (`THESIS_OS.md`, `THESIS_STRUCTURE.md`, `REFERENCE_MAPPING.md`) and repeatable quality gates (lexicon consistency, citation resolution, cross-section reconciliation).

## What is implemented in this repository

- **Graph data**: `.agent/knowledge-skill-graph.json`
  - Node types: `knowledge`, `skill`, `task`, `risk`, `artefact`
  - Edge types: `REQUIRES`, `ROUTES_TO`, `MITIGATES`, `UPDATES`, `PREREQUISITE`
- **CLI utility**: `scripts/knowledge_skill_graph.py`
  - Validates graph integrity
  - Lists tasks/skills
  - Resolves task -> ordered skill route (including prerequisites)
  - Prints skill manifests (required knowledge, mitigated risks, updated artefacts)

## Core design principles (aligned with THESIS_OS)

1. **Golden Thread first**: skills route through argument alignment before style polishing.
2. **Lexicon lock**: DTSE terminology is enforced centrally.
3. **Evidence discipline**: unresolved claims are tagged and later resolved into page-level citations.
4. **Theory-to-model traceability**: methodology assumptions must map back to framework concepts.
5. **Comparative interpretation guard**: results are framed as conditional, not predictive certainties.

## Source pinning

The `graph_source_version` value records the baseline snapshot commit that the graph was pinned to when it was validated. A run is treated as compatible as long as that pinned commit is an ancestor of the current `HEAD`, so normal forward progress does not break compatibility. The CLI only warns when the pin diverges from `HEAD` history, not when `HEAD` simply moves ahead. This matters for reproducibility because each run can still be traced back to a known source baseline.

`graph_source_version` is the baseline snapshot commit for the graph and tells the CLI which source state the policy was pinned against. If that pinned commit is an ancestor of the current `HEAD`, the run is treated as compatible and no mismatch warning is shown. The mismatch warning is emitted only when the pin diverges from `HEAD` history. `--validate-policy` stays strict and refuses dirty trees, while `--allow-dirty` applies only to task/skill commands and does not bypass `--validate-policy`.

## Source pinning and policy gating

`graph_source_version` is the baseline snapshot commit for the graph, and the pin is treated as valid when that commit is an ancestor of the current `HEAD`, which means no mismatch warning is shown. The warning appears only when the pin diverges from `HEAD` history. `--validate-policy` is strict and refuses dirty trees to preserve reproducibility checks. `--allow-dirty` is an execution override that applies only to `--task` and `--skill` runs, not to `--validate-policy`, and the end-to-end checks live in `scripts/sanity_graph_policy.sh`.

## Quick usage

```bash
python3 scripts/knowledge_skill_graph.py --validate
python3 scripts/knowledge_skill_graph.py --list-tasks
python3 scripts/knowledge_skill_graph.py --task task.update-methodology
python3 scripts/knowledge_skill_graph.py --skill skill.reference-resolution
```

## Suggested workflow

1. Identify the task node (for example `task.update-methodology`).
2. Resolve its ordered skill route.
3. Execute skills in order, using each skill's required knowledge nodes.
4. Emit checklist/report outputs where applicable.
5. Run `--validate` after graph updates to ensure routing remains coherent.

## How to extend safely

- Add new nodes before adding edges to them.
- Keep `PREREQUISITE` edges between skills only.
- If a new chapter or artefact is added, create a `knowledge` or `artefact` node and wire it via `REQUIRES`/`UPDATES`.
- Keep terminology aligned with `THESIS_OS.md` (for example DTSE, not ORSTE).
