#!/usr/bin/env python3
"""Print a chapter as the three versions in parallel, verse by verse.

Decision 0116: no automated check can see a *meaning* divergence between the
three versions, which is the one thing 0002 absolutely forbids. Mark 14:41 got
through `check_usfm.py`, the concordance check and the asymmetry check because
all three renderings were the right length and used the ruled vocabulary — one
was an imperative and two were questions. Reading them side by side is the only
control we have.

    tools/parallel.py MRK 14
    tools/parallel.py MRK 14 --width 100
    tools/parallel.py HEB 10 --notes      # include footnote text
"""
import argparse
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_translation import VERSIONS, load_danish, strip_markers  # noqa: E402

import re  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def load_raw(version, book):
    """Verses with footnotes left in, so --notes can show them."""
    out = {}
    for path in sorted((ROOT / version / "translation").glob(book + "*.usfm")):
        text = path.read_text(encoding="utf-8")
        for block in re.split(r"\\c ", text)[1:]:
            chapter = int(block.split(None, 1)[0])
            pieces = re.split(r"\\v (\d+)", block)[1:]
            for num, body in zip(pieces[::2], pieces[1::2]):
                out[(chapter, int(num))] = body.strip()
    return out


def notes_of(raw):
    return [re.sub(r"\s+", " ", m).strip() for m in
            re.findall(r"\\f\s\+\s*\\fr\s+\S+\s+\\ft\s+(.*?)\\f\*", raw, re.S)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("chapter", type=int)
    ap.add_argument("--width", type=int, default=112)
    ap.add_argument("--notes", action="store_true")
    args = ap.parse_args()

    book = args.book.upper()
    plain = {v: load_danish(v, book) for v in VERSIONS}
    raw = {v: load_raw(v, book) for v in VERSIONS}
    keys = sorted(k for k in plain["esv"] if k[0] == args.chapter)
    if not keys:
        sys.exit("%s %d er ikke oversat" % (book, args.chapter))

    print("=" * args.width)
    print("%s %d — de tre versioner parallelt. Læs for MENINGSFORSKELLE (0002), "
          "ikke for stil." % (book, args.chapter))
    print("=" * args.width)
    for key in keys:
        print("\n\u2500\u2500 v. %d " % key[1] + "\u2500" * (args.width - 9))
        for v in VERSIONS:
            body = plain[v].get(key, "\u2014")
            wrapped = textwrap.fill(body, width=args.width - 6,
                                    initial_indent="%-4s " % v.upper(),
                                    subsequent_indent="     ")
            print(wrapped)
            if args.notes:
                for n in notes_of(raw[v].get(key, "")):
                    print(textwrap.fill(n, width=args.width - 10,
                                        initial_indent="     \u2937 ",
                                        subsequent_indent="       "))
    print()


if __name__ == "__main__":
    sys.exit(main())
