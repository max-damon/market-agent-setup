---
name: ig-story
description: >-
  Écrire les stories Instagram du jour : la séquence écran par écran, quels
  stickers utiliser où, et celui qui amène en message privé. À utiliser pour
  « stories », « je mets quoi en story », « séquence de stories », « idée de
  sondage », « je n'ai rien à raconter en story », ou pour vendre quelque chose
  sans en faire une publication.
---

# ig-story

Les stories ne sont pas un fil en plus petit. Le fil, c'est comme ça que des
inconnus te trouvent. Les stories, c'est comme ça que les gens qui te suivent
déjà décident si tu es quelqu'un à qui acheter, et c'est le seul endroit
d'Instagram où un appui devient une conversation en un geste.

Personne en dehors des abonnés ne les voit, donc le rôle est complètement
différent : la profondeur, pas la portée.

Si `contexte/voix-instagram.md` existe dans le projet ouvert, lis-le avant
d'écrire.

## La forme du jour

Trois à sept écrans par jour. Au-delà d'environ sept, le taux de passage monte
et les derniers écrans ne sont vus par personne, et c'est justement là qu'on
met la demande.

```
1       L'OUVERTURE  quelque chose qui se passe aujourd'hui, avec un visage ou une main.
2-3     LE MILIEU    le vrai contenu : la méthode, le résultat, l'erreur.
4       LA DEMANDE   un sticker. Sondage, boîte à questions, quiz ou lien.
5       LA FIN       la réponse, le résultat, ou la mise en place de demain.
```

La demande à l'écran 4, pas au 7. On perd du monde à chaque appui, et la
demande doit être vue par ceux qui sont encore là.

## Les stickers et leur vrai rôle

| sticker | rôle | quand |
| --- | --- | --- |
| **Sondage** | l'appui le moins cher qui existe | tu veux du volume de réponses, pas de l'information |
| **Boîte à questions** | récolter les mots exacts des gens | tu as besoin d'idées de contenu ou d'objections, mot pour mot |
| **Quiz** | apprendre en laissant se tromper | il y a une idée reçue courante dans la niche |
| **Curseur** | prendre la température | rien d'important. Amusant, peu utile |
| **Lien** | la seule surface cliquable hors bio | il y a un vrai endroit où aller |
| **Compte à rebours** | une échéance à laquelle on peut s'abonner | un lancement, un live, une date de clôture |
| **À vous** | de la portée au-delà des abonnés, de temps en temps | la question est une à laquelle tout le monde dans la niche peut répondre |

La boîte à questions est la plus sous-estimée. Chaque réponse est une légende,
une accroche de Reel ou une ouverture de message écrite dans les mots de
l'audience. Passe-les à `$ig-reel` avec la formule #16.

## Règles

- **Un visage ou une main au premier écran.** Du texte sur fond de couleur se
  fait passer, et le premier écran décide si les autres seront vus.
- **Une idée par écran.** Personne ne lit un paragraphe en story.
- **Le texte au milieu.** Sur 1080x1920, rien au-dessus de y=250 ni en dessous
  de y=1600. La ligne du profil est en haut et la barre de réponse en bas.
- **Parle à une personne.** « Tu », au singulier si c'est son ton. La story
  est ce qui ressemble le plus à un message privé sans en être un.
- **Ne repartage pas ta publication en story sans commentaire.** C'est l'écran
  le plus ignoré de la plateforme. Si tu renvoies vers une publication, dis ce
  qui s'est passé dans les commentaires et pourquoi ça vaut le détour.
- **Vends en story, pas en publication.** Trois écrans de contexte, un écran
  d'offre, un écran de preuve. Cette séquence vend plus qu'une publication sur
  le même sujet et ne coûte aucune portée.

## L'entonnoir vers les messages, honnêtement

La séquence qui marche : une story qui nomme un problème, une boîte à
questions ou un sondage qui permet de dire « c'est moi », puis une réponse à
chaque personne qui a répondu. La conversation commence parce qu'elles ont
parlé en premier.

Les réponses automatiques par mot-clé sont une fonction prévue pour les comptes
professionnels, via les outils d'Instagram et ses partenaires agréés. Envoyer
des messages en masse à des gens qui n'ont pas interagi ne l'est pas, et c'est
ce qui fait restreindre les comptes. La règle est simple : **elles agissent
d'abord, ensuite tu réponds.**

## Résultat

Les écrans dans l'ordre, chacun avec ce qu'on voit, ce qui est dit et quel
sticker, plus quoi faire des réponses :

```
STORIES  ·  mardi  ·  5 écrans

1  [selfie, en marchant]    « Troisième demande de remboursement cette année. Même raison. »
2  [capture d'écran]        la clause, surlignée
3  [face caméra]            « La validation, c'est une impression. La livraison, c'est une date. »
4  [sondage]                « Déjà eu un souci de validation tardive ? »  Oui / Pas encore
5  [texte sur photo]        « Réponds-moi et je t'envoie la clause. »

Après : chaque personne qui vote Oui reçoit une réponse. C'est tout l'entonnoir.
```

Passe le texte dans `$ig-human`. Rien n'est publié. Elle publie elle-même.
