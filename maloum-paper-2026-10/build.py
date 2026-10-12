# Generator für das MALOUM-Paper (Skael-Stil wie nxt-you-strategie-2026-10).
import html, os, re

OUT = os.path.dirname(os.path.abspath(__file__))
IMG = "../assets/maloum-konkurrenz/"
LIB = "https://www.facebook.com/ads/library/?id="
EDITION = "12. Oktober 2026<br>Entwurf · Erik &amp; Arthur"

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
.story .tb{position:absolute;left:8%;right:8%;text-align:center;font-size:5cqw;font-weight:600;line-height:1.55}
.story .tb span{background:#fff;color:#111;padding:.6cqw 2.4cqw;border-radius:1.6cqw;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.story .tb.blk span{background:#111;color:#fff}
.story .lnk{position:absolute;left:50%;bottom:15%;transform:translateX(-50%);background:#fff;color:#2f6bff;border-radius:2.4cqw;padding:2.2cqw 3.6cqw;font-size:3.8cqw;font-weight:700;white-space:nowrap;box-shadow:0 1cqw 4cqw #0003}
.story .timer{position:absolute;left:50%;top:34%;transform:translateX(-50%);background:#fff;color:#111;border-radius:3cqw;padding:2.4cqw 5cqw;font-size:11cqw;font-weight:700;letter-spacing:.04em;font-variant-numeric:tabular-nums}
.story .q span{font-size:4.2cqw}
.phone .tag{margin-bottom:6px}
.fig{margin:26px 0;background:#fff;border:1px solid #e4e6ec;border-radius:12px;padding:18px}
.fig img{width:100%;height:auto;display:block;border-radius:6px}
.fig figcaption{font-size:12.5px;color:#6b7280;margin-top:10px}
.steps{padding-left:22px}.steps li{margin:0 0 12px;line-height:1.65}
.camp-table td,.camp-table th{font-size:13px;vertical-align:top}
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
<div class="agenda-row"><span>01</span><div><h3>Kampagnenstruktur</h3><p>MALOUM läuft künftig in vier Kampagnen: Brand Push (bestehend), Creator Warm-Up, Creator Scaling und Fix Test. Alle 14 Tage werden Gewinner ins Scaling gezogen. <a href="kampagnen.html">Struktur ansehen</a></p></div></div>
<div class="agenda-row"><span>02</span><div><h3>So sehen die Ads aus</h3><p>Zwei Formate mit je drei Ads, also sechs Ads je Creatorin: „Neue Bilder“ und „Fragesticker“. Alle wirken wie eine Story, die die Creatorin selbst gepostet hat. <a href="ads.html">Ads ansehen</a></p></div></div>
<div class="agenda-row"><span>03</span><div><h3>Video-Skripte für Stella und Leyla</h3><p>Zwei kurze Videos, ein Take, selbst gefilmt. Mit Briefing, No-Gos und Abgabe, so wie es an jede Creatorin rausgeht. <a href="skripte.html">Skripte lesen</a></p></div></div>
<div class="agenda-row"><span>04</span><div><h3>Was die Konkurrenz macht</h3><p>53 Creator-Ads aus der Meta Ad Library. Die Langläufer bestätigen unseren Weg. Das Fragesticker-Format hatten wir zuerst. <a href="konkurrenz.html">Konkurrenz ansehen</a></p></div></div>
</section>

<section><h2>Warum jetzt ein Neustart</h2>
<ul class="short-list">
<li><strong>Das alte FAQ-Format wird gesperrt.</strong> 24 von 72 Ads im Konto sind abgelehnt, fast immer wegen „Adult Sexual Solicitation“. Der Auslöser ist vor allem der Text: „schreib mir“, „ich antworte“, „heute Abend chatten“.</li>
<li><strong>Bestandskunden laufen gut, neue Käufer werden weniger.</strong> Der Umsatz aus älteren Kohorten liegt im Oktober bei rund 1.900 € pro Tag und damit über dem September. Gleichzeitig ist die Zahl neuer Erstkäufer über unsere Ads seit Anfang September Woche für Woche gefallen.</li>
<li><strong>Zu viele kleine Kampagnen.</strong> Mit 10 bis 20 € Tagesbudget pro Creatorin bekommt Meta zu wenige Käufe, um zu lernen. Die einzige Kampagne mit genug Budget, MAL WARMUP, war auch die einzige, die sich über Zeit verbessert hat.</li>
</ul>
<p class="fine">Zahlen aus dem Oktober-Report 01.–11.10. und Eriks Konto-Audit vom 06.10. Backend-Daten von MALOUM sind die Grundlage, nicht die Pixel-Werte.</p>
</section>

<section><h2>Auf einen Blick</h2>
<div class="decision-ledger">
<article><span>Struktur</span><h3>Vier Kampagnen statt über zehn</h3><p>Brand Push läuft weiter. Creatorinnen ohne Deal starten im Warm-Up, Gewinner wandern ins Scaling, Agentur-Deals und Startbudgets laufen im Fix Test.</p></article>
<article><span>Budget</span><h3>200 € pro Tag für die Creator-Kampagnen</h3><p>150 €/Tag Warm-Up und 50 €/Tag Scaling zum Start, dazu fest 1.000 € je Deal-Creatorin bzw. 500 € Startbudget im Fix Test. Brand Push wie bisher.</p></article>
<article><span>Ads</span><h3>Sechs Ads je Creatorin</h3><p>Ein Foto rein, Name tauschen, fertig. Die Bilder erstellen wir selbst, die beiden Videos dreht die Creatorin.</p></article>
<article><span>Rhythmus</span><h3>Alle 14 Tage auswerten</h3><p>Nach Backend-Neukunden je Creatorin und Anzeige. Nach 28 Tagen ohne Gewinner macht eine Creatorin Platz für neue.</p></article>
</div>
<div class="notice"><strong>Stand: Entwurf für das Weekly.</strong><p>Dieses Paper ändert nichts an Kampagnen, Budgets oder Tracking. Umgesetzt wird erst nach Freigabe.</p></div>
</section>
"""
page("index.html", "Der <em>Neustart</em> für MALOUM.",
     "Neue Kampagnenstruktur, neue Ads, Video-Skripte für die Creatorinnen und ein Blick auf die Konkurrenz.",
     index)

# ---------------------------------------------------------------- Kampagnen
kampagnen = """
<section><h2>Vier Kampagnen</h2>
<p>MALOUM läuft in vier Kampagnen: <strong>Brand Push</strong> (die bestehende Kampagne läuft weiter), <strong>Creator Warm-Up</strong>, <strong>Creator Scaling</strong> und <strong>Fix Test</strong>. So sieht das im Werbeanzeigenmanager aus, mit Platzhaltern statt echter Namen:</p>
<figure class="fig"><img src="assets/kampagnen-werbeanzeigenmanager.png" alt="Die vier Kampagnen mit Anzeigengruppen und Anzeigen im Werbeanzeigenmanager" loading="lazy"><figcaption>Kampagnen, Anzeigengruppen und Anzeigen mit Budgets, wie sie im Werbeanzeigenmanager angelegt werden.</figcaption></figure>
</section>

<section><h2>So wandern die Creatorinnen durch die Kampagnen</h2>
<figure class="fig"><img src="assets/kampagnen-ablauf.png" alt="Ablauf: Neue Creatorin über Warm-Up oder Fix Test ins Creator Scaling" loading="lazy"><figcaption>Wer gewinnt, wird alle 14 Tage ins Scaling gezogen.</figcaption></figure>
<ol class="steps">
<li><strong>Ohne Deal → Creator Warm-Up.</strong> Jede neue Creatorin ohne Deal bekommt dort eine Anzeigengruppe <code>&lt;Name&gt; | AS01 | Purchase</code> mit 6 Anzeigen. Das Budget sitzt auf der Kampagne, Meta verteilt es selbst. Die Starken fressen die Schwachen, und das ist gewollt.</li>
<li><strong>Alle 14 Tage wird ausgewertet</strong>, nach Backend-Neukunden je Creatorin und Anzeige. Gewinner-Anzeigen werden ins Creator Scaling hochgezogen, mit derselben Beitrags-ID, und im Warm-Up pausiert.</li>
<li><strong>Kein Gewinner?</strong> Dann bleibt sie erstmal im Warm-Up und ist in der nächsten Runde wieder dabei. Vorschlag: Nach zwei Runden ohne Gewinner (28 Tage) wird sie entfernt und macht Platz für neue Creatorinnen.</li>
<li><strong>Creator Scaling enthält nur Gewinner-Anzeigen</strong>, eine Anzeigengruppe <code>&lt;Name&gt; | AS01 | Scale</code> je Gewinnerin. Das Budget sitzt auf der Kampagne und wird alle 2–3 Tage um höchstens 20 % erhöht. Stella startet direkt hier.</li>
<li><strong>Fix Test ist für zwei Fälle da.</strong> <em>Agentur-Deal:</em> Die Creatorin hat ein zugesagtes Budget, z. B. Tess und Emma von Eros. Sie läuft hier mit festen 1.000 € auf ihrer eigenen Anzeigengruppe und wird nicht gefressen. <em>Startbudget:</em> Eine neue Creatorin bekommt im Warm-Up so wenig Budget, dass wir keine Zahlen für sie haben (Vorschlag: unter 200 € in den ersten 14 Tagen). Dann bekommt sie im Fix Test 500 € für 14 Tage und geht danach mit ihren Zahlen ins Scaling oder zurück ins Warm-Up. Läuft sie gut, kommen ihre Ads ins Creator Scaling, das Fix-Test-Budget gleichen wir dann ab.</li>
<li><strong>Brand Push läuft wie bisher</strong> von der MALOUM-Seite, mit den PayPal-Anzeigen, und ist unabhängig von den Creator-Kampagnen.</li>
</ol>
</section>

<section><h2>Die vier Kampagnen im Detail</h2>
<div class="table-wrap"><table class="camp-table"><thead><tr><th></th><th>Brand Push</th><th>Creator Warm-Up</th><th>Creator Scaling</th><th>Fix Test</th></tr></thead><tbody>
<tr><th>Kampagnenname</th><td>MAL | BRAND PUSH (bestehend)</td><td>MAL | CREATOR WARM-UP | Sales | &lt;Monat&gt;</td><td>MAL | CREATOR SCALING | Sales</td><td>MAL | FIX TEST | Sales | &lt;Monat&gt;</td></tr>
<tr><th>Wo sitzt das Budget?</th><td>auf der Kampagne</td><td>auf der Kampagne</td><td>auf der Kampagne</td><td>auf jeder Anzeigengruppe</td></tr>
<tr><th>Wie viel?</th><td>wie bisher</td><td>150 €/Tag zum Start (4.500 € im Monat)</td><td>50 €/Tag zum Start (1.500 € im Monat)</td><td>1.000 € fest je Deal-Creatorin bzw. 500 € Startbudget</td></tr>
<tr><th>Wer ist drin?</th><td>MALOUM selbst</td><td>alle Creatorinnen ohne Deal</td><td>Gewinnerinnen aus Warm-Up und Fix Test, Stella direkt</td><td>Creatorinnen mit Agentur-Deal oder Startbudget</td></tr>
<tr><th>Anzeigengruppe</th><td>Maloum | Brand Purchase</td><td>&lt;Name&gt; | AS01 | Purchase</td><td>&lt;Name&gt; | AS01 | Scale</td><td>&lt;Name&gt; | AS01 | Deal | &lt;Budget&gt; oder &lt;Name&gt; | AS01 | Start | 500</td></tr>
<tr><th>Anzeigen</th><td>PayPal Story + Feed</td><td>6 je Creatorin</td><td>nur Gewinner-Anzeigen</td><td>6 je Creatorin</td></tr>
<tr><th>Anzeigen-Name</th><td>Maloum | Story | AD01</td><td>&lt;Name&gt; | Story+Feed | AD01</td><td>gleicher Name wie vorher</td><td>&lt;Name&gt; | Story+Feed | AD01</td></tr>
<tr><th>Optimierungs-Event</th><td>Purchase New</td><td>Purchase New</td><td>Purchase New, später Test mit First Purchase</td><td>je Anzeigengruppe laut Deal (Eros: Follow)</td></tr>
</tbody></table></div>
</section>

<section><h2>Was wir abschalten</h2>
<div class="table-wrap"><table><thead><tr><th>Was</th><th>Warum</th><th>Was passiert damit</th></tr></thead><tbody>
<tr><th>Bisherige FAQ-/Chat-Ads</th><td>11 von 16 Ads mit Kontakt- oder Antwortversprechen sind gesperrt. Jede weitere Sperre erhöht das Risiko für das Konto.</td><td>Pausieren, nicht löschen</td></tr>
<tr><th>Lea Sophy</th><td>288 € im Oktober, kein Neukunde. Im September 778 € und 1 Käufer.</td><td>Pausieren</td></tr>
<tr><th>Einzelkampagnen je Creatorin</th><td>Zwei Kampagnen pro Creatorin teilen ein ohnehin kleines Budget.</td><td>Als Anzeigengruppen im Warm-Up bzw. Fix Test neu anlegen</td></tr>
</tbody></table></div>
<p class="fine">Neue Ads legen wir als neue Ads an statt bestehende zu bearbeiten. Jede Bearbeitung löst eine neue Prüfung durch Meta aus.</p>
</section>

<section><h2>Tracking: was vor dem Start stehen muss</h2>
<ul class="short-list">
<li><strong>Ein UTM-Schema für alle Ads</strong>, direkt beim Anlegen gesetzt. Nur so können wir alle 14 Tage nach Backend-Neukunden je Creatorin und Anzeige auswerten.</li>
<li><strong>Ein Testkauf vor dem Start:</strong> Klick auf die Ad, Registrierung, Kauf, und dann prüfen, ob alles im Export ankommt.</li>
<li><strong>Abstimmung mit André</strong> zu Pixel und Events. Offen ist vor allem, warum Meta deutlich mehr Käufe meldet als im Backend ankommen.</li>
</ul>
</section>
"""
page("kampagnen.html", "Kampagnen&shy;struktur.",
     "Brand Push, Creator Warm-Up, Creator Scaling und Fix Test. Wer gewinnt, wird alle 14 Tage ins Scaling gezogen.",
     kampagnen)

# ---------------------------------------------------------------- Ads


def story(cls, user, inner, cta="Mehr dazu"):
    return f'<div class="story {cls}"><div class="bar"></div><div class="top"><i></i>{user} · Gesponsert</div>{inner}<div class="cta">{cta}</div></div>'


LINK = '<div class="lnk">🔗 NEUE BILDER</div>'
six = [
    ("a", "stella4twenty", '<div class="ph" style="inset:14% 6% 30% 6%">Foto der Creatorin<br>bildfüllend</div><div class="tb" style="top:20%"><span>Hab heute neue Bilder gemacht</span></div>' + LINK,
     "AD01", "Neue Bilder · Bild", "Bild 9:16 + 4:5", "Hab heute neue Bilder gemacht / Link unten",
     "Meine neuesten Bilder findest du auf meinem Maloum-Profil. Anschauen kostet nichts.", "Neue Bilder ansehen"),
    ("c", "deineeleyla", '<div class="ph" style="inset:14% 6% 30% 6%">Foto der Creatorin</div><div class="timer">00:08</div><div class="tb blk" style="top:60%"><span>Meine neuen Bilder sind online</span></div>' + LINK,
     "AD02", "Neue Bilder · Countdown-GIF", "GIF 9:16, 8 s", "Timer läuft 8 s runter, dann: Meine neuen Bilder sind online",
     "Meine neuesten Bilder sind online. Klick auf den Link, anschauen kostet nichts.", "Jetzt ansehen"),
    ("b", "stella4twenty", '<div class="play">▶</div><div class="ph" style="inset:58% 12% 22% 12%">Creatorin spricht<br>in die Kamera</div><div class="tb" style="top:16%"><span>hab heute neue bilder gemacht</span></div>',
     "AD03", "Neue Bilder · Video", "Video 9:16", "Skript „Neue Bilder“, Untertitel machen wir",
     "Hab neue Bilder gemacht, schau sie dir an. Anschauen kostet nichts.", "Neue Bilder ansehen"),
    ("d", "deineeleyla", '<div class="q"><b>Stelle mir eine Frage</b><span>Wo kann ich deine neuen Bilder sehen?</span></div><div class="tb" style="top:auto;bottom:24%"><span>Meine neuesten Bilder findest du hier unten im Link.</span></div>' + LINK.replace('NEUE BILDER', 'MEIN PROFIL'),
     "AD04", "Fragesticker · Bild", "Bild 9:16", "Frage: „Wo kann ich deine neuen Bilder sehen?“ · Antwort: „Meine neuesten Bilder findest du hier unten im Link.“",
     "", "Neue Bilder ansehen"),
    ("a", "stella4twenty", '<div class="q"><b>Stelle mir eine Frage</b><span>Ich hab keine Kreditkarte. Kann ich deine Bilder trotzdem sehen?</span></div><div class="tb blk" style="top:auto;bottom:24%"><span>Ja, klar. Klick einfach auf den Link, bezahlen geht auch mit PayPal.</span></div>',
     "AD05", "Fragesticker · Bild", "Bild 9:16", "Frage: „Ich hab keine Kreditkarte. Kann ich deine Bilder trotzdem sehen?“ · Antwort: „Ja, klar. Klick einfach auf den Link, bezahlen geht auch mit PayPal.“",
     "", "Geht auch mit PayPal"),
    ("e", "deineeleyla", '<div class="q"><b>Stelle mir eine Frage</b><span>Wo kann ich deine neuen Bilder sehen?</span></div><div class="play" style="top:58%">▶</div><div class="ph" style="inset:66% 14% 18% 14%">Creatorin antwortet<br>im Video</div>',
     "AD06", "Fragesticker · Video", "Video 9:16", "Frage: „Wo kann ich deine neuen Bilder sehen?“ · Antwort im Video laut Skript",
     "", "Neue Bilder ansehen"),
]
cards = "".join(
    f'<figure class="phone">{story(c, u, inner)}<figcaption><span class="tag">{ad}</span><span class="tag {"green" if "Video" in f else ""}">{fmt}</span><h3>{f}</h3><p>{t}</p>{f"<p><strong>Primärtext:</strong> {p}</p>" if p else ""}<p class="fine">Headline: {h}</p></figcaption></figure>'
    for c, u, inner, ad, f, fmt, t, p, h in six
)

ads = f"""
<section><h2>Zwei Formate, sechs Ads je Creatorin</h2>
<p>Jedes Format ist eine Vorlage: <strong>ein Foto der Creatorin rein, Name tauschen, fertig.</strong> Zwei Formate mit je drei Ads, also sechs Ads je Creatorin.</p>
<div class="table-wrap"><table><thead><tr><th>Ad</th><th>Format</th><th>Inhalt</th><th>Datei</th></tr></thead><tbody>
<tr><th>AD01</th><td>Neue Bilder</td><td>Bild mit Text „Hab heute neue Bilder gemacht“, Link-Sticker</td><td>Bild 9:16 + 4:5</td></tr>
<tr><th>AD02</th><td>Neue Bilder</td><td>Countdown-Timer, läuft 8 s runter, dann Link-Sticker</td><td>GIF 9:16, 8 s</td></tr>
<tr><th>AD03</th><td>Neue Bilder</td><td>Creatorin sagt es selbst in die Kamera (Skript)</td><td>Video 9:16</td></tr>
<tr><th>AD04</th><td>Fragesticker</td><td>„Wo kann ich deine neuen Bilder sehen?“</td><td>Bild 9:16</td></tr>
<tr><th>AD05</th><td>Fragesticker</td><td>„Ich hab keine Kreditkarte. Kann ich deine Bilder trotzdem sehen?“</td><td>Bild 9:16</td></tr>
<tr><th>AD06</th><td>Fragesticker</td><td>Creatorin beantwortet die Frage im Video (Skript)</td><td>Video 9:16</td></tr>
</tbody></table></div>
<div class="detail-grid">
<div class="detail-card"><h3>Sieht aus wie ihre eigene Story</h3><p>Story-Textstil mit weißem oder schwarzem Balken, echte Sticker-Optik, Foto bildfüllend, <strong>kein MALOUM-Logo</strong>.</p></div>
<div class="detail-card"><h3>Die Bilder erstellen wir selbst</h3><p>Aus den Fotos der Creatorin. Nur die beiden Videos (AD03, AD06) dreht sie selbst, nach dem Skript.</p></div>
</div>
</section>

<section><h2>So sehen die sechs Ads aus</h2>
<p class="quiet">Skizzen zur Orientierung. Die gestrichelten Flächen sind Platzhalter für das echte Foto bzw. Video der Creatorin.</p>
<div class="phone-grid">{cards}</div>
</section>

<section><h2>Format 1: Neue Bilder</h2>
<p>Die Creatorin sagt einfach, dass sie neue Bilder gemacht hat, so wie sie es auch privat in ihrer Story posten würde.</p>
<div class="table-wrap"><table><thead><tr><th>Ad</th><th>Text im Bild</th><th>Primärtext</th><th>Headline</th></tr></thead><tbody>
<tr><th>AD01 Bild</th><td>Hab heute neue Bilder gemacht / Link unten</td><td>Meine neuesten Bilder findest du auf meinem Maloum-Profil. Anschauen kostet nichts.</td><td>Neue Bilder ansehen</td></tr>
<tr><th>AD02 Countdown-GIF</th><td>Timer läuft 8 s runter, dann: Meine neuen Bilder sind online</td><td>Meine neuesten Bilder sind online. Klick auf den Link, anschauen kostet nichts.</td><td>Jetzt ansehen</td></tr>
<tr><th>AD03 Video</th><td><a href="skripte.html">Skript Video 1</a></td><td>Hab neue Bilder gemacht, schau sie dir an. Anschauen kostet nichts.</td><td>Neue Bilder ansehen</td></tr>
</tbody></table></div>
</section>

<section><h2>Format 2: Fragesticker</h2>
<p>Die Creatorin teilt eine Frage aus ihrem Fragesticker und antwortet kurz. <strong>Die Fragen drehen sich nur um ihre Bilder und die Plattform, nie um Kontakt.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Ad</th><th>Frage im Sticker</th><th>Antwort im Bild</th><th>Headline</th></tr></thead><tbody>
<tr><th>AD04 Bild</th><td>Wo kann ich deine neuen Bilder sehen?</td><td>Meine neuesten Bilder findest du hier unten im Link.</td><td>Neue Bilder ansehen</td></tr>
<tr><th>AD05 Bild</th><td>Ich hab keine Kreditkarte. Kann ich deine Bilder trotzdem sehen?</td><td>Ja, klar. Klick einfach auf den Link, bezahlen geht auch mit PayPal.</td><td>Geht auch mit PayPal</td></tr>
<tr><th>AD06 Video</th><td>Wo kann ich deine neuen Bilder sehen?</td><td><a href="skripte.html">Skript Video 2</a></td><td>Neue Bilder ansehen</td></tr>
</tbody></table></div>
</section>

<section><h2>Varianten</h2>
<p>Gewinner laufen bei der Konkurrenz mit 8–14 Varianten und oft als Video. Deshalb: je Format drei Ads, eine davon als Video, und je Gewinner-Ad in der zweiten Woche <strong>4–6 Varianten mit anderem Foto oder anderer Frage</strong>.</p>
<div class="dd">
<div class="do"><h3>Rein</h3><ul>
<li>Neue Bilder, Plattform, Bezahlung („geht auch mit PayPal“, „anschauen kostet nichts“)</li>
<li>Story-Textstil, echte Sticker-Optik, Foto bildfüllend</li>
<li>Normale, gut aussehende Fotos: Gesicht bis Brust, Alltagskleidung</li>
</ul></div>
<div class="dont"><h3>Nicht rein</h3><ul>
<li>Chat- und Antwort-Versprechen: „schreib mir“, „privat“, „heute Abend“, „exklusiv für dich“</li>
<li>„nur die Hälfte“-Andeutungen</li>
<li>Altersangaben mit Schulbezug</li>
<li>Bad, Spiegel-Selfie, Bett, bauchfrei, tiefer Ausschnitt, Unterwäsche, Bademode, hochgezogene Trikots</li>
</ul></div>
</div>
<p class="fine">Grundlage: Eriks Analyse der 24 gesperrten Ads. 23 von 25 Sperrvermerken lauten „Adult Sexual Solicitation“.</p>
</section>
"""
page("ads.html", "So sehen die <em>Ads</em> aus.",
     "Zwei Formate, sechs Ads je Creatorin. Alle sehen aus wie eine Story, die die Creatorin selbst gepostet hat.",
     ads)

# ---------------------------------------------------------------- Skripte
skripte = """
<section><h2>Zwei Videos, ein Take, selbst gefilmt</h2>
<p>Es soll wirken wie eine ganz normale Story, nicht wie Werbung. Das Briefing unten geht so an jede Creatorin raus.</p>
<div class="table-wrap"><table><tbody>
<tr><th>Kunde</th><td>MALOUM</td></tr>
<tr><th>Creatorinnen</th><td>Stella, Leyla</td></tr>
<tr><th>Deliverables</th><td>2 kurze Videos: „Neue Bilder“ und „Fragesticker“</td></tr>
<tr><th>Stil</th><td>ein Take ohne Schnitt, selbst gefilmt, wie eine normale Instagram-Story</td></tr>
<tr><th>Länge</th><td>10–15 Sekunden</td></tr>
<tr><th>Format</th><td>Hochformat 9:16, Handykamera, 1080p oder 4K</td></tr>
<tr><th>Takes</th><td>je Video 2 komplette Takes, wir nehmen den besten</td></tr>
<tr><th>Abgabe bis</th><td><span class="tag yellow">offen</span> Datum eintragen</td></tr>
<tr><th>Postproduktion</th><td>Untertitel und Sticker machen wir, du lieferst nur das Rohvideo</td></tr>
</tbody></table></div>
<div class="notice"><strong>Das Ziel</strong><p>Deine Follower sollen wissen, wo sie deine neuen Bilder finden, dass Anschauen nichts kostet und dass man keine Kreditkarte braucht. Sag es in deinen eigenen Worten, es muss nicht wörtlich sein.</p></div>
</section>

<section><h2>Video 1: Neue Bilder</h2>
<div class="script"><h3>AD03 · Neue Bilder</h3><div class="meta">Video 9:16 · 10–15 Sek. · ein Take</div>
<blockquote><p>„Hey, ich hab heute neue Bilder gemacht! Meine neuesten Bilder findest du hier unten im Link. Und weil mich das viele fragen: Nein, dafür brauchst du keine Kreditkarte. Einfach draufklicken und anschauen, anschauen kostet nichts. Viel Spaß!“</p></blockquote></div>
</section>

<section><h2>Video 2: Fragesticker</h2>
<div class="script"><h3>AD06 · Fragesticker</h3><div class="meta">Video 9:16 · 10–15 Sek. · ein Take · Frage im Sticker setzen wir: „Wo kann ich deine neuen Bilder sehen?“</div>
<blockquote><p>„Meine neuesten Bilder findest du hier unten im Link. Und weil mich das auch viele fragen: Nein, dafür brauchst du keine Kreditkarte. Einfach draufklicken, anschauen kostet nichts. Viel Spaß!“</p></blockquote>
<p class="fine">Die Fragen drehen sich nur um die Plattform und deine Bilder, nie um Kontakt. Bitte keine eigenen Fragen wie „Kann ich dir schreiben?“ dazunehmen.</p></div>
</section>

<section><h2>No-Gos</h2>
<p>Die Videos laufen als Werbung bei Instagram und Facebook, Meta prüft jede Anzeige. Bitte deshalb nicht:</p>
<div class="table-wrap"><table><tbody>
<tr><th>Orte</th><td>kein Bad, kein Spiegel-Selfie, kein Bett oder Schlafzimmer</td></tr>
<tr><th>Outfit</th><td>nicht bauchfrei, kein tiefer Ausschnitt, keine Unterwäsche oder Bademode</td></tr>
<tr><th>Gesten</th><td>keine zweideutigen Posen, kein Kussmund, kein Zwinkern</td></tr>
<tr><th>Wörter</th><td>nicht „schreib mir“, „privat“, „heute Abend“ oder „exklusiv für dich“</td></tr>
<tr><th>Hintergrund</th><td>keine fremden Gesichter, keine Kennzeichen, keine Musik</td></tr>
</tbody></table></div>
</section>

<section><h2>Abgabe</h2>
<ul class="short-list">
<li><strong>2 Takes je Version als Originaldatei</strong> bis [Datum eintragen], per WeTransfer oder Google-Drive-Link. Nicht über WhatsApp oder Instagram, dort wird die Qualität schlechter.</li>
<li><strong>Dateinamen:</strong> Name_Video_Take, z. B. <code>Stella_NeueBilder_Take1.mov</code> oder <code>Leyla_Fragesticker_Take2.mov</code>.</li>
<li><strong>Video 1 „Neue Bilder“:</strong> 2 komplette Takes. <strong>Video 2 „Fragesticker“:</strong> 2 komplette Takes.</li>
<li>Alles im Hochformat, ohne Filter, ohne Musik. Fragen gehen jederzeit an Erik.</li>
</ul>
</section>
"""
page("skripte.html", "Video-Skripte für <em>Stella und Leyla.</em>",
     "Zwei kurze Videos, ein Take, selbst gefilmt. Mit Briefing, Skripten, No-Gos und Abgabe.",
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

<section><h2>Was die Langläufer für uns bedeuten</h2>
<p>Die Langläufer (Lucy 183 Tage, Rina 160 Tage, leoo.baut 97 Tage) bestätigen unseren Weg und bringen drei Ergänzungen:</p>
<div class="table-wrap"><table><thead><tr><th>Befund</th><th>Was wir daraus machen</th></tr></thead><tbody>
<tr><th>Alle Langläufer laufen über das Profil der Creatorin: eigener Name, Selfie, MALOUM nur als Link</th><td>Genau unser Creator-Ads-Prinzip. Technisch als <strong>Partnership Ad</strong>: Die Creatorin gibt in Instagram die Werbe-Freigabe, wir schalten über ihr Konto.</td></tr>
<tr><th>Der Fragesticker lief bei der Konkurrenz monatelang, bei MALOUM wurde er gesperrt. Unterschied: dort keine Chat-Versprechen</th><td>Fragesticker bleibt (Format 2). Fragen ohne Kontakt-Bezug.</td></tr>
<tr><th>Jede Langläuferin hat eine klare Persona (Dorfmädchen, Fitness, Gamerin) und fragt danach („Wer möchte mit mir zocken?“)</th><td>Nicht übernommen: Unsere Formate müssen für jede Creatorin mit einem Foto duplizierbar sein. Interaktion holen wir nur über den Fragesticker, der bei allen gleich funktioniert.</td></tr>
<tr><th>Gewinner laufen mit 8–14 Varianten und oft als Video</th><td>Je Format drei Ads, eine davon als Video; je Gewinner-Ad in der zweiten Woche 4–6 Varianten mit anderem Foto oder anderer Frage.</td></tr>
<tr><th>Rinas Langläufer: „exklusive Einblicke hinter den Kulissen“</th><td>Deckt sich mit Format 1 „Neue Bilder“.</td></tr>
</tbody></table></div>
</section>

<section><h2>Was wir übernehmen und was nicht</h2>
<div class="dd">
<div class="do"><h3>Übernehmen</h3><ul>
<li>Creatorin als Absender (Partnership Ads)</li>
<li>Fragesticker mit Fragen zu Look und Alltag</li>
<li>Kurze Videos, in denen die Creatorin selbst spricht</li>
<li>Ein gutes Format, viele Varianten</li>
</ul></div>
<div class="dont"><h3>Nicht übernehmen</h3><ul>
<li>Lucys „18 und geh noch zur Schule“. Bei Adult-Content rechtlich und ethisch tabu.</li>
<li>Chat- und Antwort-Versprechen: „Chatte jetzt mit mir“, „schreib mir zuerst“</li>
<li>„nur die Hälfte“-Andeutungen</li>
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
