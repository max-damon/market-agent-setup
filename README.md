# Market Agent Setup

Configuration Codex pour une consultante marketing indépendante : consignes globales, banque de skills et modèle de projet client. Ce dépôt contient **la configuration commune**, sans données de client. Chaque client aura son propre dossier et, si la synchronisation Git est retenue, son propre dépôt GitHub privé.

## Structure

```text
market-agent-setup/
├── AGENTS.md                 consignes globales à personnaliser
├── memory.md                 état durable de cette configuration
├── .agents/skills/           banque de skills activés selon la tâche
├── templates/client/        AGENTS.md et memory.md de départ
├── scripts/install.sh       relie les consignes et skills au Mac
├── scripts/update.sh        récupère les nouveautés GitHub sans fusion forcée
├── scripts/new-client.sh    crée un dossier client local à partir du modèle
└── LEARNING.md              guide de choix et de mise en place
```

`AGENTS.md` est le nom exact que Codex reconnaît. Une modification des consignes exige une nouvelle tâche Codex pour être prise en compte. Les skills ont chacun un nom et une description distincts : Codex peut les choisir selon la demande, ou elle peut les appeler explicitement, par exemple `$editorial-calendar`.

## Installer sur chacun des deux Macs

Prérequis : accès à ce dépôt GitHub depuis **son propre compte** et Git installé. Le dépôt doit rester privé si la configuration contient des préférences non publiques. Installer l'application Codex et s'y connecter séparément ; le script ne gère ni abonnement ni authentification.

Depuis le Terminal du Mac mini, puis du MacBook Air :

```bash
git clone https://github.com/max-damon/market-agent-setup.git "$HOME/market-agent-setup" && bash "$HOME/market-agent-setup/scripts/install.sh"
```

Si le dépôt est déjà cloné, lancer seulement `bash "$HOME/market-agent-setup/scripts/install.sh"`. Le script relie `~/.codex/AGENTS.md` et chaque skill dans `~/.agents/skills/` au dépôt. Il garde une copie datée d'un éventuel `AGENTS.md` global déjà présent ; il s'arrête si un skill portant le même nom existe déjà ou si un `AGENTS.override.md` masque les règles. Il ne touche pas à `config.toml`, aux identifiants et aux autres skills.

**Contrôle :** ouvrir une nouvelle tâche Codex et demander « Quels fichiers de consignes utilises-tu ? Quels skills marketing vois-tu ? ». Pour un test plus direct, demander « Utilise `$editorial-calendar` pour proposer trois sujets fictifs ».

## Modifier et synchroniser les deux Macs

Git **ne synchronise pas automatiquement** les modifications locales. Après avoir modifié une règle ou un skill, relire le diff et vérifier l'absence de données sensibles, puis committer et pousser depuis le Mac utilisé :

```bash
cd "$HOME/market-agent-setup"
git status --short
git diff --check
git add AGENTS.md memory.md .agents/skills README.md LEARNING.md scripts templates .gitignore
git diff --cached --check
git diff --cached
git commit -m "Mettre à jour la configuration marketing"
git push
```

Sur l'autre Mac, lancer :

```bash
bash "$HOME/market-agent-setup/scripts/update.sh"
```

Le script refuse d'écraser des modifications locales, effectue un `git pull --ff-only` et relie les nouveaux skills. Une nouvelle tâche Codex prend ensuite les règles à jour. Si les deux Macs ont modifié le même dépôt avant synchronisation, résoudre le conflit explicitement avant de poursuivre. Une modification de skill sur un Mac ne sera visible sur l'autre **qu'après push puis pull** ; Git apporte l'historique, pas la synchronisation instantanée.

## Créer le premier projet client

Une fois le nom choisi, sur un Mac :

```bash
bash "$HOME/market-agent-setup/scripts/new-client.sh" nom-du-client
```

Cela crée `~/Clients/nom-du-client/` avec `AGENTS.md`, `memory.md`, `contexte/`, `travail/`, `livrables/` et un dépôt Git local. Remplir d'abord le contexte avec la consultante ; seuls les **faits confirmés** entrent dans `AGENTS.md`. `memory.md` se remplit au fil des décisions et retours validés, selon la règle globale. Les documents de référence vont dans `contexte/`.

Pour le retrouver sur les deux Macs, créer **un dépôt GitHub privé distinct par client** après vérification des clauses du contrat et des fichiers à versionner. Pousser depuis le premier Mac, cloner depuis le second. Les fichiers volumineux ou confidentiels dont le stockage GitHub n'est pas autorisé restent dans l'outil client approuvé ; `AGENTS.md` peut pointer vers leur emplacement sans copier leur contenu.

Dans Codex, ouvrir le dossier du client comme projet local. Vérifier qu'une nouvelle tâche lit bien les consignes globales, le `AGENTS.md` du client et son `memory.md`, sans information d'un autre client. Les autres dossiers clients doivent rester hors du dossier principal de ce projet.

## Comment utiliser les agents et les skills

Une tâche Codex est l'agent principal. Elle peut demander directement « Prépare une étude du marché de X », « Construis un brief de campagne » ou « Relis ce livrable » : la description du skill aide Codex à sélectionner la méthode. Elle peut forcer un skill avec `$market-research`, `$campaign-brief` ou `$marketing-review`.

Pour un travail en plusieurs étapes, utiliser des résultats vérifiables :

```text
recherche sourcée → profil d'audience → brief de campagne validé
→ calendrier ou contenus → contrôle qualité → validation humaine
```

Des sous-agents spécialisés ne sont utiles que si plusieurs recherches indépendantes peuvent avancer en parallèle. Ils ne remplacent pas un brief clair, les sources du client ou sa validation. Le rôle d'un skill est de décrire la méthode ; l'accès à Google Slides, Canva, GA4 ou un compte publicitaire nécessite une connexion et des droits vérifiés séparément.

## Avant d'élargir la configuration

Tester un client et deux livrables récurrents pendant deux semaines. Mesurer le temps jusqu'au livrable accepté, les corrections et les erreurs, en comptant le temps passé à entretenir les fichiers. Ajouter un skill ou une intégration seulement quand un besoin répétitif est observé.
