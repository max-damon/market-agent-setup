#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
if [[ -n "$(git -C "$repo_root" status --porcelain)" ]]; then
  echo "Modifications locales détectées. Les relire, les committer et les pousser ou les écarter avant la mise à jour." >&2
  exit 1
fi
git -C "$repo_root" pull --ff-only
bash "$repo_root/scripts/install.sh"
