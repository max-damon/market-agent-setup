#!/usr/bin/env python3
"""
caption.py - vérifie une légende Instagram et montre exactement ce que le fil
affiche avant le « … plus ».

Instagram affiche environ 125 caractères de légende dans le fil et cache le
reste derrière un appui. Presque toutes les légendes qui échouent échouent là :
l'accroche est à la troisième phrase, la première ligne est une salutation, ou
tout commence par un hashtag. Ce script affiche la fenêtre visible dans un
cadre pour la lire comme un inconnu qui fait défiler, puis vérifie les points
qui valent la peine d'être vérifiés.

La coupure à 125 caractères est une approximation : elle bouge selon
l'appareil, la taille de police et les retours à la ligne. Garde une marge
plutôt que de viser pile 125. Change-la avec --truncate pour tester plus court.

Utilisation
  python3 caption.py legende.txt
  python3 caption.py legende.txt --keywords "stratégie instagram,consultante marketing"
  pbpaste | python3 caption.py -
  python3 caption.py legende.txt --json
"""

import argparse
import json
import re
import sys
import textwrap

LIMIT = 2200             # Limite stricte d'Instagram pour une légende.
TRUNCATE = 125           # Environ là où le fil coupe en « … plus ».
HASHTAG_LIMIT = 5        # Plafond par publication depuis le 18 décembre 2025
                         # selon l'auteur du pack d'origine (annonce du compte
                         # @Creators : « moins de hashtags (jusqu'à 5), plus
                         # ciblés »). À revérifier si Instagram change la règle.

HASHTAG_RE = re.compile(r"(?:^|\s)(#\w+)")
MENTION_RE = re.compile(r"(?:^|\s)(@[\w.]+)")
LINK_RE = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:fr|com|co|io|net|org|ai|app|be|ch)/\S*",
                     re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿←-⇿️]")
CONCRETE_RE = re.compile(r"[$€]\s?\d|\b\d[\d,.]*\b|(?<!^)\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]{2,}\b",
                         re.MULTILINE)

ASKS = [
    (re.compile(r"(?i)\b(?:comment(?:e|ez)|écri(?:s|vez)) (?:le mot |[«\"“] ?)?[A-ZÀ-Ý0-9]{2,}\b"
                r"|\bcomment (?:the word |\")?[A-Z0-9]{2,}\b"), "commenter un mot-clé"),
    (re.compile(r"(?i)\b(?:écris-moi|écrivez-moi|envoie-moi un (?:dm|message)|en dm|en mp"
                r"|par message|dm me|message me)\b"), "écrire en message privé"),
    (re.compile(r"(?i)\b(?:enregistre|enregistrez|sauvegarde|sauvegardez|garde|gardez) "
                r"(?:ce|cette|ça|le|la|ces)\b|\bsave (?:this|it)\b"), "enregistrer"),
    (re.compile(r"(?i)\b(?:partage|partagez|envoie|envoyez) (?:ce|cette|ça|ce post|à)\b"
                r"|\bshare (?:this|it)\b"), "partager"),
    (re.compile(r"(?i)\b(?:abonne-toi|abonnez-vous|suis-moi|suivez-moi|follow (?:me|for))\b"),
     "s'abonner"),
    (re.compile(r"(?i)\blien (?:en|dans (?:ma|la)) bio\b|\blink in (?:my )?bio\b"), "lien en bio"),
    (re.compile(r"(?i)\b(?:fais défiler|faites défiler|glisse|glissez|swipe)\b"), "faire défiler"),
    (re.compile(r"(?i)\b(?:dis-moi|dites-moi|et toi\s?\?|et vous\s?\?|lequel|laquelle"
                r"|tell me|which one)\b"), "répondre à une question"),
]

FILLER_TAGS = {"#viral", "#fyp", "#explore", "#explorepage", "#foryou", "#foryoupage",
               "#pourtoi", "#pourtoii", "#tendance", "#trending", "#instagood", "#love",
               "#follow", "#like4like", "#reels", "#reelsinstagram", "#reelsfrance",
               "#viralreels", "#instadaily", "#instafrance", "#photooftheday"}


def visible_window(text, cut):
    """Ce que le fil affiche. Instagram coupe au milieu des mots, ce script aussi."""
    flat = text.strip()
    return flat if len(flat) <= cut else flat[:cut]


def render_box(window, truncated, out=sys.stdout, width=52):
    print("\n  CE QUE LE FIL AFFICHE", file=out)
    print("  +" + "-" * (width + 2) + "+", file=out)
    lines = []
    for raw in window.split("\n"):
        lines.extend(textwrap.wrap(raw, width) or [""])
    for line in lines[:8]:
        print(f"  | {line:<{width}} |", file=out)
    tail = "… plus" if truncated else "(la légende tient entière)"
    print("  +" + "-" * (width + 2 - len(tail) - 2) + f" {tail} " + "+", file=out)


def analyse(text, cut=TRUNCATE, keywords=None):
    text = text.rstrip()
    stripped = text.strip()
    chars = len(stripped)
    lines = stripped.split("\n")
    first_line = lines[0].strip() if lines else ""
    tags = HASHTAG_RE.findall(stripped)
    mentions = MENTION_RE.findall(stripped)
    links = LINK_RE.findall(stripped)
    emoji = EMOJI_RE.findall(stripped)
    window = visible_window(stripped, cut)
    truncated = chars > cut
    asks = [name for pattern, name in ASKS if pattern.search(stripped)]
    filler = [t for t in tags if t.lower() in FILLER_TAGS]
    keywords = [k.strip() for k in (keywords or []) if k.strip()]

    checks = []

    def add(name, status, detail):
        checks.append({"check": name, "status": status, "detail": detail})

    add("LONGUEUR", "ÉCHEC" if chars > LIMIT else "OK",
        f"{chars} / {LIMIT} caractères" + (f", {chars - LIMIT} de trop"
                                            if chars > LIMIT else ""))

    if not first_line:
        add("1RE LIGNE", "ÉCHEC", "la légende commence par une ligne vide")
    elif first_line.startswith("#") or first_line.startswith("@"):
        add("1RE LIGNE", "ÉCHEC",
            "commence par un hashtag ou une mention, alors que c'est la seule place qui mérite une phrase")
    elif len(first_line) > cut:
        add("1RE LIGNE", "ALERTE",
            f"{len(first_line)} caractères, donc coupée à {cut} en pleine idée. "
            "Bien si la coupure crée du suspense, mauvais si elle tombe au milieu d'une subordonnée")
    else:
        add("1RE LIGNE", "OK", f"{len(first_line)} caractères, visible en entier")

    concrete = CONCRETE_RE.findall(window)
    add("ACCROCHE CONCRÈTE", "OK" if concrete else "ALERTE",
        f"{len(concrete)} chiffre(s) ou nom(s) dans la partie visible"
        + ("" if concrete else " - rien de vérifiable avant l'appui"))

    if len(tags) > HASHTAG_LIMIT:
        add("HASHTAGS", "ÉCHEC", f"{len(tags)} hashtags, au-delà du plafond de {HASHTAG_LIMIT}. "
                                 "Les suivants ne comptent pas et le bloc fait daté")
    elif len(tags) == HASHTAG_LIMIT and filler:
        add("HASHTAGS", "ALERTE", f"{len(tags)} hashtags, au plafond, dont "
                                  f"{len(filler)} génériques. Utilise les cinq pour des sujets")
    elif filler:
        add("HASHTAGS", "ALERTE", f"{len(tags)} hashtags, dont {len(filler)} génériques "
                                  f"({', '.join(filler[:3])}). Ils ne décrivent rien")
    else:
        add("HASHTAGS", "OK", f"{len(tags)} hashtag(s)" + (f" : {' '.join(tags)}" if tags else ""))

    if not tags:
        add("PLACE DES TAGS", "OK", "aucun hashtag à placer")
    elif any(re.search(r"(?:^|\s)" + re.escape(t) + r"\b", window) for t in tags):
        add("PLACE DES TAGS", "ALERTE", "un hashtag est dans la partie visible : "
                                        "de la place du fil gâchée pour une étiquette")
    else:
        add("PLACE DES TAGS", "OK", "les hashtags sont sous la coupure")

    add("LIENS", "ALERTE" if links else "OK",
        f"{len(links)} lien(s) dans la légende, or les légendes ne sont pas cliquables. "
        f"Mets-le en bio ou en message privé" if links else "aucun lien mort dans le texte")

    if len(asks) == 1:
        add("UNE DEMANDE", "OK", f"un seul appel à l'action : {asks[0]}")
    elif not asks:
        add("UNE DEMANDE", "ALERTE", "aucun appel à l'action. Décide à quoi sert cette publication")
    else:
        add("UNE DEMANDE", "ALERTE", f"{len(asks)} demandes ({', '.join(asks)}). "
                                     "Deux demandes, c'est comme aucune")

    density = len(emoji) * 100 / max(chars, 1)
    add("EMOJI", "ALERTE" if density > 4 else "OK",
        f"{len(emoji)} emoji, {density:.1f} pour 100 caractères"
        + (" - ça fait décoration" if density > 4 else ""))

    if keywords:
        low = stripped.lower()
        found = [k for k in keywords if k.lower() in low]
        missing = [k for k in keywords if k.lower() not in low]
        in_window = [k for k in found if k.lower() in window.lower()]
        status = "OK" if not missing else ("ALERTE" if found else "ÉCHEC")
        add("MOTS RECHERCHÉS", status,
            f"{len(found)}/{len(keywords)} présents"
            + (f", {len(in_window)} dans la partie visible" if found else "")
            + (f". Manquants : {', '.join(missing)}" if missing else ""))

    fails = sum(1 for c in checks if c["status"] == "ÉCHEC")
    warns = sum(1 for c in checks if c["status"] == "ALERTE")
    verdict = "À CORRIGER" if fails else ("À RELIRE" if warns else "PRÊTE")

    return {
        "characters": chars, "limit": LIMIT, "truncate_at": cut,
        "visible": window, "truncated": truncated,
        "first_line_chars": len(first_line),
        "hashtags": tags, "mentions": mentions, "links": links,
        "emoji": len(emoji), "asks": asks,
        "checks": checks, "verdict": verdict,
    }


def render(a, out=sys.stdout):
    head = (f"CONTRÔLE DE LÉGENDE  ·  {a['characters']} / {a['limit']} car.  ·  "
            f"{len(a['hashtags'])} hashtags  ·  {len(a['asks'])} demande(s)")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    render_box(a["visible"], a["truncated"], out=out)
    print("", file=out)
    for c in a["checks"]:
        print(f"  {c['status']:<6} {c['check']:<18} {c['detail']}", file=out)
    print("-" * max(len(head), 62), file=out)
    print(f"  VERDICT  {a['verdict']}\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Vérifie une légende Instagram.")
    ap.add_argument("input", nargs="?", default="-", help="fichier de la légende, ou - pour stdin")
    ap.add_argument("--truncate", type=int, default=TRUNCATE,
                    help=f"caractères affichés avant « … plus » (défaut {TRUNCATE})")
    ap.add_argument("--keywords", default="",
                    help="termes séparés par des virgules sur lesquels tu veux être trouvée")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, cut=args.truncate, keywords=args.keywords.split(","))
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0 if a["verdict"] == "PRÊTE" else 1)


if __name__ == "__main__":
    main()
