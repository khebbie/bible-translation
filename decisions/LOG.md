# Decision log

Append-only. Every settled question, with the charter clause that justifies it. This
is what keeps chapter 40 consistent with chapter 3 — the committees' real output was
accumulated precedent as much as text.

Format: `### NNNN — question` · date · scope (all / esv / niv / nlt) · decision ·
rationale · status (settled / provisional / open).

---

### 0001 — Output format
**2026-07-28 · all · settled**
USFM 3.1 as canonical output, one file per book per version. See `FORMAT.md`.
*Rationale:* the format real translation committees use (Paratext); lossless to USX
for app/DBL ingestion; has native markers for the footnotes, section headings, poetry
lines and divine-name handling our three charters explicitly require.

### 0002 — Exegesis is shared, rendering is not
**2026-07-28 · all · settled**
Stages 1–2 (philological + exegetical brief) are produced once in `briefs/` and used
by all three versions. The three versions may not differ in what a passage *means*.
*Rationale:* the charters differ on rendering philosophy, not on exegesis. Divergent
exegesis between our own versions would be a defect, not a feature.

### 0003 — Translate the Greek, not the English version
**2026-07-28 · all · settled**
Render from the brief and the source text. Where our English counterpart made an
*interpretive expansion*, do not copy it just because it is in the ESV/NIV/NLT.
*Rationale:* caught in the Rom 3:25 check — our ESV-style had "til at modtages ved tro"
because ESV English reads "to be received by faith", where the Greek is only διὰ
πίστεως. Copying the English silently imports its interpretive choices while claiming
to be literal. See `briefs/rom-3.21-26.checks.md` finding 2.

### 0004 — Textual base and variant policy
**2026-07-28 · all · settled**
Follow NA/UBS (via SBLGNT + TAGNT edition tags). Footnote translation-affecting
variants; ignore variants tagged lowercase in TAGNT. Where the KJV/TR tradition has
material the critical text lacks, footnote it — NLT's charter requires this explicitly,
ESV and NIV both do it in practice.
*First application:* Rom 3:22, TR/Byz "καὶ ἐπὶ πάντας". Omitted, footnoted in all three.

### 0005 — YHWH
**2026-07-28 · all · settled**
`\nd HERREN\nd*` in all three versions. *’adonay YHWH* → "Herren HERREN".
*YHWH tseba’oth* → **splits by charter**: ESV-style "Hærskarers HERRE" (traditional
Danish), NLT-style translates the meaning ("Himlens hære"), per its charter's explicit
"LORD of Heaven's Armies" rule. NIV-style: traditional.
*Status of the tseba'oth split:* provisional until first OT pericope.

### 0006 — δικαιόω / δικαιοσύνη
**2026-07-28 · all · provisional**
- ESV-style: **retfærdiggøre / retfærdighed** — charter mandates retaining theological
  terminology (its own list includes *justification*).
- NIV-style: **gøre retfærdig / retfærdighed** — transparent member of the pair.
- NLT-style: **erklære retfærdig** — charter bans the Latinate abstraction
  (*justification* → "made right with God"), but plain declarative Danish keeps the
  root, which v26 needs.
*Rejected for NLT-style:* **"frikende"** (acquit) — better Danish, sharper forensic
metaphor, better aloud, but breaks the δίκαιος/δικαιόω root pair at Rom 3:26.
**Open for Klaus:** is that the right trade?

### 0007 — The δίκαιος/δικαιόω pair must stay visible
**2026-07-28 · all · settled**
Wherever the same root is juxtaposed for effect (Rom 3:26 is the type case), all three
versions must keep a visibly shared Danish root, however freely they otherwise render.
*Rationale:* this is where Paul's argument lands; losing it loses the passage in any
philosophy.

### 0008 — ἱλαστήριον
**2026-07-28 · esv, niv · provisional; nlt · settled**
ESV-style and NIV-style: **"sonoffer"** — commits to *propitiation*.
NLT-style: **"det offer, der bærer vores skyld bort"** — meaning-based, avoids the
technical term.
All three footnote the LXX mercy-seat background (Ex 25:17–22; Lev 16).
**Open:** "sonoffer" forecloses the mercy-seat reading, which the brief judged a
serious contender. Revisit before Hebrews.

### 0009 — πάρεσις is not forgiveness
**2026-07-28 · all · settled**
Never render πάρεσις (Rom 3:25) with tilgivelse/forlade. Use "gå ustraffet hen",
"bære over med", or equivalent, and footnote.
*Rationale:* the whole problem v25 raises is that God had *not* yet dealt with those
sins. "Forgave" destroys the argument in every version.

### 0010 — πίστις Χριστοῦ
**2026-07-28 · all · settled (with a Danish note worth keeping)**
Render objectively ("tro på Jesus Kristus"), footnoting the subjective reading —
following what ESV, NIV and NLT all do.
*Danish note:* Danish could preserve the ambiguity where English cannot — "Jesu Kristi
tro" is genitivally ambiguous in exactly the way πίστεως Ἰησοῦ Χριστοῦ is. The
ESV-style charter's own logic (preserve source ambiguity, maximise transparency)
arguably points there. Not taken, because all three English counterparts resolve it and
the Danish construction reads as subjective to most ears. **Flagged as the clearest
case so far where Danish can do something English couldn't.**

### 0011 — δωρεάν register split
**2026-07-28 · all · provisional**
ESV-style **"uforskyldt"** (older Danish theological register, echoes the 1931/1948
tradition its charter tells us to anchor in); NIV-style and NLT-style **"ufortjent" /
"gratis"**.
**Open for Klaus:** does *uforskyldt* read as dignified or as archaic?

---

## Open questions not yet forced by a pericope

From `CHARTERS.md`, still undecided: **De/du** (especially in address to God); how
close each version sits to the 1992 Danish Bible's register; metric conversion policy
for the NLT-style version.
