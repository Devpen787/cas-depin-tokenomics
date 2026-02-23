#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "Usage: ./scripts/run_validated_task.sh TASK_ID OUTPUT_FILE MODEL_ID AFFECTED_FILES" >&2
  exit 1
fi

TASK_ID="$1"
OUTPUT_FILE="$2"
MODEL_ID="$3"
AFFECTED_FILES="$4"

echo python3 scripts/knowledge_skill_graph.py --task "$TASK_ID" --validate-output "$OUTPUT_FILE" --model-id "$MODEL_ID" --affected-files "$AFFECTED_FILES"
python3 scripts/knowledge_skill_graph.py \
  --task "$TASK_ID" \
  --validate-output "$OUTPUT_FILE" \
  --model-id "$MODEL_ID" \
  --affected-files "$AFFECTED_FILES"
