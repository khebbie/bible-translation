# CLAUDE.md

**Goal: produce three Danish Bible translations** — one in the style of the ESV, one
in the style of the NIV, one in the style of the NLT — working directly from Hebrew
and Greek.

See `README.md` for what NIV/ESV/NLT translated from, `CHARTERS.md` for how the three
differ from each other, and `WORKFLOW.md` for the roles and the per-pericope pipeline.

## Current state

Sources, charters and workflow are **done**. **Luke is complete** in all three versions
(1,149 verses each), plus Romans 3:21–26 as the original scaffolding pericope. See
`PROGRESS.md` for the live count and `decisions/LOG.md` for the 82 binding rulings.
`tools/check_usfm.py` validates output after every chapter. The repo is git-tracked on
`main` with a GitHub remote; one commit per chapter.

```
bible/
├── README.md          textual basis of NIV/ESV/NLT + source manifest
├── CHARTERS.md        the three philosophies compared; open Danish questions
├── WORKFLOW.md        roles, per-pericope pipeline, artifacts to maintain
├── FORMAT.md          USFM 3.1 as canonical output, and why
├── CLAUDE.md          this file
├── briefs/            shared philological + exegetical briefs, one per pericope
│                        + .checks.md — back-translation findings
├── PROGRESS.md        live chapter count + notes carried forward
├── decisions/LOG.md   append-only precedent; READ BEFORE TRANSLATING
├── glossaries/        key-terms.tsv (terms) + names.tsv (people & places)
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

1. `bd ready` — the next chapter to translate. Claim it with `bd update <id> --claim`.
2. Read `decisions/LOG.md` — it is binding precedent, not notes.
3. Read `glossaries/key-terms.tsv` and `glossaries/names.tsv` — these are the working
   memory. **Never invent a rendering for a term or a name that is already in them**,
   and add any new ruling immediately (0020). Logging the decision is not enough;
   letting the glossary drift behind the log was a real failure through Luke 1–7.
4. Read `PROGRESS.md` for the notes carried forward into this chapter.
5. Read the relevant `charter/METHOD.md`, and `CHARTERS.md` to see what that version
   must *not* sound like. The three have to be recognisably different from each
   other; that difference comes from the charters, not from taste.
6. Follow `WORKFLOW.md`. At book scale, full written briefs are only for passages that
   earn one (0020) — the glossary and precedent carry routine narrative.

When the chapter is done and validated: update `PROGRESS.md`, log new decisions, add
new terms to the glossaries, then `bd close <id>`.

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


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->
