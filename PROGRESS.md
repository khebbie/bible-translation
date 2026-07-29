# Progress

| Book | Chapters | ESV-style | NIV-style | NLT-style |
|---|---|---|---|---|
| Luke | **24 / 24 — færdig** | ✅ hele bogen | ✅ hele bogen | ✅ hele bogen |
| Mark | 11 / 16 | ✅ ch. 1–11 | ✅ ch. 1–11 | ✅ ch. 1–11 |
| Romans | pericope only | ✅ 3:21–26 | ✅ 3:21–26 | ✅ 3:21–26 |

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

## Standing debt

- **No cold-reader pass has ever been run.** Every check so far was done in a context
  that had already seen the Greek. Worth running fresh every few books, on the
  NLT-style especially.
- **Still no schema validator.** `tools/check_usfm.py` now checks verse
  completeness, marker balance, verse order, footnote refs and cross-version
  agreement — run it after every chapter. That is not USFM *schema* conformance;
  `usfm-grammar` is still worth adding. See `FORMAT.md`.
