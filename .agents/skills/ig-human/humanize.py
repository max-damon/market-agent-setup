#!/usr/bin/env python3
"""
humanize.py - retire l'empreinte machine d'un brouillon.

Trois passes, dans cet ordre :

  1. INVISIBLES   supprime ou normalise les caractères qu'un clavier ne
                  produit jamais : espaces de largeur nulle, liants, traits
                  d'union conditionnels, BOM, caractères d'étiquette Unicode,
                  espaces insécables et fines. Ils survivent au copier-coller
                  et sont la trace la plus mécanique d'un texte généré.
  2. TYPOGRAPHIE  tiret cadratin -> virgule, tiret demi-cadratin -> trait
                  d'union, apostrophes et guillemets anglais courbes -> droits,
                  points de suspension -> trois points, puce -> tiret. Les
                  guillemets français « » ne sont pas touchés.
  3. LEXIQUE      remplace le vocabulaire tout fait de slop.json par des mots
                  simples, en gardant les majuscules et sans toucher aux liens.

Les tournures suspectes (énumération en trois temps, « ce n'est pas juste X,
c'est Y », murs de hashtags) sont SIGNALÉES, jamais réécrites automatiquement :
changer la forme d'une phrase demande du jugement, c'est le travail du modèle
ou de l'autrice, pas d'une expression régulière.

Utilisation
  python3 humanize.py brouillon.txt
  python3 humanize.py brouillon.txt --report
  pbpaste | python3 humanize.py - --report
  python3 humanize.py brouillon.txt --json
  python3 humanize.py brouillon.txt -o propre.txt
  python3 humanize.py draft.txt --lexicon slop-en.json   # texte en anglais
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
LOWER = "a-zà-öø-ÿœæ"
LETTER = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    """'U+200B' -> 0x200b ;  'U+E0000-U+E007F' -> (début, fin)."""
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def protect_urls(text):
    """Remplace les liens par des repères pour qu'aucune passe ne les modifie."""
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


def pass_invisible(text, lex):
    """Supprime ou remplace par une espace les caractères invisibles."""
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": "supprimé" if entry["action"] == "delete" else "espace normale"})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    # Tout caractère de format (Cf) restant est invisible par définition.
    stray = [c for c in text if unicodedata.category(c) == "Cf"]
    if stray:
        hits.append({"name": "autres caractères de format invisibles", "count": len(stray),
                     "action": "supprimé"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf")
    return text, hits


def pass_typographic(text, lex):
    hits = []
    for entry in lex["typographic"]:
        ch = entry["from"]
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch} {entry['name']}", "count": n,
                     "to": entry["to"].strip() or "(espace)"})
        if ch == "—":
            # « mot — mot » et « mot—mot » deviennent une virgule et une espace.
            text = re.sub(r"\s*—\s*", ", ", text)
        elif ch == "–":
            text = re.sub(r"\s*–\s*(?=\d)", "-", text)      # 5–10  -> 5-10
            text = re.sub(r"\s+–\s+", ", ", text)            # employé comme cadratin
            text = text.replace("–", "-")
        else:
            text = text.replace(ch, entry["to"])
    # Une virgule insérée devant une ponctuation existante sonne faux.
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*\n", "\n", text)
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


def pass_lexical(text, lex):
    """Remplace mots et expressions toutes faites. Les plus longs d'abord."""
    hits = []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"]), reverse=True)
    for entry in entries:
        find = entry["find"]
        pattern = re.compile(r"\b" + re.escape(find).replace(r"\ ", r"\s+") + r"\b",
                             re.IGNORECASE)
        found = pattern.findall(text)
        if not found:
            continue
        hits.append({"find": find, "replace": entry["replace"] or "(supprimé)",
                     "count": len(found), "family": entry["family"]})
        text = pattern.sub(lambda m: _match_case(m.group(0), entry["replace"]), text)
    # Nettoyage après suppression : une proposition supprimée laisse de la
    # ponctuation orpheline, ce qui se lit plus mal que le cliché d'origine.
    # En français, l'espace avant ; : ! ? est conservée.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?m)^[ \t]*(?:[,.;:]+[ \t]*)+", "", text)
    text = re.sub(r"(?m)^[ \t](?=\S)", "", text)
    text = re.sub(r"\s+([,.])", r"\1", text)
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = text.replace("...", "\x00ELL\x00")          # protège les vrais points de suspension
    text = re.sub(r"\.\s*\.+", ".", text)
    text = re.sub(r"([!?])\s*\.", r"\1", text)
    text = text.replace("\x00ELL\x00", "...")
    text = re.sub(r"(?m)^[ \t]+$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Un tiret devenu virgule suivi d'un connecteur laisse une phrase soudée
    # (« c'est important, donc, c'est la preuve »). On en fait un point.
    text = re.sub(r",\s*(aussi|donc|pourtant|au final|en gros|bref|also|so|still)\s*,\s*",
                  lambda m: ". " + m.group(1)[0].upper() + m.group(1)[1:] + ", ", text)
    return text, hits


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    # L'uniformité de longueur des phrases est aussi une tournure.
    lens = [len(s.split()) for s in SENT_RE.findall(text) if len(s.split()) > 2]
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": f"Phrases de longueur uniforme (variation {cv:.2f})",
                "count": len(lens),
                "fix": "Coupe une phrase en deux. Laisse une autre s'allonger. Les machines écrivent égal.",
            })
    return flags


def restore_capitals(original, text):
    """Supprimer une ouverture laisse le mot suivant en minuscule.

    Ne corrige que pour qui met des majuscules en début de phrase : une voix
    volontairement en minuscules est un style, pas un défaut.
    """
    starts = re.findall(rf"(?:^|[.!?]\s+|\n)\s*([{LETTER}])", original)
    if not starts or sum(1 for c in starts if c.isupper()) * 2 < len(starts):
        return text
    return re.sub(rf"(?:^|(?<=[.!?] )|(?<=[.!?]\n)|(?<=\n))\s*([{LOWER}])",
                  lambda m: m.group(0)[:-1] + m.group(1).upper(), text)


def humanize(text, lex):
    raw_for_case = text
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex)
    text, lexi = pass_lexical(text, lex)
    text = restore_capitals(raw_for_case, text)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "structures": scan_structures(text, lex),
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])

    head("RAPPORT D'HUMANISATION")
    print(f"{total} trace(s) machine retirée(s), "
          f"{len(report['structures'])} tournure(s) signalée(s) à réécrire", file=out)

    if report["invisible"]:
        head("1. CARACTÈRES INVISIBLES")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TYPOGRAPHIE")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. CLICHÉS")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["structures"]:
        head("4. TOURNURES SUSPECTES  (non corrigées : à réécrire toi-même)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("PROPRE")
        print("  Rien à retirer.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Retire l'empreinte machine d'un brouillon.")
    ap.add_argument("input", nargs="?", default="-", help="fichier, ou - pour stdin")
    ap.add_argument("-o", "--out", help="écrire le texte nettoyé ici plutôt que sur la sortie")
    ap.add_argument("--report", action="store_true", help="afficher ce qui a changé (sur stderr)")
    ap.add_argument("--json", action="store_true", help="sortie {text, report} en JSON")
    ap.add_argument("--lexicon", default=LEX, help="chemin du lexique (slop-en.json pour l'anglais)")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"écrit dans {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
