---
name: ig-profile
description: >-
  Noter un profil Instagram sur 100 avec une grille de 12 critères et réécrire
  ce qui perd des points : champ nom, bio, lien, stories à la une, trois
  publications épinglées, grille. À utiliser pour « optimise mon profil »,
  « corrige ma bio », « note mon Instagram », « pourquoi les gens ne
  s'abonnent pas », ou quand elle colle son profil pour savoir comment il se lit.
---

# ig-profile

Presque tout le monde optimise la mauvaise chose ici. Le profil n'est pas une
vitrine qu'on parcourt. C'est un **écran de décision**, atteint depuis un seul
reel, qui a environ trois secondes pour répondre à une question : est-ce qu'il
y a plus de ça ici, et est-ce que c'est pour moi.

## Entrée

Demande de coller ou de capturer : le champ nom, l'identifiant, la bio, la
destination du lien, les noms des stories à la une, ce qui est épinglé, et les
neuf premières couvertures de la grille. Une capture du haut du profil et des
deux premières rangées suffit pour un premier passage.

Ne te connecte jamais à Instagram à sa place.

Si le profil est celui d'un client, lis d'abord le `AGENTS.md` du client et
`contexte/voix-instagram.md` s'il existe.

## Noter

Lis `rubric.json` dans le dossier de ce skill. Douze critères, 100 points,
chacun avec ce que vaut la note maximale et l'échec habituel. Note chaque
critère, montre le tableau, donne le total. Sois honnête : la plupart des
profils sont entre 30 et 45 au premier passage, et une note généreuse ne sert à
rien.

```
SCORE DU PROFIL  38/100

  champ nom        2/12   nom seul, aucun mot que les gens recherchent
  1re ligne bio    3/12   trois noms et un emoji café
  trois épinglées  0/10   rien d'épinglé
  stories à la une 2/8    « Divers », « Vie », « 2023 »
  lisibilité       4/8    six couvertures sur neuf sont un visage en pleine phrase
  ...
```

## Puis réécrire, dans cet ordre

Corrige par ordre décroissant de points perdus. Ne réécris pas tout d'un coup :
elle doit aller changer chaque champ elle-même.

**1. Le champ nom (30 caractères).** La ligne en gras sous la photo, pas
l'identifiant. C'est le champ que la recherche Instagram compare, et la plupart
des comptes n'y mettent qu'un nom. Format qui marche :
`{Prénom Nom} | {ce qu'elle fait, avec les mots recherchés}`. Donne trois options.

**2. Première ligne de bio.** Pour qui c'est et ce qui change. Pas un intitulé
de poste, pas d'adjectifs, pas de liste d'identités séparées par des barres. Le
reste des 150 caractères porte une preuve ou une offre simple.

**3. Les trois épinglées.** Trois emplacements, trois rôles : la meilleure
preuve, l'explication la plus claire de l'offre, la meilleure présentation de
la personne. C'est la correction la plus rentable du profil et elle prend
quatre appuis.

**4. Stories à la une.** Quatre à six, nommées d'après les questions d'un
client : Tarifs, Résultats, Comment ça marche, Qui suis-je. Pas « Divers ».
Supprime le reste.

**5. Le lien.** Une destination qui correspond à ce que la bio vient de
promettre. Cinq sont autorisés ; deux, c'est déjà un menu.

**6. Couvertures de la grille.** Les neuf premières en miniature. Les
couvertures de reels se choisissent. Quatre mots de texte sur une couverture
rendent la grille lisible d'un coup d'œil. Si le plugin Canva est connecté,
propose de préparer les couvertures à partir de son modèle (sur une copie).

## Résultat

Le tableau de notes, puis les réécritures en blocs prêts à copier, par ordre de
priorité, chacune passée dans `$ig-human`. Renote à la fin et montre l'écart
honnêtement. Si la réécriture atteint 84 et pas 98, dis 84, et dis ce qui
manque : en général une grille, une habitude de stories et une publication
épinglée qui n'existe pas encore. Rien de tout ça n'est une réécriture.

Ce skill n'enregistre rien sur Instagram. Elle modifie chaque champ elle-même.
