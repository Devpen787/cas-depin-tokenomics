# Graph Governance and Maintenance Rules

## Purpose
This document defines how we safely maintain the thesis knowledge-skill graph and its CLI without accidental routing drift. The goal is reproducible, reviewable behaviour across daily use, CI checks, and long-term thesis maintenance. These rules apply to `.agent/knowledge-skill-graph.json`, `scripts/knowledge_skill_graph.py`, and related sanity scripts.

## Daily usage workflow (recommended)
Before editing thesis content, run this sequence: `python3 scripts/knowledge_skill_graph.py --validate`, then `python3 scripts/knowledge_skill_graph.py --validate-policy`, then `python3 scripts/knowledge_skill_graph.py --task <task-id>`. This ensures structure and policy are valid before route execution and makes operator intent explicit.

## Change types and required checks
- **Script/CLI logic changes** (`scripts/knowledge_skill_graph.py`): run `--validate`, `--validate-policy`, `scripts/sanity_graph_policy.sh`, `scripts/sanity_no_writes.sh`, `scripts/sanity_topology.sh`, and `scripts/regression_task_routes.sh`.
- **Graph topology/routing changes** (nodes/edges in `.agent/knowledge-skill-graph.json`): run all checks above plus verify affected `--task` outputs and edge/node count expectations.
- **Metadata-only graph changes** (for example `preferred_order`, `graph_source_version`): run `--validate`, `--validate-policy`, and affected task-route checks; topology should remain unchanged unless explicitly intended.
- **Sanity script / CI changes**: run the modified script(s) twice for idempotency and confirm CI workflow coverage remains aligned.

## Snapshot update policy
If route ordering or topology changes are intentional, update `scripts/regression_expected/*.txt` and `scripts/regression_expected/graph_topology_snapshot.json` in the same commit. If no routing/topology change is intended, snapshot files must not change.

## `graph_source_version` policy
`graph_source_version` is a baseline provenance pin with ancestor semantics: it may be older than `HEAD` with no warning if the pin is an ancestor of `HEAD`. Advance the pin after intentional graph provenance checkpoints or merges that should become the new baseline. A divergence warning means the pin is not an ancestor and must be investigated before relying on outputs.

## `preferred_order` warning policy
Duplicate entries and non-closure references are warnings today, not hard failures. Keep this as an adoption-friendly mode for now, then review after 2–3 weeks of normal usage and decide whether to promote these warnings to CI errors.

## PR checklist
- `python3 scripts/knowledge_skill_graph.py --validate` passes.
- `python3 scripts/knowledge_skill_graph.py --validate-policy` passes on a clean tree.
- Sanity scripts pass (`sanity_graph_policy.sh`, `sanity_no_writes.sh`, `sanity_topology.sh`, `regression_task_routes.sh`).
- Snapshots/topology baseline updated only when required by intentional routing/topology changes.
- No unintended graph topology drift.
- Working tree is clean before final policy validation and merge.

## Monthly acceptance pass
Run and review these routes monthly: `task.update-methodology`, `task.prepare-results-discussion`, and `task.pre-submission-review`. Confirm ordering still matches intended QA sequencing and that outputs remain practically useful for thesis writing/review work.
