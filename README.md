# Handleiding voor de leraar — Les 2: Mijn digitale onderzoeksmap

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWWE — 2de graad Maatschappij- en welzijnswetenschappen, doorstroomfinaliteit
**Lesduur:** 1 × 50 minuten (formatief)
**Context:** Onderzoekslabo Jongeren & Welzijn, een fictieve schooleigen onderzoeksgroep
**Lokaal:** 18 — computers met Windows 11, Google Workspace in Chrome
**Lesdag:** donderdag 1 oktober 2026, 8ste lesuur (rooster van 25-09-2026)
**Kernleerplandoel:** `BV2_04.03` — digitale inhouden beheren (toepassen)

---

## 1. Inhoud van het pakket

```text
W04 - Les 02 - MWW - Mijn digitale onderzoeksmap/
├── index.html                   # de leerlingentool: route · één stap · checklist (zie §1b)
├── presentatie.html             # 8 klassikale dia's voor de fase "Ik doe"
├── css/
│   ├── style.css                # leerlingentool (Dalton-kleuren; drie kolommen, op een smal venster onder elkaar)
│   └── slides.css               # dia's (16:9, beamer)
├── js/
│   ├── script.js                # stappen, checklist, zelftest
│   └── slides.js                # dia's: onthullen, notities (N), volledig scherm (F)
├── assets/
│   ├── onderzoekslabo-logo.svg  # logo van het fictieve labo (eigen werk)
│   ├── onderzoekslabo-icon.svg  # favicon
│   ├── dalton-gent-logo.png     # logo GO! Dalton Gent
│   ├── fonts/                   # Atkinson Hyperlegible + Montserrat (OFL, zelf gehost)
│   └── screenshots/             # hier plaats jij screenshots (zie §5)
├── werkdocument/
│   ├── Onderzoeksmap-paspoort.docx         # het werkdocument dat de leerling INLEVERT
│   ├── Les2_bestanden-om-op-te-ruimen.zip  # DIT hang je aan de opdracht
│   ├── rommel/                             # de vijf losse bestanden die in de zip zitten
│   └── maak_werkdocumenten.py              # genereert alles opnieuw (python-docx, openpyxl, Pillow)
├── lesvoorbereiding.md          # volledige lesvoorbereiding volgens §46 van de AI-lesplanner
├── dalton-lesfiche.html         # Dalton-lesfiche in de kleurcode: openen, Kopieer, plakken in je planner
├── lesdoelen.json               # codes van de leerplandoelen voor je jaaroverzicht
└── README.md                    # deze handleiding
```

De website heeft geen server, database, login of tracking nodig. Er worden geen externe bestanden
geladen. `localStorage` bewaart alleen de vinkjes en de laatste stap (voorvoegsel
`onderzoekslabo_map_v2_`), met een wisknop.


### 1b. Hoe de lespagina werkt (versie 2)

De pagina volgt de opbouw van PedalPro: rustig, één ding tegelijk.

- **Links de route** — alle stappen met hun naam, altijd zichtbaar. Een afgewerkte stap krijgt
  een groen vinkje.
- **Midden één stap** — altijd dezelfde vijf blokken: één zin uitleg · *Wat moet je doen?*
  (3 tot 6 handelingen) · hoogstens één tip · *Hulp nodig?* (dichtgeklapt) · *Klaar als*.
- **Rechts de checklist** — 23 concrete taken, per stap gegroepeerd. Die vervangen de losse
  "Klaar"-vinkjes en de lijsten *Controleer jezelf* van versie 1.
- **Op een smal venster** staat alles onder elkaar: bovenaan een rij genummerde bolletjes, dan de
  stap, dan alleen de taken van díe stap. Hoe de leerlingen hun vensters schikken, kiezen ze zelf;
  de pagina zegt er niets over.
  *Toon alles* opent de hele lijst; in stap 8 staat ze altijd helemaal open.
- **Theoriekaart** is een gewone pagina met tien kaartjes, geen uitschuifpaneel meer.
- **Alleen Windows 11**: alle klassen werken in lokaal 18. De pagina geeft geen Chromebook-uitleg
  meer en vraagt ook niet naar het toestel.

Wat er ten opzichte van versie 1 wegviel: de onderstreepte woorden met uitleg (nu het kaartje
*Woorden* op de theoriekaart), de blokken *Waarom?* en *Waar werk je?* (nu één zin en een label
bovenaan), de tijden per stap (staan in `dalton-lesfiche.html`), en van de zestien hints bleef er
per stap één *Hulp nodig?* over.

> [!IMPORTANT]
> **In versie 1 stonden vijf klikpaden verkeerd.** Nagelezen in de Nederlandse helppagina's van
> Google op 23-09-2026 en in versie 2 overal rechtgezet, ook in het paspoort:
>
> | Stond er | Wordt |
> |---|---|
> | rol **Lezer** | **Kijker** (Kijker · Reageerder · Bewerker) en de knop **Sturen** |
> | Verplaatsen naar | rechtsklik › **Ordenen** › **Verplaatsen** (of slepen) |
> | + Nieuw › Nieuwe map | **Nieuw** › **Map**, dan **Maken** |
> | Bestand › Versiegeschiedenis › Versiegeschiedenis bekijken | rechtsboven op **Laatste bewerking** |
> | Organiseren › Mapkleur · Toevoegen aan met ster | **Ordenen** › **Kleur van map** · **Ordenen** › **Toevoegen aan Met ster** |
>
> Bronnen: [Bestanden delen](https://support.google.com/drive/answer/2494822?hl=nl) ·
> [Bestanden ordenen](https://support.google.com/drive/answer/2375091?hl=nl) ·
> [Wijzigingen bekijken](https://support.google.com/docs/answer/190843?hl=nl).
> Dezelfde fouten staan ook in les 2 van 3MWb (De Speelboom): *Lezer* 14× op de lespagina, 3× in de
> dia's en 2× in het paspoort, *Nieuwe map* 6×, *Organiseren* 4× (nagekeken op 23-09-2026).

---

## 2. Klaarzetten in 3 stappen (± 15 minuten)

Dit pakket vraagt **minder** voorbereiding dan les 2 van 3MWb: er worden geen bestanden naar
Google-formaat omgezet en er is maar één Classroom-post.

### Stap 1 — Publiceren via GitHub Pages ✅ *al gebeurd*

Dit pakket staat al online, met Pages op branch `main`, map `/ (root)`:

- **Repository:** <https://github.com/jonasdaltongent/Onderzoeksmap-Labo>
- **Lespagina voor de leerlingen:** <https://jonasdaltongent.github.io/Onderzoeksmap-Labo/>
- **Dia's voor het bord:** <https://jonasdaltongent.github.io/Onderzoeksmap-Labo/presentatie.html>

Dat adres staat ook al op dia 7 en in `lesdoelen.json` (veld `bron`), dus daar hoef je niets
meer aan te passen. Hernoem je de repository later, pas het dan op beide plaatsen aan (zoek in
`presentatie.html` op `PAS AAN`).

Deel met de leerlingen altijd het **Pages-adres**, niet de repositorylink. Na een wijziging
duurt het 1 à 2 minuten voor de site opnieuw gepubliceerd is:

```bash
git add -A && git commit -m "beschrijf je wijziging" && git push
```

### Stap 2 — Je e-mailadres  ⚠️ **verplicht, maar niet op de website**

Voor stap 7 hebben de leerlingen jouw e-mailadres nodig. Dat staat **bewust niet op de lespagina**:
die staat openbaar op GitHub Pages, en een e-mailadres op een openbare pagina wordt vroeg of laat
opgepikt door spambots.

Geef het adres op twee plaatsen:
1. in de **instructietekst van de opdracht** in Classroom;
2. **op het bord**, tijdens de les (dia 7 herinnert je eraan).

Drive vult het adres bovendien zelf aan zodra de leerling begint te typen.

### Stap 3 — Eén opdracht in Google Classroom

**Eenmalig, en daarna nooit meer:** zet in Google Drive de instelling aan die een Word-bestand bij het
uploaden meteen omzet naar Google Documenten. Ga naar
[drive.google.com/drive/settings](https://drive.google.com/drive/settings) en vink **Uploads
converteren naar de indeling van een Editor van Google Documenten** aan
([Drive-help](https://support.google.com/drive/answer/2424368?hl=nl)). Let op: vanaf dan wordt élk
Word-, Excel- of PowerPoint-bestand dat jij uploadt een Google-bestand.

Daarna, voor deze les:

1. Maak de opdracht en klik onder **Bijvoegen** op **Uploaden**. Kies
   `werkdocument/Onderzoeksmap-paspoort.docx`.
2. Staat er geen `.docx` meer achter de naam van de bijlage? Dan is het een Google-document. Kies
   **Een kopie maken voor elke leerling**. Elke leerling krijgt een eigen kopie met de eigen naam in
   de titel ([Classroom-help](https://support.google.com/edu/classroom/answer/6020265?hl=nl)).
3. Upload op dezelfde manier `werkdocument/Les2_bestanden-om-op-te-ruimen.zip` en kies
   **Leerlingen kunnen bestand bekijken**. Een zip-bestand wordt niet omgezet; dat hoeft ook niet.
4. Voeg de lespagina toe met **Link**.

> [!IMPORTANT]
> **Test het één keer.** Dat de uploadknop *in Classroom* die Drive-instelling volgt, staat niet in
> de Google-documentatie. Heet het paspoort na stap 1 nog `…docx`? Upload het dan in Drive zelf
> (**Nieuw** › **Bestanden uploaden**: daar zet de instelling het zeker om) en voeg het in Classroom
> toe met **Drive**. Laat weten wat je zag, dan zet ik het juiste pad in de lesplanner.

> [!NOTE]
> *Een kopie maken voor elke leerling* kan je alleen kiezen **voordat** je de opdracht post.

| | Opdracht: **Les 2 — Mijn digitale onderzoeksmap** |
|---|---|
| **Bijlage 1** | de link naar de lespagina (GitHub Pages) |
| **Bijlage 2** | `Onderzoeksmap-paspoort` (Google-document) — **Een kopie maken voor elke leerling** |
| **Bijlage 3** | `Les2_bestanden-om-op-te-ruimen.zip` — **Leerlingen kunnen bestand bekijken** |
| **Punten** | Zonder cijfer (formatief) |
| **Deadline** | vrijdag 2 oktober 2026, 20.00 uur |

> [!IMPORTANT]
> Alleen het **paspoort** krijgt *Een kopie maken voor elke leerling*. Het zip-bestand **niet**:
> anders krijgt elke leerling een eigen kopie, en dat is precies het kluwen dat we wilden vermijden.
> Eén gedeelde kopie volstaat — de leerlingen downloaden hem toch.

### Afvinklijst vóór de les

- [x] Het Pages-adres werkt en staat al op dia 7. (Getest op 21-09-2026.)
- [ ] Mijn e-mailadres staat in de instructietekst van de opdracht.
- [ ] De opdracht heeft drie bijlagen, met de juiste instelling per bijlage.
- [ ] Het paspoort is een **Google-document** (geen `.docx` achter de naam), en een testleerling krijgt er een eigen kopie van met de eigen naam in de titel.
- [ ] Ik heb met een **leerlingaccount** getest of dat account het zip-bestand kan downloaden.
- [ ] De Dalton-lesfiche staat in je planner (open `dalton-lesfiche.html`, klik op **Kopieer de fiche**, plak).
- [ ] `presentatie.html` opent op de beamer; `N` toont mijn notities, `F` is volledig scherm.

### Alternatief: een gedeelde map in plaats van een zip

Wil je de vijf bestanden liever eerst in Drive laten zien? Maak dan een map, zet de vijf bestanden
uit `werkdocument/rommel/` erin en deel die map als **Kijker** met de klas. De leerlingen selecteren
alle vijf de bestanden en kiezen **Downloaden**; Drive maakt daar zelf een zip van. Dat werkt, maar
het staat niet in de Google-documentatie — met één zip-bestand is *rechtsklik → Downloaden* wél
gedocumenteerd gedrag. Kies je toch voor de map, pas dan stap 3 op de lespagina aan.

---

## 3. Het verloop van de les

| Fase | Tijd | Wat |
|---|---|---|
| **Instructie** | **10'** | Dia 1–2 lesstart (3'), dia 3–6 demo (5'): ophalen/uitpakken/uploaden en bestand 1 hernoemen, dia 7 *Zo werk je verder* (2') |
| **Keuzewerktijd** | **40'** | Dia 7 blijft staan; de leerlingen werken stap 1 tot 8 af, inleveren inbegrepen. Dia 8 in de laatste minuut. |

Keuzewerktijd = 50 minuten − instructietijd. Zeg aan het einde mondeling dat wie niet klaar is, toch inlevert.

Volledige uitwerking: `lesvoorbereiding.md` §15–17. Sprekersnotities met de hardop-denk-tekst:
druk op `N` in `presentatie.html`.

**Eerste rondgang, kijk alleen naar twee dingen.** Ze blokkeren allebei alles wat erna komt:

1. Staat de hoofdmap in **Mijn Drive** en niet in de map *Classroom*?
2. Zijn de vijf bestanden van **Downloads** naar **Drive** geraakt?

---

## 4. Verbetersleutel

De leerling levert alleen het **Onderzoeksmap-paspoort** in. De mappen bekijk je via *Gedeeld met mij*.

### Deel 2 — de vijf bestanden

| Oude naam | Verwachte nieuwe naam | Submap |
|---|---|---|
| `Document zonder titel` | `2026-09-21_onderzoeksplan_schermgebruik-slaap_v1` | `03_Verslag` (voorbeeld, al ingevuld) |
| `interview Amina 2 boos` | `2026-09-22_interview_respondent-02_v2` | `01_Ruwe-data` |
| `graphiek 2` | `2026-09-25_verwerkte-data_slaapduur_v1` | `02_Verwerkte-data` |
| `bron site jongeren slaap def` | `2026-09-20_bronfiche_slaapduur-jongeren_v1` | `04_Bronnen` |
| `IMG_20260923_194512` | `2026-09-23_whiteboard_variabelen_v1` | `05_Beeldmateriaal` |

Kleine verschillen in het middenstuk zijn **goed**. Wat moet kloppen: de datumvorm `JJJJ-MM-DD`,
het versienummer (`v2` bij het interview, `v1` bij de rest), geen spaties, en geen voornaam.

### Korte antwoorden bij de vragen

| Vraag | Waar het om gaat |
|---|---|
| 1 | In **Downloads**, op de computer zelf. Dat is **lokale** opslag, nog niet de cloud. |
| 2 | Twee van: alleen op die ene computer · thuis kan je er niet aan · groepsgenoten en leraar kunnen er niet aan · geen back-up · bij een defect ben je de ruwe data kwijt. |
| 3 | In **Google Drive**: daar kan je aan op elk toestel waarop je aanmeldt, ook thuis. |
| 4 | Jaar-maand-dag zet alles vanzelf op chronologische volgorde; `21-09-2026` sorteert op dag. |
| 5 | De voornaam is een **persoonsgegeven** en staat in elke lijst, elke gedeelde map en elke schermafbeelding. Met `respondent-02` blijft het bruikbaar zonder herkenbaar te zijn (**pseudonimiseren**). |
| 6 | De buur kon niets veranderen: als Kijker kan je alleen kijken. |
| 7 | Als Bewerker kon de buur wel typen (en zou die ook kunnen hernoemen of verwijderen). |
| 8 | Ikzelf: eigenaar · groepsgenoten: bewerker of kijker, met argument · leraar: kijker · andere klas: geen toegang · respondenten: geen toegang (ze mogen wel weten wat er met hun gegevens gebeurt). |
| 9 | De regel van de buur, gevonden via **Laatste bewerking** rechtsboven in het document, met naam en tijdstip. |

### Essentiële fouten — geef hier altijd feedback op

- De voornaam van de respondent staat nog in de bestandsnaam.
- Gedeeld als **Bewerker** of via "iedereen met de link" in plaats van als Kijker.
- De hoofdmap staat in de map *Classroom* in plaats van in *Mijn Drive*.
- Datum als `22-9-26`.
- Ruwe en verwerkte data in dezelfde submap.
- De bestanden staan nog steeds alleen in Downloads.

---

## 5. Screenshots (optioneel)

`index.html` verwacht zes schermafbeeldingen in `assets/screenshots/`. Ze zijn **niet verplicht**:
ontbreekt er een, dan laat de pagina die plaats gewoon weg. Leerlingen zien geen lege kaders.

Open `index.html?leraar` om te zien waar ze komen: je krijgt dan een roze kader met de verwachte
bestandsnaam. De volledige lijst en de afspraken staan in `assets/screenshots/LEESMIJ.md`.

> Zolang je er geen plaatst, verschijnen er zes 404-meldingen in de console van de browser. Dat is
> normaal en zichtbaar voor niemand behalve wie de ontwikkelaarsconsole opent.

---

## 6. Het materiaal opnieuw genereren

```bash
python3 "werkdocument/maak_werkdocumenten.py"
```

Dat maakt het paspoort, de vijf rommelbestanden **en** de zip opnieuw aan. Vereist `python-docx`,
`openpyxl` en `Pillow`. Wil je iets wijzigen, lees dan eerst de waarschuwing bovenaan het script:
de slechte bestandsnamen en de datumvorm `DD-MM-JJJJ` zijn lesmateriaal, geen slordigheid.

---

## 7. Leerplandoelen in je jaaroverzicht

```bash
python3 "../../_tools/update_leerdoelen.py" lesdoelen.json
```

> [!NOTE]
> In `Leerplandoelen 2026-2027.xlsx` staat het blad **3 Maatsch. en welzijnswet.** wel klaar, maar
> het is nog leeg ("Leerplan nog niet beschikbaar op deze computer"). Het script schrijft de
> regels dus wel weg op het blad *Registratie*, maar meldt bij elk doel dat er geen rij voor is en
> dat het niet geteld wordt. Vul dat blad eerst aan met de doelen uit
> `Leerplannen_2de_graad_TOINFO_MWW_doorstroom.md` — dat leerplan staat nu wél op deze computer.
>
> De klasgroepcode in `lesdoelen.json` moet daarom `3 MWW` blijven (met spatie): daarmee vindt het
> script het juiste blad. De echte klasnaam `3MWWE` staat in het veld `klasnaam`.

---

## 8. Wat nog moet blijken in de klas

Drie dingen die ik niet vooraf kon testen. Noteer na de les wat er gebeurde:

1. **Haalbaarheid van stap 2 en 3 samen** (mappen bouwen + ophalen, samen 15 minuten). Als dat te
   krap is: laat stap 2 tot vier jaarmappen beperken en de vijf submappen pas later
   maken.
2. **De duotest in stap 7** bij een oneven aantal leerlingen. De hint geeft twee terugvalopties.
3. **Windows en het klembord:** als het lokaal op Windows draait, komt het knipsel uit
   Knipprogramma op het klembord. Plakken met `Ctrl + V` in het Google-document zou moeten werken;
   lukt dat niet, dan moet de leerling het knipsel eerst bewaren en daarna invoegen. Dat staat als
   terugvaloptie in de hint bij stap 6.
