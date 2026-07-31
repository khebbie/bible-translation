# Progress

| Book | Chapters | ESV-style | NIV-style | NLT-style |
|---|---|---|---|---|
| Luke | **24 / 24 — færdig** | ✅ hele bogen | ✅ hele bogen | ✅ hele bogen |
| Mark | **16 / 16 — færdig** | ✅ hele bogen | ✅ hele bogen | ✅ hele bogen |
| Matthew | 15 / 28 | ✅ ch. 1–15 | ✅ ch. 1–15 | ✅ ch. 1–15 |
| Romans | pericope only | ✅ 3:21–26 | ✅ 3:21–26 | ✅ 3:21–26 |
| Hebrews | ch. 10 only | ✅ 10 | ✅ 10 | ✅ 10 |

**Task tracking is in beads.** `bd ready` returns the next chapter. All 89 Gospel
chapters exist as `bd` issues under four epics (MAT `bible-1x3`, MRK `bible-bxe`,
LUK `bible-ycn`, JHN `bible-4m1`), chained sequentially. This table is a human-readable
mirror — beads is the source of truth for *what is left*; this file holds the
*notes carried forward*.

Files are `<version>/translation/<BOOK>.usfm`; append chapters in order.

## Notes carried forward

- Register is now set by Luke 1 and must hold: ESV-style keeps the Septuagintal
  καί-chains ("Og det skete…"); NIV-style keeps the cadence audible but breaks
  sentences; NLT-style is plain modern Danish. See decision 0021.
- **Name policy is fixed — decision 0028.** OT figures take their Danish OT form
  (Esajas, Boaz, Obed, Nakshon, Amminadab, Hesron, Peres, Tera, Arpakshad, Noa,
  Metusalem, Enok, Shealtiel, Zerubbabel); Luke-only genealogy names are transliterated
  (Melki, Jannaj, Josek, Joda, Joanan, Resa, Maat, Semein, Naggaj, Esli, Elmadam,
  Kosam, Addi, Jorim, Jonam, Eljakim, Melea, Menna, Mattata, Admin, Arni). This governs
  Matthew's genealogy too — do not re-decide it there.
- **`\nd HERREN\nd*` is now live in NT quotations** — decision 0033. Used at 4:8, 4:12,
  4:18, 4:19. Apply wherever an OT citation renders YHWH; ordinary κύριος stays "Herren".
- Fixed in Luke 4: Kapernaum, Sarepta, Elias, Elisa, Na'aman, Sidon, Djævelen, Satan.
- **Menneskesønnen** is fixed for ὁ υἱὸς τοῦ ἀνθρώπου in all three (0036), including
  the NLT-style. ἐπιστάτης = "Mester" (0037), ἁμαρτωλός = "synder" (0038).
- **μακάριος / οὐαί fixed (0040):** ESV- and NIV-style "Salige er I…" / "Ve jer…";
  NLT-style "Gud velsigner jer, som…" / "Hvor vil I komme til at sørge…". Apply at
  7:23; 10:23; 11:27–28, 42–52; 12:37–43; 14:14–15; 23:29.
- Apostle names fixed at 6:14–16: Peter, Andreas, Jakob, Johannes, Filip,
  Bartholomæus, Matthæus, Thomas, Jakob (Alfæus' søn), Simon Zeloten, Judas (Jakobs
  søn), Judas Iskariot.
- **δοῦλος = "tjener" by default in the Gospels** (0043), "slave" only where ownership
  is the point. **Currency split is live** (0046): ESV/NIV keep "denarer" + footnote,
  NLT-style converts to months/years of wages.
- Gerasenes settled at 8:26/8:37 (0048); κράσπεδον = "kvasten på kappen" (0050).
- **The travel narrative began at 9:51** and runs to 19:44 — the long central section
  unique to Luke. Register should stay steady across it.
- **Fadervor settled (0059):** Luke's shorter five-petition form, with the Matthean
  additions quoted in full in the footnote. ESV-style uses the received Danish wording
  for the petitions Luke has.
- **Small-coin policy set (0062):** ἀσσάριον = "skilling"; λεπτόν = "skærv" in the
  ESV-style — keep that word so 12:59 and the widow's mite in 21:2 read as one.
- **Dry measures set (0065):** σάτον = "mål" + footnote in ESV/NIV-style; NLT-style
  converts to litres. The size is often the point of a parable — do not let it vanish.
- **Textual-variant policy is now fully worked out** across 0073, 0080, 0081, 0082:
  verses the critical text lacks are omitted and footnoted (17:36; 23:17); bracketed
  passages are printed with a note (22:19b–20; 22:43–44; 23:34a; the Luke 24 Western
  non-interpolations). Never bracket typographically in Danish — it overstates the
  evidence in one direction or the other.
- **Measures ladder is complete:** λεπτόν/ἀσσάριον (0062), δηνάριον (0046), δραχμή
  (0069), μνᾶ (0077), σάτον (0065), βάτος/κόρος (0071), στάδιον (24:13). ESV/NIV keep
  the ancient unit + footnote; NLT-style converts, to metric or a wage period.
- κύριος in Luke 1 is regular "Herren", not `\nd`. `\nd HERREN\nd*` is reserved for
  YHWH in the Hebrew text and for explicit OT quotation in the NT (decision 0005).
- Recurring names fixed in Luke 1: Zakarias, Elisabet, Maria, Josef, Theofilus,
  Nazaret, Judæa, Galilæa, Johannes, Gabriel, Abia(ja).

## Mark — notes carried forward

- **εὐθύς is the engine of Mark** (0084): ESV-style "straks" concordantly all ~42 times;
  NIV-style mostly "straks"; NLT-style may vary but must not lose the breathlessness.
- **Historic present kept** in the ESV-style where Danish carries it (0085). Mark's Greek
  is rough and paratactic — **the ESV-style must read noticeably rougher in Mark than in
  Luke**, or the charter is not being applied.
- **NA28 governs over SBLGNT** where they diverge (0083); TAGNT settles it. First hit was
  Mark 1:41 (compassion, not anger) and 1:1 ("Guds Søn" kept).
- **Three controls now run per chapter, and each caught something the others missed:**
  `tools/check_usfm.py` (well-formed), `tools/audit_translation.py` (did the Danish carry
  the Greek — 0113), and **`tools/parallel.py BOOK CH`, read by eye for meaning
  divergences** (0116). The parallel read is not optional: in Mark 14 it alone caught the
  0002 violation at 14:41, the 0019 over-reach at 14:38, and the 0117 harmonisation at
  14:65. None of the three was visible to either script.
- **0117 — Passion-narrative warning, live from Mark 14 to 16:** the remembered wording
  arrives from memory instead of from the page. Check every familiar detail against the
  Greek of *this* Gospel.
- **The NLT-style over-reaches under pressure** — twice now (Heb 10:22, Mark 14:38) it
  dissolved a contrast the Greek marks, where 0019's gate test was never met. When a verse
  contains a paired abstraction (ånd/kød, tro/tillid), check 0019 before recasting.

## Matthew — notes carried forward

- **0028 governs the genealogy and was not re-decided** (0120). Names verified against the
  Hebrew: Ram (not Aram), Salmon, Hesron, Amminadab, Nakshon, Boaz, Obed, Isaj.
- **Asa and Amon at 1:7–8 and 1:10**, though NA28 spells them Asaf and Amos — 0120 rules
  this orthographic, not textual, and footnotes it. Do not revisit.
- **0121 — παρθένος at 1:23** applies 0103 to Matthew: translate the Greek Old Testament
  form the author quotes, footnote the Hebrew *alma*, harmonise in neither direction.
  Matthew quotes the OT constantly, so 0103/0121 will be in play for the whole book.
- **χριστός across the book:** ESV-style "Kristus" throughout, NIV-style "Kristus",
  NLT-style **"Messias"** — Matthew's audience is Jewish throughout, so 0027 sends the
  NLT-style to "Messias" everywhere, including the name-pair at 1:1 and 1:18.
- **0124 — Himmeriget/Himmelriget** for βασιλεία τῶν οὐρανῶν, kept distinct from "Guds rige"
  throughout. Watch 12:28 and 19:24, where Matthew himself switches to "Guds rige".
- **δικαιοσύνη is a Matthean theme** (3:15; 5:6.10.20; 6:1.33; 21:32) and **0125 now requires
  the Danish root in all three**. It had already been dissolved four times out of four in the
  NLT-style before being caught. 6:1 and 6:33 are next; 21:32 later. 0114 leaves it at
  `standard` scope, so **read the audit's advisory counts, not just the failures** — four hits
  on one lemma in one chapter was the signal.
- **Do not harmonise the baptism voice:** Matthew 3:17 is third person ("Denne er"), Mark 1:11
  and Luke 3:22 second person ("Du er"). Footnoted, not levelled — 0117 territory.
- **0127 — Matthew doubles.** Two demoniacs (8:28), two blind men (9:27; 20:30), two donkeys
  (21:2–7), and Gadara where Mark and Luke have Gerasa. **Never reduce to the Markan number**
  — that is 0117's warning in another key.
- **0083 bites in Matthew.** At 6:33 SBLGNT and WH omit τοῦ θεοῦ; NA28 has it. Reading the
  SBLGNT file alone would have produced "søg først riget". **Consult TAGNT wherever a phrase
  looks unexpectedly bare** — the SBLGNT file is the vehicle, not the authority.
- `tools/check_usfm.py` now carries the full MAT verse counts; 17:21, 18:11 and 23:14 are
  already in the omitted list per 0073.

## Hebrews 10 — out of sequence

Translated on request 2026-07-30, while Mark 13 was still open and before any of
Hebrews 1–9 exists. Files are `<version>/translation/HEB-10.usfm` (chapter-level draft
per `FORMAT.md`) and must be **merged into `HEB.usfm`** when the book is done properly.

- Shared brief: `briefs/heb-10.md`. Decisions **0101–0110**.
- **0101 is the load-bearing one:** προσφορά = "offergave" concordantly at 10:5.8.10.14.18.
  If that chain breaks, the argument of vv1–18 breaks. Same for τελειόω (1, 14) and
  ἁγιάζω (10, 14, 29) — and do not level ἁγιάζω's perfect/present.
- **0103 is a standing rule for the whole book:** where Hebrews' argument rests on a
  Greek Old Testament reading the Masoretic Text does not support (10:5 "a body" against
  the Hebrew "ears"), translate what Hebrews wrote and footnote the Hebrew. This will
  recur constantly in Hebrews — it is the book's method.
- **0105** fixes ἀδελφοί for all the epistles: ESV-style "brødre" + a first-occurrence
  footnote per book; the other two "brødre og søstre".
- `tools/check_usfm.py` now carries the full HEB verse counts (13 chapters).
- Still untranslated in Hebrews: everything except chapter 10. No `bd` epic exists for
  it; the Gospels remain the planned sequence.

## Where to pick up (2026-07-31)

`bd ready` returns **MAT 16**. Matthew 1–15 is done in all three versions; 13 Matthew
chapters and all 21 of John remain, plus `bible-kny` (glossary scope) and `bible-5fp`
(cold reader).

Live warnings for the chapters ahead:
- **17:21, 18:11 and 23:14** are TR-only and must be omitted with a footnote (0073).
  `tools/check_usfm.py` already knows they are not missing.
- **20:30 two blind men, 21:2–7 two donkeys** — 0127; never reduce to the Markan number.
- **21:32** is the last δικαιοσύνη in the Matthean chain; 0125 requires the Danish root.
- **26–28 is the Passion narrative** — 0117 is live: check every remembered detail
  against the Greek of *this* Gospel, especially the trial questions, the cry from the
  cross, the inscription, and the names of the women.
- **John** will need its own opening decisions: ὁ λόγος in 1:1–18, οἱ Ἰουδαῖοι (the NLT
  charter has an explicit rule), the ἐγώ εἰμι sayings, and 7:53–8:11, where 0119's
  heading device is the model.

## Standing debt

- **No cold-reader pass has ever been run.** Every check so far was done in a context
  that had already seen the Greek. Worth running fresh every few books, on the
  NLT-style especially.
- **Still no schema validator.** `tools/check_usfm.py` now checks verse
  completeness, marker balance, verse order, footnote refs and cross-version
  agreement — run it after every chapter. That is not USFM *schema* conformance;
  `usfm-grammar` is still worth adding. See `FORMAT.md`.
