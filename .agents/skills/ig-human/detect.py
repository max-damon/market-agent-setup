#!/usr/bin/env python3
"""
detect.py - un panel de cinq critères qui note à quel point un texte a l'air
écrit par une machine.

Ce que c'est : cinq heuristiques locales inspirées des signaux que mesurent les
détecteurs publics : variation de la longueur des phrases, éléments concrets,
vocabulaire tout fait, empreinte typographique et voix. Tout est calculé sur ta
machine à partir du texte seul. Rien n'est envoyé.

Ce que ce n'est PAS : GPTZero, Originality, Copyleaks, Winston ou Turnitin. Il
n'appelle pas leurs API et ne peut pas promettre leur verdict. Il repère ce
qu'ils repèrent tous, c'est pourquoi corriger ces points fait souvent bouger
leurs scores aussi. C'est la seule affirmation honnête.

Version française : lexique français (slop.json), marqueurs de l'oral français
à la place des contractions anglaises. Les seuils viennent de la version
anglaise et n'ont pas été recalibrés sur un corpus français. Le lexique anglais
d'origine reste disponible : --lexicon slop-en.json.

Chaque critère renvoie un score HUMAIN de 0 à 100. Plus c'est haut, mieux c'est.

Utilisation
  python3 detect.py brouillon.txt
  pbpaste | python3 detect.py -
  python3 detect.py brouillon.txt --json
  python3 detect.py avant.txt apres.txt      # comparer deux versions
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

LETTERS = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(rf"[{LETTERS}']+")
# L'équivalent français des contractions anglaises : les marques de l'oral.
ORAL = re.compile(
    r"\b(?:ça|y a|ya|t'as|t'es|t'étais|j'suis|chui|j'sais|bah|ben|genre|du coup"
    r"|en vrai|trop|carrément|perso|franchement|truc|trucs)\b"
    r"|\b(?:c'est|j'ai|j'avais|t'as|on a|on est|je sais|j'sais|il faut|faut|je suis"
    r"|j'veux|je veux|ça marche|ça sert) (?:pas|plus|jamais|rien)\b"
    r"|\b\w+'(?:s|t|re|ve|ll|d|m)\b",
    re.IGNORECASE)
PRONOUNS = re.compile(
    r"\b(?:je|j|me|m|moi|mon|ma|mes|nous|notre|nos|on|tu|t|te|toi|ton|ta|tes"
    r"|vous|votre|vos|i|me|my|we|us|our|you|your)\b", re.IGNORECASE)
NUMBERS = re.compile(r"\b\d[\d,.]*%?|[$€]\s?\d|\d\s?€")
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]{2,}\b", re.MULTILINE)
# En français, mois et jours n'ont pas de majuscule et les nombres s'écrivent
# souvent en lettres : on les compte comme éléments concrets.
FR_CONCRETE = re.compile(
    r"\b(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre"
    r"|novembre|décembre|lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche"
    r"|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|quinze|vingt"
    r"|trente|quarante|cinquante|soixante|cent|mille|million|millions)\b",
    re.IGNORECASE)


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Ramène la valeur sur 0-100 où `human` -> 100 et `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def norm(text):
    """Apostrophe typographique -> droite, pour que le lexique s'applique."""
    return text.replace("’", "'").replace("‘", "'")


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(norm(text))


def check_burstiness(text):
    """Les humains varient fortement la longueur des phrases. Les modèles écrivent égal."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "trop court pour juger"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"variation {cv:.2f} sur {len(lens)} phrases (viser 0,55 ou plus)"


def check_specificity(text):
    """Chiffres, noms et choses concrètes. Le texte générique est abstrait."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "trop court pour juger"
    per100 = 100 / len(w)
    joined = re.sub(r"(?<=\d)[ \u00a0\u202f,.](?=\d{3}\b)", "", text)   # 4 000 € = un nombre
    hits = (len(NUMBERS.findall(joined)) + len(set(PROPER.findall(text)))
            + len(FR_CONCRETE.findall(text)))
    density = hits * per100
    score = scale(density, human=6.0, machine=0.5)
    return score, f"{hits} éléments concrets, {density:.1f} pour 100 mots (viser 4 ou plus)"


def check_slop(text, lex):
    """Densité de vocabulaire tout fait, d'après le lexique."""
    w = words(text)
    if not w:
        return 50.0, "vide"
    flat = norm(text)
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = re.compile(r"\b" + re.escape(entry["find"]).replace(r"\ ", r"\s+") + r"\b",
                             re.IGNORECASE)
        n = len(pattern.findall(flat))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} expressions toutes faites, {density:.1f} pour 100 mots"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Des caractères qu'un clavier de téléphone ne produit pas.

    Adapté au français : l'apostrophe courbe (’) est produite par le clavier
    iPhone et n'est pas comptée ; l'espace insécable devant ; : ! ? » et après «
    est la typographie française normale et n'est pas comptée non plus.
    """
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    curly = sum(text.count(c) for c in "‘“”")
    ellip = text.count("…")
    nbsp_all = len(re.findall(r"[   ]", text))
    nbsp_fr = len(re.findall(r"[  ](?=[;:!?»])|(?<=«)[  ]", text))
    nbsp = nbsp_all - nbsp_fr
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} invisible(s), {em} tiret(s) cadratin(s), {curly} guillemet(s) anglais courbe(s), "
              f"{ellip} points de suspension typographiques, {nbsp} espace(s) insécable(s) hors typo française")
    return score, detail


def check_voice(text, lex):
    """Marques de l'oral, personne, et les formes par défaut des modèles."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "trop court pour juger"
    flat = norm(text)
    per100 = 100 / len(w)
    oral = len(ORAL.findall(flat)) * per100
    person = len(PRONOUNS.findall(re.sub(r"'", " ", flat))) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(flat))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(oral, human=3.0, machine=0.0) * 0.35
             + scale(person, human=8.0, machine=1.0) * 0.35
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("puces-uniformes")
    detail = (f"{oral:.1f} marques de l'oral, {person:.1f} pronoms personnels "
              f"pour 100 mots, {tells} tournure(s) suspecte(s)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["RYTHME", "CONCRET", "CLICHÉS", "EMPREINTE", "VOIX"]


def run(text, lex):
    results = {
        "RYTHME": check_burstiness(text),
        "CONCRET": check_specificity(text),
        "CLICHÉS": check_slop(text, lex),
        "EMPREINTE": check_fingerprint(text),
        "VOIX": check_voice(text, lex),
    }
    scores = [results[c][0] for c in CHECKS]
    # Le critère le plus faible pèse sur le verdict : un détecteur n'a besoin
    # que d'un signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "OK" if overall >= 70 and min(scores) >= 55 else (
        "À REVOIR" if overall >= 50 else "SIGNALÉ")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "PANEL DE DÉTECTION IA" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'SCORE HUMAIN':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "OK":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Signal le plus faible : {weakest}. Corrige-le en premier.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Note à quel point un texte a l'air écrit par une machine.")
    ap.add_argument("input", nargs="?", default="-", help="fichier, ou - pour stdin")
    ap.add_argument("compare", nargs="?", help="second fichier, pour comparer avant/après")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX, help="chemin du lexique (slop-en.json pour l'anglais)")
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "OK" else 1)


if __name__ == "__main__":
    main()
