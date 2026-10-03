---
name: ig-reel
description: >-
  Écrire un Reel Instagram à partir d'une idée brute : accroches tirées de 26
  formules et notées, script parlé, texte à l'écran et séquencier minuté, dans
  la voix de la personne. À utiliser pour un Reel, un script de vidéo courte,
  une accroche, une voix off, « fais un reel sur… », « qu'est-ce que je dis
  dans cette vidéo », ou juste avant un tournage sans première phrase.
---

# ig-reel

Transforme une idée brute en Reel que les gens regardent jusqu'au bout.

Deux outils sont dans le dossier de ce skill et ils fonctionnent. Utilise-les :
ne juge pas l'accroche à l'œil et ne devine pas la durée.

```bash
python3 <dossier de ce skill>/hookscore.py accroches.txt     # classe les accroches
python3 <dossier de ce skill>/hookscore.py --hook "une phrase"
python3 <dossier de ce skill>/beats.py script.txt --target 30  # séquencier minuté
```

## Fichiers du projet

Les chemins ci-dessous sont relatifs au projet Codex ouvert : le dossier de son
compte personnel, ou le dossier d'un client si elle écrit pour lui.

- `contexte/voix-instagram.md` : la voix (qui parle, à qui, mots interdits).
- `travail/instagram/swipe.md` : ce qui marche dans la niche, écrit par `$ig-viral`.
- `travail/instagram/journal.md` : l'historique des publications validées.

## Avant d'écrire

1. Lis `contexte/voix-instagram.md`. S'il n'existe pas, demande **trois de ses
   propres reels ou légendes**, déduis-en la voix et propose de créer le fichier
   à partir du modèle `MarketAgent/Configuration/templates/instagram/voix-instagram.md`.
   Un script dans la mauvaise voix est inutilisable, parce qu'il faut le dire à
   voix haute.
2. Lis `hooks.json` dans le dossier de ce skill : 26 formules, chacune avec un
   modèle, un exemple, la version écran, son usage et la façon dont on la gâche.
3. Si l'idée est mince, ne la gonfle pas. Pose une seule question groupée : que
   s'est-il passé, à qui, et qu'est-ce que ça a coûté ou rapporté. Un Reel a
   besoin d'une chose précise et vraie. Obtiens-la avant d'écrire.
4. Si `travail/instagram/swipe.md` existe, lis-le : ce sont ses propres
   preuves sur les formules qui marchent dans sa niche en ce moment. Elles
   priment sur les réglages par défaut de ce fichier.

## La forme

Un Reel se décide dans les deux premières secondes et se garde dans les cinq
suivantes.

```
0:00 - 0:02   ACCROCHE    l'affirmation. Phrase dite et phrase écrite, rédigées
                          séparément. Du mouvement dès la première image.
0:02 - 0:07   L'ENJEU     pourquoi ça compte pour la personne qui regarde. Une ligne.
0:07 - ...    LE CORPS    une idée par temps, et l'image change à chaque temps.
3 DERN. s     LA CHUTE    tenir la promesse de l'accroche, puis une seule demande.
DERN. LIGNE   LA BOUCLE   reprendre un mot de l'accroche pour que le revisionnage tombe juste.
```

Durée : 15 à 45 secondes. Les Reels peuvent durer 3 minutes, presque personne
ne devrait s'en servir.

## La boucle de travail

**1. Trois accroches, pas une.** Choisis trois formules de `hooks.json` qui
collent vraiment à l'idée et écris pour chacune la phrase dite et la phrase
écrite. Trois formules différentes, pas trois réécritures.

**2. Note-les.** Mets les trois phrases dites dans un fichier, une par ligne, et
lance `hookscore.py`. Montre le classement. Si la première est sous 50, tu n'as
pas encore l'accroche et aucune retouche n'y changera rien.

**3. Écris le script** sur l'accroche gagnante. Une langue parlée, comme elle
parle vraiment. Des phrases courtes. Aucune phrase qu'elle devrait répéter.

**4. Minute-le.** `beats.py script.txt --target {durée}`. Corrige chaque alerte :
accroche au-delà de 3 secondes, temps de plus de 4 secondes, suite de temps
sans rien de concret, pas de boucle. Relance jusqu'à ce que ce soit propre. Si
elle connaît son débit, ajoute `--wpm`.

**5. Humanise.** Passe le script dans `$ig-human` avant de le montrer. Une
phrase qui sonne écrite se remarque dès qu'on la dit à voix haute.

**6. Présente le bloc.** Le script dans un bloc de code, le texte à l'écran en
liste séparée avec les minutages, puis :

```
REEL PRÊT
accroche :   #3 Personne ne te dit, 86 FORTE
durée :      28,4 s en 9 temps à 165 mots/min
à l'écran :  6 cartons
humanizer :  4 traces retirées, score humain 81 OK
légende :    lance $ig-caption ensuite

Réponds « oui » pour l'enregistrer au journal, ou dis-moi quoi changer.
```

**7. Ne publie jamais.** Ce skill produit un script. Elle tourne et publie. Sur
« oui », ajoute une ligne à `travail/instagram/journal.md` (crée-le si besoin)
avec la date, la formule utilisée et la première phrase, pour que `$ig-audit`
ait un historique.

## Le texte à l'écran est un script à part

Écris-le séparément, à chaque fois. Il est lu avant d'être entendu.

- **Six mots maximum par carton.** Il est lu à bout de bras par quelqu'un qui
  n'écoute pas encore.
- **Le carton d'accroche est là dès la première image**, pas après un silence.
- **Reste dans la zone sûre.** Sur une image 1080x1920, rien au-dessus de
  y=230 ni en dessous de y=1440, et garde libres les 230 pixels de droite.
  L'interface recouvre tout le reste : légende, boutons, bandeau audio.
- **Jamais l'accroche là où se trouve la légende**, en bas de l'image.
- **Sous-titres incrustés pour le corps.** La plupart des gens regardent
  d'abord sans le son.

## Les règles qui font la différence

- **Une idée par Reel.** S'il y en a deux, c'est deux Reels. Dis-le.
- **Des chiffres plutôt que des adjectifs.** « 4 200 € » vaut mieux que
  « beaucoup ». Si elle n'a pas donné de chiffre, demande-le plutôt que d'écrire
  autour du trou.
- **Coupe l'intro.** Pas de salutation, pas de « dans cette vidéo », pas de
  nom, pas de jingle. La vidéo commence à la phrase qu'on atteindrait
  normalement à la sixième seconde.
- **Change d'image à chaque temps.** Un plan fixe de 8 secondes, c'est là que
  les gens partent, et `beats.py` le signalera.
- **Une seule demande à la fin.** Commenter un mot-clé, enregistrer, ou
  s'abonner. Une.
- **N'invente jamais.** Aucun chiffre, client, chiffre d'affaires ou résultat
  inventé sous son nom, même provisoire. S'il faut un chiffre inconnu, laisse
  `{{ton chiffre}}` dans le script et signale-le.
- **Pas de script construit sur un son tendance qu'elle ne peut pas utiliser.**
  Si l'idée a besoin de sa propre voix, dis-le.

## Exemple

```
$ig-reel on est passées de 5 heures à 20 minutes par devis avec un seul modèle
```

```
ACCROCHES  (notées)
  86  FORTE     #5  Le temps compressé  « Mes devis me prenaient cinq heures. Vingt minutes maintenant. »
                                         à l'écran : 5 H -> 20 MIN
  71  FORTE     #1  L'aveu du coût       « Je facturais quatre heures de mise en page par semaine. Pendant deux ans. »
                                         à l'écran : 2 ANS PERDUS
  54  CORRECTE  #9  Le vol autorisé      « Pique-moi le modèle de devis qui a tout changé. »
                                         à l'écran : PIQUE-MOI ÇA

On tourne la #5 : le rapport est crédible, il se lit d'un coup d'œil à
l'écran, et le chiffre est le tien.
```

Les scores ci-dessus sont illustratifs : lance toujours `hookscore.py` sur les
vraies accroches.
