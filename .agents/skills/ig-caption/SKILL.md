---
name: ig-caption
description: >-
  Écrire la légende Instagram (la ligne qui survit à la coupure « … plus », le
  corps, une seule demande, les mots recherchés et les hashtags) et la
  vérifier avant publication. À utiliser pour « écris la légende », « fais la
  description », un reel ou un carrousel prêt qui a besoin de texte, ou une
  question sur les hashtags Instagram.
---

# ig-caption

Un outil est dans le dossier de ce skill et il fonctionne :

```bash
python3 <dossier de ce skill>/caption.py legende.txt
python3 <dossier de ce skill>/caption.py legende.txt --keywords "stratégie instagram,consultante marketing"
```

Il affiche la légende comme le fil l'affiche : les 125 premiers caractères dans
un cadre, le reste derrière l'appui. Lis ce cadre avant tout le reste.

Si `contexte/voix-instagram.md` existe dans le projet ouvert, lis-le avant
d'écrire.

## D'abord, décide quel est le rôle de cette légende

C'est la décision qui ruine les légendes quand on la saute.

**Rôle A : la vidéo a déjà accroché.** Un Reel porte sa propre accroche dans
les deux premières secondes, dite et écrite. La légende n'est pas une deuxième
accroche ; rivaliser avec la vidéo, c'est perdre les deux. Son rôle : la
demande, le contexte qui donne du sens à la demande, et les mots que les gens
recherchent.

**Rôle B : la légende est le contenu.** Une photo, une image seule, une
couverture de carrousel qui ouvre une boucle. Ici la première ligne est
l'accroche et elle fonctionne comme celle d'un Reel : concrète, courte, coupée
sur un suspense plutôt qu'au milieu d'une subordonnée.

Dis lequel tu écris. Si elle a un Reel avec une accroche forte, écris un A et
explique pourquoi.

## La forme

```
Ligne 1     125 caractères visibles. Rôle A : la demande, simplement.
            Rôle B : l'accroche.
            Jamais une salutation, jamais un hashtag, jamais un emoji en premier caractère.
Corps       paragraphes courts, une ligne vide entre chacun. Deux à six.
            C'est là que vivent les mots recherchés.
La demande  une seule. Commenter un mot-clé, enregistrer, ou écrire en message privé.
Hashtags    cinq maximum, sur leur propre ligne en bas, ou aucun.
```

La limite est de 2 200 caractères et presque rien n'en a besoin. Une légende
qui mérite l'appui puis livre 600 caractères bat celle qui en livre 1 800.

## Les hashtags, honnêtement

Les hashtags ne sont plus un levier de portée. D'après l'auteur du pack
d'origine, **Instagram a plafonné les hashtags à cinq par publication le
18 décembre 2025** (contre trente avant), en conseillant « moins de hashtags,
plus ciblés ». Adam Mosseri avait déjà dit en février 2025 que les hashtags
n'augmentent pas la portée et servent d'étiquette. Si une règle différente
s'applique au moment de l'utilisation, signale-le.

Donc : cinq maximum, précis, comme étiquettes de sujet. `#viral`, `#fyp`,
`#pourtoi`, `#explorepage` ne décrivent rien. Supprime-les.

## Les mots recherchés comptent plus que les hashtags

La recherche Instagram lit le texte de la légende. L'expression sur laquelle
elle veut être trouvée va dans la légende, telle qu'une personne la taperait,
dans une phrase normale. « Stratégie Instagram » en toutes lettres à la ligne
trois, pas « #strategieinstagram » dans un bloc en bas.

Demande-lui deux ou trois de ces expressions, puis passe-les au vérificateur.

## Règles

- **Pas de lien dans la légende.** Les légendes ne sont pas cliquables. Un lien
  dans le texte est du texte mort. Bio ou message privé.
- **Une seule demande.** Deux demandes, c'est comme aucune. `caption.py` les compte.
- **Le mot-clé doit pouvoir se taper.** Un mot, sans espace ni emoji, et dit
  aussi à voix haute dans la vidéo. `Commente CONTRAT` marche.
  `Commente « le guide du contrat »` ne marche pas.
- **S'il y a un lien, écris le premier commentaire à part** et dis-le dans le récapitulatif.
- **Les emoji comme ponctuation, pas comme décoration.** Le vérificateur alerte
  au-delà de 4 pour 100 caractères.
- **Le texte alternatif vaut 20 secondes.** Pour les carrousels et les photos,
  écris-le : il est lu par les lecteurs d'écran et par Instagram.

## La boucle

1. Décide rôle A ou B et dis lequel.
2. Rédige.
3. Passe-la dans `$ig-human`. Les légendes sont courtes, donc les clichés s'y
   entendent plus qu'ailleurs.
4. Lance `caption.py` avec ses mots recherchés. Corrige chaque ÉCHEC. Pour
   chaque ALERTE, décide à voix haute plutôt qu'en silence.
5. Donne le bloc prêt à copier, puis le récapitulatif :

```
LÉGENDE PRÊTE
rôle :       A - le reel porte l'accroche
visible :    118 caractères sur 125 avant la coupure
demande :    une, commenter CONTRAT
hashtags :   3
recherche :  « stratégie instagram » ligne 3, « consultante marketing » ligne 5
contrôle :   PRÊTE
```

Rien n'est publié. Elle colle la légende elle-même.
