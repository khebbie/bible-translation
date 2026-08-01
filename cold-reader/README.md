# Kold læsning

Én rapport pr. kapitel: `<BOG>-<kapitel>.md`, fx `LUK-7.md`.

Den kolde læser er den eneste kontrol vi har på **eksegese og dansk stil**.
`tools/check_usfm.py` svarer på *er filen velformet*, `tools/audit_translation.py` på
*bar dansken hvad græsken markerede* — ingen af dem kan svare på om gengivelsen er
rigtig, eller om en version lyder som sit charter (0113).

## Reglen

Fase A læses **blindt**: ingen `sources/`, ingen `briefs/`, ingen `decisions/LOG.md`.
Kun de tre USFM-filer — plus `CHARTERS.md` og `<version>/charter/METHOD.md`, som er
specifikation for register, ikke kilde. Fejltilstanden er *anchoring*: har man læst
begrundelsen først, rationaliserer man udkastet i stedet for at udfordre det
(WORKFLOW.md, "Working autonomously").

Fase B åbner græsken og afgør hver anmærkning. Rettelser følger græsken og charteret,
aldrig den engelske ESV/NIV/NLT (0003).

## Skabelon

```markdown
# LUK 7 — kold læsning

Læst blindt: <dato>. Fase B: <dato>.

## 1. Forståelse
v. 4 — «...» hvem er "han"? Måtte læse to gange.

## 2. Dansk
v. 12 (NLT-stil) — «...» lyder oversat; en dansker ville sige «...».

## 3. Charter
ESV-stil: ...
NIV-stil: ...
NLT-stil: ... (et NLT-vers der lyder ordret er en fejl mod charteret)

## 4. Falder de sammen?
v. 21, v. 33 — næsten ordret ens i alle tre.

## 5. Udfordringer
...

## Fase B — afgørelser
v. 4 — RETTET: ...
v. 12 — AFVIST: græsken har ..., og charteret kræver ...
```
