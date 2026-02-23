#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

VALID_CLAIM_ID="$(
  python3 - <<'PY'
from pathlib import Path
import csv

repo_root = Path.cwd()
references = repo_root / "references"
paths = sorted(references.glob("**/claim_ledger*.csv"))
for path in paths:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "claim_id" not in reader.fieldnames:
            continue
        for row in reader:
            value = (row.get("claim_id") or "").strip()
            if value:
                print(value)
                raise SystemExit(0)
raise SystemExit(1)
PY
)"

if [[ -z "${VALID_CLAIM_ID}" ]]; then
  echo "FAIL: could not resolve a valid claim_id from references/**/claim_ledger*.csv" >&2
  exit 1
fi

run_case() {
  local mode="$1"
  local file="$2"
  local stamp_mode="${3:-nostamp}"
  local cmd=(
    python3 "${REPO_ROOT}/scripts/knowledge_skill_graph.py"
    --allow-dirty
    --task task.update-methodology
    --validate-output "${file}"
    --model-id gpt-5.2
    --affected-files sections/personC_methodology.tex
  )
  if [[ "${stamp_mode}" == "nostamp" ]]; then
    cmd+=(--no-stamp)
  fi
  set +e
  "${cmd[@]}" >/dev/null 2>&1
  local rc=$?
  set -e
  if [[ "${mode}" == "pass" && ${rc} -ne 0 ]]; then
    echo "FAIL: expected pass for ${file}" >&2
    exit 1
  fi
  if [[ "${mode}" == "fail" && ${rc} -eq 0 ]]; then
    echo "FAIL: expected failure for ${file}" >&2
    exit 1
  fi
}

cat > "${TMP_DIR}/pass_bullet_claim.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- Supported bullet [CLAIM_ID:__CLAIM__]
## GAPS
None.
EOF

cat > "${TMP_DIR}/pass_paragraph_claim.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
This paragraph is supported [CLAIM_ID:__CLAIM__].
## GAPS
None.
EOF

cat > "${TMP_DIR}/pass_nonassertive.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- Editorial update only [NONASSERTIVE]

This paragraph is non-assertive [NONASSERTIVE].
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_missing_sections.md" <<'EOF'
## SUMMARY
Summary.
## RESULT
- Missing required sections [CLAIM_ID:__CLAIM__]
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_unknown_claim.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- Unknown claim id [CLAIM_ID:UNKNOWN-999]
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_new_claim_missing_key.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
NEW_CLAIM{id=NEW-001; statement=Missing evidence key}
## GAPS
None.
EOF

cat > "${TMP_DIR}/pass_numbered_bullet.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
1. Numbered bullet [CLAIM_ID:__CLAIM__]
## GAPS
None.
EOF

cat > "${TMP_DIR}/pass_multiline_bullet.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- Primary bullet line
  continuation line with claim [CLAIM_ID:__CLAIM__]
## GAPS
None.
EOF

cat > "${TMP_DIR}/pass_extra_heading_inside_result.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
## Notes
This paragraph remains valid [CLAIM_ID:__CLAIM__].
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_duplicate_required_heading.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- First result [CLAIM_ID:__CLAIM__]
## RESULT
- Duplicate required heading [CLAIM_ID:__CLAIM__]
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_out_of_order_headings.md" <<'EOF'
## SUMMARY
Summary.
## RESULT
- Result comes too early [CLAIM_ID:__CLAIM__]
## TRACEABILITY
Trace.
## GAPS
None.
EOF

cat > "${TMP_DIR}/fail_indented_paragraph_after_bullet.md" <<'EOF'
## SUMMARY
Summary.
## TRACEABILITY
Trace.
## RESULT
- Claimed bullet [CLAIM_ID:__CLAIM__]
    Indented paragraph without marker should be separate and fail.
## GAPS
None.
EOF

python3 - <<'PY' "${TMP_DIR}" "${VALID_CLAIM_ID}"
from pathlib import Path
import sys
tmp_dir = Path(sys.argv[1])
claim_id = sys.argv[2]
for path in tmp_dir.glob("*.md"):
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace("__CLAIM__", claim_id), encoding="utf-8")
PY

python3 - <<'PY' "${TMP_DIR}/pass_stamp_crlf.md" "${VALID_CLAIM_ID}"
from pathlib import Path
import sys
path = Path(sys.argv[1])
claim_id = sys.argv[2]
content = (
    "## SUMMARY\r\n"
    "Summary.\r\n"
    "## TRACEABILITY\r\n"
    "Trace.\r\n"
    "## RESULT\r\n"
    f"- Claimed bullet [CLAIM_ID:{claim_id}]\r\n"
    "## GAPS\r\n"
    "None.\r\n"
)
path.write_bytes(content.encode("utf-8"))
PY

run_case pass "${TMP_DIR}/pass_bullet_claim.md"
run_case pass "${TMP_DIR}/pass_paragraph_claim.md"
run_case pass "${TMP_DIR}/pass_nonassertive.md"
run_case pass "${TMP_DIR}/pass_numbered_bullet.md"
run_case pass "${TMP_DIR}/pass_multiline_bullet.md"
run_case pass "${TMP_DIR}/pass_extra_heading_inside_result.md"
run_case fail "${TMP_DIR}/fail_missing_sections.md"
run_case fail "${TMP_DIR}/fail_unknown_claim.md"
run_case fail "${TMP_DIR}/fail_new_claim_missing_key.md"
run_case fail "${TMP_DIR}/fail_duplicate_required_heading.md"
run_case fail "${TMP_DIR}/fail_out_of_order_headings.md"
run_case fail "${TMP_DIR}/fail_indented_paragraph_after_bullet.md"

cp "${TMP_DIR}/pass_stamp_crlf.md" "${TMP_DIR}/pass_stamp_crlf.before.md"
run_case pass "${TMP_DIR}/pass_stamp_crlf.md" stamp
python3 - <<'PY' "${TMP_DIR}/pass_stamp_crlf.before.md" "${TMP_DIR}/pass_stamp_crlf.md"
from pathlib import Path
import sys
before_path = Path(sys.argv[1])
after_path = Path(sys.argv[2])
before = before_path.read_text(encoding="utf-8")
after = after_path.read_text(encoding="utf-8")

def strip_provenance(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.startswith("PROVENANCE|"))

if strip_provenance(before) != strip_provenance(after):
    raise SystemExit("FAIL: stamping modified text outside TRACEABILITY provenance line.")

after_bytes = after_path.read_bytes()
if b"\r\n" not in after_bytes:
    raise SystemExit("FAIL: expected CRLF output after stamping.")
if b"\n" in after_bytes.replace(b"\r\n", b""):
    raise SystemExit("FAIL: newline style changed from CRLF.")
PY

echo "PASS: output contract sanity fixtures passed."
