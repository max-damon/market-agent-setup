# Market Agent Setup

Configuration Codex pour une consultante marketing indépendante : consignes globales, neuf skills et modèle de projet client. **GitHub sert uniquement de source pour la première installation.** Les fichiers actifs vivent dans **son iCloud Drive**, sur le Mac mini et le MacBook Air.

## Installation en une commande sur chaque Mac

Activer iCloud Drive et attendre qu'il apparaisse dans le Finder. Dans le Terminal du **Mac mini**, lancer :

```bash
curl -fsSLo /tmp/install-market-agent.sh https://raw.githubusercontent.com/max-damon/market-agent-setup/main/install.sh && bash /tmp/install-market-agent.sh
```

Le script télécharge temporairement le dépôt, copie sa configuration initiale dans `iCloud Drive/MarketAgent/Configuration`, crée `iCloud Drive/MarketAgent/Clients`, puis relie les consignes et skills aux emplacements lus par Codex. Il supprime son clone temporaire ; elle n'a aucun dépôt Git à gérer.

**Attendre ensuite** que `MarketAgent/Configuration` soit visible et téléchargé sur le **MacBook Air**, puis lancer exactement la même commande sur ce Mac. Le script détecte les fichiers iCloud existants et les utilise sans les remplacer. Ce lancement séquentiel évite de créer deux copies concurrentes pendant la première synchronisation.

Le script sauvegarde un éventuel `~/.codex/AGENTS.md` avant de le remplacer par un lien. S'il trouve déjà des skills personnels dans `~/.agents/skills` ou un `AGENTS.override.md`, il s'arrête avec un message explicite pour ne rien écraser. Installer l'application Codex et se connecter à son compte séparément : ce script installe la **configuration**, pas l'application ni les accès à Canva ou Google.

## Où sont les fichiers ?

```text
iCloud Drive/MarketAgent/
├── Configuration/
│   ├── AGENTS.md                   consignes communes, partie personnelle à remplir
│   ├── .agents/skills/             neuf skills marketing ; nouveaux skills ici
│   ├── templates/client/          modèles AGENTS.md et memory.md
│   ├── scripts/new-client.sh      crée un client directement dans iCloud
│   ├── install.sh                 rétablit les liens locaux si besoin
│   ├── README.md et LEARNING.md   guides de démarrage
│   ├── Next Step.md               feuille de route des futurs workflows
│   └── .market-agent-ready         témoin d'installation complète
└── Clients/
    └── nom-du-client/
        ├── AGENTS.md              contexte et règles du client
        ├── memory.md              décisions et enseignements durables
        ├── contexte/              documents de référence autorisés
        ├── travail/               recherches et brouillons
        └── livrables/             résultats validés

~/.codex/AGENTS.md  → iCloud Drive/MarketAgent/Configuration/AGENTS.md
~/.agents/skills    → iCloud Drive/MarketAgent/Configuration/.agents/skills
```

Les deux liens sont créés **localement sur chaque Mac**. Les vrais fichiers sont dans iCloud. Un nouveau `SKILL.md` placé dans `Configuration/.agents/skills/<nom>/` devient visible sur l'autre Mac après synchronisation iCloud ; ouvrir une nouvelle tâche Codex si nécessaire. Aucune opération Git n'est demandée à la consultante. [Découverte officielle des skills](https://learn.chatgpt.com/docs/build-skills).

## Créer un projet client

Depuis l'un ou l'autre Mac, après installation :

```bash
bash "$HOME/Library/Mobile Documents/com~apple~CloudDocs/MarketAgent/Configuration/scripts/new-client.sh" nom-du-client
```

Le script crée le dossier client **dans iCloud Drive**, avec `AGENTS.md`, `memory.md` et les trois sous-dossiers. Remplir `AGENTS.md` avec la consultante : faits stables, liens vers la fiche Notion, le dossier Drive et le dossier Canva, circuit de validation. Codex tient `memory.md` comme un journal de bord : une entrée datée de quelques lignes après chaque opération importante, pour savoir où on en est et pouvoir demander « qu'est-ce qu'on a fait sur… ? ».

Dans Codex, ajouter ce dossier client comme **projet local** et le choisir comme dossier principal, sur chaque Mac. Chaque client a son propre dossier principal pour éviter que Codex mélange les contextes. [Documentation des projets locaux](https://learn.chatgpt.com/docs/projects).

## Utiliser les agents et skills

Une tâche Codex est l'agent principal. Elle peut demander « Prépare une étude du marché », « Construis un brief de campagne » ou « Relis cette présentation » : la description de chaque skill permet de sélectionner la méthode. Elle peut aussi l'appeler explicitement avec `$market-research`, `$campaign-brief` ou `$marketing-review`.

Pour une mission complète : recherche sourcée → profil d'audience → brief validé → calendrier ou contenus → contrôle → validation humaine. Chaque étape transmet un résultat vérifiable à la suivante. Les sous-agents sont réservés aux travaux réellement indépendants ; la session principale reste responsable du brief et de la synthèse.

Un skill décrit la méthode. Créer ou modifier un document Google Slides, un design Canva ou une campagne nécessite une connexion disponible et des droits réels. Le guide [LEARNING.md](LEARNING.md) donne le parcours d'adoption ; [Next Step.md](Next%20Step.md) détaille les workflows à construire avec elle.

## Synchronisation et limites

- Modifier les fichiers **dans iCloud Drive** ; laisser iCloud terminer la synchronisation avant de changer de Mac. Ne pas éditer le même `AGENTS.md` ou `memory.md` sur deux Macs en même temps. [Gestion des conflits iCloud par Apple](https://support.apple.com/en-qa/guide/mac-help/mh40780/mac).
- Garder le dossier `MarketAgent` téléchargé sur les deux Macs pour travailler hors ligne et éviter qu'un fichier ne soit indisponible au début d'une tâche.
- iCloud synchronise aussi les suppressions. Garder une sauvegarde indépendante, par exemple Time Machine.
- Les conversations Codex, connexions, jetons et `~/.codex/config.toml` restent propres à chaque Mac. Pour reprendre exactement une conversation du Mac mini depuis le portable, utiliser une connexion distante vers ce Mac si elle est disponible.
- Vérifier que les contrats des clients autorisent **iCloud Drive** avant d'y déposer leurs documents. Sinon, ne placer dans le projet que les règles et références autorisées, sans copier les données interdites.
