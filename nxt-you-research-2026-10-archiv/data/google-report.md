# NXT YOU: Google Ads, Nachfrage und KI – strategischer Tiefenbericht

**Stand: 11.10.2026 · EUR · Europe/Berlin.** Produktionsdaten wurden aus den verifizierten Audits dieses Tages wiederverwendet; Marktdaten wurden für diesen Bericht frisch recherchiert. Dieser Auftrag ist ausschließlich read-only. Alle Maßnahmen unten sind Vorschläge, sofern nicht ausdrücklich als bereits in A umgesetzt bezeichnet.

**E1–E7: private unterstützende Originalbelege, nicht in öffentlichen Downloads enthalten.**

## 1. Entscheidung in einem Satz

**Nicht mehr Budget bereitstellen, um eine Ausgabenquote zu erfüllen. Zuerst Messung und Angebotsklarheit herstellen, dann gezielt kaufbereite Nachfrage gewinnen und nur nach nachgewiesener Wirtschaftlichkeit skalieren.** Der Markt verschwindet nicht; er ist jedoch deutlich selektiver, und KI verschiebt, wofür Käufer Geld ausgeben. Die konkret geringe NXT-Auslieferung ist durch Rangbegrenzung bei freien Budgets belegt – nicht durch einen nachgewiesenen KI-bedingten Nachfrageeinbruch.

### Die fünf wichtigsten Antworten

1. **Warum wird so wenig ausgegeben?** Aktuell sind 360 €/Tag eingestellt, nicht 350 €: Exact 120 €, Prospecting 240 €. Vom 01.–10.10. wurden 1.104,16 € ausgegeben, also 110,42 €/Tag und 30,67 % der rechnerischen Tagesfreigabe. Beide Kampagnen verlieren im Oktober 0 % Impression Share wegen Budget, aber 75,43 % beziehungsweise 88,85 % wegen Rang. Gebotsgrenzen und Qualität sind plausible Hebel; die genaue Aufteilung ist nicht identifiziert. (E1, E3)
2. **Hat die neue Landingpage den Anzeigenrang zerstört?** Nicht pauschal. Im gleich langen September-Vergleich verbessert sich Exact beim Search Impression Share; Prospecting bekommt mehr Klicks bei niedrigerem CPC. Gleichzeitig brechen gemessene Conversions ein. Einzelne historische QS-Komponenten verschlechtern sich tatsächlich, aber ein kausaler LP-Gesamteffekt ist nicht bewiesen. (E2)
3. **Ist nur Tracking schuld?** Nein, auch das ist nicht belegt. Tracking hat konkrete Mängel. Zusätzlich sinken in den gespeicherten Google-Leadkohorten die echten Leads von elf auf sieben und die A/B-Leads von sieben auf zwei. Die Qualitätsbewertung ist allerdings teilweise buchungsabhängig. Messfehler und reales kommerzielles Problem können gleichzeitig vorliegen. (E3, E4)
4. **Wird der Markt schlechter?** Teilweise ja: Der deutsche Mittelstand hat seine Digitalisierungsausgaben 2024 reduziert, die Breite der Startup-Finanzierung bleibt schwach und die Schweizer IT-Services-Stimmung fällt für Q4 2026 unter die Wachstumsgrenze.[4][11][12]

   Gleichzeitig prognostiziert Bitkom für 2026 wachsende Software- und IT-Service-Umsätze.[1] Das ist ein selektiver Markt, kein genereller Zusammenbruch.
5. **Was ändert KI?** Die belastbare Evidenz zeigt steigende Nutzung und Ausgaben sowie Kompetenz-, Integrations- und Datenschutzprobleme. Sie beweist nicht, dass KI NXT-Leads vernichtet. NXT sollte deshalb nicht nur „wir programmieren eine App“ verkaufen, sondern belastbare Produktentscheidungen, Integration und produktionsfähige Umsetzung – mit messbarem Geschäftsnutzen. Der letzte Satz ist eine strategische Ableitung, keine gemessene NXT-Erfolgsprognose.[3][5][8]

## 2. Status: Was ist geändert, was nicht?

| Paket | Verifizierter Stand | Was ausdrücklich nicht bewiesen ist |
|---|---|---|
| A: Anzeigen/Negatives | Zwei zusätzliche RSAs 827649794599 und 827649794602 in Gruppe 176710794896 gespeichert und zurückgelesen; sechs eng begrenzte Exact-Negatives angelegt | Anzeigenfreigabe, reale Auslieferung und Qualitäts-/Lead-Uplift der neuen Anzeigen; beim Readback noch PENDING/REVIEW_IN_PROGRESS |
| B: Messung/Consent | Vorbereitete Code-Artefakte; 15/15 isolierte lokale Tests bestanden | **Nicht live repariert.** Kein verifizierter GTM-Adminzugang, native Onepage-CMP nicht über verfügbare Schreibschemas bearbeitbar; kein End-to-End-Erfolg |
| C: Gebote | Keine Änderung angewendet | Kein Cap-, tCPA- oder Budgettest gestartet; C bleibt gesperrt |
| Angebot | Neue RSAs verzichten auf Preiszahl und grenzen Prototyp von fertiger App ab | Preiswiderspruch ungelöst: bestehende Anzeigen „Festpreis ab 5.000 €“, live Landingpage 6.400 € für Founders Sprint |

Quelle: E6/E7. Alle 47 bestehenden Anzeigen und 116 Positivkeyword-Zeilen blieben bei A in den geprüften Konfigurationsfeldern unverändert. Die beiden neuen Anzeigen liegen in derselben gemischten Gruppe: **kein getrenntes Keyword-Routing und kein randomisiertes Experiment.** Die sechs Negatives betreffen 82,34 € beobachteten historischen Spend, keinen prognostizierten Sparbetrag.

**Konsequenz:** Dieser Bericht darf weder „Tracking repariert“ noch „Skalierung freigegeben“ suggerieren. Ein abgeschlossener lokaler Codetest ist kein Produktionsnachweis.

## 3. Vorher–nachher: Was hat sich tatsächlich verändert?

### 3.1 Sauberer Fenstervergleich

**Vorher 04.–31.08.2026, nachher 01.–28.09.2026:** je 28 vollständige Tage, gleiche Wochentagsverteilung; Nachfenster mit zwölf vollen Puffertagen bis 10.10. Die aktuelle Ziel-URL `/app-entwickeln-lassen` ist ab 01.09. erstmals im gespeicherten täglichen Landing-Delivery-Report nachweisbar. Das datiert ihre erste beobachtete Auslieferung, nicht alle Websiteversionen. Das Vorfenster enthält bereits August-Funneländerungen. (E1/E2)

| Kampagne/Fenster | Spend | Impressionen | Klicks | CPC | Ads-Conv. | CPA | Search IS | Rangverlust | Budgetverlust |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Exact vorher | 421,82 € | 336 | 31 | 13,61 € | 5 | 84,36 € | 41,00 % | 59,00 % | 0,00 % |
| Exact nachher | 584,05 € | 447 | 43 | 13,58 € | 0 | n. a. | 56,56 % | 40,43 % | 3,01 % |
| Prospecting vorher | 3.202,60 € | 8.073 | 449 | 7,13 € | 15 | 213,51 € | <10 % | 80,60 % | 9,94 % |
| Prospecting nachher | 3.278,57 € | 10.851 | 506 | 6,48 € | 6 | 546,43 € | 11,73 % | 84,99 % | 3,28 % |
| **Gesamt vorher** | **3.624,42 €** | **8.409** | **480** | **7,55 €** | **20** | **181,22 €** | — | — | — |
| **Gesamt nachher** | **3.862,62 €** | **11.298** | **549** | **7,04 €** | **6** | **643,77 €** | — | — | — |

**Rechnerisch:** Spend +6,57 %, Klicks +14,38 %, CPC −6,82 %, gemessene Conversions −70,00 %, CPA +255,24 %. Klick-zu-Ads-Conversion sinkt von 4,17 % auf 1,09 % (−73,77 % relativ). Der zentrale Effizienzverlust liegt in der **gemessenen Conversionrate**, nicht in einem CPC-Anstieg. Berechnet aus ungerundeten Exportwerten, siehe `calculations-qa.json`.

Das heißt nicht, dass jede Conversionrate ein reines Landingpage-Ergebnis ist: Eventdefinition, Attribution, Kontaktmix, Buchungsroute und kommerzielle Qualität wirken mit. Nur sechs Nachher-Conversions und 43 Exact-Klicks sind eine dünne Basis. Die Budgetverdoppelung am 14.09. und die historische Primärstellung des Lead-Submit-Ziels am 13.08. verhindern einen kontrollierten LP-Kausalvergleich. (E1/E2)

### 3.2 Nicht alle Zeitfenster erzählen dieselbe Geschichte

| Vergleich | Spend vorher → nachher | Ads-Conv. | CPA | Bedeutung |
|---|---:|---:|---:|---|
| 09.08.–05.09. → 06.09.–03.10.; jüngstes Fenster mit sieben vollen Puffertagen | 2.731,97 → 4.372,42 € | 20 → 7 | 136,60 → 624,63 € | Jüngere Schwäche in der gemessenen Conversionrate bei annähernd stabilem CPC |
| 17.07.–13.08. → 14.08.–10.09.; mindestens 30 volle Puffertage | 6.799,86 → 1.974,70 € | 10 → 17 | 679,99 → 116,16 € | Kein durchgehender Niedergang direkt ab August-Migration |

Quelle E1. Historische Lag-Abfrage 01.07.–10.09.: 30 von 32 primären Conversions unter einem Tag, zwei im Bucket ONE_TO_TWO_DAYS. Diese Stichprobe beschreibt historische Plattformereignisse, nicht den Vertriebszyklus. Nachlaufpuffer garantieren weder endgültige Attribution noch technisch korrekt definierte Events.

### 3.3 Monatsverlauf als Kontext, nicht als Experiment

| Monat 2026 | Spend | Klicks | Google-Ads-Conversions | CPA |
|---|---:|---:|---:|---:|
| Januar | 5.714,91 € | 808 | 21 | 272,14 € |
| Februar | 6.358,17 € | 992 | 22 | 289,01 € |
| März | 7.635,75 € | 1.098 | 32 | 238,62 € |
| April | 2.618,62 € | 374 | 11 | 238,06 € |
| Mai | 5.590,65 € | 715 | 29 | 192,78 € |
| Juni | 5.968,12 € | 757 | 22 | 271,28 € |
| Juli | 6.468,52 € | 676 | 11 | 588,05 € |
| August | 4.752,28 € | 548 | 21 | 226,30 € |
| September | 4.101,82 € | 584 | 6 | 683,64 € |
| Oktober 01.–10. | 1.104,16 € | 186 | 3 | 368,05 € |

Quelle E1, unabhängig gegen Account-Monatsabfrage geprüft. Der Oktober-CPA ist weder ein qualifizierter Leadpreis noch Entwarnung: drei Ads-Ereignisse, keine zehn abgeschlossenen Verkaufskohorten. Die monatlichen Ereignisdefinitionen sind historisch nicht ohne Einschränkung vergleichbar.

## 4. Warum die 360 € Tagesbudget nicht ausgegeben werden

### 4.1 Die operative Diagnose

| Ebene | Beobachtet | Interpretation | Nächster Nachweis |
|---|---|---|---|
| Budget | Exact 120 €, Prospecting 240 €; am 14.09. von 60/120 € verdoppelt | Die heutige Freigabe ist nicht knapp | Kein weiterer Budgetanstieg ohne tatsächliche Budgetlimitierung und Wirtschaftlichkeit |
| Auktion | 01.–10.10. Exact 75,43 %, Prospecting 88,85 % rank lost IS; budget lost IS jeweils 0 % | Viele berechtigte Auktionen werden wegen Rang nicht gewonnen | Periodenmetriken, Suchmix und Wirtschaftlichkeit nach einem isolierten Test vergleichen |
| Gebote | Beide Portfolio-tCPA 400 €; CPC-Caps 25 € Exact / 15 € Prospecting | Caps können teurere sinnvolle Auktionen ausschließen; tCPA kann bei schwachem erwarteten Signal defensiv wirken | Cap-Effekt unbekannt, nicht aus durchschnittlichem CPC ableitbar |
| Qualität | Gemischte Diagnose; einige Keywords mit Relevanz- oder LP-Schwäche | Kein einheitlicher Qualitätskollaps | Komponenten je stabiler Keyword-ID und echte Leadqualität |
| Status | Kampagnen LIMITED/UNKNOWN; Exact zusätzlich HAS_ADS_DISAPPROVED | UNKNOWN nicht als konkreten Fehler übersetzen | Fünf vorher aktive Anzeigen waren APPROVED; zwei neue noch in Prüfung |
| Marktnachfrage | Kein marktweiter, konstant abgegrenzter Suchvolumenverlauf erhoben | Niedriger Spend ist kein Beweis für weniger Menschen mit Bedarf | Keyword-Planner-Zeitreihe, konstante Geo-/Intentdefinition und Auktionsvergleich separat erheben |

Quellen E1/E2/E6. Am 04.–10.10. gab Exact 53,36 €, Prospecting 701,27 € aus: insgesamt 754,63 € und 107,80 €/Tag. Dies ist ein anderes Fenster als 01.–10.10.; die Beträge dürfen nicht vermischt werden.

### 4.2 QS ist nicht Ad Rank

Google bezeichnet den Qualitätsfaktor 1–10 als **Diagnoseinstrument**, nicht als direkten Auktionsinput oder zu optimierende Geschäfts-KPI. Er fasst erwartete CTR, Anzeigenrelevanz und Landingpage-Erfahrung zusammen.[13] Der auktionsabhängige Ad Rank berücksichtigt unter anderem Gebot, aktuelle Qualität, Schwellen, Wettbewerb, Suchkontext und erwartete Assetwirkung.[14]

Deshalb gelten folgende Grenzen:
- Niedriger CPC widerlegt keine bindende CPC-Obergrenze: teurere potenzielle Auktionen können vor einem gewonnenen Klick ausscheiden.
- Rank lost IS ist kein durchschnittlicher Rangplatz und keine isolierte Landingpage-Note.
- Tatsächliche CTR, erwartete CTR und Ad Strength sind verschiedene Größen.
- Die unten gezeigten QS-Mittel dienen ausschließlich dem historischen Diagnosevergleich, nicht einer neuen „QS-Ziel-KPI“.
- Die generische robots.txt-Sperre und noindex beweisen keine AdsBot-Sperre; der technische Audit fand keine explizite AdsBot-Sperre und erhielt mit den geprüften User-Agents HTTP 200. Ein echter Google-Crawl wurde damit nicht nachgewiesen. (E3)

## 5. Kampagnen- und Keywordstrategie: wirtschaftliche Priorität statt QS-Kosmetik

### 5.1 Das feste historische Keywordpanel

18 identische Kombinationen aus Adgroup- und Criterion-ID haben in beiden Fenstern historische QS-Impressionen. QS-Abdeckung: vorher 2.903/8.409 Impressionen (34,52 %), nachher 4.283/11.298 (37,91 %). Die meisten Kontoimpressionen liegen damit außerhalb dieser Diagnoseabdeckung. (E2)

- Trafficgewichteter QS der jeweils beobachteten Population: 6,29 → 6,42.
- Mittel der 18 keywordweisen gewichteten QS: 5,35 → 4,86.
- Mittel der keywordweisen BELOW-Anteile bei LP-Erfahrung: 22,22 → 32,63 %.

Der erste Wert kann steigen, obwohl dieselben Keywords schlechter werden: Die Population und Gewichte verändern sich. Umgekehrt behandelt der Panelmittelwert kleine und große Keywords gleich. Fehlender QS ist unbekannt, nicht null. **Die vollständigen Kosten aller gelieferten Keywords bleiben der wirtschaftliche Nenner.**

| Keyword / stabile ID | Spend vorher → nachher | Conv. | QS | Diagnose und Entscheidung |
|---|---:|---:|---:|---|
| `app entwickler` Broad · 176710794896~15283592336 | Nachher 1.789,25 € | Nachher 2 | Nicht im gemeinsamen Panel | 275 Klicks, CPA 894,62 €; rund 46,32 % des gesamten Nachher-Spends. Höchste Priorität: echte Suchintention und CRM-Ergebnisse prüfen, nicht wegen fehlendem QS ignorieren |
| `app entwickler finden` · 176710794936~297107142146 | 428,37 → 431,01 € | 3 → 0 | 6,85 → 7 | Keine der drei Komponenten BELOW. QS 7 ist keine Wirtschaftlichkeitsgarantie; Käufer-/Recherche-Mix und Nachkontakt prüfen |
| `app bauen lassen` · 176710794896~297402262529 | 315,37 → 471,69 € | 0 → 3 | 6 → 6 | Anzeigenrelevanz bei 100 % seiner QS-Impressionen BELOW. Passende Copy testen; nicht blind pausieren |
| `prototyp erstellen lassen` · 176710794896~1635983349281 | 234,60 → 114,13 € | 2 → 0 | 5 → 5,48 | LP-Erfahrung durchgehend BELOW; klickbarer App-Prototyp, nicht physischer Prototyp oder fertige Software, muss sichtbar sein |
| `app entwickeln lassen` · 167460505095~295367505740 | 112,55 → 149,47 € | 4 → 0 | 7 → 7 | Gute Diagnose ersetzt keinen Conversion-/Leadnachweis; Exact mit nur wenig Volumen nicht voreilig verwerfen |
| `app entwicklung` · 167460505095~295367506500 | 34,44 → 134,20 € | 0 → 0 | 5 → 4,89 | Erwartete CTR durchgehend BELOW; kaufbezogene Differenzierung statt generischer App-Copy |
| `app agentur` · 167460505095~304860037816 | 41,35 → 83,09 € | 0 → 0 | 7 → 5 | Erwartete CTR kippt auf BELOW, LP nicht BELOW; zunächst Anzeige/Intent statt Komplettumbau |
| `web app entwicklung` · 176710794896~296813407573 | 56,82 → 25,10 € | 0 → 0 | 4 → 2 | LP BELOW von 0 auf 100 %, nur 27 → 58 QS-Impressionen; spezifischer Web-App-Nachweis, aber geringe wirtschaftliche Priorität |
| `software entwickeln lassen` · 176710794896~7005106381 | 68,57 → 0 € | 2 → 0 | 3 → 1,36 | LP BELOW von 0 auf 81,82 %, 73 → 33 QS-Impressionen; niedriger QS ohne Nachherkosten ist nicht der große Spendhebel |

Quelle E2; alle übrigen gelieferten Keywords und die 36 Panel-Periodenzeilen liegen als CSV bei. Keine Keywordpausierung wird allein aus Nullconversions empfohlen.

### 5.2 Suchbegriffe: Was der sichtbare Ausschnitt hergibt

September: sichtbare Suchbegriffkosten 2.295,02 € von 4.101,82 € (55,95 %), sichtbare Klicks 306 von 584. Oktober 01.–10.: 565,47 € von 1.104,16 € (51,21 %), 92 von 186 Klicks. Prospecting allein hat 52,41 % beziehungsweise 47,93 % Kostenabdeckung. Das ist **keine vollständige Suchnachfragepopulation**. (E6)

Bereits umgesetzt wurden ausschließlich sechs beobachtete Exact-Ausschlüsse in den jeweiligen Gruppen: `prototyp in china produzieren lassen`, `appstudio download`, `monaco editor react`, `kostenlose apps erstellen`, `kostenlose app erstellen`, `glideapps com sign up`. Kein pauschales Token wie „kostenlos“, „App“, „Entwickler“ oder „Prototyp“ wurde ausgeschlossen. Der Begriff `powerapp download` mit zwei gemeldeten Conversions blieb zunächst unangetastet; seine echte Qualität und die Eventkorrektheit sind nicht bewiesen. (E6)

**Weitere Entscheidungssystematik, noch nicht angewendet:**
1. Suchbegriffe nach Beauftragungsintention, DIY/Tool, Jobs/Ausbildung, physischem Prototyp und unklarem Bedarf klassifizieren; unbekannte Zeilen unbekannt lassen.
2. Erstquelle, Kampagne/Keywordreferenz und Leadqualität verbinden, soweit tatsächlich vorhanden. Keine deterministische Personen-zu-Suchbegriff-Zuordnung erfinden.
3. Eindeutige Fehlintention eng ausschließen; gemischte Intention mit spezifischer Copy/Formularqualifikation prüfen.
4. Erst bei reifer schlechter Wirtschaftlichkeit und ausreichender beobachteter Nachfrage Matchtype-Eingrenzung oder getrennten Intent-Test freigeben.
5. Broad nicht aus Prinzip verbieten, aber ohne sauberes Zielsignal auch nicht ausweiten. Automatische Empfehlungen zu Display Expansion, Search Partners oder Broad sind keine strategische Freigabe.

## 6. Messreife, Leadqualität und der tatsächliche Geschäftserfolg

### 6.1 Drei verschiedene Zahlenwelten

| Monat | Google-Rohformulare | Echte Google-Leads A/B/C | Davon A/B | Leads mit Buchung | Ads Submit + Booked | Google-Spend | CPL | CPQL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| August | 16 | 11 | 7 | 10 | 11 + 10 | 4.752,28 € | 432,03 € | 678,90 € |
| September | 8 | 7 | 2 | 1 | 5 + 1 | 4.101,82 € | 585,97 € | 2.050,91 € |
| Oktober bis Dashboard-Audit | 2 | 1 | 0 | 0 | 3 + 0 | 1.112,54 € | 1.112,54 € | n. a. |

Quelle E4. **Oktober hier enthält den partiellen 11.10. und einen anderen Abrufzeitpunkt**; deshalb nicht mit 1.104,16 € bis 10.10. gleichsetzen. Die monatlichen Rohformulare sind Ereigniszählungen, echte Leads deduplizierte Kohorten mit gespeicherter Quelle, Ads-Zahlen attribuierte Ereignisse. Eine Person kann Submit und Booking auslösen. Buchungen sind nicht bestätigte Teilnahme und können nach dem Kohortenmonat stattfinden.

Die effektive A/B-Quote der echten Google-Leads sinkt von 63,64 % auf 28,57 %. Die beiden September-A/B-Leads haben keine gematchte Buchung; der einzige gebuchte September-Google-Lead ist C. A/B ist jedoch heute wirksames Team-/Regelscoring, teilweise durch Buchung beeinflusst. Das ist nicht unabhängig von Terminmenge und kein historischer point-in-time Score. (E4)

**Kommerzielle Lücke:** Dieser Ads-/Marktbericht belegt keinen Umsatz, keinen kassierten Umsatz und keine realisierte Marge. Won-Opportunities, eindeutige Neukunden, Anzahlungen und Folgeaufträge müssen separat geprüft werden. Plattform-CPA 400 € ist daher kein belegter Break-even.

### 6.2 Die zwei unterschiedlichen Trackingbaustellen

**Website-/Funnelmessung:** Richtiger aktiver Container GTM-WL994WL und passende Ads-Labels sind vorhanden. Gleichzeitig setzt die native Initialisierung vor Bannerinteraktion vier Consentfelder auf granted. Das Lead-Ereignis hängt an einem öffentlich erreichbaren Kalender-Schrittaufruf statt einem bestätigten Backend-Erfolg. Für den direkten LP-Kalender ist keine gleichwertige Ads-Booked-Übersetzung im veröffentlichten Code erkennbar; ein externer/serverseitiger Weg bleibt unbestätigt. Kein kompletter Trackingausfall und keine konkrete Zahl verlorener Leads sind daraus bewiesen. (E3/E7)

**Alter Import:** Separat meldet GOOGLE_ADS_WEB_CLIENT EXPIRED_EVENT, 68 fehlgeschlagene Events im jüngsten Summary: 60 für entfernte Action 6643357390 und acht für entfernte Action 6685208089, zuletzt 10.10.2026 00:50:42 Kontozeit. Die Summaries wiederholen 60+8 an mehreren Tagen. Das sind nicht 68 neue verlorene NXT-Leads und nicht sicher siebenmal verschiedene Datensätze. Die aktuellen Onepage-Actions sind nicht diese Importactions. Importplanung und Originalzeitpunkte prüfen; GTM-Neueinbau oder Budgeterhöhung beheben diesen alten Fensterfehler nicht. (E5)

### 6.3 Messreife als explizites Freigabegate

Messreife ist **nicht** „Tag vorhanden“ oder „Action ENABLED“, sondern ein überprüfter Vertrag:

| Stufe | Exakte Definition | Dedupe/Beleg | Rolle |
|---|---|---|---|
| Formularstart / CTA | Interaktion, kein Lead | Session-/Eventdiagnose | Sekundär, nicht als Geschäftserfolg optimieren |
| Lead erfolgreich | Server akzeptiert Formular, echte stabile Lead-ID, kein RPC-Fehler | Lead-ID, Testreadback im CRM | Mögliche frühe Optimierungsstufe, erst nach technischer Freigabe |
| Buchung | Calendly bestätigt tatsächlichen Termin | Invitee-ID, Kalenderreadback; Wiederholungen deduplizieren | Funnelstufe, nicht zusätzlich als eigener Kunde zählen |
| Qualifiziert | Budget/Finanzierung, Auftragstyp, Entscheidungskompetenz und Zeitbedarf geprüft | CRM-Status mit Zeitpunkt, Owner und Ablehnungsgrund | Zukünftiger wirtschaftsnäherer Import, zuerst sekundär validieren |
| Gespräch gehalten | Tatsächliche Teilnahme dokumentiert | Sales-Bestätigung, nicht bloß vergangener Kalendereintrag | Salesleistung und Qualität |
| Angebot | Konkreter Scope und Preis versandt | Opportunity-ID, Angebotsdatum | Pipeline, kein Umsatz |
| Won / bezahlt | Vertrag gewonnen / Zahlung erhalten getrennt | Won-Status, Vertragswert, Zahlungseingang | Kundengewinnung, Deckungsbeitrag, Cash |

**Gate B:** Consent init/accept/reject/revoke/reload, alle Buchungswege, Formularfehler, Reload/Doppelcallbacks, eindeutige IDs, Click-ID-/UTM-Persistenz und kontrollierter CRM-/Kalenderreadback müssen bestanden sein. Native CMP- und GTM-Zugänge fehlen derzeit. Erst nach technischen Vorarbeiten einen ausdrücklich freigegebenen echten Test ohne Anzeigenklick und ohne Produktions-Bidding-Verunreinigung durchführen; nicht autonom Kalenderplätze anlegen. (E7)

**Gate Zielwechsel:** Nicht gleichzeitig Submit und Booking unreflektiert als gleichwertige Akquisition optimieren. Empfohlen ist mittelfristig eine führende wirtschaftliche Zielstufe je Kampagne. Ob zunächst korrektes Lead-Success oder später Qualified Lead geeignet ist, hängt von überprüfter Qualität, Menge und Verzögerung ab. Qualifizierungsimport zunächst sekundär parallel validieren; alte entfernte Qualified-Leads-Action nicht blind reaktivieren. Ein seltener sauberer Zielstatus kann wirtschaftsnäher sein, aber weniger Lernsignal liefern. Es gibt aus diesen Daten keine belegte universelle Mindestmenge für einen erfolgreichen Wechsel.

**Reife der Auswertung:** Technische Eventreife, 7-/30-Tage-Plattformnachlauf und 30-/60-/90-Tage-Vertriebskohorten sind getrennte Dinge. Reporting wöchentlich nach Akquisitionskohorte, monatlich nach Abschluss- und Zahlungsmonat. Neue Kohorten dürfen nicht mit voll abgeschlossenen alten Kohorten auf Winrate verglichen werden.

## 7. Deutschland/DACH: Wie viel ist Markt, wie viel Konto?

### 7.1 Belastbare Marktbelege, jeweils mit richtiger Zeitachse

| Quelle / Veröffentlichung | Gemessen oder prognostiziert | Exakter Befund | Was daraus nicht folgt |
|---|---|---|---|
| Bitkom, 07.07.2026 | **Prognose Gesamtjahr 2026** | ITK 246,4 Mrd. €, +4,1 %; IT 170,8 Mrd. €, +5,4 %; Software 58,1 Mrd. €, +9,9 %; IT-Services +3,1 % | Kein Ist-Wachstum von NXT-Projekten, keine Zahl externer App-Aufträge.[1][6] |
| Bitkom, 22.01.2026 | Frühere Prognose | Damals ITK 245,1 Mrd. €, +4,4 %; Software 58,3 Mrd. €, +10,2 % | Nicht mit Juli-Werten mischen. Höheres späteres Volumen bei niedrigerer Wachstumsrate kann mit veränderter Basis zusammenfallen; keine pauschale Nachfragereduktion daraus errechnen.[2] |
| KfW-Digitalisierungsbericht 2025, veröffentlicht April 2026 | Rückblick: Projektabschlüsse 2022–2024; Ausgabenjahr 2024 | Anteil Mittelständler mit abgeschlossenen Digitalisierungsvorhaben 30 %, −5 Prozentpunkte; 2024 Ausgaben 23,8 Mrd. €, −8,1 Mrd. € in laufenden Preisen | **Kein 2026-Istwert.** Digitalisierungsausgaben sind breiter als externe Software-Agenturhonorare.[4] |
| KfW VC Q3 2026, Datenstand 01.10.2026 | Beobachtete/revisionsfähige Finanzierungsrunden | Q3 rund 4,5 Mrd. €; sechs Megadeals vereinen rund 3,5 Mrd. €. Nur 89 Runden mit berichtetem Volumen ab 1 Mio. €; YTD 276 statt 304 im Vorjahreszeitraum | Rekordvolumen heißt nicht breite Gründerliquidität; 89 ist nicht die Gesamtzahl sämtlicher Deals.[12] |
| Destatis, Ergebnisse 2025, am 11.10.2026 abgerufen | Amtliche Unternehmensbefragung | 26 % nutzen KI; 23 % bei 10–49, 36 % bei 50–249, 57 % ab 250 Beschäftigten. Ergebnisse der Erhebung 2026 erst für November/Dezember angekündigt | Keine Gleichsetzung mit Anteil beauftragter Agenturen oder 2026-Adoption.[5] |
| Statistik Austria, 24.06.2026 | Berichtszeitraum erstes Halbjahr 2025, Unternehmen ab zehn Beschäftigten, definierte Wirtschaftszweige | Österreich 30 % KI-Nutzung, EU-27 20 %, Deutschland 26 % | Kein Vollmarkt inklusive Soloselbstständiger; keine österreichische Agenturumsatzprognose.[8] |
| Swico, 28.09.2026 | Befragung Juli–September, Erwartungsindex Q4 2026 | ICT 104,0 Punkte (−5,5); Software 104,7; IT-Services 98,9; verzögerte Projektentscheide | Indexpunkte sind keine Umsatzprozente. Kein realisierter Q4-Umsatz.[11] |
| Bitkom/IDC, 22.09.2026 | Prognose KI-Ausgaben 2026/2027 | KI-Markt 2026 28,7 Mrd. €, +48 %; KI-Dienstleistungen 6,8 Mrd. €, +30 %; 2027 Gesamtmarkt 40,3 Mrd. € erwartet | KI-Gesamtmarkt umfasst Software, Services und Hardware; nicht zusätzlich zum IT-Markt addieren und nicht mit KI-Plattformen gleichsetzen.[3] |

**Gesamturteil:** Es ist gut begründbar, dass Anbieter trotz wachsender Digitalumsätze vorsichtigere Käufer und schwerere Freigaben erleben. Softwareumsätze können durch Cloudprodukte wachsen, während individuelle Gründungsprojekte verschoben werden. Für Deutschland liefert KfW einen historischen Mittelstands-Dämpfer; für die Schweiz zeigt der aktuelle Swico-Index konkrete Investitionszurückhaltung. Für Österreich ist KI-Adoption belegt, nicht ein gleichwertiger aktueller Agenturnachfrageindex. Diese unterschiedliche Beweisdichte bleibt sichtbar.[1][4][11]

### 7.2 Funding: Für Gründerangebote ist die Verteilung wichtiger als die Schlagzeile

Der jüngste KfW-Bericht weist im Q3 2026 73 % des Dealvolumens der Scale-up-Phase zu; Seed liegt bei 227 Mio. €. Die 89 Runden ab 1 Mio. € unterscheiden sich von den 140 insgesamt im Appendix erfassten Deals. AI ist eine branchenübergreifende Zuordnung: 61 AI-Finanzierungsrunden und rund 3,1 Mrd. € in Q3 dürfen nicht zu den Gesamtdeals addiert werden.[12]

**Strategische Konsequenz:** Ein Founder-Sprint sollte Finanzierungsfähigkeit und konkreten Validierungszweck abfragen. „Hat eine Idee“ und „kann Scope plus Folgeentwicklung finanzieren“ sind nicht dieselbe Käufergruppe. Fördermittel, Investorensuche und zukünftiger Umsatz dürfen nicht als bereits verfügbares Projektbudget behandelt werden. Das ist ein Qualifikationsvorschlag, keine Behauptung über einzelne NXT-Leads.

### 7.3 Drei Ebenen, drei verschiedene Fragen

| Ebene | Geeignete Frage | Vorliegende Evidenz | Fehlende Evidenz |
|---|---|---|---|
| Gesamtmarkt | Wird insgesamt mehr für Digitalisierung/Software ausgegeben? | Offizielle Befragungen, Branchenprognosen, Finanzierungsdaten | Exakter adressierbarer Markt für NXT-Sprints und Custom-App-Aufträge |
| Suchauktion | Wie viel passende kaufbereite Suche können wir wirtschaftlich gewinnen? | NXT-Impressionen, Kosten, rank/budget lost IS, sichtbare Suchbegriffe | Konstanter Keyword-Planner-Zeitverlauf, vollständige Suchbegriffe, belastbarer Wettbewerbertrend |
| NXT-Funnel | Werden Besucher zu finanzierungsfähigen Kunden? | Rohformulare, deduplizierte Leads, effektive Scores, Buchungen, Messkonfiguration | Verifizierte Teilnahme, lückenloser Opportunity-/Zahlungs-/Margenjoin, produktionsverifizierte Messung |

Eine wachsende Softwarebranche beweist keinen funktionierenden NXT-Funnel. Umgekehrt beweist ein schwacher NXT-September keinen schrumpfenden DACH-Softwaremarkt. Es liegen keine Daten vor, die den Anteil von KI, Konjunktur oder Websiteänderungen am Rückgang kausal zerlegen.

## 8. KI: Risiko und Nachfragechance ohne erfundene Kausalität

### 8.1 Was die Daten tatsächlich tragen

Bei deutschen Nichtnutzern, die KI bereits erwogen haben, nennt Destatis fehlendes Wissen (72 %), rechtliche Unsicherheit (62 %), Datenschutz/Privatsphäre (60 %), Inkompatibilität (45 %), Datenverfügbarkeit/-qualität (44 %) und Kosten (32 %) als Gründe gegen den Einsatz. **Der Nenner sind nicht alle Unternehmen.**[5]

In Österreich haben 77 % der Nichtnutzer KI noch nicht erwogen. Die österreichischen Tabellenprozente zu Hemmnissen beziehen sich auf alle Nichtnutzer und sind deshalb nicht direkt mit den deutschen 72/62/60-Prozent-Werten vergleichbar.[8]

Bitkom beschreibt strukturelle Veränderungen von Entwicklungsprozessen, Produkten und Geschäftsmodellen in einem Positionspapier. Das ist eine Branchenanalyse, kein kausaler Nachweis einer bestimmten Produktivitätssteigerung oder eines Umsatzverlusts für Agenturen.[10]

### 8.2 Arbeitshypothesen für NXT – ausdrücklich zu testen

| Hypothese | Risiko/Chance | Wie NXT sie prüft |
|---|---|---|
| Einfache Demo-/Prototyparbeit wird stärker mit DIY-KI verglichen | Erklärungsbedarf für einen bezahlten Sprint steigt | In gewonnenen/verlorenen Gesprächen nach Eigenbau, Alternativen, Budget und Kaufgrund fragen; nicht aus Keywords allein ableiten |
| KI senkt bei manchen Aufgaben internen Aufwand | Marge kann steigen, Preisvergleich kann härter werden | Zeit/QA/Nacharbeit je realem Deliverable erfassen; keine pauschalen „80 % günstiger“-Versprechen |
| Bestehende Unternehmen brauchen Integration statt isolierter Demo | Anschlussgeschäft über Daten, Rechte, Schnittstellen, Betrieb | Einen klar abgegrenzten Integrations-Use-Case mit vorheriger Prozesskennzahl und Akzeptanztest pilotieren |
| Käufer verlangen wirtschaftlichen Nachweis vor Vollprojekt | Kleiner bezahlter Discovery-/Machbarkeitsauftrag kann Freigabe erleichtern | Angebot mit Entscheidung, Risiken, Scope und Business Case; Übergangsquote zur Umsetzung kohortenbasiert messen |
| KI-gebauter Prototyp ist noch keine produktionsfähige Software | Chance für Review, Härtung und Übernahme | Code-/Architektur-Audit mit eindeutigem Scope; Nachfrage erst mit Kundeninterviews und kleinem Intent-Test validieren |

### 8.3 Angebotsarchitektur für die nächsten Monate

**Nicht einfach „KI-Agentur“ auf die bestehende Seite schreiben.** Drei klar voneinander abgegrenzte Wege sind als Angebotsstrategie plausibel:

1. **Founder / App-Idee:** Entscheidungs- und Prototyp-Sprint. Lieferumfang: klickbarer Prototyp, UI/UX, dokumentierter Scope und Umsetzungsplan – nur soweit wirklich lieferbar. Kein fertiger App-Bau zum Sprintpreis. Qualifikation: Zielnutzer, Nachfragevalidierung, Budget für Sprint und folgende Entwicklung.
2. **Bestehendes Unternehmen:** Web-App / interner Prozess / Integration. Käuferproblem, vorhandene Systeme, Datenverantwortung, Sicherheitsanforderungen, messbares Ergebnis und Betriebsverantwortung vor Technologie stellen. Ein konkreter, belegbarer Referenzfall ist mehr wert als beliebige Technologie-Logos.
3. **KI-Prototyp zur Produktion:** Review und Härtung als neues Pilotangebot, erst nach Leistungs-/Kapazitätsfreigabe. Eigentum am Code, Tests, Authentifizierung, Integrationen, Datenverarbeitung, Monitoring und Betriebsübergabe definieren; nicht garantieren, jeden fremden Prototyp retten zu können.

Priorität hat zunächst die Klarheit des bereits verkauften Angebots. Neue Produktlinien werden nicht gleichzeitig mit Messreparatur und Gebotsänderung breit beworben. Schweizer und österreichische Märkte nicht ungeprüft in die deutschen Kampagnen öffnen: lokale Nachfrage, Preis-/Währungsdarstellung, Referenzen, rechtliche Bedingungen und vertriebliche Kapazität separat prüfen. Der Audit belegt keine aktuell konfigurierte DACH-Gesamtabdeckung.

## 9. Preis und Wirtschaftlichkeit: Ein billiger Lead ist nicht das Ziel

### 9.1 Preis-/Scope-Konflikt sofort entscheiden

Der Offer-Owner muss festlegen, ob der gültige Sprintpreis 5.000 € oder 6.400 € ist und ob die Werte brutto/netto, Einstiegspreis oder fester Paketpreis sind. **Dieser Bericht entscheidet das nicht.** Die zwei neuen RSAs vermeiden Preisangaben; die alten Preisclaims sind trotzdem live im Bestand. Der Umfang von Sprint und separater Vollentwicklung muss in Anzeige, Hero, Paket, FAQ, Formular und Verkaufsgespräch konsistent sein. (E6)

Eine höhere transparente Preisschwelle kann weniger Anfragen erzeugen und dennoch wirtschaftlich besser sein. Umgekehrt ist eine hohe A/B-Quote wertlos, wenn Angebote nicht gekauft werden. Deshalb nicht auf maximale Leadzahl oder künstlich niedrigen CPL optimieren.

### 9.2 Die ökonomische Messkette

**Media-CAC = Spend / gewonnene Neukunden der reifen Akquisitionskohorte.** Voller CAC ergänzt zurechenbare Vertriebs- und Akquisitionskosten. Deckungsbeitrag berücksichtigt direkte Projektkosten; Vertragswert ist kein Deckungsbeitrag und keine Zahlung.

Für Szenarien gilt:

`P(Won je Lead) = P(qualifiziert|Lead) × P(gehalten|qualifiziert) × P(Angebot|gehalten) × P(Won|Angebot)`

`max. CPL vor weiteren Akquisitionskosten = erwarteter Deckungsbeitrag je Neukunde × P(Won je Lead)`

`max. CPQL = erwarteter Deckungsbeitrag × P(Won|qualifiziert)`

Die bedingten Raten müssen auf korrekt verbundenen IDs basieren. Personen, die eine Stufe überspringen, separat darstellen; nicht alle Wins durch eine unvollständige Teilstufe dividieren. Langfristigen Entwicklungs-/Retainerwert nur mit beobachteten Anschlussquoten, direkter Marge und realistischem Zeithorizont einrechnen.

### 9.3 Rechenbeispiel, ausdrücklich keine Prognose

**Annahmen in allen drei Fällen:** 3.000 € Media, CPL 300 €, damit zehn rechnerische Leads; beispielhafter Netto-Sprintpreis 6.400 €, direkte Deckungsbeitragsmarge 50 %, also 3.200 € vor Akquisitionskosten. Der Nettopreis und die Marge sind nicht verifiziert. Keine Folgeentwicklung, keine Fixkosten, keine Saleskosten und kein Zahlungsausfall eingerechnet.

| Szenario | Qualifiziert/Lead | Gehalten/qualifiziert | Angebot/gehalten | Won/Angebot | Won/Lead | Erwartungswert Wins | Media-CAC | Max. CPL bei 3.200 € DB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Vorsichtig | 30 % | 50 % | 60 % | 20 % | 1,80 % | 0,18 | 16.666,67 € | 57,60 € |
| Arbeitsfall | 50 % | 70 % | 70 % | 25 % | 6,125 % | 0,6125 | 4.897,96 € | 196,00 € |
| Stark | 65 % | 80 % | 80 % | 30 % | 12,48 % | 1,248 | 2.403,85 € | 399,36 € |

Bruchteile sind mathematische Erwartungswerte, keine vorhergesagten Teilkunden. Bei nur zehn Leads können reale Ergebnisse stark abweichen. Bei alternativ angenommenen 5.000 € netto und gleicher Marge sinkt der erlaubte CPL auf 45,00 / 153,13 / 312,00 €. Die CSV enthält alle Annahmen und Formeln sind in `calculations-qa.json` geprüft.

**Entscheidender Punkt:** Selbst 300 € CPL wäre im Arbeitsfall für das isolierte Sprintgeschäft nicht tragfähig, bevor Saleskosten berücksichtigt werden. Der tCPA von 400 € zählt aktuell Plattformereignisse, nicht diese deduplizierten Leads. Die Zahlen dürfen deshalb nicht direkt gegeneinander als identische Kennzahlen bewertet werden.

## 10. 30/60/90 Tage: konkrete Maßnahmen mit Freigaben und Stopps

Zeitangaben sind Planung ab Startfreigabe, keine Zusage, dass fehlende Zugänge oder geringe Fallzahlen innerhalb von 90 Tagen gelöst sind. Gates haben Vorrang vor Kalenderdaten.

### Tage 0–30: Messung, Angebot und Baseline

| Arbeitspaket / Owner | Konkrete Tätigkeit | Abnahme | Stopp-/Rückfallregel |
|---|---|---|---|
| Offer-Owner | Gültigen Preis, Steuerdarstellung, Scope und Folgeentwicklung entscheiden; bestehende Preisclaims und LP konsolidieren | Schriftlich freigegebene gemeinsame Offerdefinition; kein Widerspruch im aktiven Bestand | Keine neuen Preisversprechen ohne Entscheidung |
| Tracking-Owner | Autorisierten GTM- und Builder-Zugang beschaffen; Draft-/Workspace-Backups; CMP und Eventbridge gemeinsam integrieren | Vollständige B-Testmatrix einschließlich Backend-/Kalenderreadback und Consent bestanden | Bei fehlendem Zugriff B weiter BLOCKED; kein später Custom-Code-Workaround als echte Consent-Reparatur ausgeben |
| Ads-Owner | Neue RSAs auf Prüfstatus/Delivery kontrollieren, Intent- und Suchbegriffreview nach Kosten; A nicht blind nochmals erstellen | Readback der exakten IDs, sichtbare Coverage, versioniertes Änderungslog | Keine QS-/Leadwirkung aus reiner Freigabe ableiten |
| Import-Owner | Wiederkehrenden alten Import mit EXPIRED_EVENT lokalisieren | Originalzeilen, Click-/Eventzeitpunkte und Quelle identifiziert; nach autorisierter Korrektur nächster Import geprüft | Keine Zeitstempel auf heute umschreiben; keine anderen Website-Actions abschalten |
| Sales-Owner | Einheitliche Stufen, tatsächliche Teilnahme, Ablehnungsgründe und zuständigen Bearbeiter erfassen | Jede neue Anfrage hat Quelle, Kohorte, Bearbeitungsstatus und nächste Aktion; fehlende Daten als unbekannt | Keine alten Leads automatisiert besser scoren, um Kennzahlen zu verbessern |
| Reporting-Owner | Rohereignisse, eindeutige Leads, Qualifikation und Umsatzdefinitionen trennen | Wöchentlicher Export mit ursprünglicher Quelle und Monatsdatum; Google/Meta-Duplikatproblem nicht wiederholen | Keine undatierten Definitionen als Conversionperformance importieren |

**Baseline erst nach der letzten relevanten A/B-/Offeränderung starten:** 14 vollständige stabile Tage. Änderungen am Zielsignal werden im Zeitverlauf markiert; alte und neue CPA-Definitionen nicht nahtlos vergleichen. Als Arbeits-SLA kann das Team beispielsweise eine erste persönliche Reaktion innerhalb eines Arbeitstags vereinbaren; das ist eine neue Zielvorgabe, keine gemessene bisherige Leistung.

### Tage 31–60: kontrollierte Nachfrage- und Gebotsprüfung

1. **Intent-Test fertig bewerten:** App-bauen-/Prototyp-Ansprache anhand tatsächlicher Suchbegriffe, Leads und Qualität prüfen. Eine Anzeige in gemischter Gruppe belegt kein exklusives Routing. Bei weiterer Strukturtrennung erst klare wirtschaftliche Hypothese, ausreichend Volumen und separate Freigabe.
2. **Gated C nur bei bestandenem B und wirtschaftlichem Limit:** Aktuelle Portfolios erneut lesen. Nur Prospecting-Cap 15,00 → 16,50 € als +10-%-Test erwägen; tCPA 400 €, Budget 240 €, Exact-Cap 25 € und Exact-Budget 120 € unverändert. Das ist eine vorsichtige Dosis, kein berechnetes Optimum. (E2/E6)
3. **Testdesign:** 14 vollständige Testtage plus mindestens sieben volle Conversion-Nachlauftage. Anzeigen, LP und Keywords währenddessen stabil lassen. Bei noch unreifen Verkaufsstufen Entscheidung vertagen. Sequentieller Test ohne Kontrollarm ist richtungsweisend, nicht kausal eindeutig.
4. **Vorab Risikolimit:** Nur als alte Planungsreferenz ergibt zweimal 701,27 € eine 14-Tage-Basis von 1.402,54 €; +20 % Review-Schwelle 1.683,05 €. Vor Start durch echte neue Baseline ersetzen und vom Owner freigeben. Manuelle Review-Schwelle, kein automatisch wirksames Systemlimit und keine Spendprognose.
5. **Täglich beobachten:** Messausfall, irrelevante Suche, Kosten, Formfehler; wöchentlich direkt abgefragter rank/budget lost IS, relevante Klicks, CPL/CPQL und CRM-Stufen. Höherer CPC allein ist kein Fehler, wenn die wirtschaftliche Qualität verbessert wird.
6. **Rollback:** Messausfall, eindeutiger Qualitätsverlust oder freigegebenes Kostenlimit überschritten → Test stoppen und autorisiert auf 15 € zurück. Kein messbarer Mehrwert bei reifer Auswertung → Baseline wiederherstellen oder begründet weiterprüfen, nicht automatisch dauerhaft höher bleiben. Bei dünner Stichprobe Ergebnis „unklar“.
7. **Parallel ohne Kampagnenmischung:** Kleine qualitative Kunden-/Lost-Deal-Analyse zu DIY/KI, Entscheidungskriterien und Budget. Neue Web-App-/Integrationspositionierung zunächst in Gesprächen und als freigegebene Angebotsunterlage testen, nicht sofort breit einkaufen.

### Tage 61–90: wirtschaftliche Skalierung oder kontrolliertes Redesign

| Ergebnislage | Entscheidung | Was nicht getan wird |
|---|---|---|
| Messung sauber, höhere qualifizierte Nachfrage, CAC/DB innerhalb freigegebener Grenzen | Eine weitere kleine isolierte Erweiterung: Gebot **oder** Intent **oder** Geografie; neues Limit und Baseline | Kein gleichzeitiges Hochfahren aller Hebel |
| Mehr Spend/Klicks, keine wirtschaftliche Verbesserung | C zurücknehmen; Suchintention/Offer/Sales entlang realer Stufen diagnostizieren | Mehr Budget nicht als Therapie für schlechte Abschlussökonomie |
| Hoher Form-CVR, schwache Qualifikation | Preis-/Scope-/Budgetfilter und Copy schärfen; irreversible Ausschlüsse nur evidenzbasiert | Nicht auf möglichst viele billige Formularstarts optimieren |
| Gute Qualifikation, geringe Teilnahme/Angebotsquote | Salesprozess, Terminführung, tatsächliche No-shows und Angebotsklarheit prüfen | Nicht automatisch Landingpage oder KI verantwortlich machen |
| Gute Angebote, schwache Winrate | Lost Reasons, Alternativen, Preis/Scope, Finanzierung und Entscheidungskompetenz untersuchen | Keine Preisreduktion ohne Margen-/Kaufgrundanalyse |
| Zu wenig reife Fälle | Test und Cohort-Readout mit genehmigtem Budget verlängern oder Hypothese verwerfen | Keine Signifikanz oder Marktprognose aus Einzelfällen |

**Mittelfristige Zielarchitektur:** Saubere frühe Events, sekundär validierter Qualifizierungsimport und schließlich ein wirtschaftsnäheres führendes Bidding-Ziel, sofern Volumen und Reife dafür reichen. Kein sofortiger Sprung auf Value-Bidding mit fiktiven 250-€-Buchungswerten. Bestehende Standardwerte sind keine gemessenen Deckungsbeiträge. (E3)

## 11. Steuerungscockpit: Was jede Woche auf eine Seite gehört

- **Auslieferung:** tatsächlicher Spend, Freigabe, Klicks, CPC, direkt erhobener Search IS sowie Verlust wegen Rang/Budget – getrennt nach Kampagne.
- **Intent:** sichtbare Suchbegriff-Kostenabdeckung, relevante/irrelevante/unklare Anteile ausschließlich im sichtbaren Nenner; neue Ausschlüsse mit ID und Grund.
- **Messung:** Formularerfolg, Buchung, Consent-Tests, Dedupefehler, Importdiagnostik, Abweichung zu Backendereignissen mit Zeitfensterdefinition.
- **Funnel:** eindeutige echte Leads, budget-/scopequalifizierte Leads, bestätigte Teilnahmen, Angebote, Wins, Zahlungseingänge; je Akquisitionskohorte und Reifestand.
- **Wirtschaft:** CPL, CPQL, Kosten je gehaltenem Gespräch, Media-/voller CAC, realisierter Deckungsbeitrag, Cash-Payback; bei null oder unbekanntem Nenner „n. a.“, nicht null Euro.
- **Änderungslog:** A/B/C-Zustand, Prüfstatus, exakter Testbeginn, Offer-/Zieldefinitionsversion; keine Vermischung von vorgeschlagen, gespeichert, ausliefernd und end-to-end verifiziert.
- **Marktmonat:** gleiche definierte Intent-/Geo-Zeitreihe aus Keyword Planner sowie Wettbewerbs-/Auktionsdaten, sofern zugänglich. Diese Ergänzung ist noch nicht erhoben; ohne sie bleibt marktweite Suchnachfrage offen.

**Erfolg bedeutet:** mehr finanzierungsfähige, sauber attribuierte und profitabel gewonnene Projekte – nicht maximaler Spend, maximaler QS oder möglichst viele Plattformconversions.

## 12. Evidenzregister und Grenzen

### Interne, am 11.10.2026 verifizierte Evidenz

| ID | Lokale Quelle | Tragende Befunde |
|---|---|---|
| E1 | Konto- und Zeitfenster-Audit (privater unterstützender Originalbeleg, nicht im Download) | Settings, Monats-/reife Fenster, URL-Historie, Budgets, Lag |
| E2 | Keyword- und Rang-Audit (privater unterstützender Originalbeleg, nicht im Download) | Gleichlange Perioden, direkte IS-Werte, stabile Keyword-IDs, QS-Abdeckung |
| E3 | Tracking-Audit (privater unterstützender Originalbeleg, nicht im Download) | Aktiver GTM/Labels, Wege, Consent, Goals, URLs, technische Grenzen |
| E4 | Lead-Abgleich (privater unterstützender Originalbeleg, nicht im Download) | 247 Nicht-Team-Lead-IDs konsistent, 27/27 KPI-Abgleiche, Rohformular-/Kohortenunterschiede |
| E5 | Importdiagnostik (privater unterstützender Originalbeleg, nicht im Download) | EXPIRED_EVENT, betroffene Actions, keine Website-Totalausfallbehauptung |
| E6 | Umsetzung A (privater unterstützender Originalbeleg, nicht im Download) | Zwei neue RSAs, sechs Exact-Negatives, Preiswiderspruch, C nicht angewendet |
| E7 | Vorbereitung B (privater unterstützender Originalbeleg, nicht im Download) | B BLOCKED, Zugriffsgrenzen, lokale Tests, kein produktiver Repair |

Die privaten Lead-Rohdaten wurden nicht in dieses Reportpaket kopiert. Die beigefügten CSVs enthalten aggregierte Kampagnen-/Keywordwerte. Diese Untersuchung ersetzt kein kontrolliertes LP-Experiment, keine Rechtsberatung zur Consent-Konfiguration und keine verifizierte Gewinn-/Zahlungsrechnung.

### Recherche- und Rechen-QA

Marktquellen am 11.10.2026 frisch gelesen. Aktuellere Quellen wurden gezielt gesucht: Swico Q4 statt nur Q3, KfW VC Q3 statt nur Q2. Bitkom-Juli-Prognose ersetzt im aktuellen Marktbild die Januar-Prognose. PDF-Tabellen wurden zusätzlich direkt als Text extrahiert, weil der Web-Extractor Diagrammwerte teilweise verlor; direkte HTML-Lektüre ergänzte fehlende Pressemitteilungsabsätze. `mcporter` war nicht installiert; Recherche erfolgte über Websuche und direkte schreibfreie HTTP-Abrufe. Agent-Reach-Updatecheck meldete v1.5.0 als aktuell.

Alle Szenarien sind Annahmen, keine Absatz-/Umsatzprognosen. Kosten-/Klick-/Conversiondeltas wurden aus ungerundeten CSV-Werten neu berechnet. Der Quellenledger, wörtliche Evidenz, Claimregister, Quellenkopien und QA-Dateien liegen in demselben Ordner. Öffentliche Quellen folgen mit stabilen nummerierten Links.

## Sources

[1] https://www.bitkom.org/Presse/Presseinformation/Digitalbranche-weiterhin-stabil — Digitalbranche zeigt sich weiterhin stabil | Presseinformation | Bitkom e. V.
[2] https://www.bitkom.org/Presse/Presseinformation/Digitalwirtschaft-bleibt-Stabilitaetsanker — Digitalwirtschaft bleibt Stabilitätsanker: 245 Milliarden Euro Umsatz in 2026 | Presseinformation | Bitkom e. V.
[3] https://www.bitkom.org/Presse/Presseinformation/Deutscher-KI-Markt-waechst-um-48-Prozent — 28,7 Milliarden Euro für KI: Deutscher Markt wächst um 48 Prozent | Presseinformation | Bitkom e. V.
[4] https://www.kfw.de/PDF/Download-Center/Konzernthemen/Research/PDF-Dokumente-Digitalisierungsbericht-Mittelstand/KfW-Digitalisierungsbericht-2025.pdf — KfW-Digitalisierungsbericht Mittelstand 2025
[5] https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/IKT-in-Unternehmen-IKT-Branche/IKT-U-Erhebung/info.html — Nutzung von IKT in Unternehmen  -  Statistisches Bundesamt
[6] https://www.bitkom.org/sites/main/files/2026-07/bitkom-praesentation-halbjahres-konjunktur-2026.pdf — Halbjahres-PK Bitkom 2026
[8] https://www.statistik.at/fileadmin/announcement/2026/06/20260624IKTU2025.pdf
[10] https://www.bitkom.org/EN/List-and-detailpages/Publications/How-AI-Is-Transforming-the-Software-Industry
[11] https://www.swico.ch/de/news/detail/swico-ict-index-q4-2026-digitalwirtschaft-spurt-zuruckhaltung-bei-investitionen
[12] https://www.kfw.de/PDF/Download-Center/Konzernthemen/Research/PDF-Dokumente-Dashboard/KfW-VC-Dashboard-Q3-2026.pdf
[13] https://support.google.com/google-ads/answer/6167118?hl=en
[14] https://support.google.com/google-ads/answer/1722122?hl=en


## QS-Nenner: vollständige Population versus festes Panel

[QS-Abdeckung nach Periode (CSV)](data/qs_coverage_by_period.csv) enthält volle QS-Population, abgedeckte Impressionen, Konto-Impressionen, eindeutige QS-Keywords, gewichteten QS, Zeitfenster und Snapshot-Hashes. 2.903 / 8.409 = 34,52 % und 4.283 / 11.298 = 37,91 %. Der [gemeinsame 18-Keyword-Paneldatensatz](data/matched_keywords_before_after.csv) belegt separat die Panel-Mittelwerte; er ist nicht der Nenner der vollständigen QS-Abdeckung. Private Rohsnapshots werden nicht ausgeliefert.
