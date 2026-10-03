---
name: ig-carousel
description: >-
  Construire un carrousel Instagram : la couverture qui donne envie de faire
  défiler, le texte diapositive par diapositive, et les fichiers 1080x1350 à
  publier. À utiliser pour « carrousel », « slides », « post à faire défiler »,
  « transforme ça en carrousel », ou une idée en liste ou en étapes qui
  mourrait en image seule.
---

# ig-carousel

Le carrousel est le format où l'on reste le plus longtemps sur la grille, parce
qu'un glissement est une interaction et un défilement ne l'est pas. Il a aussi
une seconde chance : Instagram peut le remontrer à partir d'une diapositive
suivante à quelqu'un qui n'a pas interagi la première fois, donc la
diapositive deux doit tenir seule elle aussi.

Le format récompense une idée découpée en étapes. Il punit une légende coupée
en morceaux.

Si `contexte/voix-instagram.md` existe dans le projet ouvert, lis-le avant
d'écrire.

## Quand le préférer à un Reel

Carrousel quand l'idée a **une suite et mérite d'être relue** : des étapes, une
méthode en plusieurs parties, un avant/après, une liste qu'on a envie de
capturer. Reel quand l'idée a du mouvement, un visage, ou une chute qu'il faut
voir arriver.

Si l'idée tient en une affirmation, ce n'est ni l'un ni l'autre : passe-la à
`$ig-reel` et dis-le.

## Structure

6 à 10 diapositives. Le maximum est 20, et 20 est presque toujours un livre que
personne ne finit. Sous 5, le glissement ne démarre jamais.

```
1         COUVERTURE  l'accroche. 6 mots maximum, lisible en miniature dans la
                      grille. Une ligne de promesse en dessous.
2         L'ENJEU     pourquoi ça compte, en une phrase. C'est aussi une seconde
                      couverture, donc pas de mise en place.
3 à N     UNE IDÉE PAR DIAPO. Un titre de 3 à 7 mots, 25 mots maximum en dessous.
                      Si une diapo a besoin d'un paragraphe, c'est deux diapos.
N+1       RÉCAP       tout en une liste. C'est la diapo qu'on capture.
DERNIÈRE  CTA         une action. Enregistrer, commenter un mot-clé, ou s'abonner. Une.
```

## Règles de texte

- **La couverture fait 80 % du résultat.** Six mots. Gros. Rien ne sauve une
  couverture que personne ne fait défiler.
- **Pense au recadrage de la grille.** La grille du profil recadre en portrait,
  et le ratio exact a déjà changé. Construis en 1080x1350 et garde le texte de
  couverture bien au centre, à plus de 120 pixels de chaque bord.
- **Numérote les diapos** (3/8). On va plus souvent au bout quand on voit la fin.
- **Aucune diapo n'est un paragraphe.** Si ça ne tient pas en 25 mots, coupe.
- **La diapo récap est celle qu'on capture et qu'on envoie.** Les envois sont
  le signal le plus fort qu'on puisse obtenir. Elle doit se lire seule.
- **L'identifiant sur chaque diapo**, petit, dans un coin en bas. Les captures
  voyagent sans toi.
- **Texte alternatif au moins sur la couverture.**

## Fabriquer les fichiers

Instagram attend du 1080x1350 (4:5), en JPEG ou PNG, jusqu'à 20 éléments.

Dans son setup, la voie normale est **Canva** : si le plugin Canva est connecté,
cherche son modèle de carrousel (ou son kit de marque), crée une **copie** et
remplis-la, puis montre le lien du brouillon. Ne modifie jamais le modèle
d'origine. Sans Canva, construis en HTML (`width:1080px; height:1350px`, une
`<section>` par diapo, une seule couleur d'accent, texte de 32 px minimum) et
exporte chaque diapo en image. Si le projet a une charte, utilise-la ; n'invente
pas de palette.

## Résultat

D'abord le texte diapo par diapo, en liste numérotée lisible en dix secondes et
modifiable avant toute mise en forme. Ensuite la **légende**, qui pour un
carrousel est un rôle B dans `$ig-caption` : la légende travaille, parce que la
couverture a déjà utilisé ses six mots.

Passe les deux dans `$ig-human`. Ne fabrique les fichiers qu'une fois le texte
validé.

```
CARROUSEL  ·  8 diapos

1  COUVERTURE  LA CLAUSE À 4 000 €
               La ligne que je mets maintenant dans chaque contrat.
2  ENJEU       J'avais validé le travail. Neuf jours après, ils ont demandé à être remboursés.
3              CE QU'ELLE DIT
               Paiement à la livraison, pas à la validation.
...
7  RÉCAP       Les quatre lignes, dans l'ordre.
8  CTA         Commente CONTRAT et je t'envoie la clause complète.

Légende : rôle B, accroche en ligne 1, une demande, 3 hashtags.
```

Rien n'est publié. Elle publie elle-même.
