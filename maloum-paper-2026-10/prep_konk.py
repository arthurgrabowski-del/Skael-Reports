"""Ad-Library-Scrape -> data/konkurrenz.json + Thumbnails in ../assets/maloum-konkurrenz/"""
import json, os, re, datetime as dt
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "..", "assets", "maloum-konkurrenz")
M = json.load(open("/tmp/adlib2/merged_all.json"))
OURS = {'Lia Engel','Stella4twenty','Deine Leyla','Nikoleta','Tess.sxh','maloum.official','Diese.emma','Ossi.desii','Zoeelena','Tsophie','Samantra','Gwendo'}
ALIAS = {'Lucia Laubnitz':'Lucy (lil.lucy)','Kate':'Kate (katewagner)','Kate wagner':'Kate (katewagner)','Katexwag':'Kate (katewagner)'}
CRE = ('maloum','ninj.link','myotherlink','onlyfans','fanvue','4based','fansly','mym.fans')
NOT_CREATOR = ('Roman Knox','Foxy','supercreator','Polsia','Zupría','Rulta','She Earns','Digital Majestic','Fanvue','Zasta')
KNOWN = set(ALIAS) | {'Rina Photography','Marlene Nagel','Lilly Dorn','leoo.baut','Leni Wagner'}
T = dt.date(2026, 10, 12)
def d(s): return dt.date(int(s[6:]), int(s[3:5]), int(s[:2])) if s else None
TAGS = [  # (klasse, label, keywords)
 ('r','Schule/18 – tabu',['schule','schülerin']),
 ('r','Kontakt-/Chat-Versprechen',['schreib','antwort','chatt','kontakt','sag einfach hi','kennenlernen',' date','-date']),
 ('b','Fragesticker',['frage','frag mich','wie findest du']),
 ('b','Persona/Hobby',['cosplay','manga','zock','gamer','dorf','traktor','dirndl','fitness','gym','studentin','berg','stall']),
 ('b','Behind the Scenes',['kulissen','einblick','shooting','exklusiv']),
 ('b','Kein Snap mehr',['snap']),
 ('b','Zahlung',['paypal','klarna','kreditkarte','apple pay']),
 ('b','Zwei Seiten / Bruchteil',['bruchteil','hälfte','zwei seiten','montag','samstag']),
 ('b','Schüchtern/Neu',['schüchtern','neu hier','nervös','traut']),
]
out = []
for x in M:
    page = x['page']
    if page in OURS or any(n.lower() in page.lower() for n in NOT_CREATOR): continue
    if not (any(k in (x.get('dom') or '') for k in CRE) or page in KNOWN): continue
    if not x.get('start'): continue
    s = d(x['start']); e = d(x['end']) if x.get('end') and not x['active'] else T
    body = re.split(r' / (?:HTTPS?://)?[A-Z0-9.]+\.(?:COM|LINK|BIO)', x['body'])[0]
    low = ' ' + body.lower() + ' '
    tags = [(c, l) for c, l, ks in TAGS if any(k in low for k in ks)]
    days = (e - s).days + 1
    if days >= 90: tags.append(('g', f'{days} Tage Laufzeit'))
    if x['var'] >= 4: tags.append(('g', f"{x['var']} Varianten"))
    img = None
    for src in (f"/tmp/adlib2/shots/{x['id']}.png", f"/tmp/adlib/shots/{x['id']}.png"):
        if os.path.exists(src):
            dst = os.path.join(A, f"{x['id']}.jpg")
            if not os.path.exists(dst):
                im = Image.open(src).convert('RGB'); im.thumbnail((520, 1100)); im.save(dst, quality=78)
            img = f"{x['id']}.jpg"; break
    out.append(dict(id=x['id'], who=ALIAS.get(page, page), page=page, body=body[:320], start=x['start'],
                    end=x.get('end') or '', active=bool(x['active']), days=days, var=x['var'], dom=x.get('dom') or '',
                    tags=tags, img=img, s=s.isoformat()))
os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
json.dump(out, open(os.path.join(HERE, 'data', 'konkurrenz.json'), 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), 'ads', sum(o['active'] for o in out), 'aktiv', sum(1 for o in out if o['img']), 'mit Bild')
for k, v in Counter(o['who'] for o in out).most_common(): print(v, k)
