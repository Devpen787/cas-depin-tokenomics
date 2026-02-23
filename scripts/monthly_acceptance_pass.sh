#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

status="$(git status --porcelain)"
if [[ -n "${status}" ]]; then
  fail "Working tree must be clean before monthly acceptance pass. Current status:\n${status}"
fi

echo "== Core validation =="
python3 scripts/knowledge_skill_graph.py --validate
python3 scripts/knowledge_skill_graph.py --validate-policy

echo "== Monthly acceptance routes =="
python3 scripts/knowledge_skill_graph.py --task task.update-methodology
python3 scripts/knowledge_skill_graph.py --task task.prepare-results-discussion
python3 scripts/knowledge_skill_graph.py --task task.pre-submission-review

echo "== Manual review checklist =="
echo "- ordering still matches intended QA sequence?"
echo "- outputs useful / low-noise?"
echo "- any route feels semantically off?"

echo "PASS: monthly acceptance pass completed."
