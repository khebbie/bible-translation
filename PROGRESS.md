# Progress

| Book | Chapters | ESV-style | NIV-style | NLT-style |
|---|---|---|---|---|
| Luke | 3 / 24 | ✅ ch. 1–3 | ✅ ch. 1–3 | ✅ ch. 1–3 |
| Romans | pericope only | ✅ 3:21–26 | ✅ 3:21–26 | ✅ 3:21–26 |

**Next:** Luke 4 onward. Files are `<version>/translation/LUK.usfm`; append chapters in
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
- Luke 4 has the temptation (OT quotations from Deut — check whether Luke follows LXX,
  and use `\nd HERREN\nd*` where the quotation renders YHWH, per 0005) and the Nazareth
  sermon quoting Isa 61, where Luke's citation diverges from both MT and LXX.
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
