---
name: ig-human
description: >-
  Retirer l'empreinte machine d'un texte (tirets cadratins, clichés d'IA,
  caractères invisibles) et le noter sur un panel de cinq critères avant
  publication. À utiliser quand un texte doit sonner humain, pour « humanise »,
  « est-ce que ça fait IA », « enlève les tirets », « ça sonne ChatGPT », et
  avant de montrer toute légende, script, commentaire, réponse ou message
  Instagram.
---

# ig-human

Deux outils sont dans le dossier de ce skill et ils fonctionnent. Utilise-les,
ne juge pas à l'œil.

```bash
python3 <dossier de ce skill>/humanize.py brouillon.txt --report     # nettoie et montre ce qui change
python3 <dossier de ce skill>/detect.py brouillon.txt                 # note, cinq critères
python3 <dossier de ce skill>/detect.py avant.txt apres.txt           # prouve l'écart
```

Les deux lisent `slop.json` : environ 170 mots et expressions toutes faites en
français avec leur remplacement, 18 familles de caractères invisibles, 11
substitutions typographiques et 18 tournures suspectes. Le lexique est fait
pour être modifié : si elle emploie un mot que le lexique retire, enlève-le du
fichier. Pour un texte en anglais, ajoute `--lexicon <dossier de ce skill>/slop-en.json`.

## Pourquoi c'est plus important sur Instagram qu'il n'y paraît

Les légendes sont courtes et les scripts sont dits à voix haute. Une phrase qui
sonne écrite pèse plus dans 600 caractères que dans un article, et une voix off
que personne ne pourrait dire naturellement se repère à la première prise. Le
vrai risque n'est pas un détecteur : c'est une personne qui fait défiler parce
que ça sonne comme une marque, ou une créatrice qui bute sur son propre script.

## Ce qui est corrigé automatiquement

**1. Caractères invisibles.** Espaces de largeur nulle, liants, traits d'union
conditionnels, BOM, caractères d'étiquette Unicode, espaces insécables et
fines. Un clavier n'en produit pas. `humanize.py` les supprime tous (les
espaces insécables deviennent des espaces normales, donc « Pourquoi ? » garde
son espace).

**2. Typographie.** Tiret cadratin en virgule, demi-cadratin en trait d'union,
apostrophes et guillemets anglais courbes en droits, points de suspension en
trois points, puce en tiret. Les guillemets français « » ne sont pas touchés.
Le tiret cadratin est celui qui compte.

**3. Les clichés.** « Dans un monde en constante évolution », « il est crucial
de », « tirer parti de », « incontournable », « plongeons dans », « booster
votre visibilité », plus le bloc Instagram : « arrête de scroller », « dans
cette vidéo », « abonne-toi pour plus », « tag quelqu'un qui a besoin de ça »,
« l'algorithme adore ». Chacun est remplacé par un mot simple ou supprimé.
Après une suppression, relis la phrase : le français a des accords qu'un
remplacement automatique ne gère pas toujours.

## Ce qui n'est PAS corrigé automatiquement

Les tournures sont **signalées, pas réécrites**, parce que changer la forme
d'une phrase demande du jugement :

- « Ce n'est pas juste X, c'est Y » et « Non seulement X, mais aussi Y »
- Les énumérations en trois temps
- Les lignes-questions rhétoriques : « Le résultat ? »
- Le préambule vidéo : « dans cette vidéo je vais vous montrer »
- « Et si je vous disais que… », « N'hésitez pas à… »
- Les listes à puces en emoji
- Trois mots ou plus en majuscules d'affilée
- Les murs de hashtags
- Les appâts réflexes : « abonne-toi pour plus », « identifie quelqu'un qui »

C'est ton travail : réécris chaque ligne signalée en gardant le sens, puis
relance `detect.py`. C'est ce qui fait passer de À REVOIR à OK, et c'est ce
qu'un script ne sait pas faire.

## Les cinq critères

`detect.py` note cinq signaux de 0 à 100 ; plus c'est haut, plus c'est humain :

| critère | ce qu'il mesure | à quoi ressemble la machine |
| --- | --- | --- |
| RYTHME | variation de longueur des phrases | toutes les phrases de la même longueur |
| CONCRET | chiffres, noms, dates pour 100 mots | des noms abstraits, aucun chiffre |
| CLICHÉS | expressions du lexique pour 100 mots | vocabulaire tout fait |
| EMPREINTE | invisibles, tirets cadratins, guillemets anglais courbes pour 1 000 caractères | typographie trop parfaite |
| VOIX | marques de l'oral (« ça », « on », « c'est pas », « du coup »), pronoms, tournures | aucune marque de l'oral, révélations mises en scène |

Le verdict pèse la moyenne à 60 % et le **critère le plus faible** à 40 %,
parce qu'un seul signal suffit. OK demande 70 ou plus, sans critère sous 55.

## À dire honnêtement

Ce sont cinq heuristiques locales inspirées des signaux des détecteurs publics.
Elles tournent sur sa machine et rien n'est envoyé. Ce ne sont **pas** GPTZero,
Originality, Copyleaks, Winston ou Turnitin, elles n'appellent pas leurs API et
ne peuvent pas promettre leur verdict. Les seuils viennent de la version
anglaise et n'ont pas été recalibrés sur du français : un score est un repère,
pas une mesure. Ne dis jamais qu'un texte est indétectable.

## Ordre des opérations

1. `humanize.py brouillon.txt -o propre.txt --report`
2. Lis les tournures signalées. Réécris ces lignes toi-même.
3. `detect.py brouillon.txt propre.txt` pour montrer l'avant/après.
4. Si le verdict n'est pas OK, corrige le critère le plus faible indiqué et
   recommence. Deux tours, c'est normal. Cinq tours veut dire que le brouillon
   a été écrit par formule : il faut un autre brouillon, pas plus de passes.
5. Montre le texte nettoyé et le score. Jamais le score seul.

Les fichiers de travail (`brouillon.txt`, `propre.txt`) vont dans
`travail/instagram/` du projet ouvert.
