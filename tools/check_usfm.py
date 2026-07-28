#!/usr/bin/env python3
"""Sanity-check the Danish USFM output.

Not a schema validator (see FORMAT.md) — this checks the things that have
actually gone wrong: missing/duplicated verses, unbalanced note and character
markers, and chapters that disagree across the three versions.
"""
import re
import sys
import glob

# Verse counts per chapter, NA/UBS versification.
COUNTS = {
    "LUK": {1: 80, 2: 52, 3: 38, 4: 44, 5: 39, 6: 49, 7: 50, 8: 56, 9: 62,
            10: 42, 11: 54, 12: 59, 13: 35, 14: 35, 15: 32, 16: 31, 17: 37,
            18: 43, 19: 48, 20: 47, 21: 38, 22: 71, 23: 56, 24: 53},
    "MRK": {1: 45, 2: 28, 3: 35, 4: 41, 5: 43, 6: 56, 7: 37, 8: 38, 9: 50,
            10: 52, 11: 33, 12: 44, 13: 37, 14: 72, 15: 47, 16: 20},
}

PAIRS = [("\\f +", "\\f*"), ("\\fq ", "\\fq*"), ("\\nd ", "\\nd*"),
         ("\\add ", "\\add*")]

# Verses absent from the critical text; omitted by decision 0073, not missing.
OMITTED = {
    "LUK": {(17, 36), (23, 17)},
    "MAT": {(17, 21), (18, 11), (23, 14)},
    "MRK": {(7, 16), (9, 44), (9, 46), (11, 26), (15, 28)},
    "JHN": {(5, 4)},
}


def check(path):
    text = open(path, encoding="utf-8").read()
    book = re.match(r"\\id (\w+)", text).group(1)
    expected = COUNTS.get(book, {})
    problems = []
    chapters = {}

    for block in re.split(r"\\c ", text)[1:]:
        ch = int(block.split(None, 1)[0])
        verses = [int(v) for v in re.findall(r"\\v (\d+)", block)]
        chapters[ch] = verses
        if ch in expected:
            omitted = OMITTED.get(book, set())
            missing = [n for n in range(1, expected[ch] + 1)
                       if n not in verses and (ch, n) not in omitted]
            extra = [n for n in verses if n > expected[ch]]
            if missing:
                problems.append(f"ch{ch} missing {missing}")
            if extra:
                problems.append(f"ch{ch} beyond end {extra}")
        dupes = sorted({n for n in verses if verses.count(n) > 1})
        if dupes:
            problems.append(f"ch{ch} duplicated {dupes}")
        if verses != sorted(verses):
            problems.append(f"ch{ch} verses out of order")

    for opener, closer in PAIRS:
        if text.count(opener) != text.count(closer):
            problems.append(
                f"{opener.strip()} unbalanced: "
                f"{text.count(opener)} open / {text.count(closer)} close")

    # a footnote must carry an \fr reference
    if text.count("\\f +") != text.count("\\fr "):
        problems.append(f"footnotes without \\fr: "
                        f"{text.count('\\f +')} notes / {text.count('\\fr ')} refs")

    return book, chapters, problems


def main():
    paths = sorted(sys.argv[1:] or glob.glob("*/translation/*.usfm"))
    all_chapters = {}
    failed = False

    for path in paths:
        book, chapters, problems = check(path)
        total = sum(len(v) for v in chapters.values())
        status = "OK" if not problems else "FAIL"
        if problems:
            failed = True
        print(f"{path}: {book} {len(chapters)} ch, {total} verses  {status}")
        for p in problems:
            print(f"    ! {p}")
        all_chapters.setdefault(book, {})[path] = {
            c: len(v) for c, v in chapters.items()}

    # cross-version agreement
    for book, per_file in all_chapters.items():
        if len(per_file) < 2:
            continue
        reference_path, reference = next(iter(per_file.items()))
        for path, counts in per_file.items():
            if counts != reference:
                diff = {c: (reference.get(c), counts.get(c))
                        for c in set(reference) | set(counts)
                        if reference.get(c) != counts.get(c)}
                print(f"    ! {path} disagrees with {reference_path}: {diff}")
                failed = True

    print("ALL OK" if not failed else "PROBLEMS FOUND")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
