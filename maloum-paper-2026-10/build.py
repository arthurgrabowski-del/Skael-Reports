# Generator für das MALOUM-Paper (Skael-Stil wie nxt-you-strategie-2026-10).
import html, os, re

OUT = os.path.dirname(os.path.abspath(__file__))
IMG = "../assets/maloum-konkurrenz/"
LIB = "https://www.facebook.com/ads/library/?id="
EDITION = "12. Oktober 2026<br>Entwurf · Weekly mit Tobias"

PAGES = [
    ("index.html", "Überblick"),
    ("kampagnen.html", "Kampagnenstruktur"),
    ("ads.html", "So sehen die Ads aus"),
    ("skripte.html", "Creator-Skripte"),
    ("konkurrenz.html", "Konkurrenz"),
]

EXTRA_CSS = """
.phone-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin:28px 0}
.phone{margin:0;min-width:0}
.story{container-type:inline-size;aspect-ratio:9/16;border-radius:18px;position:relative;overflow:hidden;color:#fff;font-family:Poppins,Arial,sans-serif;background:linear-gradient(160deg,#c9b7a6,#7d6a5c 55%,#3b3029)}
.story.b{background:linear-gradient(170deg,#9fb3c8,#56708c 60%,#26384d)}
.story.c{background:linear-gradient(165deg,#d8c3b0,#a07f69 50%,#4d382c)}
.story.d{background:linear-gradient(170deg,#b9c7b0,#6f8566 55%,#2f3d2b)}
.story.e{background:linear-gradient(170deg,#2a2f3d,#141821)}
.story.f{background:linear-gradient(160deg,#e9e4dc,#cfc6b8)}
.story .top{position:absolute;top:4cqw;left:5cqw;right:5cqw;display:flex;align-items:center;gap:2.5cqw;font-size:3.6cqw;font-weight:500}
.story .top i{width:8cqw;height:8cqw;border-radius:50%;background:#ffffffb3;display:block}
.story .bar{position:absolute;top:1.6cqw;left:4cqw;right:4cqw;height:.7cqw;background:#ffffff80;border-radius:2px}
.story .ph{position:absolute;inset:22% 12% 34% 12%;border:1.5px dashed #ffffff9e;border-radius:12px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:3.4cqw;line-height:1.35;padding:4cqw;color:#ffffffe0}
.story .q{position:absolute;left:12%;right:12%;top:18%;background:#fff;color:#111;border-radius:4cqw;overflow:hidden;text-align:center;box-shadow:0 2cqw 6cqw #0003}
.story .q b{display:block;background:linear-gradient(90deg,#7b4dff,#e1306c);color:#fff;font-size:3.6cqw;font-weight:500;padding:2.6cqw}
.story .q span{display:block;font-size:4.6cqw;font-weight:600;padding:3.6cqw 3cqw}
.story .ans{position:absolute;left:8%;right:8%;bottom:17%;font-size:5.6cqw;font-weight:600;line-height:1.25;text-shadow:0 1px 8px #0008}
.story .ans small{display:block;font-size:3.6cqw;font-weight:400;margin-top:2cqw}
.story .cta{position:absolute;left:5cqw;right:5cqw;bottom:4cqw;background:#ffffffe6;color:#111;border-radius:10cqw;text-align:center;font-size:3.6cqw;font-weight:600;padding:2.6cqw}
.story .split{position:absolute;inset:14% 4% 26% 4%;display:grid;grid-template-columns:1fr 1fr;gap:2cqw}
.story .split div{border:1.5px dashed #ffffff9e;border-radius:10px;display:flex;flex-direction:column;justify-content:flex-end;padding:3cqw;font-size:3.4cqw;line-height:1.3}
.story .split b{font-size:4.6cqw}
.story .coll{position:absolute;inset:13% 6% 28% 6%;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:1.6cqw}
.story .coll div{background:#ffffff26;border-radius:8px;display:flex;align-items:flex-end;padding:2cqw;font-size:3.2cqw;font-weight:600}
.story .poll{position:absolute;left:14%;right:14%;top:56%;background:#fff;color:#111;border-radius:4cqw;padding:3cqw;text-align:center;font-size:4cqw;font-weight:600}
.story .poll div{display:grid;grid-template-columns:1fr 1fr;gap:2cqw;margin-top:2.4cqw}
.story .poll span{border:1px solid #ddd;border-radius:3cqw;padding:2cqw;font-size:3.6cqw;color:#7b4dff}
.story .notes{position:absolute;inset:12% 7% 22% 7%;background:#fffdf3;color:#222;border-radius:10px;padding:5cqw;font-size:3.7cqw;line-height:1.55}
.story .notes h4{margin:0 0 3cqw;font-size:5cqw;color:#222}
.story .notes p{margin:0 0 1.6cqw;font-size:3.7cqw;max-width:none}
.story .letter{position:absolute;inset:40% 6% 16% 6%;font-size:3.6cqw;line-height:1.55;text-shadow:0 1px 6px #0009}
.story .play{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:16cqw;height:16cqw;border-radius:50%;background:#ffffff40;display:flex;align-items:center;justify-content:center;font-size:7cqw}
.story .ost{position:absolute;left:8%;right:8%;top:16%;font-size:5.2cqw;font-weight:600;line-height:1.25;text-shadow:0 1px 8px #0008}
.phone figcaption{padding-top:14px}
.phone figcaption h3{font-size:16px;margin:0 0 6px}
.phone figcaption p{font-size:13px;margin:0 0 6px;line-height:1.6}
.tag{display:inline-block;font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.04em;text-transform:uppercase;padding:2px 8px;border-radius:20px;background:#eef2ff;color:#3a6ef4;margin-right:6px}
.tag.red{background:#fee2e2;color:#dc2626}.tag.green{background:#dcfce7;color:#16a34a}.tag.yellow{background:#fef3c7;color:#b45309}
.camp{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin:26px 0}
.camp article{background:#fff;border:1px solid #e4e6ec;border-radius:10px;padding:18px;min-width:0}
.camp article.off{background:#fafafa;border-style:dashed}
.camp h3{font-size:16px;margin:8px 0 8px}
.camp p,.camp li{font-size:12.5px;line-height:1.6;margin:0 0 6px}
.camp ul{padding-left:18px;margin:6px 0 0}
.camp .num{font-family:'DM Mono',monospace;font-size:11px;color:#3a6ef4}
.script{background:#fff;border:1px solid #e4e6ec;border-radius:10px;padding:22px 24px;margin:22px 0}
.script h3{margin:0 0 6px;font-size:18px}
.script .meta{font-family:'DM Mono',monospace;font-size:11px;color:#6b7280;margin-bottom:14px}
.script table{min-width:560px}
.script blockquote{font-size:14px;margin:14px 0 0}
.dd{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:20px 0}
.dd>div{border-radius:10px;padding:18px 20px}
.dd .do{background:#f0fdf4;border:1px solid #bbf7d0}.dd .dont{background:#fef2f2;border:1px solid #fecaca}
.dd h3{font-size:15px;margin:0 0 10px}.dd ul{margin:0;padding-left:18px}.dd li{font-size:13px;margin:0 0 6px}
.shot-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin:26px 0}
.shot{border:1px solid #e4e6ec;border-radius:10px;background:#fff;overflow:hidden;margin:0}
.shot img{width:100%;height:340px;object-fit:cover;object-position:50% 85%;display:block;border-radius:0;background:#f3f5f9}
.shot figcaption{padding:14px 16px;font-size:12.5px;line-height:1.6}
.shot figcaption b{display:block;font-size:14px;margin-bottom:4px;color:#0f1b2d}
.shot figcaption a{display:inline-block;margin-top:6px;font-size:12px}
.timeline{border-left:2px solid #c7d4fd;margin:24px 0 24px 8px;padding-left:22px}
.timeline div{position:relative;padding:0 0 18px}
.timeline div:before{content:"";position:absolute;left:-29px;top:6px;width:12px;height:12px;border-radius:50%;background:#c7d4fd}
.timeline div.us:before{background:#3a6ef4}
.timeline span{font-family:'DM Mono',monospace;font-size:11px;color:#6b7280;display:block}
.timeline p{margin:2px 0 0;font-size:14px}
@media(max-width:900px){.camp{grid-template-columns:1fr 1fr}.phone-grid,.shot-grid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.camp,.phone-grid,.shot-grid,.dd{grid-template-columns:1fr}}
@media print{.phone,.shot,.script,.camp article{break-inside:avoid}}
"""


def page(fname, title, dek, body):
    nav = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{n}</a>' for f, n in PAGES
    )
    doc = f"""<!doctype html><html lang="de"><head><meta charset="utf-8"/><meta content="width=device-width,initial-scale=1" name="viewport"/><meta content="light" name="color-scheme"/><meta name="robots" content="noindex"/><title>{re.sub(r"<[^>]+>|&shy;","",title)} | MALOUM</title><meta content="{html.escape(dek)}" name="description"/><link href="/www.skael.de-favicon.ico" rel="icon"/><link href="assets/report.css" rel="stylesheet"/><link href="assets/short.css" rel="stylesheet"/><link href="assets/detail-pages.css" rel="stylesheet"/><link rel="stylesheet" href="assets/fonts.css"><link rel="stylesheet" href="assets/paper.css"></head><body><a class="skip" href="#main">Zum Inhalt</a><header class="mast"><a class="brand" href="index.html">MALOUM<span>Skael Reports</span></a><div class="edition">{EDITION}</div></header><nav class="primary" aria-label="Kapitel">{nav}</nav><main class="short-main detail-main" id="main"><header class="hero"><h1>{title}</h1><p class="dek">{dek}</p></header>{body}</main><footer><span>MALOUM / Skael · Oktober 2026</span><a href="../Maloum-Konkurrenz-Ads-Okt-2026.html">Vollständiger Konkurrenz-Report</a></footer></body></html>"""
    open(os.path.join(OUT, fname), "w").write(doc)


# ---------------------------------------------------------------- Überblick
index = """
<section class="agenda"><h2>Das Paper in vier Teilen</h2>
<div class="agenda-row"><span>01</span><div><h3>Kampagnenstruktur</h3><p>Aus über zehn Einzelkampagnen werden vier: Testing, Scaling, Eros-Agentur und ein separater Brand-Push. Stella geht direkt ins Scaling. <a href="kampagnen.html">Struktur ansehen</a></p></div></div>
<div class="agenda-row"><span>02</span><div><h3>So sehen die neuen Ads aus</h3><p>Die Ads kommen von der Creatorin selbst, nicht von MALOUM: ihr Name als Absender, Handy-Selfies, echte Story-Optik. Neun Formate, alle ohne Chat- oder Kontaktversprechen. <a href="ads.html">Formate ansehen</a></p></div></div>
<div class="agenda-row"><span>03</span><div><h3>Skripte für die Creatorinnen</h3><p>Fertige Drehanleitungen für Stella und Leyla, dazu Vorlagen für Samantra, Gwendo, Nikoleta, Tess und Emma. Die Creatorin filmt am Handy, wir schneiden und schalten. <a href="skripte.html">Skripte lesen</a></p></div></div>
<div class="agenda-row"><span>04</span><div><h3>Was die Konkurrenz macht</h3><p>Andere Creatorinnen schalten unser altes Sticker-Format seit Monaten, teils mit bis zu 14 Varianten. Wir hatten es zuerst. Was wir daraus übernehmen und was nicht. <a href="konkurrenz.html">Konkurrenz ansehen</a></p></div></div>
</section>

<section><h2>Warum jetzt ein Neustart</h2>
<ul class="short-list">
<li><strong>Das alte FAQ-Format wird gesperrt.</strong> 24 von 72 Ads im Konto sind abgelehnt, fast immer wegen „Adult Sexual Solicitation“. Der Auslöser ist vor allem der Text: „schreib mir“, „ich antworte“, „heute Abend chatten“.</li>
<li><strong>Bestandskunden laufen gut, neue Käufer werden weniger.</strong> Der Umsatz aus älteren Kohorten liegt im Oktober bei rund 1.900 € pro Tag und damit über dem September. Gleichzeitig ist die Zahl neuer Erstkäufer über unsere Ads seit Anfang September Woche für Woche gefallen.</li>
<li><strong>Zu viele kleine Kampagnen.</strong> Mit 10 bis 20 € Tagesbudget pro Creatorin bekommt Meta zu wenige Käufe, um zu lernen. Die einzige Kampagne mit genug Budget, MAL WARMUP, war auch die einzige, die sich über Zeit verbessert hat.</li>
</ul>
<p class="fine">Zahlen aus dem Oktober-Report 01.–11.10. und Eriks Konto-Audit vom 06.10. Backend-Daten von MALOUM sind die Grundlage, nicht die Pixel-Werte.</p>
</section>

<section><h2>Was wir im Weekly entscheiden</h2>
<div class="decision-ledger">
<article><span>Budget</span><h3>Wie viel geht im Oktober in Testing und Scaling?</h3><p>Unser Vorschlag zur Aufteilung steht auf der Seite Kampagnenstruktur. Den Gesamtbetrag legen wir gemeinsam fest.</p></article>
<article><span>Creatorinnen</span><h3>Wer ist dabei, wer hat ein fixes Agenturbudget?</h3><p>Bisheriger Stand: Eros (Tess, Emma) bekommt eine eigene Kampagne. Gwendo, Samantra und Nikoleta gehen in den gemeinsamen Pool. Lea Sophy wird pausiert.</p></article>
<article><span>Material</span><h3>Wer liefert bis wann neues Material?</h3><p>Pro Creatorin 8–10 normale Handyfotos und 2–3 kurze Clips nach unseren Skripten. Bei Emma ist das am dringendsten.</p></article>
<article><span>Absender</span><h3>Laufen die Ads als Partnership Ads?</h3><p>Dann steht der Name der Creatorin oben, die Ad läuft aber über unser Konto. Dafür braucht jede Creatorin einmal ihre Freigabe in Instagram.</p></article>
</div>
<div class="notice"><strong>Stand: Entwurf.</strong><p>Erik ergänzt noch Details. Dieses Paper ändert nichts an Kampagnen, Budgets oder Tracking. Umgesetzt wird erst nach Freigabe.</p></div>
</section>
"""
page("index.html", "Der <em>Neustart</em> für MALOUM.",
     "Kampagnenstruktur, neue Ads, Skripte für die Creatorinnen und ein Blick auf die Konkurrenz. Für unser Weekly am 12. Oktober.",
     index)

# ---------------------------------------------------------------- Kampagnen
kampagnen = """
<section><h2>Vier Kampagnen statt über zehn</h2>
<p>Bisher hat jede Creatorin zwei eigene Kampagnen mit 10 bis 20 € Tagesbudget. Das ist zu wenig, damit Meta genug Käufe sieht und lernt. Künftig bündeln wir: Die Creatorinnen sind Ad Sets innerhalb weniger Kampagnen mit gemeinsamem Budget.</p>
<div class="camp">
<article><span class="num">K1 · TESTING</span><h3>Warm-up &amp; Test</h3><p>Hier testen wir neue Creatorinnen und neue Formate.</p><ul><li>Ein Ad Set je Creatorin: Leyla, Samantra, Gwendo, Nikoleta, Julia</li><li>3–5 neue Ads je Ad Set</li><li>Ziel-Event: Purchase New</li><li>Was nicht läuft, fliegt nach 5–7 Tagen raus</li></ul></article>
<article><span class="num">K2 · SCALING</span><h3>Nur Gewinner</h3><p>Hier landen Creatorinnen und Ads, die im Testing Käufe bringen.</p><ul><li>Stella von Anfang an hier</li><li>Gewinner-Ads aus K1 wandern als Kopie hierher</li><li>Ziel-Event: Purchase New</li><li>Budget steigt schrittweise mit den Ergebnissen</li></ul></article>
<article><span class="num">K3 · EROS-AGENTUR</span><h3>Tess &amp; Emma</h3><p>Eigene Kampagne, weil Eros ein festes Budget mitbringt und anders gemessen werden will.</p><ul><li>Ein Ad Set je Creatorin</li><li>Ziel-Event: Follow (MALOUM-Follow gegen Agentur-Follow testen)</li><li>Budget laut Agentur 2–3k</li></ul></article>
<article><span class="num">K4 · BRAND</span><h3>Brand-Push, separat</h3><p>Ankündigungen und organische Reels, die gut laufen, pushen wir hier. Kein Umsatzziel.</p><ul><li>Getrennt auswerten, nicht mit K1/K2 vergleichen</li><li>Erst in 1–2 Wochen starten</li></ul></article>
</div>
<p class="fine">Warum Stella nicht ins Testing kommt: In MAL WARMUP hat sie 70–80 % der Impressionen bekommen. Im gemeinsamen Testing würde sie das Budget der anderen Creatorinnen aufbrauchen, bevor diese getestet sind.</p>
</section>

<section><h2>Was wir abschalten</h2>
<div class="table-wrap"><table><thead><tr><th>Was</th><th>Warum</th><th>Was passiert damit</th></tr></thead><tbody>
<tr><th>Bisherige FAQ-/Chat-Ads</th><td>11 von 16 Ads mit Kontakt- oder Antwortversprechen sind gesperrt. Jede weitere Sperre erhöht das Risiko für das Konto.</td><td>Pausieren, nicht löschen</td></tr>
<tr><th>Lea Sophy</th><td>288 € im Oktober, kein Neukunde. Im September 778 € und 1 Käufer.</td><td>Pausieren</td></tr>
<tr><th>Doppelte Creator-Kampagnen</th><td>Zwei Kampagnen pro Creatorin teilen ein ohnehin kleines Budget.</td><td>Ad Sets in K1 bzw. K2 neu anlegen</td></tr>
<tr><th>MAL WARMUP</th><td>Lief im September stark, im Oktober aber nur 1 Neukunde bei 962 €.</td><td>Gewinner-Ads nach K2 übernehmen, dann auslaufen lassen</td></tr>
</tbody></table></div>
<p class="fine">Neue Ads legen wir als neue Ads an statt bestehende zu bearbeiten. Jede Bearbeitung löst eine neue Prüfung durch Meta aus.</p>
</section>

<section><h2>Budget: unser Vorschlag zur Aufteilung</h2>
<p>Im Oktober haben wir bisher rund <strong>200 € pro Tag</strong> ausgegeben. Unser Vorschlag ist, die Summe in den ersten zwei Wochen nicht zu erhöhen, sondern umzuverteilen. Mehr Budget erst, wenn die neuen Ads Käufe im Backend bringen.</p>
<div class="table-wrap"><table><thead><tr><th>Kampagne</th><th>Anteil am Budget (ohne Eros)</th><th>Logik</th></tr></thead><tbody>
<tr><th>K2 Scaling</th><td>ca. 55 %</td><td>Stella und bewährte Ads tragen das Volumen.</td></tr>
<tr><th>K1 Testing</th><td>ca. 35 %</td><td>Genug, damit jede neue Creatorin einige Tage Daten sammelt.</td></tr>
<tr><th>K4 Brand</th><td>ca. 10 %</td><td>Klein halten, startet später.</td></tr>
<tr><th>K3 Eros</th><td>eigenes Budget</td><td>Kommt von der Agentur, läuft getrennt.</td></tr>
</tbody></table></div>
<p class="fine">Ausgangswert: 2.197 € Spend vom 01. bis 11.10. (2.466 US-Dollar). Die Aufteilung ist ein Vorschlag. Den Gesamtbetrag für Oktober legen wir im Weekly fest.</p>
</section>

<section><h2>Tracking: was vor dem Start stehen muss</h2>
<ul class="short-list">
<li><strong>Ein UTM-Schema für alle Ads</strong>, direkt beim Anlegen gesetzt. So wissen wir im Backend, welche Ad welchen Käufer gebracht hat.</li>
<li><strong>Ein Testkauf vor dem Start:</strong> Klick auf die Ad, Registrierung, Kauf, und dann prüfen, ob alles im Export ankommt.</li>
<li><strong>Abstimmung mit André</strong> zu Pixel und Events. Offen ist vor allem, warum Meta deutlich mehr Käufe meldet als im Backend ankommen.</li>
<li><strong>Optional: Event „3 Messages sent“ testen.</strong> Liegt zwischen Registrierung und Kauf und liefert mehr Daten als ein Kauf. Nur, wenn das Team von MALOUM es technisch anlegen kann.</li>
</ul>
</section>
"""
page("kampagnen.html", "Kampagnen&shy;struktur.",
     "Weniger Kampagnen, gemeinsame Budgets, Creatorinnen als Ad Sets. Testing und Scaling getrennt, Eros mit eigener Kampagne.",
     kampagnen)

# ---------------------------------------------------------------- Ads


def story(cls, user, inner, cta="Mehr ansehen"):
    return f'<div class="story {cls}"><div class="bar"></div><div class="top"><i></i>{user} · Anzeige</div>{inner}<div class="cta">{cta}</div></div>'


formats = [
    ("a", "stella4twenty", '<div class="q"><b>Stelle mir eine Frage</b><span>wie findest du mich so ohne filter?</span></div><div class="ph">Handy-Selfie ohne Filter<br>Gesicht bis Schulter, Alltagslook</div><div class="ans">ehrlich? ich mag mich so am liebsten 🤍</div>',
     "Fragesticker, neue Fragen", "green", "Hat sich bewährt",
     "Die Sticker-Optik bleibt. Wir tauschen nur die Fragen: keine Fragen nach Antworten oder Chat, sondern nach Look, Hobby oder Alltag.", "Lucy, Kate"),
    ("b", "deineeleyla", '<div class="split"><div><b>montag</b>7:40 · vorlesung<br>dutt, hoodie, kaffee</div><div><b>samstag</b>20:15 · shooting<br>styling, licht, outfit</div></div><div class="ans" style="bottom:15%">zwei seiten von mir.<small>die zweite gibts nicht auf insta</small></div>',
     "Montag gegen Samstag", "blue", "Neu für uns",
     "Zwei Fotos nebeneinander: Alltag und Shooting. Zeigt, dass es mehr gibt, ohne etwas Anzügliches zu versprechen.", "Kate"),
    ("c", "samantra", '<div class="coll"><div>jänner</div><div>märz</div><div>mai</div><div>juli</div><div>september</div><div>oktober</div></div><div class="ans" style="bottom:15%">so sieht mein jahr aus. und deins? 💚</div>',
     "Mein Jahr / meine Woche", "blue", "Neu für uns",
     "Collage mit 6 Fotos und Monats- oder Tagesnamen. Kate läuft damit, mit klarer Persona: Dorf, Stall, Natur.", "Kate"),
    ("d", "stella4twenty", '<div class="ph" style="inset:10% 12% 62% 12%">ein Foto</div><div class="letter">hi, ich bin stella 🤍<br>hab lange überlegt, ob ich das mache. auf insta zeig ich nur einen kleinen teil von dem, was ich fotografiere. die ganzen shootings, outfits und behind the scenes landen jetzt auf meinem profil. link ist unten.</div>',
     "Persönlicher Brief", "green", "Läuft bei uns",
     "Ein Foto, darunter ein langer, ehrlicher Text in Kleinschrift. Läuft bei Stella seit dem 28.09. Wird auf Leyla und Samantra übertragen.", "Stella (eigene Ad)"),
    ("e", "deineeleyla", '<div class="play">▶</div><div class="ost">was beim shooting passiert, bevor das foto fertig ist 👀</div><div class="ph" style="inset:58% 12% 18% 12%">6–9 Sek. Clip<br>Licht, Outfit, Lachen</div>',
     "Behind the Scenes (Video)", "green", "Hat sich bewährt",
     "Ein kurzer Clip vom Shooting: Licht aufbauen, Outfit wählen, Lachen zwischen den Fotos. Rina läuft damit seit Mai mit bis zu 8 Varianten.", "Rina Photography"),
    ("f", "gwendo", '<div class="notes"><h4>5 dinge über mich</h4><p>1. ich kann nicht ohne kaffee</p><p>2. ich lache über meine eigenen witze</p><p>3. lieblingsfilm: …</p><p>4. ich hab 3 pflanzen und alle leben</p><p>5. mein profil hat mehr fotos als insta</p></div>',
     "Notizen-App", "yellow", "Test",
     "Screenshot aus der Notizen-App mit 5 Dingen über die Creatorin. Sieht nach privatem Post aus, nicht nach Werbung.", "Hypothese"),
    ("b", "nikoleta", '<div class="ph">Selfie mit Brille</div><div class="poll">brille oder ohne?<div><span>mit 🤓</span><span>ohne ✨</span></div></div>',
     "Umfrage-Sticker", "yellow", "Test",
     "Instagram-Umfrage mit zwei Antworten. Funktioniert, weil man sofort eine Meinung hat.", "Lucy"),
    ("e", "samantra", '<div class="play">▶</div><div class="ost">pov: du findest endlich mein zweites profil</div><div class="ph" style="inset:58% 12% 18% 12%">Reel-Clip, Blick in die Kamera</div>',
     "POV-Reel", "yellow", "Test",
     "Typischer Reel-Einstieg mit Texteinblendung oben. Nur Text und Blick, keine Geste.", "Hypothese"),
    ("a", "tess.sxh", '<div class="q"><b>Stelle mir eine Frage</b><span>was machst du am wochenende?</span></div><div class="ph">Foto vom Spiel / Stadion<br>Trikot normal getragen</div><div class="ans">jeden samstag im block. wer noch? ⚽</div>',
     "Persona &amp; Hobby", "blue", "Neu für uns",
     "Jede Creatorin bekommt eine klare Rolle, an der man sie erkennt: Stadion, Gaming, Natur, Uni. Kate ist das Dorfmädchen, Lucy die Gamerin.", "Kate, Lucy, Leni"),
]

cards = "".join(
    f'<figure class="phone">{story(c, u, inner)}<figcaption><span class="tag {tc}">{tl}</span><h3>{t}</h3><p>{d}</p><p class="fine">Vorbild: {v}</p></figcaption></figure>'
    for c, u, inner, t, tc, tl, d, v in formats
)

ads = f"""
<section><h2>Das Prinzip: Die Ad kommt von der Creatorin</h2>
<p>Die Ads, die bei der Konkurrenz am längsten laufen, sehen <strong>nicht nach Werbung aus</strong>. Sie wirken wie ein normaler Post der Creatorin: ihr Name oben, ein Handy-Foto, eine echte Story. MALOUM steht nur im Link.</p>
<div class="detail-grid">
<div class="detail-card"><h3>Absender: die Creatorin</h3><p>Über <strong>Partnership Ads</strong> erscheint ihr Instagram-Name als Absender. Ausgespielt wird aus unserem Konto, also mit unserem Tracking und Budget. Jede Creatorin muss das einmal freigeben.</p></div>
<div class="detail-card"><h3>Material: Handy statt Shooting</h3><p>Selfies, Story-Screenshots und kurze Clips im Hochformat. Keine gestalteten Kacheln, keine Schriftzüge im MALOUM-Design. Je echter, desto besser.</p></div>
<div class="detail-card"><h3>Ton: wie sie selbst schreibt</h3><p>Kleinschreibung, Emojis, kurze Sätze. Was zählt, ist eine Persönlichkeit, nicht das Angebot.</p></div>
<div class="detail-card"><h3>Menge: wenige Formate, viele Varianten</h3><p>Lucy fährt ein Format mit bis zu 14 Varianten. Pro gutem Format testen wir deshalb mehrere Fotos und Texte, statt ständig neue Formate zu bauen.</p></div>
</div>
</section>

<section><h2>Neun Formate für den Start</h2>
<p class="quiet">Skizzen zur Orientierung. Die gestrichelten Flächen sind Platzhalter für die echten Fotos und Clips der Creatorinnen. Alle Texte sind Beispiele und werden mit der Creatorin angepasst.</p>
<div class="phone-grid">{cards}</div>
</section>

<section><h2>Was rein darf und was nicht</h2>
<div class="dd">
<div class="do"><h3>Rein</h3><ul>
<li>Alltag, Hobby, Persönlichkeit, Shootings, Outfits</li>
<li>„auf insta zeig ich nur einen kleinen teil meiner fotos“</li>
<li>Fragen nach Look, Hobby, Wochenende</li>
<li>Gesicht bis Brust, Alltagskleidung, draußen, Café, Auto</li>
<li>PayPal und Klarna als neutraler Hinweis im Text</li>
</ul></div>
<div class="dont"><h3>Nicht rein</h3><ul>
<li>„schreib mir“, „ich antworte“, „chatten“, „privat“, „heute Abend“</li>
<li>„nur die Hälfte von mir“, „den Rest gibts im Link“</li>
<li>Spiegelselfies im Bad, Unterwäsche, hochgezogene Trikots, Po- oder Dekolleté-Fokus</li>
<li>Alter, Schule oder „schüchtern und neu“ (macht die Konkurrenz, ist für uns tabu)</li>
<li>Hinweise auf OnlyFans</li>
</ul></div>
</div>
<p class="fine">Grundlage: Eriks Analyse der 24 gesperrten Ads. 23 von 25 Sperrvermerken lauten „Adult Sexual Solicitation“. Auch eine neutral formulierte Ad wird abgelehnt, wenn Profil oder Zielseite das nicht zulassen. Das prüfen wir vor dem Start.</p>
</section>
"""
page("ads.html", "So sehen die <em>neuen Ads</em> aus.",
     "Weg vom FAQ-Format, hin zu Ads, die aussehen, als hätte die Creatorin sie selbst gepostet. Neun Formate, alle ohne Chat- oder Kontaktversprechen.",
     ads)

# ---------------------------------------------------------------- Skripte


def script(name, meta, rows, caption, note=""):
    tr = "".join(f"<tr><th>{t}</th><td>{b}</td><td>{o}</td></tr>" for t, b, o in rows)
    n = f'<p class="fine">{note}</p>' if note else ""
    return f"""<div class="script"><h3>{name}</h3><div class="meta">{meta}</div><div class="table-wrap"><table><thead><tr><th>Sek.</th><th>Was man sieht</th><th>Text im Bild / gesprochen</th></tr></thead><tbody>{tr}</tbody></table></div><blockquote><p><strong>Ad-Text:</strong> {caption}</p></blockquote>{n}</div>"""


skripte = """
<section><h2>So drehen die Creatorinnen</h2>
<ul class="short-list">
<li><strong>Handy, Hochformat, Tageslicht.</strong> Kein Profi-Setup nötig, je natürlicher, desto besser.</li>
<li><strong>Pro Skript 2–3 Takes</strong> mit leicht anderem Einstieg. Daraus bauen wir mehrere Varianten.</li>
<li><strong>Kein fertiger Schnitt.</strong> Die Creatorin schickt Rohclips, wir schneiden, setzen Text und legen die Ads an.</li>
<li><strong>Normale Kleidung.</strong> Hoodie, Jeans, Kleid, Trikot normal getragen. Kein Bad, kein Bett.</li>
</ul>
</section>

<section><h2>Stella</h2>
""" + script("S1 · Behind the Scenes vom Shooting", "Reel 9:16 · 8–12 Sek. · Format: Behind the Scenes", [
    ("0–2", "Stella hält das Handy, lacht in die Kamera, im Hintergrund Licht oder Stativ", "Text: „was beim shooting passiert, bevor das foto fertig ist 👀“"),
    ("2–6", "3–4 schnelle Schnitte: Outfit hochhalten, Licht ausrichten, Probe-Pose, Lachen", "Kein Ton nötig, nur Musik"),
    ("6–9", "Blick auf das Handy-Display mit einem fertigen, normalen Foto", "Text: „das hier schafft es nie auf insta“"),
    ("9–12", "Stella winkt kurz in die Kamera", "Text: „rest auf meinem profil, link unten 🤍“"),
], "hab mal mitgefilmt, wie so ein shooting bei mir abläuft 🙈 auf insta landet davon ehrlich gesagt nur ein bruchteil. der rest ist auf meinem profil 🤍") + script("S2 · Persönlicher Brief, Video-Version", "Reel 9:16 · 12–15 Sek. · Format: Persönlicher Brief", [
    ("0–3", "Stella sitzt im Auto oder Café, spricht direkt in die Kamera", "„hi, ich bin stella. ich wollte kurz was erzählen.“"),
    ("3–9", "Gleiche Einstellung, ruhig", "„auf insta zeig ich nur einen kleinen teil von dem, was ich fotografiere. die ganzen shootings und outfits sind jetzt auf meinem profil.“"),
    ("9–15", "Lächeln, kurzer Blick zur Seite, zurück in die Kamera", "„schau gern mal vorbei. link ist unten.“"),
], "hab lange überlegt, ob ich das mache 🙈 jetzt ist es da. alle shootings, outfits und behind the scenes an einem ort. link ist unten 🤍",
   "Bestehende Brief-Ad von Stella als Grundlage (läuft seit 28.09.). Neu ist die Video-Version.") + """
</section>

<section><h2>Leyla</h2>
""" + script("L1 · Montag gegen Samstag", "Reel oder Story 9:16 · 8–10 Sek. · Format: Montag gegen Samstag", [
    ("0–3", "Leyla im Hoodie mit Kaffee, Dutt, Uni oder Bahn", "Text: „montag 7:40“"),
    ("3–4", "Schneller Übergang (Hand vor die Kamera)", "Sound-Effekt"),
    ("4–8", "Leyla gestylt beim Shooting, Outfit und Licht, normale Pose", "Text: „samstag 20:15“"),
    ("8–10", "Blick in die Kamera, Augenbraue hoch", "Text: „welche seite kennst du? die zweite gibts nicht auf insta“"),
], "zwei seiten von mir 🙈 auf insta seht ihr meistens nur montag. der rest ist auf meinem profil, link unten") + script("L2 · Fragesticker mit neuer Frage", "Story 9:16 · statisch oder 6 Sek. · Format: Fragesticker", [
    ("0–6", "Selfie ohne Filter, Fragesticker oben: „wie findest du mich so ohne filter?“", "Antwort im Bild: „ehrlich? so mag ich mich am liebsten 🤍“"),
], "hab die frage so oft bekommen 🙈 hier mal ohne filter. mehr fotos gibts auf meinem profil",
   "Weitere Fragen zum Tauschen: „was machst du am wochenende?“, „lieblingsoutfit?“, „wie lange dauert so ein shooting?“") + """
</section>

<section><h2>Vorlagen für die anderen Creatorinnen</h2>
<p>Die Personas sind Vorschläge. Wir stimmen sie mit jeder Creatorin ab, damit es zu ihrem echten Alltag passt.</p>
""" + script("Samantra · Mein Jahr", "Story 9:16 · statische Collage · Format: Mein Jahr / Persona", [
    ("–", "6 Fotos aus dem Jahr: Stadion, Urlaub, Café, Shooting, Winter, Freundinnen", "Monatsnamen auf jedem Foto"),
    ("–", "Text unten", "„so sieht mein jahr aus. und deins? 💚“"),
], "jänner bis oktober in sechs fotos 🙈 die ganzen shootings dazwischen sind auf meinem profil") + script("Gwendo &amp; Nikoleta · Notizen-App und Umfrage", "Story 9:16 · Screenshot + Selfie · Format: Notizen-App / Umfrage", [
    ("–", "Notizen-App-Screenshot: „5 dinge über mich“", "Punkt 5 immer: „mein profil hat mehr fotos als insta“"),
    ("–", "Alternative: Selfie mit Umfrage-Sticker", "„brille oder ohne?“, „blond oder dunkel?“, „sommer oder winter?“"),
], "kleine fakten über mich, weil ihr immer fragt 🙈 mehr auf meinem profil") + script("Tess &amp; Emma (Eros) · Persona Stadion", "Reel 9:16 · 8–10 Sek. · Format: Persona &amp; Hobby · Ziel-Event: Follow", [
    ("0–3", "Auf dem Weg ins Stadion oder vor dem Fernseher, Trikot normal getragen", "Text: „jeden samstag im block“"),
    ("3–7", "Jubeln, Schal, Freundinnen, Snacks", "Musik"),
    ("7–10", "Selfie-Blick in die Kamera", "Text: „wer noch? ⚽ folg mir für mehr“"),
], "samstag ist heilig ⚽ wer noch? mehr von meinen spieltagen auf meinem profil",
   "Wichtig: Trikot nicht hochgezogen oder geknotet. Genau das hat die letzten Emma-Ads sperren lassen. Von Emma brauchen wir dafür neues Material über die Agentur.") + """
</section>
"""
page("skripte.html", "Skripte für die <em>Creatorinnen.</em>",
     "Fertige Drehanleitungen für Stella und Leyla, dazu Vorlagen für Samantra, Gwendo, Nikoleta, Tess und Emma. Jeweils mit Bildfolge, Texteinblendungen und Ad-Text.",
     skripte)

# ---------------------------------------------------------------- Konkurrenz
shots = [
    ("2499150103879616", "Lucy · Fragesticker", "„Wie findest du mich? 🙈🥰“ · aktiv seit 12.05.2026 · 4 Varianten. Unser Format, bis heute live."),
    ("1348379053810950", "Rina Photography · Behind the Scenes", "„Manche Einblicke sind einfach zu exklusiv für den Feed.“ · aktiv seit 06.05.2026 · mehrere Gestaltungen mit 2–8 Varianten."),
    ("1043101744734539", "leoo.baut · Nur ein Bruchteil", "„auf Instagram zeige ich nur einen Bruchteil“ · aktiv seit 08.07.2026 · Fragesticker plus Selfie."),
    ("1356446376514173", "Kate · Persona + Split", "„groß geworden zwischen Traktoren und Wiesen“ · aktiv seit 03.09.2026 · Montag/Samstag-Split."),
    ("965713799880512", "Kate · Mein Jahr", "„Jänner Stall, März Feld, August Ernte, Dezember Schnee. So schaut mein Jahr aus. Und deins?“ · 31.08.–11.09.2026."),
    ("1798716068001442", "Kate · Fragesticker draußen", "Fragesticker-Story in der Natur · aktiv seit 01.09.2026 · 2 Varianten."),
]
shot_html = "".join(
    f'<figure class="shot"><a href="{LIB}{i}" target="_blank" rel="noopener"><img loading="lazy" src="{IMG}{i}.jpg" alt="{html.escape(t)}"></a><figcaption><b>{t}</b>{d}<br><a href="{LIB}{i}" target="_blank" rel="noopener">In der Meta Ad Library öffnen ↗</a></figcaption></figure>'
    for i, t, d in shots
)

konk = f"""
<section><h2>Was wir gesehen haben</h2>
<p>Wir haben die öffentliche Meta Ad Library für Deutschland mit rund 45 Suchen durchsucht und <strong>53 Ads von 7 Konkurrenz-Creatorinnen</strong> gefunden, 18 davon laufen aktuell. Die meisten führen ebenfalls auf MALOUM.</p>
<ul class="short-list">
<li><strong>Die Creatorin ist der Absender.</strong> Alle lang laufenden Ads kommen von der Seite der Creatorin, nicht von einer Marke.</li>
<li><strong>Handy statt Design.</strong> Selfies, Story-Screenshots, kurze Clips. Keine gestalteten Kacheln.</li>
<li><strong>Eine klare Rolle.</strong> Kate ist das Dorfmädchen, Lucy die Gamerin, Rina die Fotografin, Leni steht im Dirndl vor den Bergen.</li>
<li><strong>Viele Varianten.</strong> Lucy fährt ein Format mit bis zu 14 Varianten, Rina mit bis zu 8. Längste Laufzeit: 183 Tage.</li>
</ul>
</section>

<section><h2>Die wichtigsten Ads</h2>
<p class="quiet">Klick auf das Bild öffnet die Ad direkt in der Meta Ad Library.</p>
<div class="shot-grid">{shot_html}</div>
</section>

<section><h2>Wer hatte das Format zuerst?</h2>
<p>Laut Ad Library <strong>lief unser Fragesticker-Format zuerst</strong>. Lucy startete 33 Tage später, Marlene und leoo.baut folgten. Der Unterschied: Ihre Ads laufen seit Monaten, unsere wurden gesperrt, weil wir sie mit Chat-Texten kombiniert haben.</p>
<div class="timeline">
<div class="us"><span>04.04.2026 · MALOUM</span><p>Lia Engel: Fragesticker-Story „Auf Instagram kaum. Auf Maloum ja.“ <a href="{LIB}1299724185605992" target="_blank" rel="noopener">↗</a></p></div>
<div><span>07.05.2026 · Konkurrenz</span><p>Lucy: erste Ad mit Fragesticker („Wer möchte mit mir zocken?“) <a href="{LIB}852096757263355" target="_blank" rel="noopener">↗</a></p></div>
<div class="us"><span>10.05.2026 · MALOUM</span><p>Stella: persönlicher Brief <a href="{LIB}2157359584805044" target="_blank" rel="noopener">↗</a></p></div>
<div><span>12.05.2026 · Konkurrenz</span><p>Lucy: „Wie findest du mich?“, läuft bis heute <a href="{LIB}2499150103879616" target="_blank" rel="noopener">↗</a></p></div>
<div><span>19.05.2026 · Konkurrenz</span><p>Marlene: Fragesticker plus „Schreib mir… ich antwort dir auch“ <a href="{LIB}1515719806589359" target="_blank" rel="noopener">↗</a></p></div>
<div><span>08.07.2026 · Konkurrenz</span><p>leoo.baut: Fragesticker plus „nur einen Bruchteil“ <a href="{LIB}1043101744734539" target="_blank" rel="noopener">↗</a></p></div>
</div>
<p class="fine">Nicht alles kam von uns: „Hab jetzt kein Snap mehr…“ lief bei Kate und Marlene schon ab Januar 2026, vor unserer Snapchat-Variante im Mai.</p>
</section>

<section><h2>Was wir übernehmen und was nicht</h2>
<div class="dd">
<div class="do"><h3>Übernehmen</h3><ul>
<li>Creatorin als Absender (Partnership Ads)</li>
<li>Fragesticker mit Fragen zu Look und Alltag</li>
<li>Klare Persona je Creatorin</li>
<li>Kurze Behind-the-Scenes-Clips</li>
<li>Ein gutes Format, viele Varianten</li>
</ul></div>
<div class="dont"><h3>Nicht übernehmen</h3><ul>
<li>Lucys „18 und geh noch zur Schule“. Bei Adult-Content rechtlich und ethisch tabu.</li>
<li>„Chatte jetzt mit mir“, „schreib mir zuerst“</li>
<li>Freizügige Bildausschnitte, wie Lucy sie nutzt</li>
</ul></div>
</div>
<p class="fine">Grenzen der Recherche: Ohne Facebook-Login zeigt die Ad Library nur rund 12 Ads pro Suche, das ist eine Stichprobe. Abgelehnte Ads erscheinen dort nie. Eine lange Laufzeit deutet auf Erfolg hin, beweist ihn aber nicht. Alle 53 Ads mit Links: <a href="../Maloum-Konkurrenz-Ads-Okt-2026.html">vollständiger Konkurrenz-Report</a>.</p>
</section>
"""
page("konkurrenz.html", "Was die <em>Konkurrenz</em> macht.",
     "53 Creator-Ads aus der Meta Ad Library. Wer womit wirbt, wer welches Format zuerst hatte und was wir daraus übernehmen.",
     konk)

open(os.path.join(OUT, "assets", "paper.css"), "w").write(EXTRA_CSS)
print("ok")
