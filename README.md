# Handleiding voor de leraar — Les 2: Mijn digitale onderzoeksmap

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWWE — 2de graad Maatschappij- en welzijnswetenschappen, doorstroomfinaliteit
**Lesduur:** 1 × 50 minuten (formatief)
**Context:** Onderzoekslabo Jongeren & Welzijn, een fictieve schooleigen onderzoeksgroep
**Toestellen:** Chromebook **of** Windows-pc, in beide gevallen met Google Workspace —
de lespagina heeft een **toestelwissel**
**Kernleerplandoel:** `BV2_04.03` — digitale inhouden beheren (toepassen)

---

## 1. Inhoud van het pakket

```text
W04 - Les 02 - MWW - Mijn digitale onderzoeksmap/
├── index.html                   # de leerlingentool (8 stappen + extra + theoriekaart)
├── presentatie.html             # 8 klassikale dia's voor de fase "Ik doe"
├── css/
│   ├── style.css                # leerlingentool (Dalton-kleuren, voor een half scherm)
│   └── slides.css               # dia's (16:9, beamer)
├── js/
│   ├── script.js                # stappen, vinkjes, toestelwissel, theoriekaart, woordenlijst, zelftest
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
├── dalton-lesfiche.md           # lesfiche in het Dalton-formaat (lestijd + KWT)
├── lesdoelen.json               # codes van de leerplandoelen voor je jaaroverzicht
└── README.md                    # deze handleiding
```

De website heeft geen server, database, login of tracking nodig. Er worden geen externe bestanden
geladen. `localStorage` bewaart alleen de vinkjes en de toestelkeuze (voorvoegsel
`onderzoekslabo_map_`), met een wisknop.

---

## 2. Klaarzetten in 3 stappen (± 15 minuten)

Dit pakket vraagt **minder** voorbereiding dan les 2 van 3MWb: er worden geen bestanden naar
Google-formaat omgezet en er is maar één Classroom-post.

### Stap 1 — Publiceren via GitHub Pages

1. Zet deze map in een GitHub-repository, bijvoorbeeld `Onderzoeksmap-Labo`.
2. Repository → **Settings** → **Pages** → branch `main`, map `/ (root)` → **Save**.
3. Wacht 1 à 2 minuten en test het adres.
4. ⚠️ **Pas het adres aan op dia 7** van `presentatie.html` (zoek op `PAS AAN`) en in
   `lesdoelen.json` (veld `bron`), als je de repository anders noemt.

Deel met de leerlingen altijd het **Pages-adres**, niet de repositorylink.

### Stap 2 — Je e-mailadres  ⚠️ **verplicht, maar niet op de website**

Voor stap 7 hebben de leerlingen jouw e-mailadres nodig. Dat staat **bewust niet op de lespagina**:
die staat openbaar op GitHub Pages, en een e-mailadres op een openbare pagina wordt vroeg of laat
opgepikt door spambots.

Geef het adres op twee plaatsen:
1. in de **instructietekst van de opdracht** in Classroom;
2. **op het bord**, tijdens de les (dia 7 herinnert je eraan).

Drive vult het adres bovendien zelf aan zodra de leerling begint te typen.

### Stap 3 — Eén opdracht in Google Classroom

Upload eerst deze twee bestanden naar Drive. **Converteer niets naar Google-formaat**: Drive opent
een `.docx` of `.xlsx` rechtstreeks in Documenten of Spreadsheets, en het bestand blijft in
Office-indeling.

- `werkdocument/Onderzoeksmap-paspoort.docx`
- `werkdocument/Les2_bestanden-om-op-te-ruimen.zip`

Maak dan **één** opdracht, onderwerp *Digitaal organiseren en communiceren*:

| | Opdracht: **Les 2 — Mijn digitale onderzoeksmap** |
|---|---|
| **Bijlage 1** | de link naar de lespagina (GitHub Pages) |
| **Bijlage 2** | `Onderzoeksmap-paspoort` — **Een kopie maken voor elke leerling** |
| **Bijlage 3** | `Les2_bestanden-om-op-te-ruimen.zip` — **Leerlingen kunnen bestand bekijken** |
| **Punten** | Zonder cijfer (formatief) |
| **Deadline** | vrijdag 25 september 2026, 20.00 uur |

> [!IMPORTANT]
> Alleen het **paspoort** krijgt *Een kopie maken voor elke leerling*. Het zip-bestand **niet**:
> anders krijgt elke leerling een eigen kopie die bij het inleveren van eigenaar verandert, en dat
> is precies het kluwen dat we wilden vermijden. Eén gedeelde kopie volstaat — ze downloaden hem
> toch naar hun eigen toestel.

### Afvinklijst vóór de les

- [ ] Het Pages-adres werkt en ik heb het adres op dia 7 aangepast.
- [ ] Mijn e-mailadres staat in de instructietekst van de opdracht.
- [ ] De opdracht heeft drie bijlagen, met de juiste instelling per bijlage.
- [ ] Ik heb met een **leerlingaccount** getest of dat account het zip-bestand kan downloaden.
- [ ] Ik weet op welk toestel de klas werkt en laat ze in de instructie op die knop klikken.
- [ ] `presentatie.html` opent op de beamer; `N` toont mijn notities, `F` is volledig scherm.

### Alternatief: een gedeelde map in plaats van een zip

Wil je de vijf bestanden liever eerst in Drive laten zien? Maak dan een map, zet de vijf bestanden
uit `werkdocument/rommel/` erin en deel die map als **Lezer** met de klas. De leerlingen selecteren
alle vijf de bestanden en kiezen **Downloaden**; Drive maakt daar zelf een zip van. Dat werkt, maar
het staat niet in de Google-documentatie — met één zip-bestand is *rechtsklik → Downloaden* wél
gedocumenteerd gedrag. Kies je toch voor de map, pas dan stap 3 op de lespagina aan.

---

## 3. Het verloop van de les

| Fase | Tijd | Wat |
|---|---|---|
| Lesstart | 3' | Dia 1–2: retrieval van les 1, dan kolom A versus B |
| **Ik doe** | **5'** | Dia 3–6: lesdoel, eindproduct, en twee dingen voordoen — ophalen/uitpakken/uploaden, en bestand 1 hernoemen |
| Jullie doen | 34' | Dia 7 blijft staan; de leerlingen werken stap 1 tot 8 af |
| Controle en indiening | 6' | Stap 8: zelftest, controlelijst, slotvragen, Inleveren |
| Afsluiting | 2' | Dia 8: exitvraag en vooruitblik op les 3 |

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
| 1 | In **Downloads**, op het toestel zelf. Dat is **lokale** opslag, nog niet de cloud. |
| 2 | Twee van: alleen op dat toestel · het toestel maakt Downloads zelf leeg · niemand anders kan eraan · geen back-up · bij een defect ben je de ruwe data kwijt. |
| 3 | Het toestel verwijdert bestanden uit Downloads om plaats te winnen. |
| 4 | Jaar-maand-dag zet alles vanzelf op chronologische volgorde; `21-09-2026` sorteert op dag. |
| 5 | De voornaam is een **persoonsgegeven** en staat in elke lijst, elke gedeelde map en elke schermafbeelding. Met `respondent-02` blijft het bruikbaar zonder herkenbaar te zijn (**pseudonimiseren**). |
| 6 | De buur kon niet typen: er verscheen een melding dat het bestand alleen-lezen is. |
| 7 | Als Bewerker kon de buur wel typen (en zou die ook kunnen hernoemen of verwijderen). |
| 8 | Ikzelf: eigenaar · groepsgenoten: bewerker of lezer, met argument · leraar: lezer · andere klas: geen toegang · respondenten: geen toegang (ze mogen wel weten wat er met hun gegevens gebeurt). |
| 9 | De regel van de buur, gevonden via **Bestand › Versiegeschiedenis › Versiegeschiedenis bekijken**, met naam en tijdstip. |

### Essentiële fouten — geef hier altijd feedback op

- De voornaam van de respondent staat nog in de bestandsnaam.
- Gedeeld als **Bewerker** of via "iedereen met de link" in plaats van als Lezer.
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
   krap is: laat stap 2 tot vier jaarmappen beperken en de vijf submappen pas in de keuzewerktijd
   maken.
2. **De duotest in stap 7** bij een oneven aantal leerlingen. De hint geeft twee terugvalopties.
3. **Windows en het klembord:** als het lokaal op Windows draait, komt het knipsel uit
   Knipprogramma op het klembord. Plakken met `Ctrl + V` in het Google-document zou moeten werken;
   lukt dat niet, dan moet de leerling het knipsel eerst bewaren en daarna invoegen. Dat staat als
   terugvaloptie in de hint bij stap 6.
