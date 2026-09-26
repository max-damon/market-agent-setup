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
- Ne jamais enregistrer de secrets, identifiants ou données personnelles sensibles dans Git, les skills ou `memory.md`.

## Mémoire par client

- Lorsqu'un nouveau projet client est créé, partir de `templates/client/AGENTS.md` et `templates/client/memory.md` (ou du script `scripts/new-client.sh`). Laisser les informations inconnues à compléter avec la consultante ; ne pas les fabriquer pour remplir le modèle.
- À la fin d'une tâche significative, mettre à jour `memory.md` uniquement lorsqu'une décision validée, une correction réutilisable, un résultat confirmé ou une prochaine étape durable a été établi.
- Garder l'état actuel plutôt qu'un journal : supprimer les doublons et les éléments devenus faux. Maximum 100 lignes ; compacter dès 80.
- Étiqueter `À vérifier` toute information non confirmée. Ne pas transformer une suggestion de l'IA en décision du client.
- Relire le fichier avant une modification si une autre session ou un autre Mac a pu le changer ; éviter les modifications simultanées sur les deux Macs.

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
