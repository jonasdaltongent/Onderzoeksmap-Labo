/**
 * Mijn digitale onderzoeksmap (Onderzoekslabo Jongeren & Welzijn) — script.js
 * Werkt op index.html (instellingen via data-attributen op <body>).
 * - één stap tegelijk tonen + vorige/volgende
 * - vinkjes en huidige stap bewaren in localStorage (enkel vinkjes, geen persoonsgegevens)
 * - voortgangsbalk + afsluitmelding
 * - theoriekaart openen/sluiten
 * - TOESTELWISSEL: Chromebook of Windows; zonder keuze blijven beide varianten zichtbaar
 * - woordenlijst (klik op een onderstreept woord)
 * - mini-test met directe feedback (wordt niet bewaard)
 * - screenshot-plaatsen: tonen de afbeelding alleen als het bestand bestaat
 * Basis overgenomen uit les 2 van 3MWb (De Speelboom); nieuw zijn de toestelwissel
 * en de woordenlijst.
 * Geen externe bibliotheken.
 */
(function () {
  'use strict';

  var body = document.body;
  var PREFIX = body.getAttribute('data-storage') || 'onderzoekslabo_map_';
  var params = new URLSearchParams(window.location.search);
  var teacherMode = params.has('leraar');
  if (teacherMode) body.classList.add('teacher');

  /* ---------- Opslag (veilig: werkt ook als localStorage geblokkeerd is) ---------- */
  function store(key, value) {
    try { localStorage.setItem(PREFIX + key, JSON.stringify(value)); } catch (e) { /* geen opslag beschikbaar */ }
  }
  function load(key, fallback) {
    try {
      var raw = localStorage.getItem(PREFIX + key);
      return raw === null ? fallback : JSON.parse(raw);
    } catch (e) { return fallback; }
  }

  /* ---------- 1. Stappen ---------- */
  var panes = Array.prototype.slice.call(document.querySelectorAll('.pane'));
  var stepButtons = Array.prototype.slice.call(document.querySelectorAll('.stepper button[data-step]'));
  var order = panes.map(function (p) { return p.id.replace('pane-', ''); });

  function showStep(key, focus) {
    if (order.indexOf(key) === -1) key = order[0];
    panes.forEach(function (p) { p.classList.toggle('active', p.id === 'pane-' + key); });
    stepButtons.forEach(function (b) {
      if (b.getAttribute('data-step') === key) b.setAttribute('aria-current', 'step');
      else b.removeAttribute('aria-current');
    });
    store('stap', key);
    if (history.replaceState) history.replaceState(null, '', '#' + key);
    window.scrollTo(0, 0);
    if (focus) {
      var h = document.querySelector('#pane-' + key + ' h1, #pane-' + key + ' h2');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    }
  }

  stepButtons.forEach(function (b) {
    b.addEventListener('click', function () { showStep(b.getAttribute('data-step'), true); });
  });
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-goto]');
    if (!t) return;
    e.preventDefault();
    closeTheory();
    showStep(t.getAttribute('data-goto'), true);
  });

  var start = window.location.hash ? window.location.hash.slice(1) : load('stap', order[0]);
  showStep(start, false);

  /* ---------- 2. Vinkjes en voortgang ---------- */
  var checks = Array.prototype.slice.call(document.querySelectorAll('input.js-check'));
  var saved = load('vinkjes', []);
  checks.forEach(function (cb) { cb.checked = saved.indexOf(cb.id) !== -1; });

  var fill = document.getElementById('progressFill');
  var label = document.getElementById('progressLabel');
  var finish = document.getElementById('finish');

  function updateProgress() {
    var required = checks.filter(function (c) { return !c.hasAttribute('data-optional'); });
    var done = required.filter(function (c) { return c.checked; }).length;
    var pct = required.length ? Math.round(done / required.length * 100) : 0;
    if (fill) fill.style.width = pct + '%';
    if (label) label.textContent = done + ' van ' + required.length;
    if (fill && fill.parentElement) fill.parentElement.setAttribute('aria-valuenow', String(pct));
    if (finish) finish.classList.toggle('show', done === required.length && required.length > 0);

    // stappenbalk: groen vinkje als het "Klaar?"-vakje van die stap aan staat
    stepButtons.forEach(function (b) {
      var box = document.getElementById('klaar-' + b.getAttribute('data-step'));
      b.classList.toggle('done', !!(box && box.checked));
    });
  }

  checks.forEach(function (cb) {
    cb.addEventListener('change', function () {
      var ids = checks.filter(function (c) { return c.checked; }).map(function (c) { return c.id; });
      store('vinkjes', ids);
      updateProgress();
    });
  });
  updateProgress();

  /* ---------- 3. Toestelwissel (Chromebook of Windows) ----------
     Geen keuze = beide varianten zichtbaar. Dat is de veilige stand: wie de wissel
     niet opmerkt, krijgt nooit het verkeerde klikpad, alleen een langere stap. */
  var toestelButtons = Array.prototype.slice.call(document.querySelectorAll('button[data-toestel]'));

  function setToestel(keuze, bewaren) {
    body.classList.remove('toestel-cros', 'toestel-win');
    if (keuze === 'cros' || keuze === 'win') body.classList.add('toestel-' + keuze);
    toestelButtons.forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-toestel') === keuze ? 'true' : 'false');
    });
    if (bewaren) store('toestel', keuze || '');
  }

  toestelButtons.forEach(function (b) {
    b.addEventListener('click', function () {
      var keuze = b.getAttribute('data-toestel');
      // opnieuw op dezelfde knop klikken = keuze ongedaan maken, beide varianten terug
      setToestel(b.getAttribute('aria-pressed') === 'true' ? '' : keuze, true);
    });
  });
  setToestel(load('toestel', ''), false);

  var reset = document.getElementById('btnReset');
  if (reset) {
    reset.addEventListener('click', function () {
      if (!window.confirm('Wil je alle vinkjes en je toestelkeuze op deze pagina wissen? Je werkdocument verandert niet.')) return;
      checks.forEach(function (c) { c.checked = false; });
      store('vinkjes', []);
      updateProgress();
      setToestel('', true);
    });
  }

  /* ---------- 4. Theoriekaart ---------- */
  var theory = document.getElementById('theory');
  var scrim = document.getElementById('scrim');
  var openers = document.querySelectorAll('[data-open-theory]');
  var lastFocus = null;

  function isDocked() { return window.matchMedia('(min-width: 1280px)').matches; }
  function openTheory(anchor) {
    if (!theory) return;
    if (!isDocked()) {
      lastFocus = document.activeElement;
      theory.classList.add('open');
      if (scrim) scrim.classList.add('show');
      theory.setAttribute('aria-hidden', 'false');
    }
    if (anchor) {
      var target = document.getElementById(anchor);
      if (target) target.scrollIntoView({ block: 'start' });
    }
    var cb = theory.querySelector('.theory-close');
    if (cb && !isDocked()) cb.focus();
  }
  function closeTheory() {
    if (!theory || isDocked()) return;
    theory.classList.remove('open');
    if (scrim) scrim.classList.remove('show');
    theory.setAttribute('aria-hidden', 'true');
    if (lastFocus) lastFocus.focus();
  }
  Array.prototype.forEach.call(openers, function (b) {
    b.addEventListener('click', function (e) { e.preventDefault(); openTheory(b.getAttribute('data-open-theory')); });
  });
  if (scrim) scrim.addEventListener('click', closeTheory);
  var closeBtn = theory ? theory.querySelector('.theory-close') : null;
  if (closeBtn) closeBtn.addEventListener('click', closeTheory);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeTheory(); hidePop(); } });
  if (theory && !isDocked()) theory.setAttribute('aria-hidden', 'true');
  // links binnen de theoriekaart (inhoudstafel)
  if (theory) {
    theory.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#th-"]');
      if (!a) return;
      e.preventDefault();
      var t = document.getElementById(a.getAttribute('href').slice(1));
      if (t) t.scrollIntoView({ block: 'start' });
    });
  }

  /* ---------- 5. Woordenlijst ---------- */
  var GLOSSARY = {
    'bestand': 'Eén document, tabel of foto op de computer. Een bestand heeft altijd een naam.',
    'map': 'Een plaats waarin je bestanden bewaart. Zoals een lade in een kast.',
    'hoofdmap': 'De grote map bovenaan. Daarin zitten al je submappen.',
    'submap': 'Een map die in een andere map zit.',
    'jaarmap': 'De hoofdmap voor het hele schooljaar. Daarin komt alles van dit vak.',
    'projectmap': 'De map van één onderzoek, met een vaste indeling: ruwe data, verwerkte data, verslag, bronnen en beeldmateriaal.',
    'mappenstructuur': 'De manier waarop jouw mappen in elkaar zitten: welke map in welke map.',
    'cloudopslag': 'Opslag op het internet, bij Google Drive. Wat daar staat, blijft bewaard en staat op elk toestel waarop je aanmeldt.',
    'google drive': 'De cloudopslag van je schoolaccount. Hier hoort al je schoolwerk en al je onderzoeksmateriaal.',
    'lokale opslag': 'De opslag in de computer of Chromebook zelf (de map Downloads). Die is alleen op dat ene toestel, en het toestel mag die map zelf leegmaken.',
    'bestanden-app': 'De app op een Chromebook waarin je je mappen ziet: Mijn bestanden (het toestel zelf) en Google Drive (de cloud). Op Windows heet die app de Verkenner.',
    'verkenner': 'De app op Windows waarin je je mappen ziet. Je opent ze met de Windows-toets en E. Op een Chromebook heet die app Bestanden.',
    'downloads': 'De map op het toestel zelf. Daar komen je gedownloade bestanden en je schermafbeeldingen terecht. Dit is lokale opslag, en dus tijdelijk.',
    'zip-bestand': 'Eén ingepakt bestand waarin meerdere bestanden zitten. Je moet het eerst uitpakken voor je de bestanden kan gebruiken.',
    'uitpakken': 'De bestanden uit een zip-bestand halen, zodat je ze los kan openen, hernoemen en verplaatsen.',
    'uploaden': 'Een bestand van je toestel naar de cloud zetten, bijvoorbeeld van Downloads naar Google Drive.',
    'bestandsnaam': 'De naam van een bestand. Een goede naam zegt meteen wat erin zit, zonder het bestand te openen.',
    'naamafspraak': 'De vaste manier waarop iedereen in het labo bestanden benoemt. Zo vindt ook je groepsgenoot jouw bestand terug.',
    'extensie': 'De letters achter de punt in een bestandsnaam, zoals .docx of .xlsx. Ze zeggen welk soort bestand het is. Laat ze staan.',
    'versiebeheer': 'Bijhouden welke versie de recentste is, met v1, v2, v3 in de naam en met de versiegeschiedenis van Drive.',
    'versiegeschiedenis': 'De lijst van alle wijzigingen in een Google-bestand: wie wat wanneer veranderde. Je kan een oudere versie terugzetten.',
    'ruwe data': 'De gegevens zoals je ze verzameld hebt, nog zonder bewerking: de antwoorden van de enquête, de opname, het transcript. Hier verander je nooit iets in.',
    'verwerkte data': 'De ruwe data nadat je ze hebt opgeschoond, geteld of berekend: tabellen, gemiddelden, grafieken.',
    'metagegevens': 'Gegevens over een bestand: wie het maakte, wanneer, en wanneer het laatst gewijzigd is. Drive houdt die zelf bij.',
    'toegangsrechten': 'Wat iemand met jouw bestand mag doen: alleen lezen, reageren, of alles bewerken.',
    'delen': 'Iemand anders toegang geven tot jouw map of bestand. Jij blijft de eigenaar.',
    'lezer': 'Iemand die je bestand mag openen en lezen, maar niets mag veranderen.',
    'reageerder': 'Iemand die je bestand mag lezen en er opmerkingen bij mag zetten, maar de tekst zelf niet mag veranderen.',
    'bewerker': 'Iemand die alles mag veranderen in je bestand: aanpassen, hernoemen en zelfs verwijderen.',
    'eigenaar': 'Degene die het bestand heeft gemaakt. De eigenaar beslist wie het mag zien.',
    'respondent': 'De persoon die je enquête invult of die je interviewt. Hun gegevens zijn persoonsgegevens.',
    'persoonsgegevens': 'Alle gegevens waarmee je iemand kan herkennen: naam, geboortedatum, klas, adres, stem op een opname.',
    'pseudonimiseren': 'De naam van een respondent vervangen door een code, bijvoorbeeld respondent-02. Alleen jij houdt bij welke code bij wie hoort.',
    'anonimiseren': 'Alle gegevens weghalen waarmee je iemand kan herkennen. Daarna is niemand nog herleidbaar, ook niet door jou.',
    'werkdocument': 'Jouw eigen Google-document uit Classroom: het Onderzoeksmap-paspoort. Dit bestand lever je in.',
    'lespagina': 'Deze website. Hier lees je wat je moet doen. De lespagina lever je niet in.',
    'classroom': 'Google Classroom: daar staan je opdracht, je werkdocument, het zip-bestand en de knop Inleveren.',
    'schermafbeelding': 'Een foto van je scherm. Op een Chromebook: Shift + Ctrl + Vensters tonen. Op Windows: Windows-toets + Shift + S.'
  };
  var pop = null;
  function hidePop() { if (pop) { pop.remove(); pop = null; } }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('.term');
    if (!t) { if (pop && !e.target.closest('.term-pop')) hidePop(); return; }
    var key = (t.getAttribute('data-term') || t.textContent).toLowerCase().trim();
    var text = GLOSSARY[key];
    if (!text) return;
    hidePop();
    pop = document.createElement('div');
    pop.className = 'term-pop';
    pop.setAttribute('role', 'tooltip');
    pop.innerHTML = '<strong>' + t.textContent + '</strong><br>' + text;
    document.body.appendChild(pop);
    var r = t.getBoundingClientRect();
    var left = Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - 320);
    pop.style.left = Math.max(8, left) + 'px';
    pop.style.top = (window.scrollY + r.bottom + 8) + 'px';
  });

  /* ---------- 6. Mini-test ---------- */
  document.querySelectorAll('.quiz-q').forEach(function (q) {
    var fb = q.querySelector('.feedback');
    q.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        q.querySelectorAll('button').forEach(function (b) { b.classList.remove('right', 'wrong'); });
        var ok = btn.hasAttribute('data-right');
        btn.classList.add(ok ? 'right' : 'wrong');
        if (fb) fb.textContent = ok ? (q.getAttribute('data-ok') || 'Juist!') : (q.getAttribute('data-nok') || 'Nog niet. Probeer opnieuw.');
      });
    });
  });

  /* ---------- 7. Screenshot-plaatsen ---------- */
  document.querySelectorAll('figure.shot').forEach(function (fig) {
    var file = fig.getAttribute('data-shot');
    var caption = fig.getAttribute('data-caption') || '';
    if (!file) return;
    var img = new Image();
    img.alt = fig.getAttribute('data-alt') || caption;
    img.onload = function () {
      fig.innerHTML = '';
      fig.appendChild(img);
      if (caption) { var c = document.createElement('figcaption'); c.textContent = caption; fig.appendChild(c); }
      fig.classList.add('loaded');
    };
    img.onerror = function () {
      if (teacherMode) fig.innerHTML = '📷 <strong>Screenshot-plaats</strong>: bewaar als <code>assets/screenshots/' + file + '</code><br>' + (fig.getAttribute('data-alt') || '');
    };
    img.src = 'assets/screenshots/' + file;
  });
})();
