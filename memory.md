# État durable du projet de configuration

## Architecture

- Ce dépôt GitHub sert de source initiale pour `install.sh`. Le script le clone temporairement et copie les fichiers actifs dans `iCloud Drive/MarketAgent/Configuration`, sans laisser de dépôt Git à la consultante.
- Le Mac mini et le MacBook Air utilisent le même iCloud Drive. Sur chacun, `~/.codex/AGENTS.md` et `~/.agents/skills` pointent vers les fichiers iCloud. Les nouveaux skills deviennent visibles sur les deux Macs après synchronisation et nouvelle tâche Codex si nécessaire.
- Chaque client possède un dossier distinct dans `iCloud Drive/MarketAgent/Clients`, avec `AGENTS.md`, `memory.md`, `contexte/`, `travail/` et `livrables/`. Aucun client réel n'est présent dans le dépôt source.

## Règles de maintenance

- Garder des descriptions de skills distinctes et précises pour l'invocation implicite ; vérifier leur frontmatter après modification.
- Ne pas placer de secrets, jetons ou documents clients dans le dépôt source. Vérifier que le contrat client autorise iCloud avant d'y stocker ses documents.
- Les changements de `AGENTS.md` prennent effet dans une nouvelle tâche Codex. Les connexions, conversations et configurations locales restent propres à chaque Mac.
- Une publication, un envoi client ou une dépense exige une instruction explicite ; les skills produisent d'abord des brouillons contrôlables.

## Vérifications

- 2026-09-26 : les neuf skills ont passé la validation de frontmatter. Installation sur deux domiciles simulant deux Macs, relance idempotente, sauvegarde de l'ancien `AGENTS.md`, arrêt sur conflits et création d'un client vérifiés.
- 2026-09-26 : `codex debug prompt-input` a découvert `editorial-calendar` via le lien symbolique du dossier utilisateur `~/.agents/skills`. La synchronisation iCloud réelle entre les deux Macs de la consultante reste à tester lors de l'installation.
