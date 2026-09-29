# Apprendre à travailler avec Codex pour une activité de conseil marketing

Ce guide reprend le cadrage initial et l'adapte au choix final : **iCloud Drive synchronise les fichiers entre le Mac mini et le MacBook Air**. GitHub fournit seulement les fichiers de départ à l'installateur ; la consultante n'aura pas à cloner, committer ou pousser.

## 1. Ce que le système doit améliorer

Un projet par client permet de retrouver rapidement son brief, son ton et ses décisions. Les skills donnent une méthode répétable pour la recherche, les campagnes, le contenu, la mesure et la présentation. Le gain attendu porte sur le temps perdu à répéter le contexte, les allers-retours de correction et la cohérence des livrables.

Ne pas annoncer un pourcentage de productivité avant le test. Mesurer le **temps jusqu'au livrable accepté**, en incluant recherche, production, relecture, corrections et entretien de la configuration.

## 2. Préparer les deux Macs

1. Utiliser **son propre compte ChatGPT** et vérifier l'accès à Codex dans son offre. Tarifs et limites peuvent changer : consulter la [documentation officielle](https://learn.chatgpt.com/docs/pricing).
2. Installer l'application Codex et se connecter sur chaque Mac. Se connecter aussi séparément aux services qu'elle utilisera, selon leurs droits.
3. Activer **iCloud Drive avec le même compte Apple** sur les deux Macs. Vérifier que son dossier est visible dans le Finder. Prévoir assez d'espace local et iCloud pour les projets clients.
4. Sur le **Mac mini**, exécuter la commande unique du [README](README.md). L'installateur télécharge le dépôt dans un dossier temporaire, copie la configuration dans iCloud et crée les liens locaux. Il ne garde pas de clone Git sur son Mac.
5. Attendre la présence de `MarketAgent/Configuration/.market-agent-ready` et des fichiers dans iCloud sur le **MacBook Air**, puis y lancer la **même commande**. L'installateur se relie aux fichiers déjà synchronisés.
6. Ouvrir une nouvelle tâche Codex sur chaque Mac et demander « Quels fichiers de consignes et skills marketing sont chargés ? ». Essayer ensuite `$editorial-calendar` sur un client fictif. Codex charge les `AGENTS.md` au démarrage de la tâche. [Documentation officielle AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skills](https://learn.chatgpt.com/docs/build-skills).

**Test de synchronisation :** modifier une phrase de test dans `Configuration/AGENTS.md` sur le Mac mini, attendre qu'elle apparaisse sur le MacBook Air, puis ouvrir une nouvelle tâche sur celui-ci. Ajouter un skill de test dans `Configuration/.agents/skills/`, attendre sa présence sur l'autre Mac et vérifier qu'il peut être appelé. Supprimer ensuite le skill de test.

## 3. Comprendre la structure

```text
iCloud Drive/MarketAgent/
├── Configuration/          AGENTS.md global, skills, modèles et guides
└── Clients/
    └── client-pilote/      un dossier principal Codex par client
        ├── AGENTS.md       faits et règles stables du client
        ├── memory.md       décisions et apprentissages validés
        ├── contexte/       documents de référence autorisés
        ├── travail/        recherches et brouillons
        └── livrables/      documents destinés au client
```

Le `AGENTS.md` global, relié à `~/.codex/AGENTS.md` sur chaque Mac, contient les principes communs et une section personnelle à remplir avec elle. Le `AGENTS.md` de chaque client précise offre, audience, ton, canaux, contraintes, preuves et validation. Les documents longs vont dans `contexte/` ; les décisions durables vont dans `memory.md`. Codex lit les consignes globales puis celles du projet ouvert. [Documentation officielle](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## 4. Créer un client pilote

1. Choisir un client dont le contrat autorise les données nécessaires dans iCloud Drive. Choisir deux livrables récurrents et un exemple validé de chacun.
2. Lancer `scripts/new-client.sh` comme indiqué dans le [README](README.md). Le dossier et les fichiers de départ sont créés directement dans iCloud.
3. Remplir avec elle le `AGENTS.md` client uniquement avec des faits confirmés. Placer les briefs et exemples approuvés dans `contexte/` si leur stockage est autorisé.
4. Dans Codex, ajouter le dossier du client comme **projet local** et le choisir comme dossier principal sur chaque Mac. Demander d'abord : « Résume ce que tu sais du client, cite les fichiers utilisés et distingue ce qui manque ». Corriger les erreurs avant de produire un livrable.
5. Créer une nouvelle tâche par résultat distinct : audit, campagne, calendrier ou présentation. Cette séparation facilite la reprise sans mélanger les objectifs.

## 5. Faire vivre `memory.md` sans le remplir de bruit

Le fichier `memory.md` est une mémoire **explicite par client**. C'est le journal de bord du client : Codex le lit au début de chaque tâche et ajoute, après chaque opération importante, une entrée datée de 2 à 5 puces (ce qui a été fait, décidé ou corrigé, où est le résultat, prochaine étape). Elle peut l'interroger : « Qu'est-ce qu'on a fait sur la stratégie Instagram ? ». Limite 300 lignes, élaguée au-delà de ~250 ; les hypothèses restent marquées « À vérifier ». Ne jamais y placer de mots de passe ou de données personnelles sensibles.

La [mémoire native de Codex](https://learn.chatgpt.com/docs/customization/memories) et les conversations ne sont pas ces fichiers. Elles restent liées à l'installation qui exécute la tâche. Si elle veut reprendre **exactement la même conversation** du Mac mini sur le MacBook Air, envisager l'[accès distant au Mac mini](https://learn.chatgpt.com/docs/remote-connections) ; les fichiers du client, eux, seront visibles localement sur les deux Macs grâce à iCloud.

## 6. Utiliser la banque de skills

Neuf skills répondent à des demandes précises : marché, audience, concurrence, brief de campagne, calendrier éditorial, déclinaison de contenu, revue de performance, contrôle marketing et présentation client. Codex peut en choisir un d'après sa description ; l'appel explicite `$nom-du-skill` reste possible. [Documentation officielle des skills](https://learn.chatgpt.com/docs/build-skills).

Deux enchaînements utiles :

```text
Nouvelle campagne :
$market-research → $audience-insights → $campaign-brief
→ validation humaine → $editorial-calendar → $content-repurposing
→ $marketing-review

Fin de mois :
export de données → $performance-review → $client-presentation
→ $marketing-review → validation humaine
```

Chaque flèche désigne un **résultat transmis** à l'étape suivante. Une hypothèse de recherche ne devient pas automatiquement un fait dans le brief. Ces séquences s'inspirent notamment des exemples publics de Rebecca Rae pour [la production de contenus](https://github.com/thatrebeccarae/claude-marketing/blob/main/examples/content-production.md) et [l'audit client vers une présentation](https://github.com/thatrebeccarae/claude-marketing/blob/main/examples/dtc-account-audit.md).

## 7. Connecter les outils après le workflow manuel

Le skill `$client-presentation` peut préparer une trame exploitable sans connexion externe. La création d'un vrai Google Slides ou design Canva dépend d'un outil connecté, de droits appropriés et d'un contrôle du rendu. Commencer par lire un document autorisé, puis créer une copie ou un brouillon. Les [capacités Canva MCP](https://www.canva.dev/docs/apps/mcp/) ne sont pas automatiquement installées par ce dépôt.

Pour GA4, Meta Ads ou Google Ads, un export CSV suffit pour tester le skill `$performance-review`. Passer ensuite à une connexion en lecture si le besoin est régulier. Garder une validation humaine avant publication, envoi ou changement de budget.

Les automatisations planifiées viendront après le pilote : par exemple un brouillon hebdomadaire de veille concurrentielle sourcée. Une tâche doit signaler l'absence de données au lieu d'inventer un bilan. [Documentation des automatisations](https://learn.chatgpt.com/docs/automations).

## 8. Formuler une demande complète

> « Dans le projet [client], prépare [livrable] pour [public]. Utilise [sources], distingue faits confirmés et hypothèses, respecte [contraintes de ton, canal, longueur, échéance]. Livre [format]. Pose seulement les questions qui changeraient la recommandation ; sinon avance en indiquant tes hypothèses. Termine par les points à vérifier avant envoi. »

Après correction, faire entrer dans `memory.md` seulement une préférence ou décision **validée et réutilisable**.

## 9. Mesurer et sécuriser la synchronisation

Tester trois tâches comparables avant et après le setup pendant deux semaines. Noter temps de brief, recherche, production, relecture, corrections, erreurs et entretien du système. Conserver les workflows qui raccourcissent le temps total sans dégrader la qualité.

iCloud synchronise également les erreurs et suppressions : prévoir Time Machine ou une autre sauvegarde indépendante. Laisser une modification arriver sur l'autre Mac avant de reprendre `AGENTS.md` ou `memory.md`, et éviter les éditions simultanées. [Gestion des conflits iCloud par Apple](https://support.apple.com/en-qa/guide/mac-help/mh40780/mac). Les connexions, jetons, paramètres locaux et conversations Codex restent propres à chaque Mac ; seules les données placées dans `MarketAgent` sont synchronisées ici.
