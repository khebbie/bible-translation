# Progress

| Book | Chapters | ESV-style | NIV-style | NLT-style |
|---|---|---|---|---|
| Luke | 5 / 24 | ✅ ch. 1–5 | ✅ ch. 1–5 | ✅ ch. 1–5 |
| Romans | pericope only | ✅ 3:21–26 | ✅ 3:21–26 | ✅ 3:21–26 |

**Next:** Luke 6 onward. Files are `<version>/translation/LUK.usfm`; append chapters in
order.

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
- Luke 6 has the Sabbath controversies, the choosing of the Twelve, and the Sermon on
  the Plain (6:20–49) — the Beatitudes and Woes are poetry and need `\q1/\q2`. Fix the
  rendering of μακάριος when it first appears at 6:20; it recurs throughout Luke.
- κύριος in Luke 1 is regular "Herren", not `\nd`. `\nd HERREN\nd*` is reserved for
  YHWH in the Hebrew text and for explicit OT quotation in the NT (decision 0005).
- Recurring names fixed in Luke 1: Zakarias, Elisabet, Maria, Josef, Theofilus,
  Nazaret, Judæa, Galilæa, Johannes, Gabriel, Abia(ja).

## Standing debt

- **No cold-reader pass has ever been run.** Every check so far was done in a context
  that had already seen the Greek. Worth running fresh every few books, on the
  NLT-style especially.
- **No USFM validator installed.** Files are checked by an inline script for verse
  completeness and balanced markers only — that is not schema validation. See
  `FORMAT.md`.
