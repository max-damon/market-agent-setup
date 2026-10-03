---
name: ig-reply
description: >-
  Gérer les commentaires sous ses propres reels et publications Instagram :
  rédiger les réponses à ceux qui en valent la peine, triés par priorité. À
  utiliser quand elle colle ses commentaires, pour « réponds à ces
  commentaires », « gère mes commentaires », « quelqu'un a dit X sous mon
  reel », ou face à une critique, un troll ou un prospect dans les commentaires.
---

# ig-reply

Le fil de commentaires sous ta propre publication, c'est là que se décide la
portée. Chaque réponse est une interaction de plus, celles de la première heure
font l'essentiel du travail, et sur Instagram une réponse peut aussi être un
Reel, le geste le plus sous-utilisé de la plateforme.

Mais tous les commentaires ne se valent pas, donc ce skill trie avant d'écrire.

Si `contexte/voix-instagram.md` existe dans le projet ouvert, lis-le avant
d'écrire.

## Entrée

Elle colle les commentaires, idéalement avec les identifiants. Des captures
suffisent. Ne parcours pas le fil avec un navigateur.

## Trier d'abord

Range chaque commentaire dans une des six catégories et annonce les nombres :

| catégorie | ce que c'est | ce qu'il reçoit |
| --- | --- | --- |
| **MOT-CLÉ** | le mot que tu as demandé de commenter | la chose promise, envoyée à la main ou par ton outil agréé |
| **PROSPECT** | quelqu'un qui décrit le problème que tu résous | une vraie réponse en public, puis une porte |
| **FOND** | ajoute une donnée, conteste, prolonge | la réponse la plus longue du fil |
| **QUESTION** | une question que beaucoup de gens se posent | elle devient un Reel, pas seulement une réponse |
| **SOUTIEN** | « 🔥 », « super post », une identification | un j'aime, et 3 à 8 mots au plus |
| **BRUIT** | démarchage, spam, mauvaise foi, provocation | rien, ou une ligne et c'est tout |

Écris dans cet ordre et arrête-toi quand la valeur s'arrête.

## Le geste que presque tout le monde rate

Si une question en commentaire est une que trente autres personnes se posent,
**réponds-y par un Reel**. Instagram attache le commentaire à la nouvelle vidéo
en sticker, la personne qui a demandé est notifiée, et une question avec une
vraie demande derrière devient une publication dont l'accroche est déjà écrite.
Signale chaque QUESTION qui s'y prête et passe-la à `$ig-reel` avec la formule #16.

## Comment répondre

- **Réponds à la vraie question.** Si on demande comment, dis comment, dans la
  réponse. N'envoie pas en message privé pour une réponse qu'on aurait pu avoir
  en public.
- **Son prénom une fois**, au début, sans point d'exclamation.
- **Adapte la longueur.** Un commentaire de quatre mots n'appelle pas une
  réponse de quatre lignes.
- **À une critique :** concède d'abord la part vraie, dans ses mots, puis tiens
  ta position. Ne supprime jamais, ne te défends pas, ne réponds jamais deux
  fois dans le même fil.
- **À un troll :** rien. Une réponse, c'est de la portée, et c'est ce qu'il est
  venu chercher. Masque le commentaire s'il est injurieux : les outils de
  modération d'Instagram existent et s'en servir, ce n'est pas perdre.
- **À un prospect :** réponds entièrement en public. La porte, c'est une phrase
  à la fin, une offre d'aide, pas une vente. La réponse publique est ce qui
  donne envie à la personne suivante d'écrire.

## Les commentaires à mot-clé

Si la publication demandait un mot-clé, ces commentaires sont tout l'intérêt
de la publication. Chacun est une personne qui a levé la main. Réponds à
chacune, puis envoie ce qui était promis. Si elle a une automatisation via les
outils d'Instagram ou un partenaire agréé, dis-le et laisse-la tourner ; sinon,
les réponses sont manuelles, et c'est très bien à ce volume. N'envoie jamais de
message en masse à des gens qui n'ont pas commenté.

## Résultat

Un bloc, groupé par catégorie, chaque réponse prête à copier et déjà passée
dans `$ig-human` :

```
RÉPONSES  ·  84 commentaires  ·  41 MOT-CLÉ, 2 PROSPECT, 3 FOND, 2 QUESTION, 34 SOUTIEN, 2 BRUIT

MOT-CLÉ  (41)  envoie la clause. Une ligne chacune, même chaleur, pas de copier-coller.

PROSPECT
@identifiant - « on a eu exactement ce problème en juin »
> Ce qui a tout réglé pour nous, c'est de ne plus du tout lier le paiement à la
> validation. Je t'envoie la formulation si ça peut servir.

QUESTION -> REEL
@identifiant - « tu fais quoi s'ils refusent de signer ? »
  34 j'aime sur ce commentaire. C'est un Reel, pas une réponse. Formule #16.

BRUIT  (2)  ignorés. Leur répondre leur donne de la portée.
```

Puis la validation : rien n'est publié tant qu'elle n'a pas dit oui. Elle colle
les réponses elle-même.
