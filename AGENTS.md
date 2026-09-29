# Consignes globales — consultante marketing

Ce fichier est partagé entre tous les projets clients. Les faits propres à un client vont dans le `AGENTS.md` de son projet, jamais ici.

## Façon de travailler

- Dans un projet client, commencer une mission substantielle par son `AGENTS.md` et son `memory.md`, puis consulter les sources utiles dans son dossier. Si l'un manque, le signaler sans inventer le contexte.
- Identifier le client et le livrable avant de produire. Ne jamais mélanger des données, exemples ou décisions de clients différents.
- Distinguer faits fournis par le client, observations sourcées, hypothèses et recommandations. Pour les données récentes, vérifier la source et la date.
- Demander seulement les informations qui changent réellement la décision ou le livrable ; avancer avec des hypothèses explicites pour le reste.
- Pour une recommandation importante, exposer le raisonnement, une alternative crédible, les risques et le critère de décision.
- Avant un livrable externe, contrôler chiffres, citations, droits des visuels, ton de marque, liens et contraintes du canal. Préparer un brouillon révisable.
- Ne pas publier, envoyer au client, modifier une campagne active ou engager un budget sans instruction explicite pour l'action concernée.
- Ne jamais placer de secrets ou identifiants dans les fichiers partagés. Stocker des données personnelles sensibles uniquement si le contrat l'autorise et si les protections nécessaires sont en place ; ne pas les résumer dans `memory.md`.

## Mémoire par client

- Lorsqu'un nouveau projet client est créé, utiliser les modèles `MarketAgent/Configuration/templates/client/AGENTS.md` et `memory.md` dans iCloud Drive, ou le script `MarketAgent/Configuration/scripts/new-client.sh`. Laisser les informations inconnues à compléter avec la consultante ; ne pas les fabriquer pour remplir le modèle.
- `memory.md` est le journal de bord du client : il permet de savoir où on en est et de répondre à « qu'est-ce qu'on a fait sur… ? ». Le lire au début de chaque tâche dans un projet client.
- Après chaque opération importante (livrable produit ou modifié, décision, correction de sa part, étape franchie, point bloquant), ajouter en haut du journal une entrée datée courte :
  ```
  ## AAAA-MM-JJ — sujet (statut : en cours / validé / en attente de …)
  - 2 à 5 puces : ce qui a été fait, décidé ou corrigé, où se trouve le résultat (lien Canva, Slides, Drive, chemin), prochaine étape.
  ```
- Pas d'entrée pour une simple question ou une exploration sans résultat. Ne pas réécrire les entrées passées ; corriger une erreur par une nouvelle entrée ou une mention `Corrigé le AAAA-MM-JJ`.
- Pour une question sur l'historique, répondre à partir du journal en citant les dates ; si le journal ne contient pas l'information, le dire plutôt que la reconstituer.
- Limite : 300 lignes. Au-delà de ~250, fusionner ou supprimer les entrées les plus anciennes ou les moins importantes, en gardant les décisions encore valables.
- Étiqueter `À vérifier` toute information non confirmée. Ne pas transformer une suggestion de l'IA en décision du client.
- Relire le fichier avant une modification si une autre session ou un autre Mac a pu le changer ; éviter les modifications simultanées sur les deux Macs. Une tâche planifiée n'écrit pas dans `memory.md` : elle dépose son résultat dans `travail/`.

## Sources externes du client

- La fiche client complète vit dans Notion, les fichiers dans Drive, les visuels dans Canva ; le `AGENTS.md` du client donne les liens. Ne pas relire ces sources à chaque tâche.
- Les relire seulement : au début d'une nouvelle mission ou d'un nouveau livrable, à la reprise d'un client dont la dernière entrée du journal date de plus de 14 jours, avant une recommandation stratégique, en cas de doute ou de contradiction avec `memory.md`, ou sur demande.
- Si une source liée est inaccessible (plugin non connecté sur ce Mac, droits manquants), le signaler et ne pas combler le manque par supposition.

## Skills et agents

- Les skills dans `~/.agents/skills/` sont des méthodes pour des tâches précises. Choisir le skill dont la description correspond au résultat demandé ; il peut aussi être appelé explicitement avec `$nom-du-skill`.
- Un « agent » est une session Codex qui utilise les consignes et outils disponibles. Commencer avec une seule session pour une mission. Employer des sous-agents seulement pour des travaux indépendants qui justifient leur coût et leur coordination ; le brief et la validation restent dans la session principale.
- Un skill n'accorde pas l'accès à Canva, Google Slides, GA4 ou aux comptes publicitaires : vérifier la connexion et les droits réels avant tout workflow qui en dépend.
- Si plusieurs skills s'enchaînent, transmettre un résultat explicite entre les étapes (sources et constats → brief validé → production → contrôle). Ne pas faire passer une hypothèse non vérifiée pour un fait dans l'étape suivante.

## Préférences personnelles — à remplir avec la consultante

- Langue et ton habituels : [À compléter]
- Types de clients et prestations prioritaires : [À compléter]
- Formats de livrables préférés : [À compléter]
- Outils réellement utilisés et comptes disponibles : [À compléter]
- Critères de qualité et exemples approuvés : [À compléter]
- Actions qui exigent toujours sa validation : [À compléter]
