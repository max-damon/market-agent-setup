---
name: ig-viral
description: >-
  Trouver les reels qui marchent vraiment en ce moment dans sa niche, les
  classer selon à quel point chacun a dépassé son propre compte, nommer la
  formule d'accroche de chacun, et en faire une swipe file à tourner. À
  utiliser pour « trouve des vidéos virales », « qu'est-ce qui marche en ce
  moment », « que publient les comptes de ma niche », « décortique ce compte »,
  « fais-moi une swipe file », « pourquoi ce reel cartonne », ou quand elle
  demande quoi faire ensuite sans preuve pour répondre.
---

# ig-viral

Le skill de recherche. Les autres écrivent ; celui-ci va regarder. À lancer une
fois par mois, pas tous les jours : une formule tient une saison.

Un outil est dans le dossier de ce skill et il fonctionne :

```bash
python3 <dossier de ce skill>/swipe.py travail/instagram/releve.tsv --out travail/instagram/swipe.md
```

Les chemins sont relatifs au projet ouvert (son compte perso ou un client).

## L'idée qui fait tout l'intérêt

**Les vues brutes ne sont pas une preuve.** Un compte à deux millions
d'abonnés qui fait 400 000 vues a eu un mardi calme. Un compte à quatre mille
abonnés qui fait 400 000 vues a trouvé quelque chose, et ce quelque chose se copie.

Tout est donc classé sur le **multiple de référence** : les vues divisées par la
médiane récente du compte. Au-dessus de 3x, c'est un signal. En dessous de
1,5x, c'est une journée normale pour ce compte et ça n'apprend rien, aussi gros
que soit le chiffre.

Relève des comptes **à moins de 10x sa propre taille environ**. Une formule qui
marche à 2 millions d'abonnés marche souvent parce que c'est 2 millions.

## Étape 1 : choisir les comptes

Demande-lui 6 à 12 comptes, ou propose-les et fais-les valider :

- **4 directs** : même niche, même offre, un peu en avance.
- **4 voisins** : autre niche, même audience. C'est là qu'on emprunte des
  formats avant que la niche les ait.
- **2 à 4 démesurés** : bien plus gros, pour le format seulement, jamais pour
  le rythme ou le ton.

Demande-lui aussi d'ouvrir sa **collection « Enregistrements »**. C'est le
corpus le plus rapide et le plus pertinent qui existe, et il est déjà filtré
par son goût.

## Étape 2 : aller regarder

Utilise l'outil de navigation dont la session dispose vraiment : le navigateur
intégré, ou son propre navigateur si l'outil est connecté. Il n'y a pas d'API
pour ça et il n'en faut pas : le volume est assez faible pour être lu.

**Règles non négociables :**

- **Ne te connecte jamais à Instagram à sa place et ne demande jamais de mot de
  passe.** Si une page exige une connexion, c'est elle qui est déjà connectée.
  Pilote son navigateur en sa présence, ou demande-lui de coller les infos.
- **On lit, on n'aspire pas.** Dix comptes, une douzaine de reels chacun, à
  vitesse humaine. La collecte automatisée en volume enfreint les conditions
  d'utilisation d'Instagram et fait bloquer les comptes. Pas de robot, pas de
  service de scraping, pas de boucle en arrière-plan.
- **Copie la formule, jamais la vidéo.** La forme de l'accroche, la structure,
  la durée, le rythme des coupes. Pas leur script, pas leur voix, pas leur
  montage. Attribue chaque ligne de la swipe file au compte d'origine.

**Quoi relever par reel**, dans les mots de la créatrice :

| champ | notes |
| --- | --- |
| compte | identifiant |
| abonnes | depuis le profil |
| mediane | regarde les 12 derniers reels et prends le nombre de vues du milieu |
| vues | ce reel |
| accroche | la première phrase, dite ou à l'écran, mot pour mot, fautes comprises |
| à l'écran | le premier carton de texte, s'il est différent |
| durée | en secondes |
| cta | ce qu'ils demandent à la fin |

La médiane est le champ important. Sans elle, on revient au classement par
nombre d'abonnés, exactement ce que ce skill veut éviter.

**Quand Instagram ne montre pas assez :** la même grammaire d'accroche existe
sur YouTube Shorts, où les vues et les transcriptions sont publiques et sans
connexion. C'est un second corpus légitime :

```bash
# vues des shorts d'une chaîne
python3 -m yt_dlp --flat-playlist --playlist-end 40 -J \
  "https://www.youtube.com/@CHAINE/shorts" > chaine.json

# la première phrase dite d'un short, depuis les sous-titres automatiques
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "fr.*" \
  --sub-format json3 -o accroche "https://www.youtube.com/watch?v=ID_VIDEO"
```

Prends chaque mot sous-titré dont l'horodatage est inférieur à 3,0 secondes :
c'est l'accroche telle qu'elle est dite. `yt_dlp` n'est pas installé par
défaut : demande avant de l'installer.

## Étape 3 : classer

Remplis `travail/instagram/releve.tsv` (séparé par des tabulations) avec une
ligne d'en-tête, puis lance le script :

```
compte	abonnes	mediane	vues	accroche
@quelquun	48000	11000	412000	personne ne te dit que tes 30 premiers reels vont flopper
```

Il calcule le multiple de référence, nomme la formule d'accroche avec les 26
formules dont `$ig-reel` se sert, note chaque accroche avec `hookscore.py`, et
montre ce qui sépare le tiers du haut du tiers du bas. Les formules sont
écrites pour des accroches françaises ; une accroche anglaise sera souvent
« non classée ».

## Étape 4 : dire ce que ça veut dire, prudemment

Rapporte trois choses, pas plus :

1. **Les formules surreprésentées** dans le tiers du haut, avec les nombres.
   Deux formules présentes quatre fois chacune sur six comptes, c'est un
   constat. Une présente deux fois, non.
2. **Ce que le tiers du haut a en commun** que le bas n'a pas : longueur de
   l'accroche, chute visuelle ou non, mouvement dès la première image, place
   de la demande.
3. **Les lignes non classées.** Chaque accroche que le script n'a pas pu nommer
   est soit du bruit, soit une formule absente de `hooks.json`. Lis-les à la
   main. C'est la colonne la plus précieuse du résultat.

Puis donne la taille de l'échantillon et le niveau de confiance en mots
simples. Quarante reels sur six comptes soutiennent une affirmation. Douze,
non, et le dire, c'est la différence entre une étude et un horoscope.

## Étape 5 : en faire quelque chose à tourner

Pour les trois meilleures formules, écris **sa version** : sa propre histoire,
son propre chiffre, dans la forme qui marche. Passe chacune à `$ig-reel` avec
le numéro de formule déjà choisi.

Ne rends jamais « fais un reel comme celui-là ». Rends une accroche qu'elle
pourrait dire demain.

## Résultat

```
SWIPE  ·  38 reels  ·  7 comptes  ·  référence : médiane du compte

AU-DESSUS DE 3x
  38,4x  accroche 86  #3  Personne ne te dit    @compte_a   412 000  (médiane 10 700)
  11,2x  accroche 79  #9  Le vol autorisé       @compte_c   180 000  (médiane 16 100)
  ...

SURREPRÉSENTÉ
  #3 Personne ne te dit   x5 dans le tiers du haut, 0 en bas
  #2 L'ordre négatif      x4
  longueur médiane        8 mots en haut, 19 en bas

NON CLASSÉES (6)
  Deux ont la même forme et elle n'est pas dans hooks.json : une accroche qui
  commence par lire à voix haute le commentaire de quelqu'un. À ajouter.

TA VERSION
  #3  « Personne ne te dit que tes 20 premiers devis sont censés être refusés. »
  ...
```

La swipe file est écrite dans `travail/instagram/swipe.md`. `$ig-reel` et
`$ig-plan` la lisent toutes les deux : une fois ce skill lancé, le reste du
pack travaille à partir de ses propres preuves au lieu des réglages par défaut.

Ce skill ne publie, ne suit, n'aime et n'écrit rien. Il lit.
