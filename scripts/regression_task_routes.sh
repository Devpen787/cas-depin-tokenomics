#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
EXPECTED_DIR="${SCRIPT_DIR}/regression_expected"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "${TMP_DIR}"
}
trap cleanup EXIT

cd "${REPO_ROOT}"
export PYTHONDONTWRITEBYTECODE=1

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

mapfile -t TASK_IDS < <(python3 - <<'PY'
import json
with open('.agent/knowledge-skill-graph.json', encoding='utf-8') as f:
    graph = json.load(f)
tasks = sorted(
    node['id']
    for node in graph.get('nodes', [])
    if isinstance(node, dict) and node.get('type') == 'task' and isinstance(node.get('id'), str)
)
for task_id in tasks:
    print(task_id)
PY
)

if [[ ${#TASK_IDS[@]} -eq 0 ]]; then
  fail "No task nodes found in graph."
fi

mkdir -p "${EXPECTED_DIR}"
generated_count=0
changed_count=0

run_task_output() {
  local task_id="$1"
  python3 scripts/knowledge_skill_graph.py --allow-dirty --task "${task_id}" 2>&1 \
    | sed '/^WARNING: git working tree is dirty; proceeding due to --allow-dirty\.$/d'
}

for task_id in "${TASK_IDS[@]}"; do
  expected_file="${EXPECTED_DIR}/${task_id}.txt"
  actual_file="${TMP_DIR}/${task_id}.txt"
  diff_file="${TMP_DIR}/${task_id}.diff"

  run_task_output "${task_id}" > "${actual_file}"

  if [[ ! -f "${expected_file}" ]]; then
    cp "${actual_file}" "${expected_file}"
    generated_count=$((generated_count + 1))
    continue
  fi

  if ! diff -u "${expected_file}" "${actual_file}" > "${diff_file}"; then
    echo "Route regression detected for ${task_id}:"
    cat "${diff_file}"
    changed_count=$((changed_count + 1))
  fi
done

if [[ ${changed_count} -ne 0 ]]; then
  fail "${changed_count} task route snapshot(s) changed."
fi

if [[ ${generated_count} -ne 0 ]]; then
  echo "Generated baseline snapshots for ${generated_count} task(s) in ${EXPECTED_DIR}."
fi

echo "PASS: all task route outputs match regression snapshots (${#TASK_IDS[@]} tasks)."
