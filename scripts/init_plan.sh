#!/usr/bin/env bash
# Bootstrap plan/ from plan-template/ for a map project.
# Usage: bash scripts/init_plan.sh [project-root]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
if [ "$#" -ge 1 ]; then
  PROJECT_ROOT="$1"
fi

TEMPLATE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)/plan-template"
PLAN_DIR="$PROJECT_ROOT/plan"
mkdir -p "$PLAN_DIR"

copied=0
for name in project-overview.md progress.md notes.md outline.md stage-gates.md; do
  src="$TEMPLATE_DIR/$name"
  dst="$PLAN_DIR/$name"
  if [ ! -f "$src" ]; then
    echo "[WARN] template missing: $src"
    continue
  fi
  if [ -f "$dst" ]; then
    echo "[SKIP] exists: $dst"
  else
    cp "$src" "$dst"
    echo "[ADD]  $dst"
    copied=$((copied + 1))
  fi
done

echo "[DONE] plan bootstrap finished. files_copied=$copied plan_dir=$PLAN_DIR"
