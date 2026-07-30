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

### 0032 — Luke 4:44 "Judæa"
**2026-07-28 · all · settled**
Follow NA/UBS **Ἰουδαίας** — "synagogerne i Judæa" — not the TR/Byz "Galilæa".
Footnote the variant. It is the harder reading (Jesus has just been in Galilee), which
is precisely why it is likelier original; Luke uses Ἰουδαία at times for the Jewish
homeland as a whole. 0004 binds; 0013 does not license smoothing a difficulty away.

### 0033 — `\nd` in New Testament quotations of the Old
**2026-07-28 · all · settled**
Where the NT quotes an OT passage that has **YHWH**, set the Danish as
`\nd HERREN\nd*`. First applied at Luke 4:8, 4:12 (Deut 6:13, 6:16) and 4:18–19
(Isa 61:1–2). Elsewhere κύριος is ordinary "Herren".
*Rationale:* this is the NLT charter's stated rule, and 0002 makes it binding on all
three. It also serves the ESV charter's requirement that OT-in-NT correspondence be
visible.

### 0034 — Luke 4:18–19 is a composite citation
**2026-07-28 · all · settled**
Luke's Isaiah reading follows the LXX of Isa 61:1–2 but drops "to bind up the
brokenhearted" and splices in "to set the oppressed free" from **Isa 58:6**. Translate
Luke's text as it stands and footnote the composition in all three versions — a reader
comparing with a Danish Isaiah will otherwise think the translation is faulty.

### 0035 — TR additions in Luke 4
**2026-07-28 · all · settled**
Omit and footnote, per 0004: 4:4 "men af hvert Guds ord"; 4:8 "Vig bort fra mig,
Satan"; 4:18 "at helbrede dem, hvis hjerte er knust". Trivial TR articles and
connectives (4:2, 4:5, 4:9, 4:41) are not noted.

### 0036 — ὁ υἱὸς τοῦ ἀνθρώπου
**2026-07-28 · all · settled**
**"Menneskesønnen"** in all three versions, always, and always definite. First
occurrence Luke 5:24; roughly 25 more follow in this Gospel.
*Rationale:* it is a title, not a description, and it carries the Dan 7:13 allusion.
Even the NLT-style keeps it: its charter's gate test is not met, since "Menneskesønnen"
is entirely clear Danish, and paraphrasing it ("jeg" or "jeg, der er sendt fra Gud")
would erase a self-designation the reader is meant to track across the whole Gospel.
0013 also favours the received Danish rendering.

### 0037 — ἐπιστάτα
**2026-07-28 · all · settled**
**"Mester"**. Luke alone uses ἐπιστάτης for Jesus (5:5; 8:24, 45; 9:33, 49; 17:13) where
the other Gospels use ῥαββί or διδάσκαλος — a deliberate Lukan choice for a
Greek-speaking readership. Keep it distinct from διδάσκαλος, which is also "Mester" in
Danish; where both appear near each other, the ESV-style may use "Mester" for ἐπιστάτης
and "Lærer" for διδάσκαλος to preserve the distinction.

### 0038 — ἁμαρτωλός
**2026-07-28 · all · settled**
**"synder"** (noun) / "syndig" (adj.) in all three. Do not soften to "et almindeligt
menneske" or similar in the NLT-style: in Luke the word is a social-religious label the
Pharisees apply, and the whole point of 5:30–32 and 15:1–2 depends on it stinging.

### 0039 — TR additions in Luke 5
**2026-07-28 · all · settled**
Omit and footnote 5:38 "og begge dele bevares". Follow NA at 5:33 (statement, not the
TR's question) and 5:17 (αὐτόν — the Lord's power was with *him* to heal). Trivial TR
articles and adverbs (5:3, 5:5, 5:15, 5:39) are not noted.

### 0040 — μακάριος and οὐαί
**2026-07-28 · all · settled**
- ESV-style and NIV-style: **"Salige er I…"** / **"Ve jer…"** — the received Danish
  forms; 0016 tells the ESV-style not to differ from the tradition gratuitously.
- NLT-style: **"Gud velsigner jer, som…"** and **"Hvor vil I komme til at sørge, I…"**
  Its charter's gate test *is* met here: "salig" is drifting out of ordinary Danish, and
  "ve" is no longer a live interjection. Making God the actor also matches what the
  passive form actually claims.
Applies wherever the words recur (6:20–26; 7:23; 10:23; 11:27–28, 42–52; 12:37–43;
14:14–15; 23:29).

### 0041 — Luke's Beatitudes stay second person
**2026-07-28 · all · settled**
Luke has "Blessed are **you** poor… for **yours** is the kingdom", against Matthew's
third person. Do not harmonise toward the more familiar Matthean form in any version.
Likewise keep Luke's four Woes, which Matthew lacks.

### 0042 — TR readings in Luke 6
**2026-07-28 · all · settled**
- 6:1 omit the TR's **δευτεροπρώτῳ** ("the second-first sabbath"), a famously obscure
  reading absent from the critical text. Footnote it — it is well known and its absence
  will be noticed.
- 6:10 omit "sund som den anden"; footnote.
- 6:48 follow NA — the house stood **"fordi den var bygget godt"**, not the TR's "for
  it was founded on a rock" (assimilated from Matt 7:25). Footnote. Luke's point is the
  *building work*, not the rock; blurring it flattens his distinctive version.

### 0043 — δοῦλος in the Gospels
**2026-07-28 · all · settled**
Default **"tjener"** where the relationship in view is domestic service (Luke 7:2–10;
12:37; 17:7), **"slave"** where ownership or bondage is the point (12:47; 15:22 —
weigh each). The ESV charter's own rule is context-graded, not concordant, for this
word, and ESV English itself reads "servant" at Luke 7:2. Footnote the Greek where
"tjener" is used for δοῦλος in a context a reader might expect "slave".
Note Luke varies deliberately at 7:7, using **παῖς** — render "dreng"/"tjenestedreng"
in the ESV-style so the shift is visible; the other two may keep "tjener".

### 0044 — δικαιόω with a non-personal object
**2026-07-28 · all · settled**
0006 fixes δικαιόω where God declares a sinner righteous. Where the object is God or
wisdom (Luke 7:29, 7:35), the sense is *vindicate / acknowledge to be right*:
- 7:29 "gav Gud ret"
- 7:35 ESV-style **"retfærdiggjort"** (its charter's concordance rule, which applies
  "to the extent that plain Danish permits"); NIV-style "har fået ret"; NLT-style
  "viser sig at have ret".
*Rationale:* "retfærdiggjorde Gud" would mislead a Danish reader into hearing a defence
of God's existence. Even ESV English breaks concordance here, reading "declared God
just" at 7:29. Concordance yields where it would distort — the charter says so itself.

### 0045 — Luke 7:47 ὅτι
**2026-07-28 · all · settled**
Translate plainly — "for hun elskede meget" — and **footnote the logic** in all three.
The parable Jesus has just told (7:41–43) makes love the *result* of forgiveness, not
its price; the second half of v47 ("den, som får lidt tilgivet, elsker lidt") confirms
it. 0013 tells us to prefer the reading that keeps the passage coherent with itself,
but the Greek ὅτι is genuinely open, so the resolution belongs in the note, not in a
rewritten text.

### 0046 — Currency at Luke 7:41 (first application of 0017)
**2026-07-28 · all · settled**
- ESV-style: **"fem hundrede denarer … halvtreds"**, footnoting that a denarius was a
  day's wage.
- NIV-style: same, with the equivalence in the footnote.
- NLT-style: convert by function — **"halvandet års løn … halvanden måneds løn"** —
  with the literal figure in the footnote.

### 0047 — TR readings in Luke 7
**2026-07-28 · all · settled**
Follow NA at 7:19 (**κύριον**, "Herren", not the TR's "Jesus"). Omit and footnote the
TR's "profet" at 7:28. Trivial TR additions (7:10, 7:11, 7:31, 7:44) are not noted.

### 0048 — Luke 8:26, 37 "gerasenernes egn"
**2026-07-28 · all · settled**
Follow NA/UBS **Γερασηνῶν** — "gerasenernes egn" — not the TR's "gadarenernes".
Footnote the variants in all three.
*Rationale:* 0004 binds us to the critical text. Gerasa lies some 50 km from the lake,
which is exactly why later copyists substituted the nearer Gadara and Gergesa; the
geographical difficulty makes Γερασηνῶν the harder and likelier reading. 0013 does not
license smoothing it away, and Luke says only "the region of", not the town itself.

### 0049 — TR additions in Luke 8
**2026-07-28 · all · settled**
Omit and footnote: 8:45 "og de, som var med ham" plus the repeated "og du siger: Hvem
rørte ved mig?"; 8:48 "Vær frimodig"; 8:54 "men han sendte dem alle ud". Trivial TR
variants (8:34, 8:38, 8:40) are not noted.

### 0050 — κράσπεδον (Luke 8:44)
**2026-07-28 · all · settled**
ESV-style and NIV-style **"kvasten på hans kappe"**; NLT-style the same with a footnote
explaining the tassel. It is not a generic hem: κράσπεδον renders the *tzitzit*
commanded in Num 15:38–39, and the woman's reaching for it is a deliberate detail.
Footnote the Numbers reference in all three.

### 0051 — Luke 9:35 "min udvalgte"
**2026-07-28 · all · settled**
Follow NA/UBS **ὁ ἐκλελεγμένος** — "Det er min Søn, den udvalgte" — not the TR's
ἀγαπητός ("den elskede"). Footnote the variant.
*Rationale:* the TR reading is assimilated from the baptism (3:22) and from the Synoptic
parallels. Luke deliberately varies: *elskede* at the baptism, **udvalgte** at the
Transfiguration, picking up the Servant of Isa 42:1. Levelling the two erases the
allusion. 0004 binds; 0013 does not license harmonising.

### 0052 — Luke 9:54–56, the long TR addition
**2026-07-28 · all · settled**
Omit and footnote in all three: "ligesom Elias gjorde" (v54) and the whole of "og sagde:
I ved ikke, hvad ånd I er af; for Menneskesønnen er ikke kommet for at ødelægge
menneskeliv, men for at frelse dem" (vv55–56).
*Rationale:* absent from the critical text. It is a well-loved passage and its
disappearance will be noticed, so 0004 requires the note — quoted in full there, since
readers of older Danish Bibles know it by heart.

### 0053 — ἔξοδος (Luke 9:31) and ἀνάλημψις (9:51)
**2026-07-28 · all · settled**
9:31 — ESV-style **"hans bortgang"**, footnoting that the Greek is *exodos*; NIV-style
"hans bortgang"; NLT-style "hvordan han skulle forlade verden", same footnote. Luke's
word choice on the mountain, with Moses standing there, is not accidental.
9:51 — ESV-style **"da tiden nærmede sig, da han skulle tages op"**; the other two may
say "da tiden nærmede sig, hvor han skulle tages op til himlen". ἀνάλημψις points
forward to the ascension, which only Luke narrates.

### 0054 — τὸ πρόσωπον ἐστήρισεν (Luke 9:51)
**2026-07-28 · all · settled**
ESV-style keeps the Semitic idiom — **"vendte han sit ansigt fast mod Jerusalem"** —
per its charter's rule on retaining idiom. NIV-style "besluttede han sig fast for at
drage til Jerusalem". NLT-style "satte han kursen mod Jerusalem, fast besluttet".
The phrase echoes Ezek 21:2 and Isa 50:7; footnote it in the ESV-style only.

### 0055 — Luke 10:1, 17: tooghalvfjerds
**2026-07-28 · all · settled**
Read **"tooghalvfjerds"** (72) with NA/SBL, footnoting "halvfjerds" in all three.
*Rationale:* the manuscript evidence is genuinely divided and NA28 brackets δύο, but
ESV, NIV and NLT all print seventy-two, and 72 matches the table of nations in Gen 10
LXX — a plausible symbolic point for Luke's mission to the wider world. Because the
evidence is balanced rather than one-sided, the footnote is not optional.

### 0056 — Luke 10:42
**2026-07-28 · all · settled**
Follow NA/SBL **ὀλίγων δέ ἐστιν χρεία ἢ ἑνός** — "kun lidt er nødvendigt, ja, kun én
ting" — not the TR's flat "ét er fornødent". Footnote the shorter reading.
*Rationale:* 0004. The longer reading is the harder one and explains the others; the TR
text looks like a simplification. The sense is not materially changed, but the wording
is, and Danish readers know the traditional phrasing.

### 0057 — ᾅδης
**2026-07-28 · all · settled**
**"dødsriget"** in all three — the established Danish rendering, and distinct from
γέεννα, which is "Helvede". Do not collapse the two: Luke 10:15 is about being brought
low, not about final judgment.

### 0058 — Luke 10:27 quotes the Shema
**2026-07-28 · all · settled**
Deut 6:5 renders YHWH, so `\nd HERREN\nd*` applies per 0033: "Du skal elske
\nd HERREN\nd* din Gud…". Same wherever the Shema or the Decalogue is quoted.

### 0059 — Luke's Fadervor is shorter than Matthew's
**2026-07-28 · all · settled**
Follow NA/SBL and print **Luke's five-petition form**: "Fader! Helliget blive dit navn,
komme dit rige! Giv os hver dag vort daglige brød, og forlad os vore synder… og led os
ikke ind i fristelse." The TR pads Luke out from Matt 6:9–13 with "vor … du som er i
himlene", "ske din vilje, som i himlen således også på jorden" and "men fri os fra det
onde".
**Footnote the omitted clauses in full, quoting them**, in all three versions. This is
the single most recognisable place where the critical text departs from what Danish
churchgoers know by heart, and 0004 plus 0014 both require that the reader be told
rather than left to suspect an error.
*Register:* the ESV-style uses the received Danish wording of the Fadervor for the
petitions Luke actually has — 0016 tells it to stay close to the tradition, and there is
no merit in a fresh rendering of words every Dane already knows. The NLT-style may
recast; even there, do not obscure that this is the Lord's Prayer.

### 0060 — ἐπιούσιος (Luke 11:3)
**2026-07-28 · all · settled**
**"vort daglige brød"** in all three, footnoting that the Greek word is otherwise
unknown and may mean "for the coming day" or "necessary for existence". The traditional
rendering is right under 0013, but the uncertainty is real and belongs in a note.

### 0061 — Βεελζεβούλ
**2026-07-28 · all · settled**
**"Beelzebul"** in all three, footnoting it as a name for the ruler of the demons.
Not "Beelzebub", which comes via the Vulgate and Syriac; the Greek is consistently
-βουλ.

### 0062 — Small coins: ἀσσάριον and λεπτόν
**2026-07-28 · all · settled** (extends 0017/0046)
- ἀσσάριον (12:6): ESV-style **"to skilling"** with a footnote giving the Greek and the
  value (1/16 denar); NIV-style the same; NLT-style **"nogle få mønter"**.
- λεπτόν (12:59): ESV-style **"den sidste skærv"** — the received Danish word, and the
  same coin as the widow's mite in 21:2, where the phrase is fixed in Danish memory;
  NIV-style "den sidste øre"; NLT-style "den allersidste krone".
Keep "skærv" for λεπτόν throughout the ESV-style so 12:59 and 21:2 read as one word.

### 0063 — Luke 12:25 ἡλικία
**2026-07-28 · all · settled**
Render as **lifespan** — "lægge en alen til sin livslængde" (ESV-style), "forlænge sit
liv en eneste time" (NIV/NLT-style) — and footnote the alternative "add a cubit to his
height".
*Rationale:* ἡλικία covers both age and stature, and πῆχυς is a measure of length, so
the Greek is genuinely mixed. But v26 calls it "the least thing", which fits a tiny
addition to a lifespan far better than eighteen inches of height. 0013 is not engaged;
the context decides.

### 0064 — ὀσφύες περιεζωσμέναι (Luke 12:35)
**2026-07-28 · all · settled**
ESV-style keeps the idiom — **"Lad jeres lænder være omgjordede"** — per its charter's
rule on retaining Semitic idiom, footnoting the sense. NIV-style "Vær klar til at gå
i gang". NLT-style "Vær klar til at rykke ud". The image is of tucking a long robe into
the belt in order to move fast.

### 0065 — σάτον (Luke 13:21)
**2026-07-28 · all · settled** (first dry-measure application of 0017)
ESV-style **"tre mål mel"** with the Greek and the volume in a footnote; NIV-style the
same; NLT-style converts to **metric — "omkring 40 liter mel"**.
*Rationale:* a saton is roughly 13 litres, so three of them is an enormous batch —
bread for a hundred people. The size is the point of the parable, and it is invisible
in "three measures". This is exactly the case 0017 exists for.

### 0066 — Luke 13:24 "den snævre dør"
**2026-07-28 · all · settled**
Follow NA **θύρα** — "dør" — not the TR's πύλη ("port"), which is assimilated from
Matt 7:13. Luke's image runs on into vv25–27, where a householder shuts *a door*; the
TR reading breaks the picture. Footnote the familiar "snævre port".

### 0067 — Luke 13:35
**2026-07-28 · all · settled**
Omit the TR's **ἔρημος** — "jeres hus overlades til jer *øde*" — and footnote it. The
word is imported from Matt 23:38. Luke's bare "jeres hus overlades til jer" is bleaker
and should not be softened by explanation either.
The closing quotation is Ps 118:26 and renders YHWH, so `\nd HERREN\nd*` applies (0033).

### 0068 — μισεῖ (Luke 14:26)
**2026-07-28 · all · settled**
ESV-style and NIV-style keep **"hader"**, with a footnote explaining the Semitic
comparative. NLT-style renders the sense: **"elsker mig så meget højere, at al anden
kærlighed blegner ved siden af"**, footnoting the literal "hader".
*Rationale:* the ESV charter is explicit that Semitic idiom is retained and that the
reader is trusted with a footnote; softening it in the text would be precisely the
"interpretive expansion" 0003 forbids. But the idiom is real — Hebrew uses "hate" for
*love less* (Gen 29:31; Deut 21:15; Mal 1:2–3), and Matt 10:37 gives the same saying as
"loves father or mother more than me". The NLT charter's gate test is met: read flat, a
modern Danish reader takes "hade" at face value and the sentence becomes monstrous.
All three footnote the other reading — this is a case where 0014 does real work.

### 0069 — δραχμή (Luke 15:8-9)
**2026-07-28 · all · settled** (extends 0062)
ESV-style **"drakmer"** with a footnote (a drachma was about a day's wage); NIV-style
**"sølvmønter"** with the same footnote; NLT-style **"sølvmønter"**, footnoting that
each was worth a day's work.
*Rationale:* the woman has ten and loses one — a tenth of her savings, not small change.
"Ti mønter" alone would lose that, so the value goes in the note in every version.

### 0070 — μαμωνᾶς
**2026-07-28 · all · settled**
ESV-style keeps **"mammon"** — it is a transliterated Aramaic word in the Greek too, not
an ordinary noun, and the charter retains such terms; footnote it as Aramaic for wealth.
NIV-style **"penge"** / "Mammon" where personified at 16:13. NLT-style **"penge"**
throughout.
*Rationale:* at 16:13 Jesus sets mammon against God as a rival master, so the ESV- and
NIV-style keep it as a name there; elsewhere it is simply money.

### 0071 — βάτος and κόρος (Luke 16:6-7)
**2026-07-28 · all · settled** (extends 0065)
ESV-style **"hundrede fad olie … hundrede tønder hvede"** with the volumes footnoted;
NIV-style the same; NLT-style converts to metric — "omkring 3.000 liter olivenolie" and
"omkring 30 ton hvede".
*Rationale:* the debts are enormous — several years' income each — and the steward's
nerve is the point of the parable. In "a hundred measures" it disappears entirely.

### 0072 — Luke 16:16 βιάζεται
**2026-07-28 · all · settled**
Render in the **middle/positive** sense — "og alle trænger ind i det med magt" (ESV-style),
"og alle presser på for at komme ind" (NIV/NLT-style) — and footnote the passive
alternative ("og enhver bruger vold imod det").
*Rationale:* the verb is genuinely ambiguous between middle and passive, and both are
ancient. The positive reading fits Luke's context — the crowds of toll collectors and
sinners pressing in from 15:1 — and 0013's coherence test favours it. The alternative
goes in the note per 0014.

### 0073 — Verses the critical text does not have
**2026-07-28 · all · settled**
Where a verse exists only in the TR/KJV tradition, **omit the verse number entirely**
and footnote it at the preceding verse, quoting the omitted words. Do not print an
empty verse number, and do not renumber the surrounding verses.
*Rationale:* this is what ESV, NIV and NLT all do, and NLT's charter requires the note
explicitly. Renumbering would break every cross-reference and concordance; a bare number
with no text looks like a production fault.
*Applies in Luke at:* **17:36** and **23:17**. It will recur at Matt 17:21; 18:11; 23:14;
Mark 7:16; 9:44, 46; 11:26; 15:28; John 5:4. `tools/check_usfm.py` carries the list.

### 0074 — ἐντὸς ὑμῶν (Luke 17:21)
**2026-07-28 · all · settled**
Render **"midt iblandt jer"** in all three, footnoting "i jer" / "inden i jer".
*Rationale:* ἐντός can mean *within* or *among*, but the addressees here are the
**Pharisees** — Jesus is not saying the kingdom is inside them. Luke's whole point is
that the kingdom is already present in his own person, standing in front of them. The
inward reading is the more familiar one in Danish devotional usage, so it goes in the
note rather than being dropped.

### 0075 — ἱλάσκομαι (Luke 18:13)
**2026-07-28 · all · settled**
All three: **"Gud, vær mig synder nådig!"** (ESV-/NIV-style) and "Gud, vær nådig mod
mig — jeg er en synder" (NLT-style), **footnoting** "ordret: lad dig forsone med mig".
*Rationale:* the verb is cognate with ἱλαστήριον (0008, "sonoffer"), and the tax
collector is asking for exactly what Rom 3:25 says God provided. But the Danish
"vær mig synder nådig" is a fixed, universally known phrase, and 0016 tells the
ESV-style not to differ from the received tradition without cause. ESV English does the
same — "be merciful" in the text, propitiation in the note. The link is preserved where
it belongs, in the footnote.

### 0076 — δικαιόω reappears in Luke (18:14)
**2026-07-28 · all · settled**
δεδικαιωμένος at 18:14 takes the renderings already fixed by **0006**: ESV-style
"retfærdiggjort", NIV-style "gjort retfærdig", NLT-style "erklæret retfærdig". Noted
here only because it is the first time the Romans vocabulary recurs inside Luke — the
glossary is doing its job, and no re-decision is needed.

### 0077 — μνᾶ (Luke 19:13-25)
**2026-07-28 · all · settled** (extends 0046/0062)
ESV-style **"pund"** with a footnote (a mina was about a hundred days' wages);
NIV-style **"pund"** with the same note; NLT-style **"tre måneders løn"** per mina,
footnoting the literal.
*Rationale:* "pund" is the received Danish rendering and keeps the ten/five/one
arithmetic clean, which the parable needs. The NLT-style conversion has to stay a unit
that can be multiplied — hence a wage period, not a modern currency figure.

### 0078 — Luke 19:38 and 19:46 are OT quotations
**2026-07-28 · all · settled**
19:38 quotes Ps 118:26 (as at 13:35), so `\nd HERREN\nd*` applies per 0033. Note that
Luke alone inserts **ὁ βασιλεύς** into the acclamation — "Velsignet være kongen, som
kommer" — keep it in all three; it is his point.
19:46 conflates Isa 56:7 with Jer 7:11. Footnote both references; do not smooth the
seam.

### 0079 — The double κύριος of Ps 110:1 (Luke 20:42)
**2026-07-28 · all · settled**
Render **"\nd HERREN\nd* sagde til min herre"**. The first κύριος translates **YHWH**
and takes the divine-name marker per 0033; the second translates *adonai* and is
ordinary "herre" (lower case).
*Rationale:* the whole argument of 20:41–44 turns on there being **two** figures in the
verse — David calls someone other than YHWH "my lord". Rendering both alike destroys
the point in any translation philosophy, which makes this a 0007-type case: protect the
argument first. The typographic distinction does the work no wording can.
Applies wherever Ps 110:1 is quoted (Matt 22:44; Mark 12:36; Acts 2:34; Heb 1:13).

### 0080 — The two bracketed passages in Luke 22
**2026-07-28 · all · settled**
**22:19b–20** (the cup after supper, "det nye testamente ved mit blod") and
**22:43–44** (the angel and the sweat like blood): **print both in the text**, and
footnote in all three that the oldest witnesses are divided.
*Rationale:* both are printed by NA28 — 19b–20 without brackets, 43–44 in double
brackets — and ESV, NIV and NLT all print both with a note. 0013 takes the received
text where the evidence is genuinely divided rather than the shorter Western reading,
and 0014 requires the reader be told. Bracketing them typographically in Danish would
imply a confidence the evidence does not support in either direction; a footnote states
the position honestly.
*Note on 22:19b–20:* this is the only account of the institution in Luke, and the
"new covenant in my blood" wording is the one Danish readers know from the liturgy —
its silent removal would be very widely noticed.

### 0081 — Luke 23:34a and 23:17
**2026-07-28 · all · settled**
**23:34a** ("Fader, tilgiv dem, for de ved ikke, hvad de gør") — print in the text with
a footnote noting that some early witnesses omit it. Same reasoning as 0080: NA28 prints
it in double brackets, all three English versions print it, and it is among the most
widely known sentences in the Gospel. Removing it silently is not an option; implying
by brackets that it is spurious overstates the evidence.
**23:17** — absent from the critical text; omitted per 0073 and footnoted at v16.

### 0082 — The Western non-interpolations in Luke 24
**2026-07-28 · all · settled**
Luke 24 carries a cluster of short phrases that Codex Bezae and some Old Latin
witnesses omit: **24:3** "Herren Jesu", **24:6** "Han er ikke her, men er opstået",
**24:12** (Peter running to the tomb), **24:36** "og sagde til dem: Fred være med jer",
**24:40** (showing hands and feet), **24:51** "og han blev båret op til himlen",
**24:52** "de tilbad ham".
**Print all of them**, with a single consolidated footnote at 24:12 and short notes at
24:51–52 in all three versions.
*Rationale:* the same policy as 0080 and 0081. NA28 prints them all; the twentieth
century's confidence in the Western text at these points has largely receded. 24:51–52
matter most: without them Luke's Gospel does not narrate the ascension at all, which
would leave Acts 1 without its counterpart, and 0013's coherence test weighs against
that.

---

## Mark

### 0083 — Where SBLGNT and NA28 diverge, NA28 governs
**2026-07-28 · all · settled** (clarifies 0004)
0004 says "follow NA/UBS (via SBLGNT + TAGNT edition tags)". SBLGNT is the **vehicle**
we read the text from; **NA28 is the authority**. Where they differ, TAGNT's edition
tags settle it and we take NA28.
*First application:* **Mark 1:41**. SBLGNT alone prints ὀργισθείς ("moved with anger");
NA28, NA27, THGNT, Tregelles, TR and Byz all read **σπλαγχνισθείς** ("moved with
compassion"). We read "han ynkedes inderligt over ham" and footnote the "anger"
reading, which is the harder one and has genuine early support.
Also applies at **Mark 1:1**, where NA28 has υἱοῦ θεοῦ but SBL and WH omit: we print
**"Guds Søn"** and footnote.

### 0084 — εὐθύς is Mark's signature and must stay audible
**2026-07-28 · all · settled**
Mark uses εὐθύς about **42 times** — more than the rest of the NT together. It is not
filler; it is the engine of his narrative pace.
- **ESV-style: "straks", concordantly, every time.** Its charter requires the same word
  for important recurring words, and no word recurs more distinctively in Mark.
- **NIV-style:** "straks" as the default, varying ("med det samme", "med ét") only where
  Danish would otherwise grate.
- **NLT-style:** may vary freely and may occasionally drop it — but **not** so often that
  the breathlessness disappears. Its charter's gate test is about clarity, and "straks"
  is not unclear; the licence here is rhythm, not sense.

### 0085 — Mark's historic present
**2026-07-28 · all · settled**
Mark constantly narrates in the present tense (ἔρχεται, λέγει). Danish narrative
tolerates the historic present better than English does, so the ESV-style **keeps it**
where the Danish carries it — this is exactly the "stylistic variety of the biblical
writers" its charter protects. NIV-style keeps it in vivid moments and otherwise uses
the past. NLT-style uses ordinary past narration.
*Standing warning for Mark:* his Greek is rough and paratactic where Luke's is polished.
**Do not smooth it.** The ESV-style in particular must read noticeably rougher in Mark
than in Luke, or the charter is not being applied.

### 0086 — Mark 1:2 attributes a composite quotation to Isaiah
**2026-07-28 · all · settled**
Follow NA/UBS **"hos profeten Esajas"**, not the TR's "hos profeterne". Footnote in all
three that the quotation combines **Mal 3:1** with **Isa 40:3**, and that the TR reading
looks like a scribal tidying of exactly that difficulty. 0013 does not license removing
a difficulty the best manuscripts preserve.

### 0087 — Mark 2:26 "da Abjatar var ypperstepræst"
**2026-07-28 · all · settled**
Translate as it stands and **footnote the difficulty**: 1 Sam 21 names **Ahimelek**, not
his son Abjatar, as the priest on that occasion.
*Rationale:* 0013 tells us to take the text as it stands and not to smooth a difficulty
the best manuscripts preserve — the same reasoning as Luke 4:44 and Mark 1:2. Some
manuscripts drop the clause entirely, which is itself evidence that early readers felt
the problem. Note the fact; do not resolve it in the text, and do not pretend it is not
there.

### 0088 — The apostle lists differ between Gospels
**2026-07-28 · all · settled**
Mark 3:18 has **Thaddæus** where Luke 6:16 has **Judas, Jakobs søn**; Mark has
**Simon Kananæeren** where Luke has **Simon Zeloten**. Render each Gospel's list as it
stands and footnote the difference once per Gospel. Do not harmonise.
*Rationale:* 0002 requires shared *exegesis*, not harmonised *wording* — and these are
different lists in different books, not a discrepancy to be resolved. "Kananæer" is
Aramaic for "zealot", so the Simon entries are the same person under two labels; that
belongs in the note.

### 0089 — Mark 4:39: Jesus muzzles the sea
**2026-07-28 · all · settled**
φιμώθητι at 1:25 (to the unclean spirit) and πεφίμωσο at 4:39 (to the sea) are the same
verb. The ESV-style must use **the same Danish words in both places** — "Ti stille!" —
so the reader sees that Jesus addresses the storm exactly as he addresses a demon. That
is Mark's point, and it is the kind of recurrence its charter's concordance rule exists
for. NIV- and NLT-style may vary the wording but must not lose the parallel; footnote it
at 4:39.

### 0090 — Mark's Aramaic
**2026-07-28 · all · settled**
Mark three times preserves Jesus' Aramaic and then translates it himself: **ταλιθα κουμ**
(5:41), **εφφαθα** (7:34), **ελωι ελωι λεμα σαβαχθανι** (15:34).
**Keep the Aramaic transliterated in all three versions, followed by Mark's own gloss.**
Do not drop it — not even in the NLT-style.
*Rationale:* the gloss is Mark's, not ours; he put the foreign words there on purpose and
then explained them, which means the reader is *meant* to hear them. Removing them
deletes an authorial act, not a translation obstacle. The NLT charter's gate test is
about clarity, and Mark has already supplied the clarity himself.
Danish spelling follows the received forms: **talitha kumi**, **effata**, **eloi, eloi,
lama sabaktani**.

### 0091 — Mark 7:19b, the narrator's aside
**2026-07-28 · all · settled**
καθαρίζων πάντα τὰ βρώματα is a **nominative participle** agreeing with the subject of
v18 — that is, it is **Mark's own comment on Jesus' words**, not part of the saying:
"Dermed erklærede han al mad for ren."
Set it off in all three versions (dash or new sentence) so the reader can see it is the
narrator speaking, and footnote that the Greek construction is what makes this an
editorial remark. Mark does the same kind of thing at 7:3–4, explaining Jewish custom to
readers who do not know it.

### 0092 — κορβᾶν (Mark 7:11)
**2026-07-28 · all · settled**
Keep the transliterated **"korban"** with Mark's own gloss ("det vil sige: en gave til
Gud") in all three, per **0090**. Mark supplies the translation himself; the foreign word
is part of what he is showing the reader.

### 0093 — κόφινος vs σπυρίς (Mark 6:43; 8:8, 19-20)
**2026-07-28 · all · settled**
Mark uses **two different words** for the baskets in the two feedings, and at 8:19–20
Jesus makes the contrast explicit — twelve *kophinoi* after the five thousand, seven
*spyrides* after the four thousand. **All three versions must use two different Danish
words**, or the questioning in 8:19–20 collapses into a pointless repetition.
Fixed: κόφινος = **"kurv"**, σπυρίς = **"kurv"** is *not* acceptable; use
κόφινος = "kurv" and σπυρίς = **"stor kurv"** (ESV-/NIV-style) or "foderkurv" /
"stor kurv" (NLT-style). A σπυρίς was large enough to hold a man (Acts 9:25);
footnote that at 8:8.

### 0094 — Mark 8:12 has no Jonah exception
**2026-07-28 · all · settled**
Where Matthew and Luke allow "except the sign of Jonah", **Mark's refusal is absolute**:
"der skal aldrig gives denne slægt et tegn." Do not import the exception from the
parallels in any version. The Greek is a Hebraic oath-formula (εἰ δοθήσεται — literally
"if a sign shall be given…"), which is why it reads so abruptly; footnote that in the
ESV-style.

### 0095 — λύτρον ἀντὶ πολλῶν (Mark 10:45)
**2026-07-28 · all · settled**
ESV-style **"en løsesum for mange"**; NIV-style the same; NLT-style **"betale prisen for
at sætte mange fri"**, footnoting the literal.
*Rationale:* λύτρον is the ransom paid to free a slave or captive, and ἀντί means *in
place of*. The ESV charter's rule on retaining theological terminology applies — this is
one of the two sayings in Mark that state the purpose of the cross, and "løsesum" is the
received Danish word. The NLT-style unpacks the metaphor but must not lose the idea of a
price paid instead of someone else.

### 0096 — Ραββουνι (Mark 10:51)
**2026-07-28 · all · settled**
Keep the transliterated **"Rabbuni"** in all three, footnoting that it is an intensified
Aramaic form of *rabbi* — roughly "min mester". Mark does not gloss this one himself, so
unlike 0090 the note carries the meaning; but the word stays, because Bartimæus'
unusual address is part of what Mark records.

### 0097 — Mark 11:17 keeps "for alle folkeslag"
**2026-07-28 · all · settled**
Mark alone completes the Isa 56:7 quotation with **πᾶσιν τοῖς ἔθνεσιν** — "et bedehus
**for alle folkeslag**" — where Luke 19:46 stops short. Keep it in all three and footnote
that Mark alone has it.
*Rationale:* the clause is the point of the scene in Mark's telling: the traders were
occupying the court of the Gentiles, the one place non-Jews could pray. Dropping it, or
harmonising toward Luke, removes Mark's reason for including the incident where he does.

### 0098 — ὡσαννά
**2026-07-28 · all · settled**
Keep **"Hosanna"** untranslated in all three, footnoting it at first occurrence as a
Hebrew cry meaning "frels dog!" which had become a shout of praise. All three English
versions do the same, and Danish liturgical usage has long since absorbed the word.
Consistent with 0090 and 0096: the foreign word stays, the meaning goes in the note.

### 0099 — Mark 13:14 "den, som læser dette, må forstå det"
**2026-07-28 · all · settled**
Keep the aside in the text in all three, set off with dashes. It is **Mark addressing
his reader directly** — one of only a handful of places in the Gospels where the narrator
steps out and speaks to whoever is holding the scroll. Footnote that the phrase points
back to Dan 9:27; 11:31; 12:11. Do not move it into a footnote or smooth it into Jesus'
speech: whose voice it is *is* the interesting thing about it.

### 0100 — Mark 13:32 "end ikke Sønnen"
**2026-07-28 · all · settled**
Render plainly in all three: "…ikke engang englene i himlen, **ikke engang Sønnen** —
kun Faderen." Do not soften, qualify, or footnote it into harmlessness.
*Rationale:* this is the clearest test of 0013's second clause — conservative
bibliology, **not** confessional retrojection. Later doctrinal formulation about the two
natures is not the text's own level of precision, and importing it here would be exactly
the sharpening 0013 forbids. Translate what Mark wrote and leave the difficulty with the
reader, where he left it.

---

## Hebrews

> Hebrews 10 was translated on request, out of sequence, while Mark was in progress
> and before any of Hebrews 1–9 exists. The rulings below are binding (0020); what is
> provisional is only that Hebrews 1–9 may later supply an *earlier* first occurrence
> of a term ruled here. Shared brief: `briefs/heb-10.md`.

### 0101 — Hebrews' offering vocabulary: two chains that must stay visible
**2026-07-30 · all · settled**
The argument of Heb 10:1–18 is carried by two words recurring against each other, and a
version that loses the recurrence loses the argument whatever its philosophy — a
**0007** case.

- **προσφορά** (10:5, 8, 10, 14, 18) is the chain that must not break: the offerings God
  did *not* want (5, 8) are replaced by the one offering of Christ's body (10, 14),
  which is why no offering remains (18). ESV-style and NIV-style: **"offergave"** at all
  five. NLT-style may vary the wording but must keep the link audible.
- **θυσία** (10:1, 5, 8, 11, 12, 26): **"offer"** in the discourse (1, 11, 12, 26), but
  **"slagtoffer"** inside the Psalm quotation (5, 8), where it renders Hebrew *zevach*
  and the received Danish wording of Ps 40:7 is fixed. Footnoted at 10:5.
- **περὶ ἁμαρτίας** (10:6, 8) is the Greek Old Testament's fixed phrase for the **sin
  offering**, standing as a noun beside ὁλοκαυτώματα: render **"syndoffer"**. At 10:18
  and 10:26 the same preposition is ordinary and becomes "for synd".
- **τελειόω** (10:1, 14) = **"gøre fuldkommen"** in all three. What the law could never
  do is what the one offering did.
- **ἁγιάζω** (10:10, 14, 29): ESV-style **"hellige"**; NIV- and NLT-style **"gøre
  hellig"** — the NLT charter bans *helliggørelse* and names this as its Danish route.
  **Do not level the tenses**: perfect at v10 (accomplished), present at v14 (ongoing).
*Rationale:* the ESV charter's concordance rule applies "to the extent that plain Danish
permits", and here plain Danish permits it on προσφορά, which is where the argument
lands. The θυσία split follows **0044**: concordance yields where it would distort, and
0016 tells the ESV-style not to differ from the received Psalm wording without cause.

### 0102 — εἰς τὸ διηνεκές: one Greek phrase, two Danish words
**2026-07-30 · all · settled**
The phrase occurs three times in Heb 10 in two senses: endless **repetition** at 10:1
(what they keep offering) against permanent **validity** at 10:12 and 10:14 (what he
offered once).
- ESV-style: **"uden ophør"** at 10:1, **"for bestandig"** at 10:12 and 10:14, with a
  footnote at 10:1 saying it is the same Greek phrase.
- NIV-style: "igen og igen" / "for altid". NLT-style: free.
*Rationale:* the same reasoning as **0044**. No single Danish word carries both senses,
and the ESV English breaks concordance here too ("continually" / "for all time"). The
footnote does the work concordance cannot, per 0014.
*Recurs at* 7:3.

### 0103 — Heb 10:5 follows the Greek Old Testament against the Hebrew
**2026-07-30 · all · settled**
Ps 40:7 in Hebrew reads **"ears you have dug for me"** (אָזְנַיִם כָּרִיתָ לִּי,
`Ps.40.7`); Hebrews reads **σῶμα δὲ κατηρτίσω μοι**, "a body you prepared for me", and
then builds 10:10 and 10:14 on the word *body*.
**Translate Hebrews' Greek as it stands, and footnote the Hebrew in all three.**
*Rationale:* **0003 cuts both ways** — we do not correct the author toward the Hebrew any
more than toward the ESV. The quotation is not decoration; the word *body* is the hinge
of the paragraph, so emending it would destroy the argument (0007). And this is exactly
what **0034** was decided for: a reader comparing with a Danish Psalter will otherwise
think the translation is faulty. The same note carries the lesser divergence in v6
(Hebrew "you have not *required*", Greek "you did not *delight in*").
**Standing rule for the whole book:** wherever Hebrews' argument depends on a Greek Old
Testament reading that the Masoretic Text does not support, translate what Hebrews wrote
and footnote the Hebrew. Do not harmonise in either direction.

### 0104 — The load-bearing repetitions in Hebrews 10
**2026-07-30 · all · settled**
Four more recurrences in this chapter are structural, not incidental, and all three
versions must keep each pair visibly linked:
- **προσέρχομαι** (10:1, 22) — the book's word for approaching God. 10:22 is the answer
  to 10:1. ESV- and NIV-style **"træde frem"**; NLT-style "gå ind til Gud".
- **παρρησία** (10:19, 35) — frames the exhortation: the confidence we *have* against the
  confidence not to *throw away*. **"frimodighed"** in ESV- and NIV-style, "frimodig
  tillid" in the NLT-style, both times.
- **τὸ θέλημα τοῦ θεοῦ ποιῆσαι** (10:7, 9, 10, 36) — what Christ came to do is what the
  readers must do. **Identical Danish wording** ("gøre Guds vilje") at all four, footnoted
  at 10:36.
- **ὑποστέλλομαι / ὑποστολή** (10:38, 39) — verb then noun, back to back, and the reason
  the author reversed the halves of Hab 2:4. Keep one Danish root across both.
Also **ἥκω** (10:7, 9) and **ἥξει** (10:37): "jeg er kommet" answered by "han kommer".
*Rationale:* 0007. These are not concordance for its own sake — each pair is an argument
the reader is meant to complete.

### 0105 — ἀδελφοί outside the Gospels
**2026-07-30 · all · settled**
First vocative ἀδελφοί in an epistle (Heb 10:19).
- **ESV-style: "brødre"**, with a footnote at the first occurrence in each book noting
  that the Greek word covers brothers and sisters. This is its charter's stated policy
  verbatim — retain *adelphoi*, footnote where it includes women.
- **NIV-style and NLT-style: "brødre og søstre"** ("kære brødre og søstre" where the NLT
  charter's read-aloud rule wants the warmth). Both charters mandate it.
*Rationale:* charter-fixed on all three sides; recorded so it is not re-decided per letter.
This is one of the clearest places where the three versions must not converge.

### 0106 — Heb 10:26 is footnoted, not softened
**2026-07-30 · all · settled**
ἑκουσίως ἁμαρτανόντων is translated plainly in all three — "synder vi med vilje" — and
**footnoted with the Torah's own distinction**: sacrifice was provided for inadvertent
sin (Lev 4) and none for sin committed "with a high hand" (Num 15:30–31). The note states
that the verse is not saying a Christian who sins is beyond forgiveness, but that someone
who repudiates the one sacrifice has no other to go to.
*Rationale:* the most misread passage in the chapter. **0013** forbids blunting the text —
the warning is genuinely severe and must stay severe — and **0014** exists precisely so
that the text can stay sharp while the reader is told what it does and does not claim. The
same handling applies at 6:4–6 when we reach it.

### 0107 — Hab 2:4 at Heb 10:38: "min retfærdige"
**2026-07-30 · all · settled**
Read NA28 **ὁ δὲ δίκαιός μου ἐκ πίστεως ζήσεται** — the μου attaches to δίκαιος, so God
is speaking of **his own** righteous one: ESV-style "Men min retfærdige skal leve af tro."
Footnote in all three that (a) the Hebrew has "the righteous shall live by **his**
faithfulness" (בֶּאֱמוּנָתוֹ, `Hab.2.4`), (b) the TR drops μου, and (c) **Paul quotes the
same half-verse without μου at Rom 1:17 and Gal 3:11**, which is the form Danish readers
know.
Also: 10:37–38 is a **composite citation** — Isa 26:20 spliced onto Hab 2:3–4 — and
Hebrews turns the Greek Old Testament's neuter "it will surely come" (the *vision*) into a
masculine **"the coming one"**, a person. Translate the messianic reading and footnote the
composition, per **0034** and **0013**. Hebrews also reverses the two halves of Hab 2:4;
do not restore the Habakkuk order.
Set 10:37–38 as poetry (`\q1`/`\q2`) in all three, as with 10:5–7 and 10:16–17.

### 0108 — Textual variants in Hebrews 10
**2026-07-30 · all · settled** (applies 0004 and 0083)
Follow NA28 throughout. **Footnoted:**
- **10:34** τοῖς **δεσμίοις** ("the prisoners"), not the TR's τοῖς δεσμοῖς **μου**
  ("**my** chains"), and the TR's ἐν οὐρανοῖς ("in heaven") after "a better and abiding
  possession" is omitted. Both go in one note. The TR reading matters beyond its wording:
  it is what made the verse read as Paul's, and it is what the KJV stream has.
- **10:17** the critical text has no verb of speaking, so the sentence begun at 10:15 never
  reaches its main clause; the TR supplies "then he adds". Footnote the anacoluthon and
  the addition — otherwise the Danish looks broken.
- **10:30** the TR adds λέγει κύριος to "Vengeance is mine"; folded into the quotation note,
  which also records that Hebrews' wording follows the Hebrew and matches Rom 12:19 rather
  than the Greek Old Testament of Deut 32:35.
- **10:38** μου, per 0107.
**Not footnoted** (trivial per 0035): 10:1 δύναται/δύνανται (whether *the law* or *the
sacrifices* cannot perfect — the sense barely moves); 10:2 κεκαθαρισμένους; 10:8 the plural
θυσίας καὶ προσφοράς against v5's singular, which is the author's own variation and is kept;
10:9 the TR's added ὁ θεός; 10:12 οὗτος/αὐτός; 10:15 εἰρηκέναι/προειρηκέναι; 10:16 singular
διάνοιαν.

### 0109 — Hebrews' sanctuary vocabulary
**2026-07-30 · all · settled**
- **τὰ ἅγια** (10:19) — ESV- and NIV-style **"helligdommen"**, NLT-style **"Det
  Allerhelligste"**; all three footnote the literal "det hellige" and that Hebrews means
  the inner room. The NLT charter's gate test is met: "det hellige" reads as an adjective
  in Danish, not a place.
- **ἱερεὺς μέγας** (10:21) is **not** ἀρχιερεύς. Render **"en stor præst"** in all three so
  the author's variation shows; "ypperstepræst" stays reserved for ἀρχιερεύς.
- **σῶμα** (10:5, 10, 22) and **σάρξ** (10:20) are not interchangeable, and 10:20 says the
  way runs through the curtain, "that is, his **flesh**". ESV- and NIV-style **"kød"** at
  10:20 against "legeme" for σῶμα; the NLT-style uses "krop" for σῶμα and must not thereby
  erase σάρξ — it renders 10:20 "sin egen krop" only because the NLT register has no
  workable "kød", and footnotes the construal.
  *Note against 0003:* the ESV English reads "his body" at 10:20. We do not.
- **10:20, "gennem forhænget, det vil sige gennem sit kød"** — the traditional construal
  equates curtain and flesh; **0013** takes it, and the instrumental alternative goes in
  the footnote per 0014.
- **10:12, εἰς τὸ διηνεκές** may attach to the offering or to the sitting down. The Danish
  word order in the ESV-style leaves it open, as the Greek does; NIV- and NLT-style resolve
  it to the offering with ESV, NIV and NLT. Footnoted once in each version.

### 0110 — χριστός in Hebrews
**2026-07-30 · nlt · settled** (extends 0027)
0027 sends the NLT-style to **"Messias"** wherever the audience in view is Jewish, which in
Hebrews is throughout. But in this letter Χριστός mostly stands in the **name-pair**
Ἰησοῦς Χριστός (10:10), where "Jesus Messias" would read as a claim being made rather than
as a name.
**Ruled:** the NLT-style keeps **"Jesus Kristus"** for the name-pair and uses "Messias" only
where Χριστός stands alone as a title. Where the subject is *supplied* by the translator and
the Greek has no name at all — Heb 10:5, where the Greek has only a participle — the
NLT-style supplies **"Jesus"**, which is clearest aloud and does not force the question.
ESV-style supplies nothing at 10:5 ("Derfor siger han…"), per **0003**: the ESV English
supplies "Christ" there and the Greek does not. NIV-style supplies "Kristus".
*Rationale:* 0027 is about audience, not about breaking up proper names; and the difference
in what each version supplies at 10:5 is a good illustration of the three charters working
as intended.

### 0111 — Heb 10:26 carries both ἑκουσίως *and* the present participle
**2026-07-30 · all · settled** (amends 0106)
`ἁμαρτανόντων` at 10:26 is a **present** participle in a genitive absolute with ἡμῶν,
and `ἑκουσίως` is a separate adverb fronted for emphasis. The verse therefore states two
things, not one: the sin is **deliberate** *and* it is **persisted in**. All three versions
must render both.
- ESV-style **corrected**: "For synder vi med vilje…" → **"For bliver vi ved med at synde
  med vilje…"**, footnoting both the aspect and the older Danish wording.
- NIV-style ("hvis vi bevidst bliver ved med at synde") and NLT-style ("hvis vi med vilje
  bliver ved med at synde") already carried both; unchanged.

*Rationale:* the ESV charter's governing rule is transparency to "the structure and exact
force of the original", and imperfective aspect is part of that force. **0016** pulls the
other way — the 1931/1992 Danish and the KJV all have the bare punctiliar "synder vi med
vilje" — but this is not differing from the tradition gratuitously: dropping the aspect
produces in Danish exactly the misreading that 0106's footnote exists to block, namely
that a *single* deliberate sin forecloses forgiveness. Better to carry it in the text than
to repair it in a note. v29's three **aorist** participles (καταπατήσας, ἡγησάμενος,
ἐνυβρίσας) describe the settled act that the present participle in v26 describes persisting
in, and the Num 15:30–31 "high hand" background is about defiance, not a lapse.

*On the argument from 1 John 3 (Klaus, 2026-07-30):* the instinct is right, the parallel is
not. 1 John 3:6, 3:9 have **no adverb** — ἁμαρτάνει, ἁμαρτάνων, ποιεῖ and ἁμαρτάνειν are
bare presents, so the whole "keeps on sinning / makes a practice of sinning" reading there
rests on aspect alone, which is why it is genuinely disputed. Heb 10:26 is the *easier*
case because the author supplied the adverb. **Do not import the 1 John 3 reasoning into
Hebrews, and do not treat this ruling as settling 1 John 3** — when we reach 1 John, that
verse gets decided on its own evidence.

*Method note, against 0003:* the warrant here is the Greek participle, not the fact that
ESV English reads "go on sinning deliberately". That the ESV made the same change to its
RSV base is confirmation, not the reason.

### 0112 — μαρτυρέω at Heb 10:15 departs from the glossary
**2026-07-30 · esv · settled**
The glossary rules μαρτυρέω → ESV-style **"bevidne"** (0019). At Heb 10:15 the Greek is
μαρτυρεῖ δὲ ἡμῖν — a **dative** complement — and Danish *bevidne* is transitive: it takes
what is testified, not the person testified to. "Bevidner for os" is not Danish.
**Ruled:** ESV-style reads **"vidner for os"**, declared in
`glossaries/concordance-exceptions.tsv` against this decision.
*Rationale:* concordance yields to grammar, as at 0044. Recorded rather than left silent,
per 0113.

### 0113 — Machine-checkable rulings, and the limits of that
**2026-07-30 · all · settled**
`tools/audit_translation.py` audits the Danish against the Greek: it enforces concordance,
enumerates source-side features Danish drops silently, and flags asymmetry between the
three versions. This decision records **what may be mechanised and what may not**, because
getting that boundary wrong is worse than having no tool.

**The glossary is now a specification, not notes.** `key-terms.tsv` carries a `scope`
column:
- **`konkordant`** — binding every occurrence. A missing rendering is a **failure**.
  Optionally narrowed by version (`konkordant:esv`) and by book
  (`konkordant@HEB`), because a ruling made in one book is not automatically global.
- **`standard`** (the default) — the usual rendering. Departing from it is normal and needs
  no note. This is most rows.

A qualifier in the source column may pin the part of speech (`εὐθύς (adv.)`) so a ruling
for one sense of an ambiguous lemma is not applied to another.

**Every departure from a `konkordant` rule must be declared** in
`glossaries/concordance-exceptions.tsv` with a decision number. The tool cannot judge
whether a break is right; it can guarantee no break happens without someone writing down
why. That is the whole mechanism.

**What this cannot do, and must not be trusted to do.** Three findings from building it:
1. **0007's condition is not a predicate.** "Wherever the same root is juxtaposed for
   effect" is a judgement. δίκαιος and δικαιοσύνη are therefore `standard`, and the root
   pair at Rom 3:26 is protected by human attention, not by the tool.
2. **Rulings over-generalise.** 0104's προσέρχομαι link is about Hebrews' cultic "approach
   God"; applied to Mark it fired on ordinary motion ("kom hen til ham"). Hence `@HEB`.
   Assume any new concordance ruling is book-local until shown otherwise.
3. **A clean run means nothing was *silently* dropped — not that the rendering is right.**
   Exegesis and Danish style are outside its reach entirely. The cold-reader pass remains
   the only control on those, and is still an unpaid debt.

*What it caught on first run,* in work already reported as finished: six defects in
Hebrews 10 (NIV-style 10:14 breaking the 0101 προσφορά chain and 10:22 σῶμα → "kroppen";
NLT-style 10:1 conflating προσέρχομαι with λατρεύω, 10:15 dropping μαρτυρέω, 10:19 missing
the 0104 παρρησία frame, 10:22 rendering πίστις as "tillid"), a Luke-specific rendering
recorded as a general rule for ἐπαγγελία, and — in **Luke, declared complete** — a plain
violation of **0038** at 15:7 and 15:10, where the NLT-style softened ἁμαρτωλός to
"ét menneske" in the very parable whose point 0038 says depends on the word stinging.
Both corrected.

### 0114 — δικαιόω is concordant only in the ESV-style
**2026-07-30 · all · settled** (narrows 0006 for machine-checking)
0006 fixes a Danish rendering of δικαιόω per version. Auditing Luke showed that only the
**ESV-style** ruling is genuinely concordant — its charter mandates flat consistency — while
the NIV- and NLT-style charters both license contextual variation, and Luke uses the verb in
three distinct senses: God declaring a sinner righteous (18:14), vindicating God or wisdom
(7:29, 7:35 — already split out by 0044), and **justifying oneself** (10:29; 16:15), which
0006 never covered.
**Ruled:** scope `konkordant:esv`; NIV- and NLT-style are `standard`. The glossary now also
records 0044's "give ret" as an ESV-style alternative, so the audit sees 7:29 as ruled
rather than as drift.
*Rationale:* a concordance rule that is really three rules produces false failures, and a
check that cries wolf stops being read. Per 0113, the honest fix is to narrow the rule to
where a charter actually demands it, not to loosen the check.

### 0115 — Mark's periphrastic future
**2026-07-30 · all · settled**
Mark builds a future with **εἰμί + present participle** (13:13 ἔσεσθε μισούμενοι;
13:25 ἔσονται … πίπτοντες) — a Semitism that stresses the continuing state.
**Ruled:** render with the ordinary Danish future in all three ("I skal hades af alle",
"stjernerne falder ned"). Danish has no progressive, and forcing one ("I vil vedblive at
være hadet") buys grammatical visibility at the cost of readable Danish in every register,
including the ESV-style's. Not footnoted — the loss is in the grammar, not the sense.
*Recorded so the audit's aspect queue does not re-raise it every chapter.*

### 0116 — Mark 14:41 is an ironic imperative, not a question
**2026-07-30 · all · settled**
Καθεύδετε τὸ λοιπὸν καὶ ἀναπαύεσθε is **formally ambiguous**: in the 2nd person plural the
present indicative and the imperative are identical, so the Greek can be read either
"Sleep on now and take your rest" or "Are you still sleeping and resting?"
**Ruled:** the **imperative** in all three versions — ESV-style "Sov nu videre og hvil
jer!", NIV-style the same, NLT-style "Så sov da videre, og hvil jer!" — with the question
reading footnoted in all three.
*Rationale:* **0013** takes the older rendering where the evidence is genuinely open, and
the imperative is what the KJV and the Danish tradition have. Note that the English
versions split here — ESV and NIV read it as a question, NLT as an imperative — which is
precisely why 0003 forbids deciding it by looking at them.
**How this was caught, and the gap it exposes:** the first draft had the ESV-style as an
imperative and the NIV- and NLT-style as questions. That is a **0002 violation** — the
three may differ in *rendering*, never in what a verse *means* — and it survived
`check_usfm.py`, the concordance check and the asymmetry check, because all three verses
were the right length and used the ruled vocabulary. It was found only by reading the
three side by side against the Greek.
*Standing lesson:* no current tool can detect a meaning divergence between the versions.
Per 0113 that is squarely in the third tier. **Read the three in parallel before closing a
chapter** — it is the cheapest control we have on 0002, and the parallel-column PDF built
for Hebrews 10 is the right shape for doing it.

### 0117 — The Passion narrative is where harmonisation gets in
**2026-07-30 · all · settled** (applies 0003, extends 0094)
Drafting Mark 14 the NLT-style rendered 14:65 as "»Sig os, hvem der slog dig!«" — the
question from **Matt 26:68 / Luke 22:64**. Mark has only **Προφήτευσον**, "Profetér!", and
he does not say Jesus was blindfolded either; περικαλύπτειν αὐτοῦ τὸ πρόσωπον is "cover his
face". Corrected in the text and footnoted that the parallels add the question.
*Rationale:* **0003** in its purest form. Nothing suggested the harmonisation — no English
version was consulted — which is exactly the danger: **the Passion narrative is the most
memorised text in the Gospels, so the harmonised version arrives from memory rather than
from the page.** 0094 made the same ruling for Mark 8:12's missing Jonah exception, and
0088 for the apostle lists.
**Standing instruction for Mark 14–16, Matt 26–28, Luke 22–24 and John 18–21:** before
closing a Passion chapter, check every remembered detail against the Greek of *that*
Gospel. Specifically at risk — the wording of the trial questions, the cry from the cross,
the inscription on the cross, the number and names of the women, and the words at the
empty tomb. Where a version has less than the reader expects, keep the less and footnote
that the parallels have more.

### 0118 — Hours of the day
**2026-07-30 · all · settled** (companion to 0017, which covers units and currency)
The Gospels count hours from sunrise, so "the third hour" is about nine in the morning.
- **ESV-style:** keep the ancient reckoning — "den tredje time", "den sjette time" — with the
  modern time in a footnote. First applied at Mark 15:25, 33, 34.
- **NIV-style and NLT-style:** give the modern time in the text — "klokken ni om morgenen",
  "fra klokken tolv til klokken tre" — footnoting the literal Greek.
*Rationale:* the NLT charter states the o'clock rule explicitly; the NIV's brief is what the
author would have written for a contemporary readership, and no Danish reader computes from
sunrise. The ESV-style keeps the ancient reckoning for the same reason it keeps ancient
units (0017): its charter trusts the reader with a footnote. Note that at Mark 15:33–34 the
three hours of darkness are a *duration* — the modern times must not obscure that it ran
from midday to mid-afternoon.

### 0119 — The ending of Mark
**2026-07-30 · all · settled** (the hardest application of 0004, 0080 and 0081)
Mark ends at **16:8**, mid-sentence, on **ἐφοβοῦντο γάρ** — "for they were afraid" — in
Sinaiticus and Vaticanus, the two oldest complete manuscripts. Eusebius and Jerome both
report that the accurate copies of their day stopped there. Antiquity produced two
continuations: the **Longer Ending** (16:9–20), known already in the second century to
Irenaeus and Tatian and present in the great majority of manuscripts; and a **Shorter
Ending**, in a handful of witnesses, sometimes alongside the Longer.

**Ruled, in all three versions:**
1. **Print 16:8 exactly as it stands**, ending on "for de var bange" / "for de var bange".
   Do not smooth the broken sentence and do not supply a closing cadence.
2. **Print 16:9–20 in the text**, under a section heading that names what it is:
   **"Den længere slutning på Markusevangeliet"**.
3. **Do not bracket typographically.** 0080 settled this: brackets in Danish overstate the
   evidence in one direction or the other. A `\s1` heading is structurally distinct in USFM,
   can be hidden by an app, and states the position in words rather than in punctuation.
4. **One substantial footnote at 16:8** giving the manuscript position, saying plainly that
   the Longer Ending's vocabulary and style differ from Mark's own, and **quoting the Shorter
   Ending in full** — it does not go in the text, being far more weakly attested.

*Rationale:* the evidence here is materially stronger against authorship than at Luke
22:43–44 or 23:34a, so the note has to say more than "some manuscripts differ" — a reader
who is told only that would reasonably conclude the question is trivial, and it is not.
But 0004 and 0014 govern the *text*: ESV, NIV and NLT all print the Longer Ending, it has
been read as Scripture since the second century, and removing twelve verses on our own
authority is not what a translation is for. **0013's conservative default takes the received
text and puts the honest doubt in the note** — which is exactly the shape of 0080 and 0081,
applied to the largest case in the New Testament.
*Note on the heading as a device:* this is the first time a heading has been used to carry
textual information rather than a summary of content. It is preferable to brackets and worth
reusing at John 7:53–8:11 when we reach it.

---

## Matthew

### 0120 — Matthew's genealogy: names, and the two prophets' names among the kings
**2026-07-30 · all · settled** (applies 0028; resolves a collision with 0004)
**Names.** 0028 governs and was not re-decided: Old Testament figures take their Danish
Old Testament form. Verified against the Hebrew — Ἀράμ is **Ram** (רָם, Ruth 4:19;
1 Chr 2:9–10), footnoted because the Greek reads Aram; Σαλμών is **Salmon**, which is the
form Ruth 4:21 itself uses (שַׂלְמוֹן) beside שַׂלְמָה in 4:20. The post-exilic names that occur
only here (Abiud, Azor, Sadok, Akim, Eliud, Mattan) are transliterated per 0028's second
clause; Eljakim and Shealtiel and Zerubbabel were already fixed by 0028 from Luke.

**Ἀσάφ at 1:7–8 and Ἀμώς at 1:10.** NA28 prints **Ἀσάφ** — the psalmist's name — where the
king was **Asa**, and **Ἀμώς** — the prophet's — where the king was **Amon**.
**Ruled:** print **Asa** and **Amon**, and footnote that the best manuscripts spell them
Asaf and Amos.
*Rationale, because 0004 and 0028 pull against each other here:* 0004 binds us to the
critical text on **translation-affecting** variants. This one is not: nobody disputes that
the men in the list are the kings Asa and Amon, so the two spellings identify the same
person and the choice is orthographic, which is 0028's territory — and 0028 exists so that
a Danish reader can see the chain running back into the Old Testament. Printing "Asaf" would
break that chain and suggest Matthew put a psalmist among the kings. **0013** and all three
English versions agree. The note keeps the evidence visible per 0014.

**Two further features of the list, footnoted rather than smoothed:** Matthew omits Ahaziah,
Joash and Amaziah between Joram and Uzziah, and his fourteen-fourteen-fourteen scheme
(1:17) does not add up if read as a complete register — say so and leave it. And at **1:16**
the chain breaks: sixteen verses of "N blev far til N" give way to a passive "blev født",
and Joseph is called Mary's husband, not Jesus' father. That break is the point of the
genealogy and must be visible in all three versions.

### 0121 — παρθένος at Matthew 1:23
**2026-07-30 · all · settled** (a second application of 0103)
Matthew quotes Isa 7:14 in the Greek form, which reads **παρθένος**, "virgin". The Hebrew
has **עַלְמָה** (*alma*) — a young woman of marriageable age, a word that does not exclude
virginity but does not state it.
**Ruled:** render **"jomfruen"** in all three, and footnote the Hebrew in all three, saying
plainly what *alma* does and does not assert.
*Rationale:* exactly 0103, which was decided at Heb 10:5 and made a standing rule — where a
New Testament author's argument rests on the Greek Old Testament, translate what he wrote
and footnote the Hebrew, harmonising in neither direction. Matthew's whole appeal depends on
παρθένος, so replacing it with "den unge kvinde" would rewrite his argument; but pretending
the Hebrew says "virgin" would be the opposite error, and 0014 requires the reader be told.
The note is deliberately even-handed: it neither concedes the point nor overstates it.
Ἐμμανουήλ keeps Matthew's own gloss, per 0090.

### 0122 — μάγοι at Matthew 2
**2026-07-30 · all · settled**
μάγοι are Persian or Babylonian scholar-priests who read the stars. They are not kings, and
Matthew does not number them.
- **ESV-style and NIV-style: "vise mænd fra Østerland"** — the received Danish wording, which
  0016 tells the ESV-style not to abandon without cause, footnoting the Greek and what the
  word means.
- **NLT-style: "stjernekyndige mænd"** — its charter's gate test is met, because "vise mænd"
  no longer tells a Danish reader what these men did, and what they did is what sets the whole
  chapter in motion.
All three footnote that the text says neither how many they were nor that they were kings.

### 0123 — Matthew's Old Testament citations do not all come from the same text
**2026-07-30 · all · settled** (refines 0103 and 0121)
Matthew 2 has four citations and they behave differently, which matters because 0103 was
written as though a New Testament author were simply LXX-dependent:
- **2:6 (Mic 5:1)** is a **composite**, spliced with 2 Sam 5:2, and its wording agrees with
  neither the Hebrew nor the Greek — Micah says Bethlehem *is* little among Judah's clans,
  Matthew that it is by no means the least. **Translate Matthew and footnote the difference;
  do not correct him toward Micah.**
- **2:15 (Hos 11:1)** follows the **Hebrew** — "my son", singular — *against* the Greek Old
  Testament's "his children". So Matthew chooses the text-form that carries his argument.
- **2:18 (Jer 31:15)** is close to the Hebrew.
- **2:23** has no source text at all; Matthew writes "the prophets", plural, and is almost
  certainly playing on Hebrew *neser* (Isa 11:1) or *nazir* (Judg 13:5). The wordplay cannot
  be carried into Danish. **Footnote it and do not attempt it.**
*Standing rule, superseding the flat form of 0103:* establish per citation which text-form the
author is using, and footnote the divergence. Never harmonise the New Testament citation
toward the Old Testament source, and never assume the Greek Old Testament is the source
merely because it usually is.

### 0124 — βασιλεία τῶν οὐρανῶν is Matthew's own phrase
**2026-07-30 · all · settled**
Matthew says "the kingdom of **the heavens**" some thirty-two times where Mark and Luke say
"the kingdom of God" — almost certainly a reverential circumlocution of the sort Jewish usage
favoured. The referent is the same; the wording is his.
**Ruled:** ESV-style **"Himmeriget"** (the received Danish form, per 0016); NIV- and NLT-style
**"Himmelriget"** (the transparent modern form). All three keep it **distinct from "Guds rige"**,
which stays reserved for βασιλεία τοῦ θεοῦ — including at Matt 12:28 and 19:24, where Matthew
himself switches to "Guds rige" and the switch must be visible. Scope in the glossary is
`konkordant@MAT`. Footnote at the first occurrence (3:2) explaining the circumlocution.
*Rationale:* 0002 forbids the three differing about what a phrase *means*, not about how they
spell it, and this is the same word in two Danish registers. But levelling Matthew's phrase into
"Guds rige" would erase an authorial choice — the same reasoning as 0036 on Menneskesønnen and
0093 on the two kinds of basket.

### 0125 — δικαιοσύνη is a Matthean theme and survives in all three
**2026-07-30 · nlt · settled** (applies 0019; narrows 0114 in practice)
Matthew uses δικαιοσύνη seven times as a **running theme** — 3:15; 5:6, 5:10, 5:20; 6:1,
6:33; 21:32 — where Mark uses it not at all and Luke once. It is one of the words the book
is built on.
Drafting Matthew 3–5 the NLT-style rendered it four times out of four as "gøre det rette",
which dissolves the theme completely. **Corrected at 3:15, 5:6, 5:10 and 5:20 to keep the
Danish root** ("retfærdighed", "leve retfærdigt", "hvad retfærdigheden kræver").
*Rationale:* **0019** is a gate, not a licence, and its three triggers are that the literal
rendering be hard to understand, misleading, or archaic. **"Retfærdighed" is none of those
in Danish** — it is an ordinary word — so the trigger was never met. The NLT charter's
allowance of a wider range for theological terms is not a licence to delete the term; the
English NLT itself keeps a noun here. This is the third time the NLT-style has over-reached
in the same way (Heb 10:22 πίστις, Mark 14:38 πνεῦμα/σάρξ, now this), which makes it a
pattern rather than an accident.
*Why the audit could not catch it:* 0114 set δικαιοσύνη to `standard` scope, because 0007's
condition ("wherever the root is juxtaposed for effect") is not a predicate a script can
test. So the tool reported it only as an advisory departure. **That advisory count is worth
reading, not just the failures** — four hits on one lemma in one chapter is a signal.
