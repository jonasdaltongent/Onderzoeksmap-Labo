#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert de bestanden voor les 2 "Mijn digitale onderzoeksmap"
(Onderzoekslabo Jongeren & Welzijn, klas 3MWWE).

  Onderzoeksmap-paspoort.docx            het werkdocument dat de leerling INLEVERT
  rommel/Document zonder titel.docx      rommelbestand 1 (samen hernoemd tijdens de demo)
  rommel/interview Amina 2 boos.docx     rommelbestand 2
  rommel/graphiek 2.xlsx                 rommelbestand 3
  rommel/bron site jongeren slaap def.docx  rommelbestand 4
  rommel/IMG_20260923_194512.png         rommelbestand 5
  Les2_bestanden-om-op-te-ruimen.zip     de vijf rommelbestanden samen — DIT hangt aan de opdracht

Gebruik:  python3 maak_werkdocumenten.py
Vereist:  python-docx, openpyxl, Pillow

LET OP bij aanpassen:
 - De slechte bestandsnamen zijn OPZETTELIJK. Ze zijn het lesmateriaal.
 - In elk rommelbestand staat een datum in de vorm DD-MM-JJJJ. De leerling moet die
   omzetten naar JJJJ-MM-DD. Wijzig die vorm dus niet.
 - De voornaam "Amina" staat bewust in de bestandsnaam EN in het transcript. De leerling
   haalt ze vandaag alleen uit de BESTANDSNAAM (respondent-02). Inhoudelijk anonimiseren
   komt in les 16.
 - De bestanden blijven .docx / .xlsx / .png. Ze worden NIET naar Google-formaat omgezet:
   Drive opent een Office-bestand rechtstreeks in Documenten of Spreadsheets.
 - Alle namen, cijfers en bronnen zijn fictief.
"""
import os
import zipfile

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from openpyxl import Workbook
from openpyxl.styles import Font as XFont, PatternFill, Alignment as XAlign

NAVY = RGBColor(0x2A, 0x39, 0x73)
GREY = RGBColor(0x4D, 0x55, 0x73)
HERE = os.path.dirname(os.path.abspath(__file__))
ROMMEL = os.path.join(HERE, "rommel")

# De vijf rommelbestanden, in de volgorde waarin ze in het paspoort staan.
ROMMELBESTANDEN = [
    "Document zonder titel.docx",
    "interview Amina 2 boos.docx",
    "graphiek 2.xlsx",
    "bron site jongeren slaap def.docx",
    "IMG_20260923_194512.png",
]


# ---------- hulpfuncties ----------
def basis_document(marge=2.0):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Arial"
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(marge)
        s.left_margin = s.right_margin = Cm(marge)
    return doc


def kop(doc, tekst_, grootte=16, ruimte_voor=14):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(ruimte_voor)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(tekst_)
    r.bold = True
    r.font.size = Pt(grootte)
    r.font.color.rgb = NAVY
    return p


def tekst(doc, s, cursief=False, klein=False, vet=False, na=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(na)
    r = p.add_run(s)
    r.italic = cursief
    r.bold = vet
    if klein:
        r.font.size = Pt(9.5)
        r.font.color.rgb = GREY
    return p


def schaduw(cel, kleur="E4E8F6"):
    tcPr = cel._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), kleur)
    tcPr.append(shd)


def antwoordlijnen(doc, aantal=2):
    for _ in range(aantal):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.add_run("_" * 86)


def kleine_cellen(tabel, punten=10):
    for rij in tabel.rows:
        for c in rij.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(punten)


# ---------- 1. Onderzoeksmap-paspoort (het werkdocument) ----------
def paspoort():
    doc = basis_document()

    p = doc.add_paragraph()
    r = p.add_run("ONDERZOEKSMAP-PASPOORT")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = NAVY
    tekst(doc, "Les 2 — Mijn digitale onderzoeksmap  ·  Toegepaste Informatica  ·  "
               "Onderzoekslabo Jongeren & Welzijn", klein=True, na=10)

    t = doc.add_table(rows=1, cols=3)
    t.style = "Table Grid"
    for i, label in enumerate(["Naam:", "Klas:", "Datum:"]):
        c = t.rows[0].cells[i]
        c.text = label + " "
        c.paragraphs[0].runs[0].bold = True
    doc.add_paragraph()

    kop(doc, "Zo werk je", 13, ruimte_voor=6)
    for s in [
        "1.  Links op je scherm staat de lespagina. Daar lees je wat je moet doen.",
        "2.  In Google Drive bouw je je onderzoeksmap. Dat is je echte werk.",
        "3.  In dit document schrijf je op wat je gedaan hebt en waarom.",
        "4.  Alleen DIT document lever je in via Google Classroom.",
    ]:
        pp = doc.add_paragraph(s)
        pp.paragraph_format.space_after = Pt(2)

    # ---- Deel 1 ----
    kop(doc, "Deel 1 — Waar staan mijn bestanden?")
    tekst(doc, "Vraag 1. Je hebt het zip-bestand gedownload en uitgepakt. In welke map staan de vijf "
               "bestanden op dat moment, en is dat lokale opslag of cloudopslag?", vet=True)
    antwoordlijnen(doc, 2)
    tekst(doc, "Vraag 2. Je laat de ruwe data van je onderzoek alleen in de map Downloads van de "
               "computer in het lokaal staan. Geef twee redenen waarom dat een slecht idee is.", vet=True)
    antwoordlijnen(doc, 3)
    tekst(doc, "Vraag 3. Wat gebeurt er met de map Downloads als de schijf van het toestel vol raakt?", vet=True)
    antwoordlijnen(doc, 1)

    # ---- Deel 2 ----
    kop(doc, "Deel 2 — Mijn vijf bestanden")
    tekst(doc, "Vul de tabel in terwijl je werkt. Het eerste bestand deed je samen met je leraar.", klein=True)

    t = doc.add_table(rows=6, cols=4)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(["Oude naam", "Mijn nieuwe naam", "In welke submap?", "Waarom die submap?"]):
        c = t.rows[0].cells[i]
        c.text = h
        c.paragraphs[0].runs[0].bold = True
        schaduw(c)
    rijen = [
        ("Document zonder titel",
         "2026-09-21_onderzoeksplan_schermgebruik-slaap_v1",
         "03_Verslag",
         "Het is tekst die we zelf schrijven, geen data."),
        ("interview Amina 2 boos", "", "", ""),
        ("graphiek 2", "", "", ""),
        ("bron site jongeren slaap def", "", "", ""),
        ("IMG_20260923_194512", "", "", ""),
    ]
    for i, rij in enumerate(rijen, start=1):
        for j, waarde in enumerate(rij):
            t.rows[i].cells[j].text = waarde
    kleine_cellen(t, 9.5)
    doc.add_paragraph()

    tekst(doc, "Vraag 4. Waarom zetten we de datum vóóraan in de bestandsnaam, en waarom in de vorm "
               "2026-09-21 en niet 21-09-2026?", vet=True)
    antwoordlijnen(doc, 2)
    tekst(doc, "Vraag 5. In de bestandsnaam van het interview schrijf je respondent-02 in plaats van de "
               "voornaam. Waarom?", vet=True)
    antwoordlijnen(doc, 2)

    # ---- Deel 3 ----
    kop(doc, "Deel 3 — Een foto van mijn onderzoeksmap")
    tekst(doc, "Voeg hieronder je schermafbeelding in: Invoegen › Afbeelding › Uploaden vanaf computer.",
          klein=True)
    tekst(doc, "Op je schermafbeelding moet je de naam van je hoofdmap, je vier jaarmappen én de vijf "
               "submappen van 04_Onderzoek kunnen lezen.", klein=True)
    kader = doc.add_table(rows=1, cols=1)
    kader.style = "Table Grid"
    kader.rows[0].height = Cm(7)
    cel = kader.rows[0].cells[0]
    cel.text = "(voeg hier je schermafbeelding in)"
    cel.paragraphs[0].runs[0].font.size = Pt(9.5)
    cel.paragraphs[0].runs[0].font.color.rgb = GREY
    doc.add_paragraph()

    # ---- Deel 4 ----
    kop(doc, "Deel 4 — Wie mag wat met mijn onderzoeksgegevens?")
    tekst(doc, "Vraag 6. Je deelde je projectmap met je buur als Lezer. Wat probeerde je buur, en wat "
               "lukte niet?", vet=True)
    antwoordlijnen(doc, 2)
    tekst(doc, "Vraag 7. Daarna maakte je je buur Bewerker. Wat kon je buur toen wél?", vet=True)
    antwoordlijnen(doc, 2)
    tekst(doc, "Vraag 8. Vul in wie welk recht krijgt op de ruwe data van jouw onderzoek, en waarom.", vet=True)

    t = doc.add_table(rows=6, cols=3)
    t.style = "Table Grid"
    for i, h in enumerate(["Wie?", "Welk recht?", "Waarom?"]):
        c = t.rows[0].cells[i]
        c.text = h
        c.paragraphs[0].runs[0].bold = True
        schaduw(c)
    for i, wie in enumerate(["ikzelf", "mijn groepsgenoten", "mijn leraar",
                             "een andere klas van de school", "de respondenten"], start=1):
        t.rows[i].cells[0].text = wie
    kleine_cellen(t, 10)
    tekst(doc, "Kies telkens uit: eigenaar · bewerker · reageren · lezer · geen toegang.", klein=True)

    # ---- Deel 5 ----
    kop(doc, "Deel 5 — Versiegeschiedenis")
    tekst(doc, "Vraag 9. Je buur typte één regel in je bestand. Welke regel was dat, en waar klikte je "
               "om te zien wie die had toegevoegd?", vet=True)
    antwoordlijnen(doc, 3)

    # ---- Deel 6 ----
    kop(doc, "Deel 6 — Tot slot")
    tekst(doc, "Vraag 10. Noem één ding dat jij vanaf nu anders gaat doen met je bestanden.", vet=True)
    antwoordlijnen(doc, 1)
    tekst(doc, "Vraag 11. Welke stap van vandaag was voor jou het moeilijkst? Waarom?", vet=True)
    antwoordlijnen(doc, 2)

    # ---- Zelfcontrole ----
    kop(doc, "Zelfcontrole — aankruisen vóór je indient")
    for s in [
        "Mijn hoofdmap staat in Mijn Drive en heeft mijn naam.",
        "Ik heb 4 jaarmappen (01 tot 04) en in 04_Onderzoek nog 5 submappen (01 tot 05).",
        "Mijn vijf bestanden staan in Google Drive en niet meer alleen in Downloads.",
        "Mijn vijf bestanden hebben een nieuwe naam volgens de naamafspraak.",
        "In geen enkele bestandsnaam staat de voornaam van een respondent.",
        "Ruwe data en verwerkte data staan in verschillende submappen.",
        "Mijn schermafbeelding staat in deel 3 en is leesbaar.",
        "Mijn hoofdmap is gedeeld met mijn leraar als Lezer, en ik ben nog eigenaar.",
        "Mijn buur staat weer op Lezer of is verwijderd.",
        "Alle elf vragen zijn ingevuld.",
    ]:
        pp = doc.add_paragraph("☐  " + s)
        pp.paragraph_format.space_after = Pt(2)

    # ---- Extra ----
    kop(doc, "Optionele uitbreiding")
    tekst(doc, "Alleen als al de rest af en ingeleverd is.", klein=True)
    tekst(doc, "a) Welke vijfde jaarmap heb jij dit schooljaar nog nodig, en waarom?", vet=True)
    antwoordlijnen(doc, 2)
    tekst(doc, "b) Wanneer mag je de ruwe data van je onderzoek verwijderen, en waarom niet vroeger?", vet=True)
    antwoordlijnen(doc, 2)

    doc.save(os.path.join(HERE, "Onderzoeksmap-paspoort.docx"))


# ---------- 2. De rommelbestanden ----------
def rommel_onderzoeksplan():
    """Slechte naam: 'Document zonder titel'. Hoort in 03_Verslag."""
    doc = basis_document(marge=2.5)
    tekst(doc, "Datum: 21-09-2026", vet=True)
    tekst(doc, "Onderzoekslabo Jongeren & Welzijn — onderzoeksgroep 3")
    doc.add_paragraph()
    tekst(doc, "Schermgebruik en slaap bij leerlingen van de tweede graad", vet=True)
    tekst(doc, "Onderzoeksvraag: Hangt de tijd die leerlingen van de tweede graad in het laatste uur "
               "voor het slapengaan aan een scherm zitten samen met hoelang ze die nacht slapen?")
    tekst(doc, "Hypothese: hoe meer schermtijd in het laatste uur voor bedtijd, hoe korter de slaapduur.")
    tekst(doc, "Aanpak:")
    for s in ["1. Vragenlijst met zeven vragen, één week lang elke ochtend in te vullen.",
              "2. Twee interviews van tien minuten, om de cijfers te kunnen uitleggen.",
              "3. Verwerking in een rekenblad: gemiddelde, mediaan en spreiding.",
              "4. Rapportering op een poster met twee grafieken."]:
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(2)
    tekst(doc, "Afspraken over de gegevens: deelnemen is vrijwillig, elke deelnemer krijgt een "
               "respondentcode, en de lijst met codes bewaren we apart. In het verslag komt geen "
               "enkele naam.")
    doc.save(os.path.join(ROMMEL, "Document zonder titel.docx"))


def rommel_interview():
    """Slechte naam: voornaam + 'boos' + versienummer los. Hoort in 01_Ruwe-data."""
    doc = basis_document(marge=2.5)
    tekst(doc, "Datum: 22-09-2026", vet=True)
    tekst(doc, "Interview 2 — respondentcode 02 — tweede versie van het transcript")
    tekst(doc, "Duur: 9 minuten  ·  Toestemming gegeven: ja  ·  Opname verwijderd na uittypen: ja")
    doc.add_paragraph()
    tekst(doc, "Transcript", vet=True)
    regels = [
        "ONDERZOEKER: Hoelang zit je gemiddeld op je gsm voor je gaat slapen?",
        "AMINA: Soms een half uur, soms veel langer. Als ik begin te scrollen ben ik het uur kwijt.",
        "ONDERZOEKER: En hoe voel je je dan de dag nadien?",
        "AMINA: Traag. Vooral het eerste lesuur. Dan ben ik ook sneller boos op mijn broer, echt om niets.",
        "ONDERZOEKER: Heb je al eens iets geprobeerd om vroeger te stoppen?",
        "AMINA: Ja, mijn gsm in de keuken leggen. Dat werkte, maar ik vergeet het meestal.",
        "ONDERZOEKER: Wat zou volgens jou het meeste helpen?",
        "AMINA: Dat we er in de klas over praten. Nu denkt iedereen dat alleen hij dat heeft.",
    ]
    for s in regels:
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(4)
    tekst(doc, "Notitie van de onderzoeker: dit is versie 2. In versie 1 stonden twee vragen dubbel.",
          klein=True)
    doc.save(os.path.join(ROMMEL, "interview Amina 2 boos.docx"))


def rommel_verwerkte_data():
    """Slechte naam: 'graphiek 2' (met typefout). Hoort in 02_Verwerkte-data."""
    wb = Workbook()
    ws = wb.active
    ws.title = "verwerkt"

    ws["A1"] = "Datum: 25-09-2026"
    ws["A1"].font = XFont(bold=True)
    ws["A2"] = "Onderzoekslabo Jongeren & Welzijn — verwerkte gegevens, week 1"
    ws["A3"] = "Let op: dit zijn de OPGESCHOONDE cijfers. De ruwe antwoorden staan in een ander bestand."

    kop_rij = 5
    kolommen = ["respondentcode", "schermtijd laatste uur (min)", "slaapduur (uren)", "leeftijd"]
    for i, k in enumerate(kolommen, start=1):
        c = ws.cell(row=kop_rij, column=i, value=k)
        c.font = XFont(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="3C51A0")
        c.alignment = XAlign(wrap_text=True, vertical="center")

    data = [
        ("respondent-01", 55, 6.5, 15),
        ("respondent-02", 60, 6.0, 15),
        ("respondent-03", 15, 8.0, 14),
        ("respondent-04", 40, 7.0, 15),
        ("respondent-05", 50, 6.5, 16),
        ("respondent-06", 10, 8.5, 14),
        ("respondent-07", 35, 7.5, 15),
        ("respondent-08", 45, 7.0, 16),
        ("respondent-09", 25, 7.5, 15),
        ("respondent-10", 55, 6.0, 16),
        ("respondent-11", 20, 8.0, 14),
        ("respondent-12", 30, 7.5, 15),
    ]
    for r, rij in enumerate(data, start=kop_rij + 1):
        for k, waarde in enumerate(rij, start=1):
            ws.cell(row=r, column=k, value=waarde)

    laatste = kop_rij + len(data)
    sam = laatste + 2
    ws.cell(row=sam, column=1, value="gemiddelde").font = XFont(bold=True)
    ws.cell(row=sam, column=2, value="=AVERAGE(B{}:B{})".format(kop_rij + 1, laatste))
    ws.cell(row=sam, column=3, value="=AVERAGE(C{}:C{})".format(kop_rij + 1, laatste))
    ws.cell(row=sam + 1, column=1, value="mediaan").font = XFont(bold=True)
    ws.cell(row=sam + 1, column=2, value="=MEDIAN(B{}:B{})".format(kop_rij + 1, laatste))
    ws.cell(row=sam + 1, column=3, value="=MEDIAN(C{}:C{})".format(kop_rij + 1, laatste))
    ws.cell(row=sam + 2, column=1, value="kortste / langste slaap").font = XFont(bold=True)
    ws.cell(row=sam + 2, column=2, value="=MIN(C{}:C{})".format(kop_rij + 1, laatste))
    ws.cell(row=sam + 2, column=3, value="=MAX(C{}:C{})".format(kop_rij + 1, laatste))

    for kolom, breedte in zip("ABCD", (18, 16, 14, 10)):
        ws.column_dimensions[kolom].width = breedte

    wb.save(os.path.join(ROMMEL, "graphiek 2.xlsx"))


def rommel_bronfiche():
    """Slechte naam: 'bron site jongeren slaap def'. Hoort in 04_Bronnen."""
    doc = basis_document(marge=2.5)
    tekst(doc, "Datum: 20-09-2026", vet=True)
    tekst(doc, "Bronfiche 1")
    doc.add_paragraph()
    tekst(doc, "Gegevens van de bron", vet=True)
    for s in [
        "Titel: Slaap en schermgebruik bij 14- tot 16-jarigen",
        "Soort bron: informatiepagina van een gezondheidsorganisatie (fictief voorbeeld voor de les)",
        "Auteur: dienst gezondheidsbevordering",
        "Jaar: 2025",
        "Bekeken op: 20-09-2026",
    ]:
        p = doc.add_paragraph(s)
        p.paragraph_format.space_after = Pt(2)
    doc.add_paragraph()
    tekst(doc, "Wat staat erin dat ik kan gebruiken?", vet=True)
    tekst(doc, "De pagina beschrijft dat jongeren van 14 tot 16 jaar gemiddeld acht tot tien uur slaap "
               "nodig hebben, en dat licht van een scherm het inslapen kan uitstellen. Er staat ook bij "
               "dat de sterkte van dat verband per persoon verschilt.")
    tekst(doc, "Hoe betrouwbaar is de bron?", vet=True)
    tekst(doc, "De organisatie vermeldt haar bronnen en er staat geen reclame op de pagina. De cijfers "
               "gaan wel over een andere leeftijdsgroep dan onze eigen steekproef. Dat vermelden we in "
               "het verslag.")
    tekst(doc, "Alle gegevens in dit bestand zijn verzonnen voor de les.", klein=True)
    doc.save(os.path.join(ROMMEL, "bron site jongeren slaap def.docx"))


def rommel_whiteboardfoto():
    """Slechte naam: de naam die de camera zelf gaf. Hoort in 05_Beeldmateriaal."""
    from PIL import Image, ImageDraw, ImageFont

    B, H = 1200, 800
    img = Image.new("RGB", (B, H), (238, 240, 236))
    d = ImageDraw.Draw(img)

    def lettertype(grootte):
        for pad in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                    "/System/Library/Fonts/Supplemental/Arial.ttf",
                    "/Library/Fonts/Arial.ttf",
                    "/System/Library/Fonts/Helvetica.ttc",
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
            if os.path.exists(pad):
                try:
                    return ImageFont.truetype(pad, grootte)
                except Exception:
                    pass
        return ImageFont.load_default(size=grootte)

    groot, mid, klein = lettertype(54), lettertype(40), lettertype(30)
    blauw, grijs, groen, rood = (42, 57, 115), (77, 85, 115), (31, 122, 85), (160, 55, 42)

    # rand van het whiteboard
    d.rounded_rectangle([20, 20, B - 20, H - 20], radius=18, outline=(190, 190, 185), width=6)
    d.rectangle([40, 40, B - 40, H - 40], fill=(252, 252, 250))

    d.text((80, 70), "ONDERZOEKSLABO  -  groep 3", font=mid, fill=blauw)
    d.text((80, 125), "Welke variabelen meten we?", font=groot, fill=blauw)
    d.line([80, 195, B - 120, 195], fill=(200, 200, 195), width=4)

    d.text((90, 235), "onafhankelijk:", font=klein, fill=grijs)
    d.text((330, 228), "schermtijd laatste uur  (minuten)", font=mid, fill=rood)

    d.text((90, 320), "afhankelijk:", font=klein, fill=grijs)
    d.text((330, 313), "slaapduur die nacht  (uren)", font=mid, fill=groen)

    d.text((90, 405), "controle:", font=klein, fill=grijs)
    d.text((330, 398), "leeftijd  +  dag van de week", font=mid, fill=blauw)

    # pijl van oorzaak naar gevolg
    d.line([360, 500, 700, 500], fill=blauw, width=6)
    d.polygon([(700, 485), (740, 500), (700, 515)], fill=blauw)
    d.text((90, 480), "verwachting:", font=klein, fill=grijs)
    d.text((360, 455), "meer scherm", font=klein, fill=rood)
    d.text((755, 455), "minder slaap", font=klein, fill=groen)

    d.text((90, 590), "meten: 1 week, elke ochtend invullen", font=klein, fill=grijs)
    d.text((90, 640), "iedereen krijgt een respondentcode - geen namen in de tabel", font=klein, fill=grijs)

    d.text((90, 710), "23-09-2026", font=mid, fill=grijs)
    d.text((B - 430, 710), "foto van het bord", font=klein, fill=(150, 150, 145))

    img.save(os.path.join(ROMMEL, "IMG_20260923_194512.png"), "PNG")


# ---------- 3. De zip voor Google Classroom ----------
def maak_zip():
    pad = os.path.join(HERE, "Les2_bestanden-om-op-te-ruimen.zip")
    # zonder mapniveau: de leerling pakt uit en heeft meteen vijf losse bestanden
    with zipfile.ZipFile(pad, "w", zipfile.ZIP_DEFLATED) as z:
        for naam in ROMMELBESTANDEN:
            z.write(os.path.join(ROMMEL, naam), arcname=naam)
    return pad


if __name__ == "__main__":
    os.makedirs(ROMMEL, exist_ok=True)
    paspoort()
    rommel_onderzoeksplan()
    rommel_interview()
    rommel_verwerkte_data()
    rommel_bronfiche()
    rommel_whiteboardfoto()
    zip_pad = maak_zip()
    print("Klaar.")
    print("  werkdocument om in te leveren : Onderzoeksmap-paspoort.docx")
    print("  aan de opdracht te hangen     : " + os.path.basename(zip_pad))
    print("  losse bronbestanden           : rommel/ ({} bestanden)".format(len(ROMMELBESTANDEN)))
