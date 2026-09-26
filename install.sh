#!/usr/bin/env bash
set -euo pipefail

source_url="${MARKET_AGENT_SOURCE_URL:-https://github.com/max-damon/market-agent-setup.git}"
icloud_root="${MARKET_AGENT_ICLOUD_ROOT:-$HOME/Library/Mobile Documents/com~apple~CloudDocs}"
shared_root="$icloud_root/MarketAgent"
config_root="$shared_root/Configuration"
clients_root="$shared_root/Clients"
codex_home="${CODEX_HOME:-$HOME/.codex}"
skill_home="$HOME/.agents/skills"

if [[ "$(uname -s)" != Darwin && "${MARKET_AGENT_TEST_MODE:-0}" != 1 ]]; then
  echo "Ce programme d'installation est destiné à macOS." >&2
  exit 1
fi
if [[ ! -d "$icloud_root" ]]; then
  echo "iCloud Drive est introuvable : $icloud_root. L'activer et attendre son apparition dans le Finder avant de relancer." >&2
  exit 1
fi
if [[ -e "$codex_home/AGENTS.override.md" ]]; then
  echo "AGENTS.override.md existe dans $codex_home et masquerait les consignes globales. Résoudre ce conflit avant de relancer." >&2
  exit 1
fi
if [[ -e "$skill_home" || -L "$skill_home" ]]; then
  if [[ -L "$skill_home" ]]; then
    if [[ "$(readlink "$skill_home")" != "$config_root/.agents/skills" ]]; then
      echo "$skill_home pointe déjà ailleurs. Installation arrêtée sans le remplacer." >&2
      exit 1
    fi
  elif [[ -n "$(ls -A "$skill_home")" ]]; then
    echo "$skill_home contient déjà des skills. Les examiner et les déplacer dans $config_root/.agents/skills avant de relancer ; aucun fichier n'a été remplacé." >&2
    exit 1
  fi
fi

if [[ ! -e "$config_root" ]]; then
  command -v git >/dev/null || { echo "Git est nécessaire pour télécharger la configuration initiale." >&2; exit 1; }
  download_dir="$(mktemp -d)"
  staging_dir=""
  cleanup() {
    [[ ! -d "$download_dir" ]] || rm -r "$download_dir"
    [[ -z "$staging_dir" || ! -d "$staging_dir" ]] || rm -r "$staging_dir"
  }
  trap cleanup EXIT
  git clone --depth 1 "$source_url" "$download_dir/source"
  [[ -f "$download_dir/source/AGENTS.md" && -d "$download_dir/source/.agents/skills" ]] || {
    echo "Le dépôt téléchargé ne contient pas la configuration attendue." >&2
    exit 1
  }
  mkdir -p "$shared_root"
  staging_dir="$(mktemp -d "$shared_root/.configuration.XXXXXX")"
  cp "$download_dir/source/AGENTS.md" "$download_dir/source/README.md" "$download_dir/source/LEARNING.md" "$download_dir/source/Next Step.md" "$download_dir/source/memory.md" "$download_dir/source/install.sh" "$staging_dir/"
  cp -R "$download_dir/source/.agents" "$download_dir/source/templates" "$download_dir/source/scripts" "$staging_dir/"
  printf '%s\n' 'Configuration initiale issue de market-agent-setup ; modifier désormais les fichiers dans iCloud Drive.' > "$staging_dir/.market-agent-ready"
  if [[ -e "$config_root" ]]; then
    echo "Une configuration est apparue pendant l'installation. Attendre la synchronisation iCloud, puis relancer." >&2
    exit 1
  fi
  staging_name="$(basename "$staging_dir")"
  mv -n "$staging_dir" "$config_root"
  if [[ -d "$config_root/$staging_name" ]]; then
    rm -r "$config_root/$staging_name"
    echo "Une configuration est apparue pendant l'installation. Attendre la synchronisation iCloud, puis relancer." >&2
    exit 1
  fi
  if [[ -d "$staging_dir" ]]; then
    echo "Une configuration est apparue pendant l'installation. Attendre la synchronisation iCloud, puis relancer." >&2
    exit 1
  fi
  echo "Configuration copiée dans iCloud Drive : $config_root"
else
  echo "Configuration iCloud existante détectée ; elle est conservée."
fi

[[ -f "$config_root/.market-agent-ready" && -s "$config_root/AGENTS.md" && -s "$config_root/templates/client/AGENTS.md" ]] || {
  echo "La configuration iCloud est incomplète. Attendre la fin de la synchronisation avant de relancer." >&2
  exit 1
}
[[ -d "$config_root/.agents/skills" ]] || { echo "Dossier de skills absent dans iCloud." >&2; exit 1; }
skill_count=0
for skill in "$config_root/.agents/skills"/*/; do
  [[ -d "$skill" ]] || continue
  [[ -s "${skill}SKILL.md" ]] || { echo "SKILL.md manquant ou vide : $skill" >&2; exit 1; }
  head -n 1 "${skill}SKILL.md" >/dev/null || { echo "Skill indisponible : $skill" >&2; exit 1; }
  skill_count=$((skill_count + 1))
done
[[ "$skill_count" -gt 0 ]] || { echo "Aucun skill trouvé dans iCloud." >&2; exit 1; }

mkdir -p "$clients_root" "$codex_home" "$HOME/.agents"
global_target="$codex_home/AGENTS.md"
if [[ -L "$global_target" && "$(readlink "$global_target")" == "$config_root/AGENTS.md" ]]; then
  :
elif [[ -e "$global_target" || -L "$global_target" ]]; then
  backup_dir="$codex_home/market-agent-backups/$(date +%Y%m%d-%H%M%S)-$$"
  mkdir -p "$backup_dir"
  mv "$global_target" "$backup_dir/AGENTS.md"
  ln -s "$config_root/AGENTS.md" "$global_target"
  echo "Ancien AGENTS.md sauvegardé dans $backup_dir"
else
  ln -s "$config_root/AGENTS.md" "$global_target"
fi

if [[ ! -L "$skill_home" ]]; then
  if [[ -d "$skill_home" ]]; then rmdir "$skill_home"; fi
  ln -s "$config_root/.agents/skills" "$skill_home"
fi

echo "Installation terminée : $skill_count skills et consignes globales reliés à iCloud Drive."
echo "Dossiers clients : $clients_root"
echo "Ouvrir une nouvelle tâche Codex pour charger les consignes et skills."
