"""Validate the captured visual baseline without imposing a redesigned template."""
from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'assets/baseline/source-manifest.json').read_text())
class Inspect(HTMLParser):
    def __init__(self):super().__init__();self.local=[];self.sections=[];self.robot=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'data-framer-name' in attrs:self.sections.append(attrs['data-framer-name'])
        if tag=='meta' and attrs.get('name')=='robots':self.robot.append(attrs.get('content'))
        if tag in ('script','link'):
            url=attrs.get('src') or attrs.get('href','')
            if url and not re.match(r'https?://',url):self.local.append(url)
for item in manifest['pages']:
    p=ROOT/item['file'];s=p.read_text();ins=Inspect();ins.feed(s)
    assert ins.robot==['noindex, follow'],p
    assert 'assets/home-baseline.v2.js' in ins.local,p
    for src in ins.local:assert (p.parent/src).exists(),(p,src)
    assert 'googletagmanager.com' not in s,p
    assert 'events.framer.com/script' not in s,p
    assert 'snap.licdn.com' not in s,p
    if item['route']=='/':
        for name in ['Header Image','Numbers','Co-Pilot','Logos','About Us','Testimonials','Why Centripetal','Contact']:
            assert name in ins.sections,name
        assert 'TRUSTED BY' in s and 'CLIENTS' in s
        assert 'CHARLIE MUNGER' in s
for module in manifest.get('frozen_modules',[]):
    path=ROOT/'assets/baseline/runtime'/module['file']
    assert '_linkedin_partner_id' not in path.read_text(),module['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==module['sha256'],module['file']
    for name in re.findall(r'[\"\'`]\./([^\"\'`]+\.mjs)[\"\'`]',path.read_text()):
        assert (path.parent/name).exists(),(module['file'],name)
comparisons=json.loads((ROOT/'assets/baseline/layout-comparison.json').read_text())
assert {e['viewport'] for e in comparisons}=={390,900,1024,1280,1440,1920}
assert all(e['equal'] and e['live']['width']==e['viewport'] and e['live']==e['concept'] for e in comparisons)
print('PASS: captured core pages, all Home sections, preview safeguards, frozen modules, and six viewport geometry comparisons.')
