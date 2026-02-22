#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

status_start="$(git status --porcelain)"
if [[ -n "${status_start}" ]]; then
  fail "Repository must be clean at start. Current status:\n${status_start}"
fi

python3 scripts/knowledge_skill_graph.py --validate
python3 scripts/knowledge_skill_graph.py --validate-policy
python3 scripts/knowledge_skill_graph.py --list-tasks
python3 scripts/knowledge_skill_graph.py --list-skills
python3 scripts/knowledge_skill_graph.py --task task.pre-submission-review
python3 scripts/knowledge_skill_graph.py --skill skill.reference-resolution

status_end="$(git status --porcelain)"
if [[ -n "${status_end}" ]]; then
  fail "Repository must remain clean after read-only checks. Current status:\n${status_end}"
fi

echo "PASS: read-only CLI commands produced no repository writes."
