#!/usr/bin/env bash
set -euo pipefail

slug="${1:-}"
if [[ ! "$slug" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "Usage : bash scripts/new-client.sh nom-du-client (lettres minuscules, chiffres, tirets)" >&2
  exit 2
fi
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
clients_root="${MARKET_AGENT_CLIENTS_DIR:-$HOME/Clients}"
target="$clients_root/$slug"
if [[ -e "$target" ]]; then
  echo "Le dossier existe déjà : $target" >&2
  exit 1
fi
mkdir -p "$target/contexte" "$target/travail" "$target/livrables"
touch "$target/contexte/.gitkeep" "$target/travail/.gitkeep" "$target/livrables/.gitkeep"
cp "$repo_root/templates/client/AGENTS.md" "$target/AGENTS.md"
cp "$repo_root/templates/client/memory.md" "$target/memory.md"
cat > "$target/.gitignore" <<'EOF'
.DS_Store
.env
.env.*
!.env.example
*.pem
*.key
credentials.json
auth.json
.codex/
EOF
git -C "$target" init -q
echo "Projet créé : $target"
echo "Remplir AGENTS.md, puis vérifier les documents et leur autorisation de stockage avant tout commit ou publication."
echo "Créer ensuite un dépôt GitHub privé distinct pour ce client et le cloner sur l'autre Mac."
