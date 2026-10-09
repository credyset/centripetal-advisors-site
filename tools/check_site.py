"""Check static concept pages using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.ids=[]; self.images=[]; self.h1=0; self.main=0
        self.title=''; self.in_title=False; self.description=[]; self.canonical=[]
        self.schemas=[]; self.schema=None; self.robots=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if tag=='main': self.main+=1
        if 'id' in a: self.ids.append(a['id'])
        if tag=='title': self.in_title=True
        if tag=='meta' and a.get('name')=='description': self.description.append(a.get('content',''))
        if tag=='meta' and a.get('name')=='robots': self.robots.append(a.get('content',''))
        if tag=='link' and a.get('rel')=='canonical': self.canonical.append(a.get('href',''))
        if tag=='script' and a.get('type')=='application/ld+json': self.schema=''
        if tag in ('a','link','script','img'):
            u=a.get('href') or a.get('src')
            if u: self.links.append(u)
        if tag=='img':self.images.append(a)
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script' and self.schema is not None:self.schemas.append(self.schema);self.schema=None
    def handle_data(self,data):
        if self.in_title:self.title+=data
        if self.schema is not None:self.schema+=data

pages={p:Page() for p in ROOT.rglob('*.html')}
for path,page in pages.items():page.feed(path.read_text())
errors=[];titles={};descriptions={}
for path,page in pages.items():
    rel=str(path.relative_to(ROOT))
    def require(ok,message):
        if not ok:errors.append(f'{rel}: {message}')
    require(page.h1==1,f'Expected one H1, found {page.h1}')
    require(page.main==1,f'Expected one main, found {page.main}')
    require(len(page.ids)==len(set(page.ids)),'Duplicate IDs')
    require(len(page.description)==1 and bool(page.description[0]),'Missing or duplicate description')
    require(len(page.canonical)==1 and page.canonical[0].startswith('https://'),'Missing absolute canonical')
    require(len(page.robots)==1 and 'noindex' in page.robots[0],'Concept must remain noindex')
    for table,value,kind in [(titles,page.title,'title'),(descriptions,page.description[0] if page.description else '', 'description')]:
        require(value not in table,f'Duplicate {kind} with {table.get(value)}');table[value]=rel
    for image in page.images:
        require('alt' in image,'Image missing alt attribute')
        require(bool(image.get('width')) and bool(image.get('height')),'Image missing explicit dimensions')
    for raw in page.links:
        url=urlsplit(raw)
        if url.scheme or url.netloc:continue
        target=(path.parent/unquote(url.path)).resolve() if url.path else path
        if target.is_dir():target=target/'index.html'
        require(target.exists(),f'Broken local URL {raw}')
        if url.fragment and target in pages:require(unquote(url.fragment) in pages[target].ids,f'Missing anchor {raw}')
    require(bool(page.schemas),'Missing structured data')
    for schema in page.schemas:
        try:json.loads(schema)
        except ValueError as e:errors.append(f'{rel}: Invalid JSON-LD {e}')
sitemap=ET.parse(ROOT/'sitemap.xml')
locs=[e.text for e in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(locs)==len(set(locs)), 'Duplicate sitemap URLs'
print(f'Checked {len(pages)} pages and {sum(len(p.links) for p in pages.values())} URLs; {len(locs)} sitemap entries.')
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print('PASS: unique metadata, H1/main landmarks, local links/anchors, image dimensions/alt, structured data, and staging noindex.')
