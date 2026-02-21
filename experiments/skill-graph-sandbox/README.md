# Skill Graph Sandbox (Non-Thesis Test Harness)

This folder provides a safe way to test the knowledge-skill graph without touching thesis chapter files.

## Goal

Measure whether graph-routed checks catch more actionable issues than a simple baseline pass.

## What this sandbox uses

- **Knowledge graph in use**: `/workspace/.agent/knowledge-skill-graph.json`
- **Routing engine**: `/workspace/scripts/knowledge_skill_graph.py`
- **Synthetic input**: `corpus/mock_results_section.tex` (contains intentionally planted issues)

No files in `sections/` are read or modified by this harness.

## Run

```bash
python3 experiments/skill-graph-sandbox/evaluate_graph_power.py \
  --task task.pre-submission-review \
  --input experiments/skill-graph-sandbox/corpus/mock_results_section.tex
```

## What you get

- Routed skills for the selected task (from the real graph)
- Baseline findings (minimal generic checks)
- Graph findings (checks activated by routed skills)
- Uplift summary (`graph findings - baseline findings`)

## Why this is useful

It gives an empirical signal before broader adoption:

1. Does routing surface more relevant issues?
2. Are the extra findings genuinely useful or mostly noise?
3. Which skills add value and which should be simplified?
