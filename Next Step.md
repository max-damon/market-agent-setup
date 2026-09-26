# Prochaines étapes — adapter Codex à sa vraie façon de travailler

La configuration actuelle fournit les consignes globales, neuf skills marketing, un modèle de projet client et une synchronisation des fichiers par iCloud Drive. **Elle ne connaît pas encore les processus réels de la consultante.** Cette page sert à recueillir ses exemples, choisir les connexions utiles et construire les workflows un par un. Elle n'active aucune connexion ni automatisation à elle seule.

## Ce que nous savons déjà

- Elle prend les notes du premier appel de lancement directement dans **Notion**.
- Elle crée des visuels et d'autres supports dans **Canva**.
- Elle utilise **Google Slides** pour présenter son travail.
- Elle assure des **coachings**, avec des préparations et des suivis qui pourraient devenir des tâches récurrentes.
- Elle travaille sur un **Mac mini** et un **MacBook Air** ; les fichiers de configuration et de chaque client doivent être dans son iCloud Drive.

Ces points décrivent des outils et des étapes, pas encore leurs détails : modèles de pages, responsabilités, volumes, fréquence, critères de qualité et droit d'accès restent à documenter.

## Les exemples à recueillir avec elle

Pour chaque parcours, prendre **un dossier récent, anonymisé si nécessaire**, et lui demander de montrer l'entrée, les étapes, le livrable final et une correction typique. Noter le temps passé, les décisions qu'elle prend elle-même et les erreurs qu'elle ne veut surtout pas voir.

| Parcours | Ce qu'il faut obtenir d'elle | Ce qu'on pourra automatiser ensuite |
| --- | --- | --- |
| **Premier appel et cadrage** | Modèle de notes Notion, exemple de notes réelles, questions posées, livrables promis, façon de confirmer les décisions. | Lire la page autorisée, extraire faits et inconnues, proposer un brief client à valider, puis enrichir le dossier du client. |
| **Création Canva** | Brand kits, modèles utilisés, dimensions, types de visuels, étapes de retouche, exemples approuvés, règles sur les images et les droits. | Préparer les textes et spécifications, retrouver ou copier le bon modèle, créer un brouillon, exporter pour contrôle. |
| **Présentation Google Slides** | Présentation type, modèle, ordre des sections, niveau de détail, graphiques, commentaires et circuit de validation. | Transformer un brief validé en trame, créer une copie du modèle, remplir les diapositives, vérifier le rendu. |
| **Coaching** | Cadence, agenda, préparation, notes, devoirs ou actions convenues, rappels, suivi après séance. | Préparer un dossier de séance, proposer un compte rendu et une liste d'actions, puis programmer seulement les suivis approuvés. |
| **Autres missions fréquentes** | Deux ou trois livrables qui reviennent souvent, leurs sources et exemples validés. | Ajouter ou ajuster un skill lorsque la méthode est réellement répétable. |

## Parcours cible 1 — de Notion au contexte client

**Déclencheur envisagé :** l'appel de lancement est terminé et ses notes Notion sont prêtes.

1. Identifier la page Notion du **bon client** et vérifier que la connexion permet de la lire. Ne pas parcourir tout son espace Notion par défaut.
2. Extraire offre, objectifs, cibles, contraintes, livrables attendus, décisions prises et questions ouvertes. Conserver le lien de la page source et la date de lecture.
3. Proposer un résumé structuré et relever les ambiguïtés. Elle confirme ou corrige ce résumé.
4. Mettre les **faits stables validés** dans `Clients/<client>/AGENTS.md` ou un document de `contexte/`, selon leur longueur. Mettre les décisions et prochaines étapes durables dans `memory.md`.
5. Lors des mises à jour ultérieures de la page Notion, comparer les changements avant de remplacer le contexte local. Ne pas écraser silencieusement une correction faite par elle.

**À décider avec elle :** Notion reste-t-il la source principale des notes ? Faut-il un instantané local après chaque appel ou seulement au lancement ? Qui valide le résumé et à quel moment ?

## Parcours cible 2 — du brief aux créations Canva

**Déclencheur envisagé :** un angle ou calendrier de contenus est validé.

1. Produire un brief créatif court : public, message, preuve, format, texte, dimensions, marque et appel à l'action.
2. Vérifier sur **son compte** les outils réellement accessibles via Canva MCP, les modèles disponibles et les droits de modification. Canva documente notamment la recherche, la création, l'édition et l'export de designs ; la disponibilité exacte dépend du compte et de l'outil connecté. [Documentation Canva MCP](https://www.canva.dev/docs/apps/mcp/), [outils et limites](https://www.canva.dev/docs/apps/mcp/tools/).
3. Créer une **copie ou un brouillon** à partir du bon modèle. Préserver l'original et indiquer le lien du design créé.
4. Contrôler visuellement les textes, coupures, dimensions, couleurs, logo, images et licences avant export ou partage.

**À décider avec elle :** quels visuels produira-t-elle toujours elle-même ? Quels modèles sont réellement réutilisables ? Faut-il seulement préparer le brief, ou également modifier Canva ?

## Parcours cible 3 — du travail validé à Google Slides

**Déclencheur envisagé :** un audit, une stratégie ou un bilan est prêt à être présenté.

1. Utiliser uniquement des analyses et recommandations validées. Construire d'abord le fil narratif et la décision attendue de la présentation.
2. Identifier le modèle Google Slides et les éléments à préserver : titres, styles, graphiques, notes orales et mentions du client.
3. Vérifier la connexion Google Drive/Slides sur le Mac qui exécute la tâche, puis créer une **copie de travail**. Le skill `$client-presentation` décrit la méthode ; il ne fournit pas lui-même l'accès au compte.
4. Relire toutes les diapositives, les chiffres et la mise en page. Elle approuve la version avant partage avec le client.

**À décider avec elle :** faut-il générer la présentation entière ou préparer une trame qu'elle finalise ? Quel niveau de retouche graphique accepte-t-elle ?

## Parcours cible 4 — préparer et suivre les coachings

**Déclencheurs envisagés :** séance prévue, séance terminée, échéance d'une action convenue.

- **Avant :** rassembler les objectifs, décisions passées, actions ouvertes et documents utiles ; produire une fiche de préparation courte.
- **Après :** à partir des notes de séance, proposer un compte rendu, les décisions prises, les actions attribuées et leurs échéances. Elle vérifie avant tout envoi ou création de tâche externe.
- **Entre deux séances :** une automatisation peut signaler les actions dues ou préparer un prochain dossier de séance. Tester d'abord manuellement le prompt et ses sources, puis choisir une cadence. Les [tâches planifiées de Codex](https://learn.chatgpt.com/docs/automations) peuvent utiliser des projets locaux, mais le Mac et l'application doivent être disponibles pour lire ces fichiers.

**À décider avec elle :** où vit l'agenda ? Où les actions sont-elles suivies aujourd'hui ? Qui reçoit les rappels ? Quels messages peut-on préparer, et lesquels peut-on envoyer seulement après validation ?

## Ordre de mise en œuvre

1. **Observer et cartographier.** Documenter ses quatre parcours avec des exemples réels et mesurer le temps actuel. Confirmer les clauses de confidentialité des clients avant tout déplacement de données dans iCloud ou un service connecté.
2. **Tester un client pilote.** Vérifier que son dossier, `AGENTS.md` et `memory.md` se synchronisent réellement entre les deux Macs. Ne traiter qu'un client à la fois pendant le pilote.
3. **Connecter Notion en lecture.** Réussir le passage « notes → brief validé → contexte client » avant d'automatiser une mise à jour.
4. **Connecter la production.** Tester Canva et Google Slides séparément, avec des copies et une vérification visuelle. Ajouter un workflow complet seulement lorsque chaque étape isolée fonctionne.
5. **Ajouter le coaching.** Tester préparation et compte rendu à la demande, puis programmer un premier rappel ou brouillon récurrent si le résultat est fiable.
6. **Créer les agents/skills manquants.** Définir un rôle spécialisé uniquement si une tâche distincte et fréquente le justifie : cadrage client, production créative, présentation ou suivi coaching. Sinon, enrichir un skill existant.

## Faire évoluer la configuration après l'installation

Les fichiers **actifs** sont ceux d'iCloud Drive. Un changement ultérieur dans ce dépôt GitHub ne les modifie pas automatiquement. Lorsque nous construirons un nouveau skill ou améliorerons un agent, il faudra décider où le modifier, comparer la nouvelle version aux personnalisations déjà faites dans iCloud, puis la déposer dans `MarketAgent/Configuration`. iCloud la transmettra ensuite au second Mac.

Avant de multiplier les évolutions, prévoir une procédure de mise à jour **avec aperçu des différences et sauvegarde**, qui ajoute les nouveaux fichiers sans écraser les règles qu'elle aura complétées. Cette procédure servira à faire évoluer le setup ; elle ne demandera pas à la consultante d'utiliser Git.

## Critères de réussite du prochain chantier

- Une note Notion autorisée devient un brief **sourcé et corrigible**, sans mélange avec un autre client.
- Une création Canva et une présentation Slides sont produites comme **brouillons révisables**, avec leurs liens et leurs modèles d'origine.
- Un coaching peut être préparé et suivi sans perdre les décisions, responsables et échéances ; aucun envoi ou rappel externe n'est déclenché par erreur.
- Les fichiers durables restent lisibles sur les deux Macs après synchronisation iCloud. Les connexions aux comptes, propres à chaque Mac, sont testées sur le Mac qui exécutera le workflow.
- Le temps total jusqu'au livrable accepté diminue sans hausse des erreurs ou de la charge de maintenance.

## Ce qu'il faudra me transmettre pour continuer

Un exemple de page Notion de lancement, deux créations Canva et leur modèle, une présentation Google Slides type, un cycle de coaching complet et la liste des outils où elle suit aujourd'hui ses actions. Des versions anonymisées suffisent pour dessiner les workflows ; les accès aux comptes ne seront nécessaires qu'au moment de tester les connexions.
