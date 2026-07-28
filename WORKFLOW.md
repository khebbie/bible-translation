# Roles and workflow

How we reproduce the committee structure. Grounded in what the ESV, NIV and NLT teams
actually did — see each `charter/METHOD.md` for the philosophies these serve.

## What the real committees looked like

They were **not** split by discipline — there was no "the linguist, the theologian,
the historian" seat. The actual division was different, and more useful:

**NLT** (~90 scholars + stylists)
- **3 scholars per book**, each with published expertise *in that book*
- a **Senior Translator** per corpus (Pentateuch, Historical, Wisdom, …) who
  consolidates their notes into a draft
- a separate class of **English stylists** — language craftspeople, not exegetes
- the **full Bible Translation Committee**, which approves *every verse*

**ESV** (100+ people)
- **14-member Translation Oversight Committee** — decides
- **50+ Translation Review Scholars** — check
- **50+ Advisory Council** — advise

**NIV**
- the **CBT**: independent, self-governing, self-perpetuating, with *sole* authority
  over the text; diversity of nationality and denomination treated as the structural
  safeguard against bias

### The three structural principles worth stealing

1. **Source-side and target-side are different people.** The stylists were not
   Hebraists. This is deliberate: someone has to judge the Danish *as Danish*,
   uncontaminated by the shape of the original.
2. **It is a loop, not a pipeline.** The scholars reviewed the stylists' edits
   afterwards — explicitly "to ensure that exegetical errors would not be introduced
   late in the process." Style can break meaning, so meaning gets the last look.
3. **Meaning is settled before rendering begins.** The NLT states the order: "The
   translators first struggled with the meaning of the words and phrases in the
   ancient context; **then** they rendered the message into clear, natural English."

## Our roles

| Role | Owns | Must not do |
|---|---|---|
| **Philologist** | Morphology, syntax, semantic range, textual variants. Works from morphhb / MorphGNT / TAGNT / lexicons. | Decide what it means. Reports *range*, not choice. |
| **Exegete** | Meaning in context: genre, discourse flow, intertextuality, ancient culture. Resolves what is resolvable; labels what is not. | Write Danish. |
| **Theologian** | Doctrinally load-bearing terms; guards both against reading later doctrine back in *and* against flattening it out. | Override the philologist on lexical range. |
| **Danish stylist** | Register, rhythm, naturalness, read-aloud quality. Works as monolingually as possible. | Touch exegesis. Their edits get reviewed back. |
| **Charter editor** | Applies *one* version's METHOD.md; makes the final call for that version. One per version — three in total. | Borrow another version's solution. |
| **Committee pass** | Cross-passage consistency: concordance, proper names, divine names, footnotes. Approves every verse. | Re-open settled exegesis without cause. |
| **Cold reader** | Reads *only* the Danish, having never seen the source, and reports what they understood. | See the Hebrew/Greek. Ever. |

## The pipeline, per pericope

**Stages 1–2 are shared across all three versions. This is the most important
structural decision in the project.** The three translations must differ in
*rendering*, not in *exegesis*. If ESV-Danish and NLT-Danish disagree about what a
verse means, that is a bug, not a stylistic difference. Doing the exegesis once,
centrally, is both cheaper and more correct.

```
1. PHILOLOGICAL BRIEF      shared    word-by-word: lemma, morph, semantic range,
                                     discourse markers, variants from TAGNT/TAHOT
2. EXEGETICAL BRIEF        shared    meaning, genre, structure; ambiguities listed
                                     as options, NOT silently resolved
        │
        ├──────────────┬──────────────┐
3.   ESV-style      NIV-style      NLT-style      each charter editor renders from
     rendering      rendering      rendering      the same brief, per METHOD.md
        │              │              │
4.   stylist        stylist        stylist        Danish as Danish; read aloud
        │              │              │
5.   BLIND CHECKS                                  (a) cold reader: what did you get?
                                                   (b) back-translation vs. source
        │              │              │
6.   COMMITTEE PASS                                concordance, divine names, terms,
                                                   footnotes; log every decision
```

### Ambiguity discipline

Stage 2 must classify every ambiguity, because the charters treat the two kinds
oppositely:

- **Ambiguous in the source** → ESV *preserves* the ambiguity; NIV and NLT weigh
  whether the reader can carry it.
- **Clear in the source, awkward in the target** → NIV *resolves* it (its Lev 4:19–20
  "atonement for the community" example is exactly this); ESV may leave it.

Silently collapsing the first kind into the second is the single most common way a
translation goes wrong.

### Back-translation

The cheap mechanical check the historical committees could not run at scale: render
the finished Danish back to literal English *without looking at the source*, then diff
against the philological brief. Additions, losses and shifts show up immediately. Run
it hardest on the NLT-style version, where drift is likeliest and least visible.

## Independence is the point

The committees' value came from people who could genuinely disagree. The failure mode
when one mind does every pass is **anchoring**: later passes rationalise the earlier
draft instead of challenging it.

So the checks that depend on independence must be run **blind — with no sight of the
prior reasoning**:

- the **cold reader** (must never have seen the source)
- the **back-translation** (must not see the philological brief while translating back)

The cumulative work — philology, exegesis — is better done with full context. The
adversarial work must be done fresh. If we want these as separate agents rather than
separate passes, say so and I will wire it up; the discipline matters more than the
mechanism, but blind checks are worth real isolation.

## Persistent artifacts

The committees' true output was accumulated precedent as much as text. Without this,
chapter 40 will not match chapter 3.

- `decisions/` — every settled question: "how do we render *hesed*", and *why*,
  with the charter clause that justifies it. Append-only.
- `glossary-<version>.tsv` — term table per version. **Mandatory for the ESV-style
  version**, whose charter requires concordance; it cannot be honoured from memory.
- `briefs/` — the stage 1–2 output per pericope, reusable by all three versions.

## Danish-specific gap

The historical committees had native speakers of the target language in the room. We
do not, and this is the project's real weak point — the stylist and cold-reader roles
are where a human Danish ear is worth most. Flag renderings that turn on Danish
idiom or rhythm for review rather than assuming they are settled.
