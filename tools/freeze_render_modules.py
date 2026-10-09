"""Freeze public generated rendering modules at the captured published hashes."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlsplit
from concurrent.futures import ThreadPoolExecutor
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'assets/baseline/source-manifest.json').read_text())
seeds={u for p in manifest['pages'] for u in p['render_module']}
assert len({u.rsplit('/',1)[0] for u in seeds})==1
origin=next(iter(seeds)).rsplit('/',1)[0]+'/'
folder=ROOT/'assets/baseline/runtime';folder.mkdir(exist_ok=True)
seen=set();pending={u.rsplit('/',1)[1] for u in seeds};records=[]
pattern=re.compile(r'[\"\'`]\./([^\"\'`]+\.mjs)[\"\'`]')
def fetch(name):
    assert '/' not in name and '..' not in name
    content=urlopen(origin+name,timeout=40).read()
    source_hash=hashlib.sha256(content).hexdigest()
    # Preserve layout code while omitting production marketing snippets.
    content=re.sub(rb'code:e=>`((?:\\.|[^`])*)`',lambda m: b'code:e=>``' if b'_linkedin_partner_id' in m[1] or b'googletagmanager.com' in m[1] else m[0],content)
    (folder/name).write_bytes(content)
    return name,content,source_hash
with ThreadPoolExecutor(max_workers=6) as pool:
    while pending:
        batch=sorted(pending-seen);pending=set()
        if not batch:break
        assert len(seen)+len(batch)<150, 'Unexpected rendering graph size'
        for name,data,source_hash in pool.map(fetch,batch):
            seen.add(name);records.append({'file':name,'source_sha256':source_hash,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
            pending.update(set(pattern.findall(data.decode()))-seen)
        print('Frozen',len(seen),'public modules',flush=True)
manifest['render_module_origin']=origin
manifest['frozen_modules']=sorted(records,key=lambda e:e['file'])
(ROOT/'assets/baseline/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for page in manifest['pages']:
    p=ROOT/page['file'];p.write_text(p.read_text().replace(origin,'assets/baseline/runtime/'))
print('Complete:',len(records),'modules;',sum(e['bytes'] for e in records),'bytes')
