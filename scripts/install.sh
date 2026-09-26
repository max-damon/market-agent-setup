#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
user_skills="$HOME/.agents/skills"
source_skills="$repo_root/.agents/skills"

[[ -f "$repo_root/AGENTS.md" ]] || { echo "AGENTS.md introuvable dans le dépôt" >&2; exit 1; }
[[ -d "$source_skills" ]] || { echo "Dossier de skills introuvable" >&2; exit 1; }
if [[ -e "$codex_home/AGENTS.override.md" ]]; then
  echo "AGENTS.override.md existe dans $codex_home : il masquerait les consignes globales. Résoudre ce conflit avant l'installation." >&2
  exit 1
fi
if [[ -L "$user_skills" ]]; then
  echo "$user_skills est déjà un lien symbolique. Vérifier son origine avant l'installation." >&2
  exit 1
fi

# Préparer toutes les vérifications avant de modifier l'installation locale.
for skill in "$source_skills"/*/; do
  [[ -d "$skill" ]] || continue
  [[ -f "${skill}SKILL.md" ]] || { echo "SKILL.md manquant : $skill" >&2; exit 1; }
  name="$(basename "$skill")"
  target="$user_skills/$name"
  if [[ -e "$target" || -L "$target" ]]; then
    if [[ -L "$target" && "$(readlink "$target")" == "${skill%/}" ]]; then
      continue
    fi
    echo "Skill déjà présent à $target ; installation arrêtée sans le remplacer." >&2
    exit 1
  fi
done

mkdir -p "$codex_home" "$user_skills"
global_target="$codex_home/AGENTS.md"
if [[ -e "$global_target" || -L "$global_target" ]]; then
  if [[ -L "$global_target" && "$(readlink "$global_target")" == "$repo_root/AGENTS.md" ]]; then
    echo "Consignes globales déjà reliées au dépôt."
  else
    backup_dir="$codex_home/market-agent-backups/$(date +%Y%m%d-%H%M%S)-$$"
    mkdir -p "$backup_dir"
    mv "$global_target" "$backup_dir/AGENTS.md"
    ln -s "$repo_root/AGENTS.md" "$global_target"
    echo "Ancien AGENTS.md conservé dans $backup_dir"
  fi
else
  ln -s "$repo_root/AGENTS.md" "$global_target"
fi

count=0
for skill in "$source_skills"/*/; do
  [[ -d "$skill" ]] || continue
  name="$(basename "$skill")"
  target="$user_skills/$name"
  if [[ ! -e "$target" && ! -L "$target" ]]; then
    ln -s "${skill%/}" "$target"
    count=$((count + 1))
  fi
done

echo "Installation terminée : AGENTS.md global et $count nouveau(x) skill(s) relié(s)."
echo "Ouvrir une nouvelle tâche Codex pour charger les consignes."
echo "Sur l'autre Mac : cloner ce dépôt et lancer aussi scripts/install.sh."
