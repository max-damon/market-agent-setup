---
name: ig-audit
description: >-
  Faire le bilan de ce qui a déjà été publié sur Instagram : quels reels ont
  vraiment marché, pourquoi, et quoi arrêter. À utiliser quand elle colle ses
  statistiques Instagram ou ses anciennes publications et demande « qu'est-ce
  qui marche », « pourquoi ça a fait un flop », « lis mes stats Instagram »,
  « audite mon contenu ». Pour un reporting multicanal (GA4, publicité, site),
  utiliser plutôt $performance-review.
---

# ig-audit

La seule source honnête de ce qui marche pour un compte, c'est ce compte. Chaque
règle de chaque guide Instagram, y compris ceux de ce pack, est un a priori.
Ses 30 dernières publications sont la preuve.

## Entrée

Demande ce qu'elle a :

- Les statistiques par publication : vues, couverture, interactions, durée de
  visionnage, enregistrements, partages, abonnements, et la part de couverture
  hors abonnés. Des captures d'écran suffisent.
- Ou le graphique de rétention de ses meilleurs et pires reels récents. Cette
  seule capture vaut plus que tout le reste.
- Ou juste les publications et leurs vues : assez pour un premier passage.

Lis aussi `travail/instagram/journal.md` dans le projet ouvert s'il existe : il
indique la formule d'accroche de chaque publication. Si c'est un compte client,
lis le `memory.md` du client pour le contexte des campagnes.

## Ce qu'il faut vraiment mesurer

Les vues brutes sont le chiffre le moins utile de la page, parce qu'elles
dépendent surtout du nombre d'abonnés. Calcule plutôt ceci, en montrant le
calcul :

| indicateur | calcul | ce qu'il dit |
| --- | --- | --- |
| **Multiple de référence** | vues / médiane des vues du compte | un vrai succès ou une journée normale |
| **Portée hors abonnés** | % de la couverture venant de non-abonnés | si ça a voyagé |
| **Rétention à 3 s** | spectateurs encore là à 3 s / spectateurs au départ | si l'accroche a marché. C'est sa note. |
| **Durée moyenne de visionnage** | dans les statistiques | si le milieu a marché |
| **Envois par couverture** | partages / couverture | le signal le plus fort. Un envoi, c'est quelqu'un qui engage son nom. |
| **Abonnements par couverture** | abonnements / couverture | si le profil a converti l'attention |

Classe par multiple de référence et par envois par couverture, pas par vues.
Un reel à 4 000 vues et 90 envois bat celui à 60 000 vues et 11 envois.

## Puis trouver le motif

Mets les cinq meilleurs et les cinq pires côte à côte, cherche ce qui les
sépare, et accepte de conclure quelque chose qui ne lui plaira pas :

- **Rétention à 3 secondes.** Si le haut et le bas diffèrent ici, c'est
  l'accroche et rien d'autre ; tout le reste est une distraction.
- **Formule d'accroche.** Quels numéros de `ig-reel/hooks.json` sont dans le haut ?
- **Format.** Reel, carrousel, image seule.
- **Durée.** Moins de 15 s, 15 à 30 s, 30 à 60 s, plus de 60 s.
- **Thème.**
- **A-t-elle répondu aux commentaires dans la première heure ?**
- **Jour et heure.** À vérifier **en dernier**, et seulement si le reste ne
  montre rien. Ce n'est presque jamais la cause, et c'est là qu'on aimerait
  qu'elle soit.

Énonce chaque constat comme une affirmation avec sa preuve, et dis à quel point
tu en es sûre. Avec 30 publications, on voit un motif. Avec 6, non, et le dire
vaut mieux qu'en inventer un.

## La distinction qui fait gagner des mois

**Un reel qui fait des vues et pas d'abonnés n'est pas un reel raté, c'est un
problème de profil.** Un reel qui ne fait pas de vues est un problème
d'accroche. Sépare les deux avant toute recommandation. Si la portée hors
abonnés est haute et les abonnements par couverture bas, arrête de réécrire les
accroches et passe à `$ig-profile`.

## Résultat

```
BILAN  ·  31 publications  ·  12 juin - 5 sept.  ·  médiane 4 100 vues

TOP 5 PAR MULTIPLE
  18,2x  #3  Personne ne te dit   74 600 vues  62 % hors abonnés  rétention 3 s 71 %  128 envois
   6,4x  #1  L'aveu du coût       26 300 vues  48 % hors abonnés  rétention 3 s 64 %   71 envois
  ...

BAS 5
   0,3x  #11 La liste             1 200 vues   9 % hors abonnés  rétention 3 s 31 %    2 envois
  ...

CE QUE DISENT LES DONNÉES
1. La rétention à 3 secondes explique tout. Haut 66 % en moyenne, bas 33 %.
2. Les publications où c'est toi qui as mauvaise mine : 8,1x en moyenne contre
   0,9x pour le reste. n=5. Le signal le plus net, et de loin.
3. Les listes d'outils font des vues et rien d'autre. Trois des cinq du bas.
4. Le jour de la semaine ne montre rien. Arrête de l'optimiser.

ARRÊTER : les listes d'outils.
FAIRE PLUS : les publications avec un coût que tu as payé et un chiffre.
```

Puis passe les conclusions à `$ig-plan`, pour que la semaine suivante repose sur
ses propres preuves, et à `$ig-viral`, pour filtrer la swipe file sur les
formules qui marchent pour ce compte. Enregistre le bilan dans
`travail/instagram/` du projet ouvert ; si une conclusion est validée et
durable, ajoute une entrée au `memory.md` selon les règles globales.
