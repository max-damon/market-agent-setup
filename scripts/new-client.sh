#!/usr/bin/env bash
set -euo pipefail

slug="${1:-}"
if [[ ! "$slug" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "Usage : bash scripts/new-client.sh nom-du-client (lettres minuscules, chiffres, tirets)" >&2
  exit 2
fi
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
icloud_root="${MARKET_AGENT_ICLOUD_ROOT:-$HOME/Library/Mobile Documents/com~apple~CloudDocs}"
clients_root="${MARKET_AGENT_CLIENTS_DIR:-$icloud_root/MarketAgent/Clients}"
[[ -d "$icloud_root" ]] || { echo "iCloud Drive est introuvable : $icloud_root" >&2; exit 1; }
target="$clients_root/$slug"
if [[ -e "$target" ]]; then
  echo "Le dossier existe déjà : $target" >&2
  exit 1
fi
mkdir -p "$target/contexte" "$target/travail" "$target/livrables"
cp "$repo_root/templates/client/AGENTS.md" "$target/AGENTS.md"
cp "$repo_root/templates/client/memory.md" "$target/memory.md"
echo "Projet créé : $target"
echo "Remplir AGENTS.md avec la consultante, puis attendre la synchronisation iCloud avant de travailler sur l'autre Mac."
