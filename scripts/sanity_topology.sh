#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
EXPECTED_FILE="${SCRIPT_DIR}/regression_expected/graph_topology_snapshot.json"
TMP_FILE="$(mktemp)"

cleanup() {
  rm -f "${TMP_FILE}"
}
trap cleanup EXIT

cd "${REPO_ROOT}"

if [[ ! -f "${EXPECTED_FILE}" ]]; then
  echo "FAIL: expected topology snapshot is missing: ${EXPECTED_FILE}" >&2
  echo "Run: python3 scripts/topology_snapshot.py --output ${EXPECTED_FILE}" >&2
  exit 1
fi

python3 scripts/topology_snapshot.py --output "${TMP_FILE}" > /dev/null

if ! diff -u "${EXPECTED_FILE}" "${TMP_FILE}"; then
  echo "FAIL: graph topology snapshot mismatch." >&2
  exit 1
fi

echo "PASS: graph topology snapshot matches expected baseline."
