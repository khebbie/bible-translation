# Output format

**Canonical output is USFM 3.1**, one file per book per version.

## Why USFM

It is what real translation projects produce. Paratext — the UBS/SIL software actual
translation committees work in — reads and writes USFM, and the Digital Bible Library
ingests its XML twin, USX. USFM → USX is lossless and round-trips, and from there
converters exist to OSIS, USFX, HTML and JSON. Anything an app needs is downstream of
USFM; nothing is upstream of it.

The decisive argument is that USFM has **native markers for exactly the features our
three charters mandate**, which no ad-hoc JSON schema would:

| Charter requirement | Marker |
|---|---|
| ESV: footnotes are "an integral part of the translation" | `\f + \fr 3.22 \ft … \f*` |
| NIV: section headings inserted, "not part of the biblical text… not intended for oral reading" | `\s1` — structurally distinct from `\p`, so apps can hide it |
| NLT: "render poetry in English poetic form", show parallelism | `\q1` `\q2` |
| All three: YHWH as LORD in small caps | `\nd HERREN\nd*` |
| Words supplied for the target language | `\add …\add*` |
| NLT: footnote the literal reading when converting units/idiom | `\f + \fr … \ft Græsk: …\f*` |

`\nd` matters more than it looks: it encodes *the divine name as a semantic category*
rather than as styling, so HERREN renders correctly whatever the app's typography.

## Conventions for this project

- Filenames: `<version>/translation/<BOOK>.usfm`, using standard 3-letter book codes
  (`ROM`, `GEN`, `PSA`). Pericope-level drafts may use `<BOOK>-<ch>.<vv>.usfm` and get
  merged into the book file later.
- `\id` line carries the book code plus a version tag: `\id ROM DA-ESV …`
- Danish book names in `\h`, `\toc1/2/3`, `\mt1`.
- Footnote caller is always `+` (auto-numbered).
- Textual-variant notes use `\ft` prefixed `Nogle håndskrifter…`; alternative
  renderings use `Eller…` — matching Danish Bible convention.
- One `\p` per paragraph; do **not** put every verse in its own paragraph. Paragraphing
  is a translation decision the ESV charter explicitly claims ("in punctuating,
  paragraphing, dividing long sentences… the path that seems to make the ongoing flow
  of thought clearest").

## Validation

No USFM validator is installed yet. Before the corpus grows, add one — the Python
`usfm-grammar` / `pythonbible` route or Paratext itself. Until then, treat the files
as hand-checked, not verified.

## What we do not do

Do not hand-write JSON, or invent a schema. If an app needs JSON, generate it from
USFM so the USFM stays the single source of truth.
