#!/usr/bin/env python3
"""Audit the Danish output against the Greek it claims to render.

`check_usfm.py` answers "is the file well-formed". This answers the harder
question: **did the Danish actually carry what the Greek marked?**

The Heb 10:26 defect is the type case. The Greek had `ἑκουσίως` (adverb) *and*
`ἁμαρτανόντων` (present participle); the ESV-style Danish rendered the adverb and
silently dropped the aspect. Nothing in the pipeline could see that, because
nothing in the pipeline had ever been told what the Greek marked. That error was
not a wrong *decision* — it was a **non-decision**, and non-decisions are exactly
what a machine can close off.

Three checks, in descending order of how mechanical they are:

  concordance  Hard. A term ruled in `glossaries/key-terms.tsv` appears in this
               verse's Greek, so the ruled Danish must appear in this verse's
               Danish. Breaking it is legal — 0044, 0101 and 0102 all break
               concordance deliberately — but every break must be declared in
               `glossaries/concordance-exceptions.tsv` **with a decision number**.
               That is the point: drift becomes a logged, justified event.

  features     Advisory. Source-side features Danish loses without a sound:
               perfect and pluperfect tense, present participles (aspect),
               genitive absolutes, middle voice. Emits a review queue, not a
               verdict. A translator must look at each one and decide.

  asymmetry    A smell detector. 0002 forbids the three versions differing about
               what a verse *means*. Where one version carries visibly less than
               the other two, either that is a charter difference or someone lost
               something. Heb 10:26 was visible here too: ESV-style was the only
               one without a durative.

Usage:
    tools/audit_translation.py HEB                    # all checks, all versions
    tools/audit_translation.py HEB --check concordance
    tools/audit_translation.py MRK --version esv --chapter 13
"""
import argparse
import glob
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIONS = ("esv", "niv", "nlt")
GLOSSARY = ROOT / "glossaries" / "key-terms.tsv"
EXCEPTIONS = ROOT / "glossaries" / "concordance-exceptions.tsv"

# A qualifier in the glossary's source column may pin the part of speech, so a
# ruling for one sense of an ambiguous lemma is not applied to another. εὐθύς is
# both "immediately" (adverb) and "straight" (adjective); Mark 1:3 is the latter.
POS_QUALIFIER = {"adv.": "D-", "adj.": "A-", "subst.": "N-", "vb.": "V-"}

# USFM book code -> (morphgnt filename fragment, NT-relative book number)
BOOKS = {
    "MAT": ("61-Mt", 1), "MRK": ("62-Mk", 2), "LUK": ("63-Lk", 3),
    "JHN": ("64-Jn", 4), "ACT": ("65-Ac", 5), "ROM": ("66-Ro", 6),
    "1CO": ("67-1Co", 7), "2CO": ("68-2Co", 8), "GAL": ("69-Ga", 9),
    "EPH": ("70-Eph", 10), "PHP": ("71-Php", 11), "COL": ("72-Col", 12),
    "1TH": ("73-1Th", 13), "2TH": ("74-2Th", 14), "1TI": ("75-1Ti", 15),
    "2TI": ("76-2Ti", 16), "TIT": ("77-Tit", 17), "PHM": ("78-Phm", 18),
    "HEB": ("79-Heb", 19), "JAS": ("80-Jas", 20), "1PE": ("81-1Pe", 21),
    "2PE": ("82-2Pe", 22), "1JN": ("83-1Jn", 23), "2JN": ("84-2Jn", 24),
    "3JN": ("85-3Jn", 25), "JUD": ("86-Jud", 26), "REV": ("87-Re", 27),
}

# Danish function words: never the distinctive part of a ruled rendering.
STOP = set("""og i at for den det de som er en et på til med af om sig har
havde blive bliver blev ikke vi jeg du han hun man der dem sin sit sine vor
vore vort jeres deres ved kan skal vil når hvor så ja jo kun mere dog men
eller også hans hendes være var vær hvad hvem selv alle al alt både over
under efter fra mod ind ud op ned igen dette disse noget nogen nogle""".split())

VOWELS = "aeiouyæøå"

# Danish strong verbs whose consonant skeleton changes: infinitive -> extra
# skeletons the same lemma legitimately appears as. Suffix-stripping and
# prefix-matching both fail on these, so they are listed rather than guessed.
IRREGULAR = {
    "gøre": ("gjort", "gør", "gjorde"), "være": ("var", "er", "vær"),
    "have": ("havde", "haft", "har"), "blive": ("blev", "blevet"),
    "give": ("gav", "givet"), "tage": ("tog", "taget"), "se": ("så", "set"),
    "sige": ("sagde", "sagt"), "komme": ("kom", "kommet"),
    "gå": ("gik", "gået"), "få": ("fik", "fået"), "stå": ("stod", "stået"),
    "bringe": ("bragte", "bragt"), "lægge": ("lagde", "lagt"),
    "sætte": ("satte", "sat"), "vide": ("ved", "vidste", "vidst"),
}


# ----------------------------------------------------------------- source side

def load_greek(book):
    """-> {(chapter, verse): [(text, pos, parsing, lemma), ...]}"""
    frag, ntnum = BOOKS[book]
    matches = glob.glob(str(ROOT / "sources" / "sblgnt" / (frag + "-morphgnt.txt")))
    if not matches:
        sys.exit("ingen MorphGNT-fil for %s (ledte efter %s-morphgnt.txt)"
                 % (book, frag))
    verses = defaultdict(list)
    for line in open(matches[0], encoding="utf-8"):
        parts = line.split()
        if len(parts) < 7:
            continue
        ref = parts[0]
        if int(ref[:2]) != ntnum:
            continue
        key = (int(ref[2:4]), int(ref[4:6]))
        verses[key].append((parts[3], parts[1], parts[2], parts[6]))
    return dict(verses)


def parse_field(parsing):
    """MorphGNT parsing code -> dict. 8 chars: person tense voice mood case
    number gender degree."""
    p = (parsing + "-" * 8)[:8]
    return {"person": p[0], "tense": p[1], "voice": p[2], "mood": p[3],
            "case": p[4], "number": p[5], "gender": p[6]}


# ----------------------------------------------------------------- target side

def strip_markers(text):
    """USFM verse text -> plain Danish, footnotes removed."""
    text = re.sub(r"\\f\s.*?\\f\*", " ", text, flags=re.S)   # notes are not the text
    text = re.sub(r"\\(nd|it|add|fq|bd|wj)\*?\s?", " ", text)
    text = re.sub(r"\\\w+\d?\s?", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_danish(version, book):
    """-> {(chapter, verse): plain Danish}, searching BOOK.usfm and BOOK-*.usfm"""
    out = {}
    paths = sorted((ROOT / version / "translation").glob(book + "*.usfm"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for block in re.split(r"\\c ", text)[1:]:
            chapter = int(block.split(None, 1)[0])
            # split into verses, keeping the marker's number
            pieces = re.split(r"\\v (\d+)", block)[1:]
            for num, body in zip(pieces[::2], pieces[1::2]):
                key = (chapter, int(num))
                out[key] = (out.get(key, "") + " " + strip_markers(body)).strip()
    return out


def clean(word):
    return word.strip(".,;:!?»«()[]—-…·'’").lower()


def forms_of(ruled):
    """A ruled Danish word -> the shapes it may legitimately appear in."""
    base = clean(ruled)
    forms = {base} | set(IRREGULAR.get(base, ()))
    if base.endswith("er") and len(base) > 4:
        # syncopated plural: offer -> ofre, with the doubled consonant simplified
        trunk = base[:-2]
        forms.add(trunk + "re")
        if len(trunk) > 1 and trunk[-1] == trunk[-2]:
            forms.add(trunk[:-1] + "re")
    return {f for f in forms if f}


def common_prefix(a, b):
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def matches(ruled, words, text):
    """Does a ruled Danish word appear in this verse, in any inflection?

    Substring containment plus a common-prefix ratio, which between them cover
    ordinary inflection (synd/synder), derivation (stille/stillet,
    forjættelse/forjættede), compounding (holde/udholdenhed) and syncopated
    plurals (offer/ofre). Deliberately loose: a false pass costs a missed
    finding, a false failure costs trust in the whole check.
    """
    for form in forms_of(ruled):
        if len(form) >= 4 and form in text:
            return True
        need = min(len(form), max(3, int(0.7 * len(form))))
        for word in words:
            if common_prefix(form, clean(word)) >= need:
                return True
    return False


def normalise(text):
    return re.sub(r"\s+", " ", text.lower())


# ------------------------------------------------------------------- glossary

def load_glossary():
    """-> {greek_lemma: {version: [alternative, ...]}}, single-word rows only.

    Multi-word and qualified sources (»κύριος (GT-citat)«, »περὶ ἁμαρτίας«) are
    not machine-checkable against a single MorphGNT lemma and are counted, not
    silently dropped.
    """
    rules, scopes, pos_pins, skipped = (
        defaultdict(lambda: defaultdict(list)), {}, {}, [])
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 8:
            continue
        source = cols[0].strip()
        # a qualified source (»παρρησία (frimodighed)«) still rules the same
        # lemma, so keep the bare Greek head and merge the alternatives
        head = source.split("(")[0].split("+")[0].strip()
        greek = "".join(c for c in head if "GREEK" in unicodedata.name(c, ""))
        if not greek or greek != head or " " in head:
            skipped.append(source)
            continue
        for qual, code in POS_QUALIFIER.items():
            if "(%s)" % qual in source:
                pos_pins[head] = code
        scope = cols[8].strip() if len(cols) > 8 else "standard"
        if scope.startswith("konkordant"):
            spec, _, books = scope.partition("@")
            bound = spec.partition(":")[2]
            scopes[head] = (set(bound.split(",")) if bound else set(VERSIONS),
                            set(books.split(",")) if books else None)
        for version, cell in zip(VERSIONS, cols[3:6]):
            cell = re.sub(r"\([^)]*\)", " ", cell).replace("…", " ").strip()
            if not cell or cell in {"—", "-"}:
                continue
            for alt in cell.split("/"):
                alt = alt.strip()
                if alt and alt not in rules[head][version]:
                    rules[head][version].append(alt)
    # Where the same lemma is ruled more than once, the tool cannot know which
    # context applies — so any ruled rendering counts. Choosing between them is
    # the translator's job; the check only catches a rendering matching *none*.
    return {k: dict(v) for k, v in rules.items()}, scopes, pos_pins, skipped


def load_exceptions():
    """-> {(book, chapter, verse, version, lemma): (decision, reason)}"""
    out = {}
    if not EXCEPTIONS.exists():
        return out
    for line in EXCEPTIONS.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#") or line.startswith("book\t"):
            continue
        cols = line.split("\t")
        if len(cols) < 6:
            continue
        book, ref, version, lemma, decision, reason = [c.strip() for c in cols[:6]]
        chapter, _, verse = ref.partition(".")
        out[(book, int(chapter), int(verse), version, lemma)] = (decision, reason)
    return out


# --------------------------------------------------------------------- checks

def check_concordance(book, greek, danish, rules, scopes, pos_pins, exceptions,
                      chapter_filter, version_filter):
    findings, undeclared, advisory = [], [], []
    for key in sorted(greek):
        chapter, verse = key
        if chapter_filter and chapter != chapter_filter:
            continue
        lemmas = {w[3] for w in greek[key]
                  if pos_pins.get(w[3], w[1]) == w[1]}
        for lemma in sorted(lemmas & set(rules)):
            for version in version_filter:
                alts = rules[lemma].get(version)
                if not alts or key not in danish.get(version, {}):
                    continue
                text = normalise(danish[version][key])
                words = text.split()
                hit = False
                for alt in alts:
                    needed = [w for w in alt.split()
                              if w.lower() not in STOP and len(w) > 1]
                    needed = needed or alt.split()   # ruling is all stopwords
                    if all(matches(n, words, text) for n in needed):
                        hit = True
                        break
                if hit:
                    continue
                declared = exceptions.get((book, chapter, verse, version, lemma))
                if declared:
                    findings.append((key, version, lemma, alts, declared))
                bound, books = scopes.get(lemma, ((), None))
                if version in bound and (books is None or book in books):
                    undeclared.append((key, version, lemma, alts))
                else:
                    advisory.append((key, version, lemma, alts))
    return undeclared, findings, advisory


# Danish cues that a durative/iterative aspect has actually been carried.
# Regexes, because Danish V2 splits the periphrasis: "bliver *vi* ved med at…".
DURATIVE = tuple(re.compile(p) for p in (
    r"\bbliv\w*( \w+)? ved\b", r"\bved med at\b", r"\bigen og igen\b",
    r"\bgang på gang\b", r"\bår efter år\b", r"\bdag efter dag\b",
    r"\buden ophør\b", r"\btil stadighed\b", r"uophørlig", r"\bstadig",
    r"\bfortsat\b", r"vedvarende", r"\bhele tiden\b", r"ustandselig",
    r"\bden ene gang efter den anden\b"))

# Danish cues for a perfect: har/er/havde/var + participle, or the perfect of a
# state. Crude on purpose — this only ranks the queue, it does not decide.
PERFECT = (" har ", " er ", " havde ", " var ", "har ", "er ")


def check_features(greek, danish, chapter_filter, versions):
    """Source-side features Danish drops without a sound -> ranked review queue.

    Deponents are suppressed for the middle-voice check: MorphGNT lists them
    with a middle-shaped lemma (δύναμαι, προσέρχομαι, ἐκδέχομαι), so there is no
    active form to contrast with and nothing for a translator to decide. A middle
    form of a verb whose *lemma* is active (κατηρτίσω from καταρτίζω) is a real
    middle and is kept.
    """
    queue = []
    for key in sorted(greek):
        if chapter_filter and key[0] != chapter_filter:
            continue
        texts = {v: normalise(danish[v].get(key, "")) for v in versions}
        flags = []
        for text, pos, parsing, lemma in greek[key]:
            if pos != "V-":
                continue
            f = parse_field(parsing)
            word = text.strip(".,;:·⸀⸂⸃")
            if f["tense"] in "XY":
                missing = [v for v in versions
                           if texts[v] and not any(c in texts[v] for c in PERFECT)]
                flags.append(("perfektum", word, lemma, missing,
                              "perfektum i græsk"))
            elif f["tense"] == "P" and f["mood"] == "P":
                missing = [v for v in versions
                           if texts[v] and not any(r.search(texts[v])
                                                   for r in DURATIVE)]
                what = ("genitiv absolut, præsens" if f["case"] == "G"
                        else "præsens participium")
                flags.append(("aspekt", word, lemma, missing, what))
            if f["voice"] == "M" and f["mood"] != "-" and not lemma.endswith("μαι"):
                flags.append(("medium", word, lemma, [],
                              "ægte medium (aktivt opslagsord)"))
        if flags:
            queue.append((key, flags))
    return queue


def check_asymmetry(danish, chapter_filter, threshold=0.62):
    """A verse where one version carries visibly less than the other two."""
    out = []
    keys = set()
    for version in VERSIONS:
        keys |= set(danish.get(version, {}))
    for key in sorted(keys):
        if chapter_filter and key[0] != chapter_filter:
            continue
        counts = {v: len(danish[v][key].split())
                  for v in VERSIONS if key in danish.get(v, {})}
        if len(counts) < 3:
            continue
        low = min(counts, key=counts.get)
        others = [c for v, c in counts.items() if v != low]
        if counts[low] < threshold * (sum(others) / len(others)):
            out.append((key, low, counts))
    return out


# ----------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", help="USFM book code, e.g. HEB")
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--version", choices=VERSIONS, action="append")
    ap.add_argument("--check", choices=("concordance", "features", "asymmetry"),
                    action="append")
    args = ap.parse_args()

    book = args.book.upper()
    if book not in BOOKS:
        sys.exit("ukendt bogkode %r" % book)
    checks = args.check or ["concordance", "features", "asymmetry"]
    versions = args.version or list(VERSIONS)

    greek = load_greek(book)
    danish = {v: load_danish(v, book) for v in versions}
    translated = {k for v in versions for k in danish[v]}
    if not translated:
        sys.exit("%s er ikke oversat endnu" % book)
    greek = {k: v for k, v in greek.items() if k in translated}
    rules, scopes, pos_pins, skipped = load_glossary()
    exceptions = load_exceptions()

    scope = "%s%s" % (book, " kap. %d" % args.chapter if args.chapter else "")
    print("== %s — %d oversatte vers, %d maskinkontrollerbare ordbogsopslag "
          "(%d kan ikke maskinkontrolleres)"
          % (scope, len(greek), len(rules), len(skipped)))

    problems = 0

    if "concordance" in checks:
        undeclared, declared, advisory = check_concordance(
            book, greek, danish, rules, scopes, pos_pins, exceptions,
            args.chapter, versions)
        print("\n-- konkordans (%d konkordansbundne opslag; øvrige er "
              "standardgengivelser, hvor afvigelse er normal)" % len(scopes))
        for (ch, v), version, lemma, alts in undeclared:
            print("   ! %d,%-3d %-4s %-14s forventede %s"
                  % (ch, v, version, lemma, " / ".join(alts)))
        problems += len(undeclared)
        if declared:
            print("   %d erklæret brud (med afgørelsesnummer):" % len(declared))
            for (ch, v), version, lemma, _alts, (dec, why) in declared:
                print("     ok %d,%-3d %-4s %-14s %s — %s"
                      % (ch, v, version, lemma, dec, why))
        if not undeclared:
            print("   ingen uerklærede brud på en konkordansbunden regel")
        if advisory:
            per = defaultdict(int)
            for _k, _v, lemma, _a in advisory:
                per[lemma] += 1
            top = ", ".join("%s %d" % kv for kv in
                            sorted(per.items(), key=lambda kv: -kv[1])[:8])
            print("   (%d afvigelser fra en standardgengivelse — ikke fejl; "
                  "hyppigste: %s)" % (len(advisory), top))

    if "features" in checks:
        queue = check_features(greek, danish, args.chapter, versions)
        counts = defaultdict(int)
        for _key, flags in queue:
            for kind, *_ in flags:
                counts[kind] += 1
        print("\n-- kildesidige træk til gennemsyn (%s)"
              % ", ".join("%s: %d" % kv for kv in sorted(counts.items())))
        print("   »intet spor i« = versioner hvor dansken ikke viser nogen"
              " markør for trækket; det er ikke nødvendigvis en fejl.")
        for (ch, v), flags in queue:
            for kind, word, lemma, missing, note in flags:
                tail = ("intet spor i: " + " ".join(missing)) if missing else ""
                print("   ? %d,%-3d %-9s %-16s %-13s %-22s %s"
                      % (ch, v, kind, word, lemma, note, tail))

    if "asymmetry" in checks:
        rows = check_asymmetry(danish, args.chapter)
        print("\n-- asymmetri mellem versionerne")
        for (ch, v), low, counts in rows:
            print("   ? %d,%-3d %s bærer mindst (%s)"
                  % (ch, v, low,
                     ", ".join("%s %d" % (k, counts[k]) for k in VERSIONS
                               if k in counts)))
        if not rows:
            print("   ingen udslag")

    print("\n%s" % ("UERKLÆREDE KONKORDANSBRUD: %d" % problems if problems
                    else "INGEN UERKLÆREDE BRUD"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
