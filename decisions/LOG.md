# Decision log

Append-only. Every settled question, with the charter clause that justifies it. This
is what keeps chapter 40 consistent with chapter 3 — the committees' real output was
accumulated precedent as much as text.

Format: `### NNNN — question` · date · scope (all / esv / niv / nlt) · decision ·
rationale · status (settled / provisional / open).

---

## Standing rules — read these first

### 0012 — The charter decides; do not escalate per passage
**2026-07-28 · all · settled**
Judgment calls are made against the charters and this log, and recorded here. Do not
stop for advice on individual renderings.

Escalate **only** when one of these is true:
- the decision would require re-doing work already completed in another book;
- two settled rules collide with no principled way to rank them;
- it is a project-wide policy question not derivable from any charter.

Even then, **batch it** into a periodic review rather than interrupting mid-book.
Findings from checks become decisions here, not questions.

*Rationale:* the historical committees delegated to Senior Translators for exactly
this reason — a whole Bible cannot be translated by referendum. Klaus's instruction,
2026-07-28.

### 0013 — Tie-breaker: conservative, not confessional
**2026-07-28 · all · settled**
Where the charters and the evidence genuinely leave a question open, default to the
**conservative** reading.

Concretely, this means:
- **Take the traditional reading of the text itself.** Traditional authorship and
  setting; historical events read as historical; the received sense of a disputed
  phrase over a novel scholarly reconstruction; messianic reference in the OT allowed
  to stand where the NT reads it that way.
- **Do not read later doctrinal formulation back into the wording.** Conservative is
  not the same as confessional. Where the Greek or Hebrew is less precise than a
  creed or a systematic-theology category, keep the text's own level of precision.
  Do not sharpen a text into a proof-text it is not.
- **Prefer the reading that keeps Scripture coherent with itself**, where the language
  genuinely permits both.
- When in doubt between an old rendering and a fashionable one, take the old one.

*Worked example:* ἱλαστήριον (Rom 3:25) → propitiation ("sonoffer"), the traditional
Protestant reading, over expiation. But we still footnote the mercy-seat background
rather than pretending the question does not exist.

*How I am reading Klaus's instruction:* conservative **bibliology** — a high view of
Scripture and a preference for traditional readings — as distinct from imposing
confessional orthodoxy onto the wording. If that is the wrong split, say so once and
I will re-cut every affected decision; do not correct it per verse.

### 0014 — Footnotes carry what the text cannot
**2026-07-28 · all · settled**
When 0013 forecloses a live alternative, footnote the alternative. The conservative
default governs the *text*; it does not license hiding the evidence.

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
*Status of the tseba'oth split:* superseded by 0018, which settles it.

### 0006 — δικαιόω / δικαιοσύνη
**2026-07-28 · all · settled**
- ESV-style: **retfærdiggøre / retfærdighed** — charter mandates retaining theological
  terminology (its own list includes *justification*).
- NIV-style: **gøre retfærdig / retfærdighed** — transparent member of the pair.
- NLT-style: **erklære retfærdig** — charter bans the Latinate abstraction
  (*justification* → "made right with God"), but plain declarative Danish keeps the
  root, which v26 needs.
*Rejected for NLT-style:* **"frikende"** (acquit) — better Danish, sharper forensic
metaphor, better aloud, but breaks the δίκαιος/δικαιόω root pair at Rom 3:26.
**Ruled:** keep "erklære retfærdig" throughout the NLT-style. Decision 0007 (protect
the root pair) outranks idiomatic sharpness — losing Paul's argument costs more than a
slightly flatter verb. Consistency across the version also serves the NLT charter's own
concordance rule for repeated rhetorical phrases. "Frikende" is not used at all, to
avoid a split rendering the reader would have to reconcile.

### 0007 — The δίκαιος/δικαιόω pair must stay visible
**2026-07-28 · all · settled**
Wherever the same root is juxtaposed for effect (Rom 3:26 is the type case), all three
versions must keep a visibly shared Danish root, however freely they otherwise render.
*Rationale:* this is where Paul's argument lands; losing it loses the passage in any
philosophy.

### 0008 — ἱλαστήριον
**2026-07-28 · all · settled**
ESV-style and NIV-style: **"sonoffer"** — commits to *propitiation*.
NLT-style: **"det offer, der bærer vores skyld bort"** — meaning-based, avoids the
technical term.
All three footnote the LXX mercy-seat background (Ex 25:17–22; Lev 16).
**Ruled** under 0013: propitiation is the traditional Protestant reading and is what
the ESV chose deliberately; the conservative default takes it. The mercy-seat sense is
preserved in the footnote per 0014, not in the text. In **Hebrews 9:5**, where
ἱλαστήριον unambiguously *is* the furniture, render "sonedækket" in all three — that is
not an exception to this rule but a different referent.

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
**2026-07-28 · all · settled**
ESV-style **"uforskyldt"**; NIV-style and NLT-style **"ufortjent" / "gratis"**.
**Ruled:** keep *uforskyldt* for the ESV-style. Its charter explicitly tells us to
anchor in the received translation stream, and *uforskyldt* sits in the 1931/1948
Danish Bible and is still understood by Danish churchgoers. The ESV retains "behold",
which is markedly more archaic in English than *uforskyldt* is in Danish — so this is
well inside that charter's tolerance. 0013 also favours the older word.

---

## Rulings closing out the first pericope

### 0015 — Second person: du
**2026-07-28 · all · settled**
**"du"** throughout, including in address to God and in prayer. All modern Danish
Bibles do this; *De* would read as stilted in every register we are targeting, and
would misrepresent the Greek and Hebrew, which have no such distinction.

### 0016 — Register against the 1992 Danish Bible
**2026-07-28 · all · settled**
- **ESV-style:** close to the authorized Danish tradition. Where the 1992 wording is
  accurate and dignified, there is no merit in differing for its own sake.
- **NIV-style:** contemporary but dignified; free of the 1992 wording where a clearer
  modern phrasing exists.
- **NLT-style:** deliberately independent of it.

### 0017 — Units, currency, dates
**2026-07-28 · all · settled**
- **ESV-style:** keep the ancient unit in the text, modern equivalent in a footnote.
- **NIV-style:** ancient unit in the text where it is meaningful, otherwise a modern
  rendering; footnote either way.
- **NLT-style:** convert, per its charter — and convert to **metric**, not to the NLT's
  American units. Footnote the literal measure. Currency by function ("en almindelig
  dagløn"); dates to the modern calendar where fixable.

### 0018 — YHWH tseba'oth
**2026-07-28 · all · settled**
ESV-style and NIV-style: **"Hærskarers HERRE"** (traditional Danish). NLT-style:
translate the meaning — **"HERREN, den Almægtige"** / "Himlens hære" as context suits,
per its charter's explicit rule for this name. Supersedes the provisional note in 0005.

### 0019 — NLT-style must apply its own trigger test before going dynamic
**2026-07-28 · nlt · settled**
The NLT charter permits a dynamic rendering **only** when the literal one is hard to
understand, misleading, or archaic/foreign. Applying that test retroactively to the
first pericope found three renderings that failed it and have been corrected:
- v21 dropped δικαιοσύνη θεοῦ entirely — "Guds retfærdighed" is perfectly clear Danish,
  so the trigger was never met. Restored at both v21 and v22, keeping the fourfold
  hinge intact in all three versions.
- v21 μαρτυρουμένη rendered "peget frem mod" (predicted) — "vidner om" is clear.
  Corrected.
- v25 προέθετο rendered "lod dø", losing the public-display sense the brief called for.
  Now "stillede Jesus frem for alles øjne".
*Standing lesson:* "meaning-based" is not a licence. The trigger test is a gate, and
it must actually be applied before recasting.

### 0020 — Process at book scale
**2026-07-28 · all · settled**
The full stage-1/2 written brief per pericope does not scale to 1,151 verses × 3. From
Luke onward:
- **Full written brief only for passages that earn it** — a real textual variant, a
  doctrinally loaded term, a genuine exegetical crux, or a Semitic idiom needing a
  ruling. Everything else is carried by the glossary and settled precedent.
- **The glossary is the working memory.** Any term ruled once goes in
  `glossaries/key-terms.tsv` and is thereafter applied without re-deciding.
- **Checks run per chapter, not per pericope**, and only findings that change the text
  get written up.
*Rationale:* the historical committees did exactly this — three specialists per book,
not a committee sitting on every verse. Depth is spent where the text is hard.

### 0021 — Luke's two registers must both survive
**2026-07-28 · all · settled**
Luke 1:1–4 is a single classical periodic sentence — the most literary Greek in the NT.
At 1:5 Luke switches deliberately into Septuagintal narrative style (Ἐγένετο ἐν ταῖς
ἡμέραις…, paratactic καί-chains, Hebraic idiom).
**This shift is a feature of the source, not an accident, and must be visible in Danish
in all three versions**, most sharply in the ESV-style, whose charter requires letting
"the stylistic variety of the biblical writers fully express itself".
- ESV-style: prologue as one period; from v5 a deliberately biblical Danish narrative
  register, καί-chains kept ("Og det skete…").
- NIV-style: prologue lightly broken; narrative contemporary but with the Semitic
  cadence audible.
- NLT-style: prologue fully broken into short sentences; narrative plain modern Danish.
  Its charter's gate test does not license flattening a register *the author chose*,
  but it does license unpacking the syntax.

### 0022 — ἀνατολὴ ἐξ ὕψους (Luke 1:78)
**2026-07-28 · all · settled**
Render as **"solopgangen fra det høje"** (ESV/NIV-style) and "det lys, der bryder frem
fra det høje" (NLT-style). ἀνατολή carries both "sunrise" and, in the LXX, the
messianic "Branch" (צֶמַח, Jer 23:5; Zech 3:8; 6:12). Per 0013 the messianic resonance
is kept rather than explained away; per 0014 the Branch sense goes in a footnote.

### 0023 — κατάλυμα (Luke 2:7) is a guest room, not an inn
**2026-07-28 · all · settled**
Render **"gæsterummet"** in all three; footnote the traditional "herberg".
*Rationale:* the NIV's own CBT notes cite this as a worked example of lexical advance —
"we are more certain than we were forty years ago that the Greek word *kataluma* used
in Luke 2:7 means 'guest room,' not 'inn'." Luke uses πανδοχεῖον for a commercial inn
(10:34). The ESV charter likewise credits "current advances in… lexicography", and 0003
binds us to the Greek rather than to ESV English's traditional "inn". 0013's
"old over fashionable" governs genuine doubt; there is none here.

### 0024 — Luke 2:14 εὐδοκίας
**2026-07-28 · all · settled**
Follow NA/UBS genitive **εὐδοκίας**: peace among people *on whom his favour rests* —
not the TR/Byz nominative behind the KJV's "goodwill toward men". Footnote the
traditional reading in all three; it is the form most readers know from carols.

### 0025 — Luke 2:33 "his father"
**2026-07-28 · all · settled**
Follow NA/UBS **ὁ πατὴρ αὐτοῦ** — "hans far" — not the TR/Byz "Joseph". Footnote the
variant.
*Rationale:* 0004 binds us to the critical text, and the TR reading is a pious
smoothing. 0013 is conservative *bibliology*, not the adoption of softened readings: it
tells us to take the text as it stands and not to sharpen — or blunt — it into a
proof-text. Luke, who has just narrated the virgin birth, calls Joseph Jesus' father in
the ordinary legal and social sense, exactly as he writes "his parents" at 2:41 and
2:43. Translating it plainly is the conservative act.

### 0026 — Luke 2:2 Quirinius
**2026-07-28 · all · settled**
Translate as it stands: "Denne første folketælling fandt sted, mens Kvirinius var
statholder i Syrien." Footnote the alternative construal of πρώτη ("before Quirinius
was governor"), which relieves the chronological difficulty but strains the Greek.
Text plain, alternative in the note — 0013 with 0014.

### 0027 — χριστός in Luke
**2026-07-28 · all · settled**
ESV-style: **"Kristus"** throughout (its charter mandates flat consistency).
NIV-style: "Kristus", with "Messias" where the Jewish frame is explicit.
NLT-style: **"Messias"** wherever the audience in view is Jewish — which in Luke 1–2 is
everywhere (shepherds, Simeon, Anna) — per its charter's explicit rule.

### 0028 — Transliteration of proper names
**2026-07-28 · all · settled**
**Old Testament figures and places take their established Danish Old Testament form**,
not a transliteration of the Greek. So Ἠσαΐας → **Esajas** (not Isaias); Βόος →
**Boaz**; Ἰωβήδ → **Obed**; Ναασσών → **Nakshon**; Ἀμιναδάβ → **Amminadab**; Ἑσρώμ →
**Hesron**; Φαρές → **Peres**; Θάρα → **Tera**; Ἀρφαξάδ → **Arpakshad**; Νῶε → **Noa**;
Μαθουσαλά → **Metusalem**; Ἑνώχ → **Enok**; Σαλαθιήλ → **Shealtiel**; Ζοροβαβέλ →
**Zerubbabel**.
*Rationale:* the ESV charter requires that OT material quoted in the NT be rendered so
the correspondence is visible — and a genealogy is a chain of OT citations. Luke's
Greek spellings are themselves LXX transliterations; reproducing them would sever the
link for a Danish reader who knows these names from the Old Testament. 0002 makes this
binding on all three versions.

**Names occurring only in Luke's genealogy** (Melki, Jannaj, Josek, Joda, Joanan, Resa,
Maat, Semein, Naggaj, Esli, Elmadam, Kosam, Addi, Jorim, Jonam, Eljakim, Melea, Menna,
Mattata, Admin, Arni…) are transliterated into Danish orthography from the Greek: χ→k,
θ→t, φ→f, ου→u, final -ς dropped.

**Contemporary first-century names** keep the Danish New Testament form already fixed in
Luke 1–2: Zakarias, Elisabet, Josef, Maria, Johannes, Kajfas, Annas, Pontius Pilatus.

This policy governs Matthew's genealogy when we reach it. Do not re-decide it there.

### 0029 — Luke 3:19 "his brother's wife"
**2026-07-28 · all · settled**
Follow NA/UBS and omit "Philip"; the TR names him. Footnote once. (Mark 6:17 has the
name; Luke's critical text does not.)

### 0030 — Luke 3:22 the voice at the baptism
**2026-07-28 · all · settled**
Follow NA/UBS: "Du er min elskede søn; i dig har jeg fundet velbehag." The Western
reading of Codex Bezae — "i dag har jeg født dig" (Ps 2,7) — is famous but stands
outside the critical text and outside the KJV tradition, so 0004 does not require a
note. Not footnoted, to keep the apparatus for variants that actually bear on the text
we follow.

### 0031 — τετραάρχης
**2026-07-28 · all · settled**
ESV-style and NIV-style: **"landsfyrste"** (the established Danish term).
NLT-style: describe the office — "regerede over…" — per its charter's rule on
institutions that have no modern counterpart.
