# CLAUDE.md

**Goal: produce three Danish Bible translations** — one in the style of the ESV, one
in the style of the NIV, one in the style of the NLT — working directly from Hebrew
and Greek.

See `README.md` for what NIV/ESV/NLT translated from, `CHARTERS.md` for how the three
differ from each other, and `WORKFLOW.md` for the roles and the per-pericope pipeline.

## Current state

Sources, charters and workflow are **done**. **One pericope translated: Romans
3:21–26**, run end to end through the pipeline as a scaffolding test. Nothing else is
translated. No tooling beyond an inline USFM sanity check. The directory is not a git
repo.

```
bible/
├── README.md          textual basis of NIV/ESV/NLT + source manifest
├── CHARTERS.md        the three philosophies compared; open Danish questions
├── WORKFLOW.md        roles, per-pericope pipeline, artifacts to maintain
├── FORMAT.md          USFM 3.1 as canonical output, and why
├── CLAUDE.md          this file
├── briefs/            shared philological + exegetical briefs, one per pericope
│                        + .checks.md — back-translation findings
├── decisions/LOG.md   append-only precedent; READ BEFORE TRANSLATING
├── glossaries/        key-terms.tsv — term table across all three versions
├── esv/  charter/     essentially literal    — METHOD.md + official preface
│      translation/  Danish USFM output
├── niv/  charter/     mediating / balanced   — METHOD.md + preface + CBT notes
│      translation/
├── nlt/  charter/     meaning-based          — METHOD.md + both intros + FAQ
│      translation/
└── sources/           ~670 MB of cloned source texts (each is its own git clone)
    ├── morphhb/           Hebrew OT — Westminster Leningrad Codex + morphology
    ├── sblgnt/            Greek NT — SBLGNT + MorphGNT parsing
    ├── Nestle1904/        Greek NT — public-domain critical text
    └── STEPBible-Data/    tagged Hebrew + Greek, lexicons, variant apparatus
```

Each `<version>/charter/` holds the **primary documents verbatim** (`.md` converted
from the publishers' own pages, `.html`/`.pdf`/`.txt` raw originals) plus a
`METHOD.md` distilling them into operative rules, with Danish-specific notes.

## Before translating anything

1. Read `decisions/LOG.md` — it is binding precedent, not notes.
2. Read the relevant `charter/METHOD.md`, and `CHARTERS.md` to see what that version
   must *not* sound like. The three have to be recognisably different from each
   other; that difference comes from the charters, not from taste.
3. Follow `WORKFLOW.md`: brief first (shared), then render three ways, then check.

**Translate the Greek/Hebrew, not the English version.** Decision 0003 — where the
ESV/NIV/NLT made an interpretive expansion, do not copy it just because it is in the
English text. This was caught in the first pericope and is the easiest mistake to make.

## Decide; do not escalate

Findings from checks become **decisions**, logged in `decisions/LOG.md` — not questions
for Klaus. A whole Bible cannot be translated by referendum. Escalate only under the
three conditions in decision 0012, and batch it into a periodic review.

**Tie-breaker (0013):** where the charters and the evidence genuinely leave a question
open, take the **conservative** reading — traditional readings of the text, the
received sense over a novel reconstruction, the old rendering over the fashionable one.
Conservative is *not* confessional: do not read later doctrinal formulation back into
the wording, and do not sharpen a text into a proof-text. Where the default forecloses
a live alternative, footnote it (0014).

**When rules collide**, the order of authority is: protect the argument → the version's
own charter → settled precedent → the conservative default → Danish idiom.
See `WORKFLOW.md`.

## Which source to reach for

| Task | Use |
|---|---|
| Hebrew text of a passage | `sources/morphhb/wlc/<Book>.xml` |
| Greek text of a passage | `sources/sblgnt/<nn>-<Bk>-morphgnt.txt` |
| Word gloss, transliteration, extended Strong's | STEPBible TAHOT / TAGNT |
| "What does NA28 read here?" | STEPBible TAGNT edition tags |
| Lexicon lookup (incl. full LSJ) | `sources/STEPBible-Data/Lexicons/` |
| Unencumbered-license Greek | `sources/Nestle1904/` |

## Format notes

**morphhb WLC** — OSIS XML, one file per book, `<verse osisID="Gen.1.1">` containing
`<w lemma= morph= id=>` elements. A `/` inside a word or lemma is a **morpheme
boundary** (prefix/suffix segmentation), not punctuation. Morph codes start with `H`.

**MorphGNT** — 7 whitespace-separated columns:
`ref · POS · parsing · text(with punctuation) · word · normalized · lemma`.

**STEPBible TAHOT/TAGNT** — tab-separated, with a long human-readable preamble before
the data. Word-type suffix on the reference (`#01=NKO`) encodes which editions have
the word: `N`=Nestlé-Aland, `K`=Textus Receptus/KJV, `O`=other; lowercase means the
difference does not affect translation.

## Gotchas

- **Versification differs between sources.** WLC uses **Hebrew** versification —
  Psalm superscriptions are verse 1, so `Ps.3.2` in WLC is Psalm 3:1 in English
  Bibles. The XML embeds a `KJV:Ps.3.1` marker to map it. STEPBible uses **NRSV**
  versification. Always normalize references before aligning sources.
- **MorphGNT reference numbers are NT-relative**, not the filename number. `61-Mt`
  contains refs starting `010101`; `87-Re` starts `270101`. Filename = whole-Bible
  number, ref field = NT book 01–27.
- **STEPBible filenames contain spaces** — always quote paths.
- `ls` is aliased to `eza` here; its output has a header line and size columns, so
  don't pipe it into scripts. Use `find`, globs, or `ls -1` explicitly.
- morphhb `wlc/` holds 40 files: 39 canonical books plus `VerseMap.xml`.

## Licensing

Permissive: morphhb (CC BY 4.0), Nestle1904 (public domain), STEPBible (CC BY 4.0).
Restricted: **SBLGNT text** has its own EULA; **TTESV** is CC BY-NC. STEPBible asks
that others be pointed at their repo rather than served copies. Check before
publishing anything derived from these.

## Conventions

- Cite chapter:verse in the source's own versification and say which one when it is
  ambiguous.
- When a translation choice turns on a textual variant, check TAGNT/TAHOT and state
  which editions support which reading rather than silently picking one.
- Don't treat NIV/ESV/NLT differences as textual unless the apparatus confirms it —
  they nearly always reflect translation philosophy, not a different base text.
