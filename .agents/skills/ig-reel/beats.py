#!/usr/bin/env python3
"""
beats.py - transforme un script de Reel en séquencier minuté avant le tournage.

Estime le temps nécessaire pour dire chaque ligne, les empile en timecodes, et
signale les quatre choses qui tuent un Reel au montage : une accroche qui
dépasse trois secondes, un temps assez long pour que le spectateur parte, une
suite de lignes sans rien de concret, et une durée totale qui ne correspond pas
à ce que tu voulais faire.

Les durées sont une estimation à partir du nombre de mots et d'un débit en mots
par minute. C'est assez précis pour préparer un montage, pas pour remplacer
l'enregistrement. Règle ton propre débit avec --wpm une fois que tu t'es
chronométrée en lisant un script à voix haute : la plupart des gens sont entre
150 et 200 ; la valeur par défaut est 165.

Utilisation
  python3 beats.py script.txt
  python3 beats.py script.txt --target 30
  python3 beats.py script.txt --wpm 185 --target 45
  pbpaste | python3 beats.py -
  python3 beats.py script.txt --json
"""

import argparse
import json
import re
import sys

LETTERS = "A-Za-zÀ-ÖØ-öø-ÿŒœÆæ"
WORD_RE = re.compile(rf"[{LETTERS}0-9$€%'’-]+")
SENT_RE = re.compile(r"[^.!?]+[.!?]*")
CONCRETE_RE = re.compile(r"[$€]\s?\d|\b\d[\d,.]*\b|(?<!^)\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]{2,}\b",
                         re.MULTILINE)
STOPWORDS = {
    "le", "la", "les", "l", "un", "une", "des", "de", "du", "d", "et", "ou",
    "mais", "si", "à", "au", "aux", "en", "dans", "sur", "pour", "par", "avec",
    "que", "qu", "qui", "ce", "c", "ça", "cette", "ces", "est", "sont", "était",
    "été", "être", "tu", "te", "t", "ton", "ta", "tes", "vous", "votre", "vos",
    "je", "j", "me", "m", "mon", "ma", "mes", "nous", "notre", "nos", "on",
    "ils", "elles", "il", "elle", "se", "s", "ne", "n", "pas", "plus", "y",
    "a", "ai", "as", "ont", "fait", "faire", "tout", "tous", "très", "bien",
    "juste", "alors", "donc",
    "the", "an", "and", "or", "but", "if", "of", "to", "in", "on", "for",
    "with", "that", "this", "it", "is", "are", "you", "your", "i", "my",
}

HOOK_WINDOW = 3.0        # secondes. Au-delà, le pouce a déjà décidé.
MAX_BEAT = 4.0           # secondes sur une idée sans changement à l'écran.
ABSTRACT_RUN = 3         # temps consécutifs sans rien de vérifiable.


def join_thousands(text):
    """« 18 000 € » se dit comme un seul mot, donc c'en est un ici aussi."""
    return re.sub(r"(?<=\d)[   ,.](?=\d{3}\b)", "", text)


def words(text):
    return WORD_RE.findall(join_thousands(text))


def content_words(text):
    out = set()
    for w in words(text):
        for part in re.split(r"['’]", w.lower()):
            if part and part not in STOPWORDS:
                out.add(part)
    return out


def pretty(token):
    """Remet le séparateur de milliers pour l'affichage."""
    return re.sub(r"(\d)(?=(\d{3})+$)", r"\1 ", token)


def tc(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}"


def split_beats(raw, wps):
    """Une ligne est un temps, sauf si elle est trop longue pour en être un."""
    beats = []
    for line in [l.strip() for l in raw.splitlines()]:
        if not line:
            continue
        if len(words(line)) / wps <= MAX_BEAT * 1.5:
            beats.append(line)
            continue
        # Paragraphe long : on coupe aux fins de phrase pour que les durées
        # aient un sens.
        parts = [p.strip() for p in SENT_RE.findall(line) if p.strip()]
        buf = ""
        for part in parts:
            candidate = (buf + " " + part).strip()
            if buf and len(words(candidate)) / wps > MAX_BEAT:
                beats.append(buf)
                buf = part
            else:
                buf = candidate
        if buf:
            beats.append(buf)
    return beats


def analyse(raw, wpm=165, target=None):
    wps = wpm / 60.0
    beats = split_beats(raw, wps)
    if not beats:
        return None

    rows, clock = [], 0.0
    for i, text in enumerate(beats):
        n = len(words(text))
        dur = n / wps
        rows.append({
            "n": i + 1,
            "start": round(clock, 2),
            "dur": round(dur, 2),
            "words": n,
            "text": text,
            "concrete": len(CONCRETE_RE.findall(join_thousands(text))),
            "label": "",
            "flags": [],
        })
        clock += dur
    total = clock

    # Étiquette les positions autour desquelles un Reel est construit.
    for r in rows:
        if r["n"] == 1 or r["start"] + r["dur"] <= HOOK_WINDOW:
            r["label"] = "ACCROCHE"
    rows[-1]["label"] = "CTA" if rows[-1]["label"] != "ACCROCHE" else "ACC/CTA"
    half = total / 2
    for r in rows:
        if not r["label"] and r["start"] <= half < r["start"] + r["dur"]:
            r["label"] = "MILIEU"

    notes = []
    if rows[0]["dur"] > HOOK_WINDOW:
        rows[0]["flags"].append(f"accroche de {rows[0]['dur']:.1f} s, au-delà de {HOOK_WINDOW:.0f} s")
        notes.append(f"Le temps 1 prend {rows[0]['dur']:.1f} s à dire. Réduis-le à "
                     f"{int(HOOK_WINDOW * wps)} mots maximum, sinon l'accroche arrive après "
                     "que la décision a été prise.")
    if rows[0]["concrete"] == 0:
        notes.append("Le temps 1 ne contient ni chiffre ni nom. Les accroches sans rien de "
                     "vérifiable sont celles qu'on fait défiler.")

    for r in rows:
        if r["dur"] > MAX_BEAT:
            r["flags"].append(f"{r['dur']:.1f} s sur un seul temps")
    long_beats = [r["n"] for r in rows if r["dur"] > MAX_BEAT]
    if long_beats:
        notes.append(f"Temps {', '.join(map(str, long_beats))} : plus de {MAX_BEAT:.0f} s. "
                     "Coupe la ligne en deux ou change ce qui est à l'écran pendant. "
                     "Un plan fixe, c'est là que les gens partent.")

    run, start = 0, None
    for r in rows:
        if r["concrete"] == 0:
            run += 1
            start = start if start is not None else r["n"]
            if run == ABSTRACT_RUN:
                notes.append(f"Temps {start} à {r['n']} : rien de concret. "
                             "Mets un chiffre, un nom ou un prix dans l'un d'eux.")
        else:
            run, start = 0, None

    # La dernière ligne renvoie-t-elle à la première ?
    loop = sorted(pretty(w) for w in content_words(rows[0]["text"]) & content_words(rows[-1]["text"]))
    if loop:
        notes.append(f"Boucle : le dernier temps reprend « {', '.join(loop[:3])} » de l'accroche. "
                     "Les revisionnages, c'est de la portée gratuite.")
    else:
        notes.append("Pas de boucle. Le dernier temps ne partage aucun mot avec l'accroche, la "
                     "vidéo finit à plat. Reprendre un mot du temps 1 est le revisionnage le "
                     "moins cher qui soit.")

    if target:
        delta = total - target
        if abs(delta) <= target * 0.1:
            notes.append(f"Durée dans la cible ({total:.1f} s pour {target:g} s).")
        elif delta > 0:
            notes.append(f"{delta:.1f} s de trop. Coupe environ {int(delta * wps)} mots.")
        else:
            notes.append(f"{-delta:.1f} s de moins que la cible. Ajoute {int(-delta * wps)} mots "
                         "ou tourne court. Court, c'est souvent mieux.")

    return {
        "wpm": wpm, "target": target,
        "total_seconds": round(total, 2),
        "total_words": sum(r["words"] for r in rows),
        "beats": rows,
        "notes": notes,
    }


def render(a, out=sys.stdout):
    head = (f"SÉQUENCIER  ·  {a['total_words']} mots  ·  ~{a['total_seconds']:.1f} s "
            f"à {a['wpm']:g} mots/min" + (f"  ·  cible {a['target']:g} s" if a["target"] else ""))
    print("\n" + head, file=out)
    print("=" * max(len(head), 72), file=out)
    for r in a["beats"]:
        label = f"{r['label']:<9}" if r["label"] else " " * 9
        print(f"  {tc(r['start'])}  {r['dur']:4.1f}s  {label}{r['text']}", file=out)
        for f in r["flags"]:
            print(f"  {'':>6}  {'':>5}  {'':<9}^ {f}", file=out)
    print("-" * max(len(head), 72), file=out)
    for n in a["notes"]:
        print(f"  - {n}", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Minute un script de Reel en séquencier.")
    ap.add_argument("input", nargs="?", default="-", help="fichier du script, ou - pour stdin")
    ap.add_argument("--wpm", type=float, default=165, help="débit en mots/minute (défaut 165)")
    ap.add_argument("--target", type=float, help="durée cible en secondes")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = analyse(raw, wpm=args.wpm, target=args.target)
    if not a:
        print("script vide", file=sys.stderr)
        sys.exit(2)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0)


if __name__ == "__main__":
    main()
