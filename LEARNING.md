# Apprendre à travailler avec Codex pour une activité de conseil marketing

Ce guide reprend et actualise le document de cadrage rédigé avant la création de ce dépôt. Il sert de parcours pas à pas pour la consultante et pour la personne qui prépare son installation.

## 1. Décision et bénéfice attendu

**Oui, le setup est adapté** si les mêmes types de missions reviennent pour plusieurs clients : recherche, planification, contenus, présentation et reporting. Un projet local par client évite de répéter son contexte et limite les confusions. Les skills rendent les méthodes de travail réutilisables ; la mémoire par projet conserve les décisions validées.

La valeur attendue est moins de temps à reconstituer un brief, moins d'allers-retours sur la structure d'un livrable et plus de cohérence entre ses productions. Aucun pourcentage de productivité n'est garanti. Mesurer le **temps réel jusqu'au livrable accepté**, incluant recherche, relecture, corrections et entretien de la configuration.

## 2. Architecture retenue pour deux Macs

```text
GitHub : market-agent-setup (ce dépôt)
  ├── AGENTS.md global
  ├── .agents/skills/ communs
  └── templates/client/

Mac mini et MacBook Air
  ├── ~/market-agent-setup/ (clone du dépôt commun)
  ├── ~/.codex/AGENTS.md → lien vers le clone local
  ├── ~/.agents/skills/<skill> → liens vers le clone local
  └── ~/Clients/<client>/ (un projet et un dépôt privé par client)
       ├── AGENTS.md
       ├── memory.md
       ├── contexte/
       ├── travail/
       └── livrables/
```

Les fichiers versionnés ne changent sur l'autre Mac qu'après **commit + push** sur le premier et **pull** sur le second. Cela donne un historique contrôlable et un retour arrière possible. Git ne synchronise ni les conversations Codex, ni les connexions aux services, ni les jetons, ni le fichier local `~/.codex/config.toml`. Se connecter à Codex et aux outils requis sur chaque Mac. Ne pas modifier le même fichier client sur les deux Macs avant synchronisation.

**Décision sur les données clients :** un dépôt privé n'autorise pas automatiquement le dépôt de fichiers confidentiels. Vérifier chaque contrat et les droits du compte GitHub ; garder ailleurs les données dont le stockage n'est pas permis. Un dépôt client peut contenir seulement ses règles, décisions non sensibles et livrables autorisés.

## 3. Installer la configuration commune

1. Créer ou utiliser **son propre compte ChatGPT** et vérifier l'accès à Codex dans son offre actuelle. Les tarifs et limites évoluent ; consulter la [documentation officielle](https://learn.chatgpt.com/docs/pricing) au moment de l'installation.
2. Installer l'application Codex sur les deux Macs et se connecter. La configuration éditoriale est indépendante du compte et de ses jetons.
3. Donner à son compte GitHub l'accès au dépôt privé `market-agent-setup`, puis exécuter sur chaque Mac la commande unique de la section « Installer » du [README](README.md).
4. Ouvrir une **nouvelle tâche** Codex pour vérifier que `AGENTS.md` global et les skills sont disponibles. Codex construit ses consignes au démarrage d'une tâche ; une tâche déjà ouverte peut conserver les anciennes règles. [Documentation officielle AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skills](https://learn.chatgpt.com/docs/build-skills).
5. Remplir avec elle la section « Préférences personnelles » du `AGENTS.md` global, puis committer et pousser cette modification après relecture. Récupérer la mise à jour sur l'autre Mac avec `scripts/update.sh`.

Le script installe **cette configuration**, pas l'application, l'abonnement ou les connexions Canva/Google. Il préserve l'ancien `AGENTS.md` dans une sauvegarde datée s'il en existe un.

## 4. Créer un client pilote

1. Choisir un client dont les documents sont autorisés dans le stockage retenu et deux livrables fréquents. Créer son dossier avec `scripts/new-client.sh`.
2. Remplir `AGENTS.md` avec les éléments **confirmés** : offre, cibles, positionnement, voix, canaux, contraintes, sources de vérité et circuit de validation. Ranger les documents de référence dans `contexte/` si leur stockage est permis.
3. Garder `memory.md` court. Codex le lit au début d'une tâche significative et le met à jour après une décision ou un enseignement durable. Une suggestion de l'IA ou une hypothèse non validée ne devient pas un fait client. Cette politique vient de `AGENTS.md` ; ce fichier n'est pas une mémoire native qui se remplit magiquement.
4. Ouvrir ce dossier comme **projet local Codex** sur le Mac utilisé. Commencer par « Résume ce que tu sais du client, cite les fichiers utilisés et distingue les manques ». Corriger les erreurs avant le premier livrable.
5. Quand le dossier est prêt, créer son dépôt GitHub privé distinct et le cloner sur l'autre Mac. Vérifier que les deux copies ont le même commit avant de changer de machine.

Un `AGENTS.md` par client évite de charger tous les clients dans les règles globales. Le nom exact est au pluriel et en majuscules : `AGENTS.md`. Codex charge les règles globales puis celles du projet. [Documentation officielle](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## 5. Utiliser la banque de skills

La banque initiale couvre neuf demandes reconnaissables : étude de marché, audience, concurrence, brief de campagne, calendrier éditorial, déclinaisons de contenus, revue de performance, contrôle marketing et présentation client. Chaque `SKILL.md` contient un déclencheur précis, une méthode, un résultat attendu et ses limites. Codex peut choisir le skill selon la demande ; la consultante peut aussi écrire son nom précédé de `$`.

Deux parcours utiles :

```text
Nouvelle campagne :
$market-research → $audience-insights → $campaign-brief
→ validation humaine → $editorial-calendar → $content-repurposing
→ $marketing-review

Fin de mois :
export de données → $performance-review → $client-presentation
→ $marketing-review → validation humaine
```

Les flèches sont des **transferts de résultats**, pas une commande magique. Pour chaque étape, indiquer à Codex quel brief ou fichier validé utiliser. Rebecca Rae documente des enchaînements comparables pour [la production de contenus](https://github.com/thatrebeccarae/claude-marketing/blob/main/examples/content-production.md) et [l'audit client vers une présentation](https://github.com/thatrebeccarae/claude-marketing/blob/main/examples/dtc-account-audit.md). La [bibliothèque de Corey Haines](https://github.com/coreyhaines31/marketingskills) illustre l'intérêt d'un contexte de marque commun à plusieurs skills.

## 6. Connecter des outils seulement quand le workflow le demande

Un skill peut préparer la structure d'un deck ou analyser un export CSV sans aucune connexion externe. Pour créer un vrai fichier Google Slides ou Canva, il faut un outil compatible, une authentification et les droits nécessaires. Tester d'abord lecture, puis création d'un **brouillon** et contrôle visuel avant partage. La [documentation OpenAI sur les skills](https://learn.chatgpt.com/docs/build-skills) distingue les instructions réutilisables des outils donnant accès aux services.

Le même principe vaut pour GA4, Meta Ads, Google Ads ou un CRM : commencer par un export ou une connexion en lecture, vérifier les indicateurs, puis envisager des actions d'écriture. Préparer des recommandations et garder la décision humaine sur une publication, un envoi ou une dépense.

### Présentations Google Slides et Canva

Si elle utilise déjà Google Workspace, commencer par un document ou une présentation **existante et autorisée**, vérifier la lecture, puis créer une copie de travail. Le skill `$client-presentation` structure le récit ; la création et la mise en page réelles dépendent d'une connexion Google Drive/Slides disponible dans son installation. Contrôler chaque diapositive avant partage.

Pour Canva, vérifier d'abord la présence d'une intégration utilisable sur son compte. La [documentation Canva sur MCP](https://www.canva.dev/docs/apps/mcp/) et son [API d'autoremplissage](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/) décrivent des possibilités, pas un accès automatiquement inclus dans ce dépôt. Garder une trame exportable en solution immédiate tant que l'intégration n'est pas validée.

### Mémoire native et accès distant

Le `memory.md` de chaque client est un fichier versionnable et relisible. La [mémoire native de Codex](https://learn.chatgpt.com/docs/customization/memories), les conversations, les caches et les connexions vivent dans l'environnement de l'installation ; Git ne les transforme pas en mémoire commune. Si elle veut reprendre **exactement la même conversation** depuis le MacBook Air, examiner l'[accès distant à son Mac mini](https://learn.chatgpt.com/docs/remote-connections). Pour une nouvelle tâche locale sur le MacBook Air, les fichiers Git synchronisés fournissent le contexte durable.

### Automatisations après le pilote

Un contrôle hebdomadaire pourrait préparer un brouillon de veille ou un bilan à partir de sources accessibles. Tester le workflow manuellement avant de le programmer ; une tâche planifiée locale dépend du Mac et de l'application qui l'exécutent. Toute automatisation doit indiquer ses sources, produire un résultat révisable et s'arrêter quand l'accès aux données manque. [Documentation des automatisations](https://learn.chatgpt.com/docs/automations).

## 7. Formuler une mission sans aller-retour inutile

Donner en une demande le client, l'objectif, les sources, le format et la validation attendue :

> « Dans le projet [client], prépare [livrable] pour [public]. Utilise [documents/liens], distingue faits confirmés et hypothèses, respecte [contraintes de ton, canal, longueur et échéance]. Livre [format précis]. Pose seulement les questions qui changeraient la recommandation ; sinon avance en indiquant tes hypothèses. Termine par les points à vérifier avant envoi. »

Pour une correction, demander un changement ciblé (« conserver l'argument, adapter le ton au public PME »). Après validation, conserver dans `memory.md` seulement la préférence ou la décision qui servira de nouveau.

## 8. Mesurer le pilote et décider de la suite

Sur deux semaines, comparer trois tâches similaires avant et après le setup. Noter pour chacune : temps de brief, recherche, production, relecture, corrections, erreurs détectées, temps de maintenance et avis de la consultante. Continuer si le temps total jusqu'au livrable accepté baisse sans hausse des erreurs. Ajouter ensuite seulement les skills ou connecteurs qui correspondent à ses prestations réelles.

Le premier objectif est un système **fiable et facile à reprendre sur les deux Macs**. Les sous-agents, automatisations programmées et créations directes dans Canva ou Slides viennent après validation des workflows manuels.
