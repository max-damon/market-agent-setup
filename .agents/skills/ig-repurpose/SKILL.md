---
name: ig-repurpose
description: >-
  Transformer un contenu long (vidéo YouTube, podcast, live, newsletter,
  article, appel client) en une semaine de reels et de carrousels Instagram. À
  utiliser pour « décline ça en reels », « transforme ça pour Instagram », « j'ai
  une vidéo, un podcast, une transcription », « découpe ça ». Pour décliner un
  contenu sur plusieurs canaux (LinkedIn, newsletter, blog), utiliser plutôt
  $content-repurposing.
---

# ig-repurpose

Un bon contenu long contient quatre à six publications. La plupart des gens en
tirent une et jettent le reste.

Si `contexte/voix-instagram.md` existe dans le projet ouvert, lis-le avant
d'écrire.

## Entrée

Une transcription, un article, une newsletter, un script, un compte rendu
d'appel, un live. Si elle donne un lien et que la session a un outil de
transcription, utilise-le ; sinon demande-lui de coller le texte. Si la source
est dans son Drive ou son Notion et que le plugin est connecté, lis-la
directement. Lis tout avant d'extraire quoi que ce soit.

Si la source est une vidéo qui lui appartient, demande aussi le fichier. Un
Reel construit sur ses propres images bat un Reel construit sur ses propres
mots relus.

Ne publie jamais le contenu d'un appel client sans son accord explicite et
celui du client.

## Extraire, ne pas résumer

Le résumé d'une vidéo n'est pas un Reel. Personne ne veut le résumé. Parcours
la source et sors ce qui tient seul :

| extraire | ce que c'est |
| --- | --- |
| **Affirmations** | chaque phrase qui lancerait un débat |
| **Chiffres** | chaque nombre, coût, durée, pourcentage |
| **Histoires** | chaque moment avec une personne, une scène et un coût |
| **Mécanismes** | chaque « en fait, ça marche comme ça » |
| **Erreurs** | chaque aveu de quelque chose qui a mal tourné |
| **Phrases** | chaque phrase déjà citable telle quelle |

Liste ce que tu as trouvé, avec les nombres, avant d'écrire quoi que ce soit.
Si la source donne moins de quatre éléments, elle est mince, et quatre
publications tirées d'elle le seront aussi. Dis-le.

## Choisir le format par extrait

Tout n'est pas un Reel.

- **Affirmation, erreur, histoire** : Reel. Il faut une voix et un visage.
- **Mécanisme, liste numérotée** : carrousel. Il faut pouvoir relire.
- **Phrase citable** : un écran de story, pas une publication.

## Construire la semaine

Chaque extrait devient une publication, et chaque publication tient
complètement seule. Le spectateur n'a pas vu la source et ne la verra jamais.
N'écris jamais « comme je le disais dans ma dernière vidéo ».

Attribue une formule d'accroche de `ig-reel/hooks.json` à chacune et varie-les.
Cinq publications tirées d'une même source avec la même forme d'accroche, ça
sent l'usine à contenu.

Si la source est sa propre vidéo, **utilise les vraies images**. L'extrait où
elle a dit la chose, avec sa vraie réaction, bat un nouvel enregistrement.
Coupe sur la phrase, pas sur la respiration.

Ordonne la semaine : l'affirmation la plus forte d'abord, l'histoire en milieu
de semaine, le mécanisme à la fin, quand ceux qui ont aimé les précédentes
l'attendent.

## Résultat

```
SOURCE : « Pourquoi on a arrêté les appels découverte » (podcast de 42 min, 8 900 mots)

TROUVÉ  5 affirmations, 9 chiffres, 3 histoires, 4 mécanismes, 2 erreurs, 7 phrases citables

SEMAINE
MAR  REEL       #2  L'ordre négatif     Arrête les appels découverte
                                        extrait à 14:20, elle rit à la fin
MER  CARROUSEL  légende rôle B          Le formulaire en 4 questions qui a remplacé l'appel
VEN  REEL       #21 En pleine phrase    « …et elle a demandé un remboursement neuf jours après »
DIM  REEL       #5  Le temps compressé  Six heures par semaine récupérées, un lien supprimé

Dis « écris mardi » et je le rédige.
```

Puis rédige à la demande, une publication à la fois, chacune avec `$ig-reel`
ou `$ig-carousel`, puis `$ig-human`. Ne livre pas quatre scripts finis d'un
coup : ils sonneront tous pareil et elle n'en tournera aucun.

Garde la liste des extraits dans `travail/instagram/` du projet ouvert.
