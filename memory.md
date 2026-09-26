# État durable du projet de configuration

## Architecture

- Ce dépôt porte les consignes globales, neuf skills marketing et les modèles de projet client. Aucun client réel ni secret n'y est stocké.
- Chaque client doit avoir un projet local Codex et un dépôt privé distinct si ses fichiers peuvent être hébergés sur GitHub. Le modèle fournit `AGENTS.md` et `memory.md` à remplir avec des faits validés.
- Sur chaque Mac, `scripts/install.sh` relie `AGENTS.md` et les dossiers des skills au clone local. `scripts/update.sh` récupère les commits distants puis relie les nouveaux skills. Le transfert exige commit/push sur un Mac, puis pull sur l'autre.

## Règles de maintenance

- Garder des descriptions de skills distinctes et précises pour l'invocation implicite ; vérifier leur frontmatter après modification.
- Ne pas intégrer automatiquement de données client, d'identifiants, de `config.toml` local ou de mémoire native Codex au dépôt commun.
- Les changements de `AGENTS.md` prennent effet dans une nouvelle tâche Codex.
- Une publication, un envoi client ou une dépense exige une instruction explicite ; les skills produisent d'abord des brouillons contrôlables.

## Vérifications effectuées

- 2026-09-26 : syntaxe Bash et frontmatter YAML contrôlés ; installation idempotente et sauvegarde du `AGENTS.md` existant testées dans un dossier personnel isolé.
- 2026-09-26 : création d'un projet client et cycle push/pull entre deux clones temporaires testés. Les connexions réelles aux comptes de la consultante restent à faire sur ses Macs.
