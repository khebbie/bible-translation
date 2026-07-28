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
