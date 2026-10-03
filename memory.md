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
- Les futures évolutions du dépôt source ne rejoignent pas automatiquement la configuration iCloud déjà installée. La procédure de mise à jour avec diff et sauvegarde est un chantier ouvert, décrit dans `Next Step.md`.

## Vérifications

- 2026-09-26 : les neuf skills ont passé la validation de frontmatter. Installation sur deux domiciles simulant deux Macs, relance idempotente, sauvegarde de l'ancien `AGENTS.md`, arrêt sur conflits et création d'un client vérifiés.
- 2026-09-26 : `codex debug prompt-input` a découvert `editorial-calendar` via le lien symbolique du dossier utilisateur `~/.agents/skills`. La synchronisation iCloud réelle entre les deux Macs de la consultante reste à tester lors de l'installation.
- 2026-09-29 : `memory.md` client passé d'un état compact (100 lignes) à un journal de bord daté (entrée de 2 à 5 puces par opération importante, 300 lignes, élagage dès ~250), sur le modèle du setup personnel de Maks. Fiche client complète dans Notion ; `AGENTS.md` client = faits stables + liens Notion/Drive/Canva, relus seulement sur déclencheurs. Tâches planifiées : écrivent dans `travail/`, jamais dans `memory.md`. Non commité, non déployé dans iCloud.
- 2026-10-03 : ajout de 13 skills Instagram `ig-*`, adaptés en français depuis Jakeschincariol/instagram-agent-skill (MIT, `LICENSE` dans chaque dossier). Fichiers relatifs au projet ouvert : voix dans `contexte/voix-instagram.md` (modèle `templates/instagram/`), journal, plan et swipe file dans `travail/instagram/`. Scripts Python sans dépendance, listes de mots et regex françaises ; lexique anglais conservé en `ig-human/slop-en.json`. Seuils hérités de la version anglaise, non recalibrés sur du français. Descriptions de `editorial-calendar`, `content-repurposing` et `performance-review` renvoient vers les `ig-*` pour Instagram seul.
