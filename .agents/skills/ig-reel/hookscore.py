#!/usr/bin/env python3
"""
hookscore.py - note la première phrase d'un Reel sur les cinq propriétés que
partagent les bonnes accroches, et classe un lot d'accroches entre elles.

Ce que c'est : cinq heuristiques locales, calculées sur ta machine à partir du
texte seul. Elles mesurent ce que les accroches qui retiennent l'attention ont
en commun : une longueur qui se dit en moins de trois secondes, un élément
concret, un enjeu, l'information utile au début plutôt qu'à la fin, et un
spectateur à qui l'on parle.

Ce que ce n'est PAS : un prédicteur de vues. La version anglaise d'origine a
été testée sur 74 vraies accroches : elle distingue bien une vraie accroche
d'une accroche volontairement mauvaise (AUC 0,83), mais presque pas les succès
d'un créateur de ses échecs (AUC 0,56, où 0,50 est le hasard). Cette version
française reprend la même logique avec des listes de mots françaises ; elle n'a
pas été recalibrée sur un corpus français.

Utilise-la pour ce qu'elle mesure bien : elle repère les salutations, les
préambules, les accroches sans rien de concret et celles qui prennent cinq
secondes à dire. Elle ne dira pas laquelle de deux accroches correctes
marchera : ça dépend du visage, du montage, du son et de la diffusion. Fais
plus confiance au graphique de rétention qu'à ce script.

Chaque critère renvoie 0 à 100. Plus c'est haut, mieux c'est.

Utilisation
  python3 hookscore.py accroches.txt          # une accroche par ligne, classées
  python3 hookscore.py --hook "18 000 €, c'est ce que m'a coûté une clause."
  pbpaste | python3 hookscore.py -
  python3 hookscore.py accroches.txt --json
"""

import argparse
import json
import re
import statistics
import sys

LETTERS = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"
WORD_RE = re.compile(rf"[{LETTERS}0-9$€%'’-]+")
NUMBER_RE = re.compile(
    r"[$€]\s?\d+(?:[.,]\d+)?"                              # 18000 €, $500
    r"|\b\d+(?:[.,]\d+)?\s?"                               # un chiffre, avec
    r"(?:%|k€|m€|€|k\b|x\b|h\b|min\b|s\b|euros?\b"          # ou sans unité
    r"|heures?\b|minutes?\b|secondes?\b|jours?\b|semaines?\b|mois\b|ans\b|années?\b"
    r"|hrs?\b|hours?\b|mins?\b|days?\b|weeks?\b|months?\b|years?\b)?",
    re.IGNORECASE)
PROPER_RE = re.compile(r"(?<!^)\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]{2,}\b")
HASHTAG_RE = re.compile(r"(?:^|\s)#\w+")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")

# Les accroches parlées disent leurs nombres à voix haute. « Zéro euro » et
# « vingt mille » sont aussi concrets que « 0 € » et « 20 000 € ».
# « un » et « premier » sont volontairement absents : ce sont des mots vides
# bien plus souvent que des quantités.
SPOKEN_NUMBERS = {
    "zéro", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
    "dix", "onze", "douze", "quinze", "vingt", "trente", "quarante",
    "cinquante", "soixante", "cent", "cents", "mille", "million", "millions",
    "milliard", "milliards", "douzaine", "moitié", "double", "triple",
    # anglais, pour les accroches relevées dans des comptes anglophones
    "zero", "two", "three", "four", "five", "ten", "twenty", "hundred",
    "thousand", "half", "twice",
}
MONEY_WORDS = {
    "euros", "euro", "balles", "k€", "ca", "chiffre", "bénéfice", "bénéfices",
    "salaire", "loyer", "marge", "facture", "factures", "devis", "tarif",
    "tarifs", "prix", "budget", "remboursement",
    "dollars", "dollar", "bucks", "grand", "percent", "revenue", "profit",
}

# Les mots qui mettent quelque chose en jeu. Une accroche sans aucun de ces
# mots est un constat ; avec un seul, c'est une raison de continuer à regarder.
STAKES = {
    "arrête", "arrêtez", "stop", "jamais", "faux", "fausse", "erreur", "erreurs",
    "perdu", "perdue", "perdre", "perds", "perte", "coûté", "coûte", "coûter",
    "cassé", "raté", "ratée", "rate", "échec", "échoué", "personne", "rien",
    "ne", "n", "pas", "viré", "virée", "supprimé", "supprimée",
    "supprime", "tué", "remplacé", "remplace", "gratuit", "gratuite", "payé",
    "payée", "facturé", "embauché", "économisé", "économiser", "premier",
    "première", "interdit", "illégal", "pire", "déteste", "détesté",
    "gaspillé", "gaspiller", "arnaque", "mensonge", "menti", "mens", "vérité",
    "secret", "caché", "cachée", "volé", "avant", "jusqu'à", "lieu", "mais",
    "sauf", "problème", "risque", "danger", "attention", "regret", "regrette",
    "aurais", "devrais", "encore", "déjà", "seulement", "seule", "seul", "sans",
    "contre", "vs", "vraiment", "oublie", "oubliez", "refusé", "refuse",
    "annulé", "annule", "faillite", "burn-out", "honte", "travers", "mal",
    # anglais
    "never", "wrong", "mistake", "lost", "lose", "cost", "failed", "nobody",
    "not", "don't", "dont", "free", "worst", "truth", "without",
}

# Les ouvertures qui dépensent la première seconde à ne rien dire.
WEAK_OPENERS = [
    "alors", "bon", "ok", "okay", "salut", "coucou", "hello", "bonjour",
    "bonsoir", "hey", "yo", "les amis", "les filles", "aujourd'hui",
    "aujourd’hui", "en gros", "honnêtement", "franchement", "écoute",
    "écoutez", "euh", "juste", "bref", "donc", "je voulais", "je veux",
    "j'ai envie", "j’ai envie", "petit", "petite", "l'une des", "l’une des",
    "un des", "une des", "est-ce que", "est-ce qu", "vous avez", "tu as",
    "as-tu", "avez-vous", "dans cette", "dans ce", "il y a", "c'est",
    "c’est", "ceci est", "voici", "en tant que", "quand on", "si tu as",
    "si vous avez", "tu sais", "vous savez", "on va parler", "parlons",
    "laissez-moi", "laisse-moi",
    # anglais
    "so", "hi", "guys", "today", "basically", "honestly", "just",
    "let's", "lets", "i wanted", "in this", "this is", "you know",
]

# Les impératifs qui méritent la première place.
IMPERATIVES = {
    "arrête", "arrêtez", "stop", "vole", "volez", "pique", "piquez", "copie",
    "copiez", "supprime", "supprimez", "essaie", "essaye", "essayez",
    "regarde", "regardez", "lis", "lisez", "garde", "gardez", "enregistre",
    "enregistrez", "sauvegarde", "utilise", "utilisez", "construis",
    "construisez", "fais", "faites", "écris", "écrivez", "envoie", "envoyez",
    "prends", "prenez", "commence", "commencez", "quitte", "quittez",
    "jamais", "toujours", "mets", "mettez", "vérifie", "vérifiez", "oublie",
    "oubliez", "évite", "évitez", "teste", "testez", "note", "notez",
    "retiens", "retenez", "ne",
    "steal", "copy", "try", "watch", "save", "use", "never", "always",
}

SECOND_PERSON_RE = re.compile(
    r"\b(?:tu|te|toi|ton|ta|tes|vous|votre|vos|you|your|yourself)\b|\bt['’]",
    re.IGNORECASE)
FIRST_PERSON_RE = re.compile(
    r"\b(?:je|me|moi|mon|ma|mes|nous|notre|nos|on|i|my|we|our)\b|\b[jm]['’]",
    re.IGNORECASE)

DEALBREAKERS = [
    (re.compile(r"(?i)^\s*(?:stop[ ,!.]|arr[êe]te[sz]? de scroller|ne scrolle[sz]? pas"
                r"|stop scrolling|don'?t scroll)"),
     "Ouvre sur « arrête de scroller ». Demander l'attention prouve qu'on ne l'a pas méritée."),
    (re.compile(r"(?i)\b(?:dans (?:cette|la) (?:vid[ée]o|reel)|dans le reel d'aujourd'hui"
                r"|(?:aujourd['’]hui,? )?je vais (?:te|vous) (?:montrer|expliquer|apprendre)"
                r"|in (?:this|today'?s) (?:video|reel)|i'?m going to show you)\b"),
     "Préambule de vidéo. Supprime-le et ouvre directement sur le résultat."),
    (re.compile(r"(?i)^\s*(?:salut|coucou|hello|bonjour|bonsoir|hey|yo|hi)\b"),
     "Salutation. Personne n'est venu sur le fil pour être salué."),
    (HASHTAG_RE,
     "Hashtag dans l'accroche. Les hashtags vont en bas de la légende, si tant est qu'ils servent."),
    (EMOJI_RE,
     "Emoji dans l'accroche. À cette taille de texte, il y a la place pour des mots "
     "ou pour un emoji, pas les deux."),
]


def clamp(n):
    return max(0.0, min(100.0, n))


def join_thousands(text):
    """« 18 000 », « 18 000 » et « 18,000 » se disent comme un seul mot."""
    return re.sub(r"(?<=\d)[   ,.](?=\d{3}\b)", "", text)


def words(text):
    return WORD_RE.findall(join_thousands(text))


def tokens(text):
    """Mots en minuscules, élisions séparées : « j'ai » donne aussi « j » et « ai »."""
    out = []
    for w in words(text):
        low = w.lower().strip("'’")
        out.append(low)
        if "'" in low or "’" in low:
            out.extend(p for p in re.split(r"['’]", low) if p)
    return out


def check_length(text):
    """Une accroche doit arriver avant que le pouce ne bouge. Environ deux secondes."""
    n = len(words(text))
    secs = n / 2.75                      # ~165 mots par minute, à l'oral
    chars = len(text.strip())
    if 5 <= n <= 12:
        score = 100.0
    elif n < 5:
        score = clamp(100 - (5 - n) * 20)
    else:
        score = clamp(100 - (n - 12) * 11)
    if chars > 60:                       # deux lignes de gros texte à l'écran
        score -= 12
    return clamp(score), f"{n} mots, {chars} caractères, ~{secs:.1f} s à l'oral (viser 5 à 12 mots)"


def check_specificity(text):
    """Une chose concrète vaut mieux que trois abstraites."""
    nums = [n.strip() for n in NUMBER_RE.findall(join_thousands(text)) if n.strip()]
    propers = set(PROPER_RE.findall(text))
    spoken = [w for w in tokens(text) if w in SPOKEN_NUMBERS or w in MONEY_WORDS]
    hits = len(nums) + len(propers) + len(spoken)
    score = 15.0 if hits == 0 else clamp(45 + hits * 30)
    found = ", ".join(nums[:2] + sorted(propers)[:2] + spoken[:2])
    return score, (f"{hits} élément(s) concret(s)" + (f" : {found}" if found else
                   " - ni chiffre, ni nom, rien de vérifiable"))


def check_stakes(text):
    """Tension, coût, négation. Quelque chose que le spectateur pourrait perdre."""
    negation = {"ne", "n", "pas"}            # « ne … pas » est une seule négation
    markers = sorted({("négation" if x in negation else x)
                      for x in tokens(text) if x in STAKES})
    if re.search(r"[$€]\s?\d|\d\s?(?:€|euros?)", join_thousands(text), re.IGNORECASE):
        markers.append("un prix")
    n = len(markers)
    score = {0: 20.0, 1: 70.0}.get(n, 100.0)
    detail = f"{n} marqueur(s) de tension" + (f" : {', '.join(markers[:4])}" if markers else
                                              " - rien n'est en jeu dans cette phrase")
    return clamp(score), detail


def check_frontload(text):
    """Le mot intéressant ne peut pas être en neuvième position."""
    w = words(text)
    if not w:
        return 0.0, "vide"
    low = [x.lower().strip("'’") for x in w]
    opener = " ".join(low[:3])
    penalty = 0
    hit_opener = None
    for weak in WEAK_OPENERS:
        if low[0] == weak or opener == weak or opener.startswith(weak + " "):
            penalty, hit_opener = 30, weak
            break
    payload = None
    for i, token in enumerate(low):
        parts = [token] + [p for p in re.split(r"['’]", token) if p]
        if (any(p in STAKES or p in SPOKEN_NUMBERS or p in MONEY_WORDS for p in parts)
                or NUMBER_RE.match(w[i]) or (i and PROPER_RE.match(w[i]))):
            payload = i
            break
    if payload is None:
        base = 30.0
        where = "aucun mot fort dans toute la phrase"
    elif payload <= 3:
        base = 100.0
        where = f"mot fort en position {payload + 1}"
    elif payload <= 6:
        base = 70.0
        where = f"mot fort en position {payload + 1}, pourrait remonter"
    else:
        base = 40.0
        where = f"mot fort en position {payload + 1}, trop tard"
    detail = where + (f" ; ouverture faible « {hit_opener} »" if hit_opener else "")
    return clamp(base - penalty), detail


def check_address(text):
    """Adressée à un spectateur, ou flottant dans le vide."""
    low = [x.lower().strip("'’") for x in words(text)]
    if SECOND_PERSON_RE.search(text):
        return 100.0, "parle au spectateur"
    if low and low[0] in IMPERATIVES:
        return 90.0, f"ouvre sur un impératif (« {low[0]} »)"
    if FIRST_PERSON_RE.search(text):
        return 70.0, "première personne, aucun spectateur nommé"
    return 35.0, "troisième personne, personne dans la pièce"


CHECKS = ["LONGUEUR", "CONCRET", "ENJEU", "ATTAQUE", "ADRESSE"]


def run(text):
    results = {
        "LONGUEUR": check_length(text),
        "CONCRET": check_specificity(text),
        "ENJEU": check_stakes(text),
        "ATTAQUE": check_frontload(text),
        "ADRESSE": check_address(text),
    }
    flags = [msg for pattern, msg in DEALBREAKERS if pattern.search(text)]
    scores = [results[c][0] for c in CHECKS]
    # La propriété la plus faible plafonne l'accroche : un seul défaut suffit
    # pour que le pouce continue de défiler.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4 - len(flags) * 15
    overall = clamp(overall)
    verdict = "FORTE" if overall >= 70 and min(scores) >= 55 and not flags else (
        "CORRECTE" if overall >= 50 else "FAIBLE")
    return results, overall, verdict, flags


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render_one(text, results, overall, verdict, flags, out=sys.stdout):
    print("\nSCORE D'ACCROCHE", file=out)
    print("=" * 62, file=out)
    print(f"  « {text.strip()} »\n", file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    for f in flags:
        print(f"\n  RÉDHIBITOIRE  {f}", file=out)
    if verdict != "FORTE":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Point le plus faible : {weakest}. Corrige-le et relance.", file=out)
    print("", file=out)


def render_table(rows, out=sys.stdout):
    print("\nCLASSEMENT DES ACCROCHES\n" + "=" * 78, file=out)
    for i, r in enumerate(rows, 1):
        mark = "->" if i == 1 else "  "
        hook = r["hook"] if len(r["hook"]) <= 62 else r["hook"][:59] + "..."
        print(f"{mark} {r['score']:5.1f} {r['verdict']:<8} {hook}", file=out)
        print(f"        plus faible : {r['weakest']} ({r['checks'][r['weakest']]['score']:.0f})",
              file=out)
        for f in r["flags"]:
            print(f"        rédhibitoire : {f}", file=out)
    print("\nTourne la première. Si la première est sous 50, aucune n'est la bonne accroche.\n",
          file=out)


def main():
    ap = argparse.ArgumentParser(description="Note une accroche de Reel sur cinq propriétés.")
    ap.add_argument("input", nargs="?", default="-",
                    help="fichier avec une accroche par ligne, ou -")
    ap.add_argument("--hook", help="noter une seule accroche passée en ligne de commande")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.hook:
        lines = [args.hook]
    else:
        raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
    if not lines:
        print("rien à noter", file=sys.stderr)
        sys.exit(2)

    payload = []
    for line in lines:
        results, overall, verdict, flags = run(line)
        payload.append({
            "hook": line,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "weakest": min(CHECKS, key=lambda c: results[c][0]),
            "flags": flags,
            "score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if len(payload) > 1 else payload[0], indent=2, ensure_ascii=False))
        return

    if len(payload) == 1:
        results, overall, verdict, flags = run(lines[0])
        render_one(lines[0], results, overall, verdict, flags)
    else:
        render_table(sorted(payload, key=lambda r: -r["score"]))

    sys.exit(0 if max(p["score"] for p in payload) >= 70 else 1)


if __name__ == "__main__":
    main()
