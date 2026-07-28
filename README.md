# Bible Translation Workspace

Working from the original Hebrew and Greek. This document records **what the major
English versions translated from**, and **what we actually have on disk** to work with.

---

## Part 1 — Textual basis of NIV, ESV, NLT

| | Old Testament (Hebrew/Aramaic) | New Testament (Greek) |
|---|---|---|
| **NIV** (2011) | Masoretic Text as in the *latest edition of Biblia Hebraica* (i.e. BHS). Marginal (Qere) readings sometimes followed over the Ketiv. Consulted: Dead Sea Scrolls, Samaritan Pentateuch, LXX, Vulgate, Syriac Peshitta, Targums, and the scribal *tiqqune sopherim* traditions. | Eclectic text, "based on the latest editions of the Nestle-Aland/United Bible Societies' Greek New Testament", with the committee making its own choices among variants. |
| **ESV** (2016 text) | *Biblia Hebraica Stuttgartensia* (5th ed., 1997). | UBS *Greek New Testament* (5th corrected ed., 2014) and Nestle-Aland *Novum Testamentum Graece* (28th ed., 2012). |
| **NLT** (2nd ed. 2004/2015) | *Biblia Hebraica Stuttgartensia* (1977). Further compared against DSS, LXX and other Greek mss, Samaritan Pentateuch, Syriac Peshitta, Latin Vulgate. | UBS *Greek New Testament* (4th rev. ed., 1993) **and** Nestle-Aland (27th ed., 1993) — same text, differing punctuation and apparatus. |

### The important nuance

All three sit on essentially the **same two critical editions**: BHS for the OT and
NA/UBS for the NT. They differ far less in *source text* than in *translation
philosophy* — ESV formal-equivalent, NLT dynamic/functional, NIV mediating. Where
they diverge textually it is usually a **decision about a variant**, not a different
base edition.

Note the ESV/NLT edition mismatch is mostly cosmetic: BHS 1977 and BHS 1997 are the
same critical text with corrected printings, and NA27→NA28 changed the text only in
the Catholic Epistles (about 34 places).

### Licensing reality

**BHS, NA28 and UBS5 are all copyrighted** by the Deutsche Bibelgesellschaft and
cannot be freely downloaded. What we can get is the underlying manuscript evidence
and free critical editions that are extremely close to them — which is what is
fetched below, including apparatus data that tells us exactly what NA28/UBS5 read.

---

## Part 2 — What is on disk (`sources/`)

### Hebrew Old Testament

**`sources/morphhb/`** — OpenScriptures Hebrew Bible (113 MB)
- `wlc/` — **Westminster Leningrad Codex**, 39 books as OSIS XML + `VerseMap.xml`.
- The WLC is a transcription of the **Leningrad Codex**, which is the very manuscript
  BHS is a diplomatic edition of. So this *is* the BHS base text, minus BHS's
  copyrighted critical apparatus.
- Full vowel points and cantillation, per-word morphology and Strong's lemmas,
  with prefix/suffix segmentation marked by `/`.
- License: CC BY 4.0.

```xml
<w lemma="b/7225" morph="HR/Ncfsa" id="01xeN">בְּ/רֵאשִׁ֖ית</w>
<w lemma="1254 a" morph="HVqp3ms" id="01Nvk">בָּרָ֣א</w>
<w lemma="430"    morph="HNcmpa"   id="01TyA">אֱלֹהִ֑ים</w>
```

### Greek New Testament

**`sources/sblgnt/`** — MorphGNT / SBLGNT (10 MB, 27 books)
- The **SBL Greek New Testament** with full morphological parsing.
- Modern critical text, very close to NA28; differs from NA28 in ~540 variation units.
- Tab-separated: `book/ch/v · POS · parsing code · text · word · normalized · lemma`.
- License: SBLGNT EULA for the text, CC BY-SA 3.0 for the parsing.

```
040101 P- -------- Ἐν     Ἐν     ἐν    ἐν
040101 N- ----DSF- ἀρχῇ   ἀρχῇ   ἀρχῇ  ἀρχή
040101 V- 3IAI-S-- ἦν     ἦν     ἦν    εἰμί
040101 N- ----NSM- λόγος, λόγος  λόγος λόγος
```

**`sources/Nestle1904/`** — Nestle 1904 GNT (68 MB)
- **Fully public domain** critical text — the closest PD text to modern NA.
- Directories: `xml/`, `morph/`, `glosses/`, `xhtml/`, `xquery/`.
- Useful when licensing must be unencumbered.

### The variant-aware layer — most valuable piece

**`sources/STEPBible-Data/`** — Tyndale House / STEPBible (482 MB, CC BY 4.0)

This is the bridge to the copyrighted editions. Every word is tagged with **which
editions contain it**, so we can see NA28/UBS5 readings without owning them.

- `Translators Amalgamated OT+NT/TAHOT *` — Hebrew OT, tagged, with variants.
- `Translators Amalgamated OT+NT/TAGNT *` — Greek NT: every word from **NA27/NA28,
  TR, SBL, THGNT, Byz, WH, Tregelles**, flagged for whether the variant actually
  affects translation.
- `Lexicons/` — Brief lexicons for Hebrew (TBESH) and Greek (TBESG), plus the full
  formatted **LSJ** (32 MB).
- `Morphology codes/` — expansions of the Hebrew and Greek morphology codes.
- `Proper Nouns/`, `Versification/` — name disambiguation and versification mapping.
- `Tagged-Bibles/TTESV` — Tyndale translation tags **for the ESV** (CC BY-NC).

TAGNT word line for John 1:1 — note the edition list in column 6:

```
Jhn.1.1#01=NKO   Ἐν (En)   In [the]   G1722=PREP   ἐν=in/on/among
                 NA28+NA27+Tyn+SBL+WH+Treg+TR+Byz
```

Word-type codes: `N` = Nestlé-Aland ("Ancient"), `K` = Textus Receptus / KJV
("Traditional"), `O` = other editions. Lowercase means the difference is too minor to
change the translation. Roughly 94% of NT words are identical across all editions.

TAHOT for Genesis 1:1, with transliteration, gloss, extended Strong's and morphology:

```
Gen.1.1#01=L  בְּ/רֵאשִׁ֖ית  be./re.Shit  in/ beginning  H9003/{H7225G}  HR/Ncfsa
Gen.1.1#02=L  בָּרָ֣א        ba.Ra'       he created     {H1254A}        HVqp3ms
Gen.1.1#03=L  אֱלֹהִ֑ים      'E.lo.Him    God            {H0430G}        HNcmpa
```

---

## Coverage summary

| Need | Source | Status |
|---|---|---|
| BHS base text | `morphhb/wlc` (Leningrad Codex) | ✅ equivalent |
| BHS apparatus | — | ❌ copyrighted; partial substitute in TAHOT |
| NA28/UBS5 text | — | ❌ copyrighted; readings recoverable from TAGNT tags |
| Modern critical GNT | `sblgnt` | ✅ |
| PD critical GNT | `Nestle1904` | ✅ |
| Hebrew + Greek morphology | morphhb, MorphGNT, STEPBible | ✅ |
| Lexicons (incl. LSJ) | `STEPBible-Data/Lexicons` | ✅ |
| Variant apparatus across editions | `STEPBible-Data` TAGNT/TAHOT | ✅ |

## Not yet fetched — candidates if needed

- **Septuagint (LXX)** — Rahlfs; consulted by all three versions for the OT.
- **Dead Sea Scrolls** biblical texts — explicitly consulted by NIV and NLT.
- **Samaritan Pentateuch**, **Syriac Peshitta**, **Latin Vulgate** (Vulgate is PD).
- **THGNT** (Tyndale House Greek NT) as a standalone edition.

## Licensing note for redistribution

`morphhb`, `Nestle1904` and `STEPBible-Data` are permissive (CC BY / public domain).
The **SBLGNT text** is under its own EULA, and **TTESV is CC BY-NC**. STEPBible also
asks that you link back to them rather than redistribute their data yourself. Check
these before publishing anything derived.
