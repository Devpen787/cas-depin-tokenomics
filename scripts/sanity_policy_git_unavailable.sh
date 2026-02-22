#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

export PYTHONDONTWRITEBYTECODE=1
PYTHON_BIN="$(command -v python3)"
STASH_MSG="sanity_policy_git_unavailable_autostash"
STASHED=0

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

cleanup() {
  local exit_code=$?
  set +e
  if [[ ${STASHED} -eq 1 ]]; then
    git stash pop >/dev/null 2>&1
  fi
  exit "${exit_code}"
}
trap cleanup EXIT

status_start="$(git status --porcelain)"
if [[ -n "${status_start}" ]]; then
  git stash push -u -m "${STASH_MSG}" >/dev/null
  STASHED=1
fi

echo "== Normal policy validation =="
normal_out="$("${PYTHON_BIN}" scripts/knowledge_skill_graph.py --validate-policy 2>&1)" || {
  echo "${normal_out}"
  fail "Normal --validate-policy failed unexpectedly."
}
echo "${normal_out}"
if ! grep -q "Policy validation passed." <<<"${normal_out}"; then
  fail "Normal --validate-policy output missing success confirmation."
fi

echo "== Policy validation with git unavailable =="
set +e
gitless_out="$(PATH="/nonexistent" "${PYTHON_BIN}" scripts/knowledge_skill_graph.py --validate-policy 2>&1)"
gitless_rc=$?
set -e
echo "${gitless_out}"

if [[ ${gitless_rc} -eq 0 ]]; then
  fail "Git-unavailable policy check unexpectedly succeeded."
fi

if ! grep -Eq "FileNotFoundError|No such file or directory: 'git'|unable to determine git" <<<"${gitless_out}"; then
  fail "Git-unavailable output missing expected fail-closed or clear-warning signal."
fi

status_end="$(git status --porcelain)"
if [[ -n "${status_end}" ]]; then
  fail "Repository must be clean at end. Current status:\n${status_end}"
fi

echo "PASS: policy behavior under git-unavailable condition is fail-closed or clearly warned."
