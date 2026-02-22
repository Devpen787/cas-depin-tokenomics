#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

export PYTHONDONTWRITEBYTECODE=1

TEMP_BRANCH="sanity/preferred-order-guards"
TARGET_TASK="task.pre-submission-review"
STASH_MSG="sanity_preferred_order_guards_autostash"
STASHED=0

ORIG_BRANCH="$(git branch --show-current)"
ORIG_HEAD="$(git rev-parse --verify HEAD)"
START_STATUS_FULL="$(git status --porcelain)"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

cleanup() {
  local exit_code=$?
  set +e

  current_branch="$(git branch --show-current 2>/dev/null)"
  if [[ "${current_branch}" == "${TEMP_BRANCH}" ]]; then
    git reset --hard "${ORIG_HEAD}" >/dev/null 2>&1
    git switch "${ORIG_BRANCH}" >/dev/null 2>&1
  fi

  if git show-ref --verify --quiet "refs/heads/${TEMP_BRANCH}"; then
    git branch -D "${TEMP_BRANCH}" >/dev/null 2>&1
  fi

  if [[ ${STASHED} -eq 1 ]]; then
    git stash pop >/dev/null 2>&1
  fi

  final_status="$(git status --porcelain)"
  if [[ "${final_status}" != "${START_STATUS_FULL}" ]]; then
    echo "FAIL: repository state changed across preferred-order guard sanity run." >&2
    echo "${final_status}" >&2
    exit 1
  fi

  exit "${exit_code}"
}
trap cleanup EXIT

if [[ -n "${START_STATUS_FULL}" ]]; then
  git stash push -u -m "${STASH_MSG}" >/dev/null
  STASHED=1
fi

if git show-ref --verify --quiet "refs/heads/${TEMP_BRANCH}"; then
  fail "Temporary branch already exists: ${TEMP_BRANCH}"
fi

git switch -c "${TEMP_BRANCH}" >/dev/null

python3 - <<'PY'
import json
from pathlib import Path

path = Path('.agent/knowledge-skill-graph.json')
graph = json.loads(path.read_text(encoding='utf-8'))

for node in graph.get('nodes', []):
    if node.get('id') == 'task.pre-submission-review':
        node['preferred_order'] = [
            'skill.reference-resolution',
            'skill.citation-gap-tagging',
            'skill.golden-thread-alignment',
            'skill.lexicon-guard-dtse',
            'skill.metric-definition-audit',
            'skill.metric-definition-audit',
            'skill.scope-contract-check',
            'skill.results-interpretation-guard',
            'skill.reconciliation-check',
            'skill.hostile-review',
            'skill.preflight-quality-gate',
        ]
        break
else:
    raise SystemExit('task.pre-submission-review not found in graph nodes')

path.write_text(json.dumps(graph, indent=2) + '\n', encoding='utf-8')
PY

git add .agent/knowledge-skill-graph.json
git commit -m "test: preferred-order guardrails sanity scenario" >/dev/null

validate_out="$(python3 scripts/knowledge_skill_graph.py --validate 2>&1)" || {
  echo "${validate_out}"
  fail "--validate failed in preferred-order guardrails sanity scenario."
}
echo "${validate_out}"
if ! grep -q "Validation passed: graph structure is consistent." <<<"${validate_out}"; then
  fail "--validate output missing success confirmation."
fi

policy_out="$(python3 scripts/knowledge_skill_graph.py --validate-policy 2>&1)" || {
  echo "${policy_out}"
  fail "--validate-policy failed in preferred-order guardrails sanity scenario."
}
echo "${policy_out}"
if ! grep -q "Policy validation passed." <<<"${policy_out}"; then
  fail "--validate-policy output missing success confirmation."
fi
if ! grep -q "preferred_order contains duplicate skill ids." <<<"${policy_out}"; then
  fail "--validate-policy missing duplicate preferred_order warning."
fi
if ! grep -q "preferred_order references skill outside routed closure: skill.scope-contract-check." <<<"${policy_out}"; then
  fail "--validate-policy missing non-closure preferred_order warning."
fi

task_out="$(python3 scripts/knowledge_skill_graph.py --task "${TARGET_TASK}" 2>&1)" || {
  echo "${task_out}"
  fail "--task failed in preferred-order guardrails sanity scenario."
}
echo "${task_out}"

line_citation="$(grep -n "skill.citation-gap-tagging - Citation Gap Tagging" <<<"${task_out}" | head -n1 | cut -d: -f1 || true)"
line_reference="$(grep -n "skill.reference-resolution - Reference Resolution" <<<"${task_out}" | head -n1 | cut -d: -f1 || true)"

if [[ -z "${line_citation}" || -z "${line_reference}" ]]; then
  fail "Could not locate citation/reference skills in task output."
fi

if (( line_citation >= line_reference )); then
  fail "Prerequisite guard failed: reference-resolution appeared before citation-gap-tagging."
fi

if grep -qE "^[[:space:]]+[0-9]+\. skill.scope-contract-check" <<<"${task_out}"; then
  fail "Non-closure skill unexpectedly appeared in routed task output."
fi

echo "PASS: preferred_order guardrails hold (warnings emitted, prerequisites respected)."
