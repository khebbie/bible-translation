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

## At book scale (decision 0020)

The full written brief below is for **passages that earn it** — a real textual variant,
a doctrinally loaded term, an exegetical crux, a Semitic idiom needing a ruling.
Routine narrative is carried by `glossaries/` and settled precedent in
`decisions/LOG.md`. Checks run per chapter, not per pericope.

**Task tracking lives in beads (`bd`), not in markdown.** Every chapter of the four
Gospels is a `bd` issue under a per-Gospel epic, chained sequentially so `bd ready`
returns exactly the next chapter. See "Working autonomously" below.

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

## Checks produce decisions, not questions

A finding is not a question for Klaus. Rule it against the charter and the tie-breaker
(`decisions/LOG.md` 0012–0014), apply the fix, and log it. Escalate only under the
three conditions in 0012, and batch it.

The order of authority when rules collide:

1. **Protect the argument.** If a rendering loses what the passage is doing — a
   wordplay the point rests on, a distinction the logic needs — that outranks every
   stylistic rule in every charter.
2. **The version's own charter**, including its gate conditions. "Meaning-based" is not
   a licence: the NLT charter's trigger test is a gate, and must actually be applied
   before recasting (0019).
3. **Settled precedent** in the decision log.
4. **The conservative default** (0013).
5. **Danish idiom and rhythm.**

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

## Working autonomously

`bd ready` returns the next chapter to translate. The loop is:

```
bd ready                     # next chapter, e.g. bible-ycn.8
bd update <id> --claim
  … translate per the pipeline above …
bd close <id> --reason="…"
```

Chapters are chained within each Gospel, and Mark/Matthew/John chapter 1 each depend on
Luke 24 — because Luke is where the naming, term and register precedent is being set,
and decision 0028 already commits Matthew's genealogy to it. To work the Gospels in
parallel instead, drop those three cross-Gospel dependencies.

Everything a fresh session needs is on disk: `decisions/LOG.md` is binding precedent,
`glossaries/key-terms.tsv` and `names.tsv` are the working memory, `PROGRESS.md` holds
the notes carried forward into the next chapter.

## Persistent artifacts

The committees' true output was accumulated precedent as much as text. Without this,
chapter 40 will not match chapter 3.

- `decisions/LOG.md` — every settled question and *why*, with the charter clause that
  justifies it. Append-only. **Binding precedent, not notes.**
- `glossaries/key-terms.tsv` — one table, a column per version. **Mandatory for the
  ESV-style version**, whose charter requires concordance; it cannot be honoured from
  memory. Any term ruled once goes in here immediately (0020) — logging the decision is
  not enough, and letting this drift was a real failure through Luke 1–7.
- `glossaries/names.tsv` — fixed Danish forms for every person and place, governed by
  0028. Consult before inventing a spelling.
- `briefs/` — stage 1–2 output for passages that earn a full brief.
- `PROGRESS.md` — live chapter count and the notes carried into the next chapter.

## Danish-specific gap

The historical committees had native speakers in the room. We do not, and the stylist
and cold-reader roles are where that costs most.

This does **not** mean stopping to ask. Decide it, log it, and let it accumulate: idiom
calls go in the glossary and the decision log, where they can be reviewed in bulk and
reversed cheaply across the whole corpus. A wrong-but-consistent choice recorded in one
place is far easier to fix later than a thousand ad-hoc ones — and infinitely cheaper
than interrupting every few verses.
