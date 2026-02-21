#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

cleanup() {
  rm -f .policy-dirty-probe
}
trap cleanup EXIT

start_status="$(git status --porcelain)"
if [[ -n "${start_status}" ]]; then
  fail "Working tree must be clean at start. Current status:\n${start_status}"
fi

echo "== Step 2: structure validation =="
python3 scripts/knowledge_skill_graph.py --validate

echo "== Step 3: policy validation =="
python3 scripts/knowledge_skill_graph.py --validate-policy

echo "== Step 4: dirty probe =="
touch .policy-dirty-probe

echo "== Step 5: list command on dirty tree (warn-only expected) =="
list_output="$(python3 scripts/knowledge_skill_graph.py --list-tasks 2>&1)" || {
  echo "${list_output}"
  fail "--list-tasks unexpectedly failed on dirty tree."
}
echo "${list_output}"
if ! grep -q "WARNING: git working tree is dirty" <<<"${list_output}"; then
  fail "--list-tasks did not emit expected dirty-tree warning."
fi

echo "== Step 6: execution command on dirty tree (refusal expected) =="
set +e
task_dirty_output="$(python3 scripts/knowledge_skill_graph.py --task task.update-methodology 2>&1)"
task_dirty_rc=$?
set -e
echo "${task_dirty_output}"
if [[ ${task_dirty_rc} -eq 0 ]]; then
  fail "--task unexpectedly succeeded on dirty tree without override."
fi
if ! grep -q "Refusing run: git working tree is dirty." <<<"${task_dirty_output}"; then
  fail "--task failure output missing expected dirty refusal message."
fi

echo "== Step 7: execution command with --allow-dirty (success expected) =="
task_allow_output="$(python3 scripts/knowledge_skill_graph.py --allow-dirty --task task.update-methodology 2>&1)" || {
  echo "${task_allow_output}"
  fail "--allow-dirty task command failed unexpectedly."
}
echo "${task_allow_output}"
if ! grep -q "proceeding due to --allow-dirty" <<<"${task_allow_output}"; then
  fail "--allow-dirty output missing expected override warning."
fi

echo "== Step 8: cleanup probe =="
rm -f .policy-dirty-probe

echo "== Step 9: final clean check =="
end_status="$(git status --porcelain)"
if [[ -n "${end_status}" ]]; then
  fail "Working tree must be clean at end. Current status:\n${end_status}"
fi

echo "Sanity checks passed."
