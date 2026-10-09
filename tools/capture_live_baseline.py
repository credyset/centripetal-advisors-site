"""Capture the authorized published Framer pages, preserving visual code and assets.

No access to the Framer account or publishing API is used. Network reads are limited
 to the public URLs below. The preview guard disables production form submission.
"""
from pathlib import Path
from urllib.request import urlopen
import re, hashlib, json
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
PAGES={'/':'index.html','/services':'services.html','/contact':'contact.html','/blogs':'blogs.html','/privacy-policy':'privacy-policy.html'}
PREVIEW='https://credyset.github.io/centripetal-advisors-site/'
SCRIPT=re.compile(r'<script\b([^>]*)>(.*?)</script>',re.S|re.I)
def clean(source,filename):
    def script(match):
        attrs,body=match.groups()
        if any(token in attrs for token in ('googletagmanager','events.framer')) or any(token in body for token in ('__framer_force_showing_editorbar_since','gtag(','_linkedin_partner_id','lintrk')):
            return ''
        return match.group(0)
    source=SCRIPT.sub(script,source)
    source=re.sub(r'<noscript\b[^>]*>.*?linkedin.*?</noscript>','',source,flags=re.S|re.I)
    source=re.sub(r'<meta\s+[^>]*name=["\']robots["\'][^>]*>','',source,flags=re.I)
    canonical=PREVIEW+('' if filename=='index.html' else filename)
    source=re.sub(r'<link\s+rel="canonical"\s+href="[^"]*"[^>]*>',f'<link rel="canonical" href="{canonical}">',source)
    source=re.sub(r'(<meta\s+property="og:url"\s+content=")[^"]*',r'\g<1>'+canonical,source)
    # Run the preview boundary early, before the published rendering bundle loads.
    source=source.replace('</head>','<meta name="robots" content="noindex, follow">\n<script src="assets/home-baseline.js"></script>\n</head>',1)
    return '\n'.join(line.rstrip() for line in source.splitlines())+'\n'
manifest={'source':'https://centripetaladvisors.com','captured':datetime.now().astimezone().isoformat(timespec='seconds'),'scope':'Published visual baseline; production analytics/editor bootstrap omitted; preview forms do not submit.','pages':[]}
for route,filename in PAGES.items():
    source=urlopen('https://centripetaladvisors.com'+route,timeout=40).read().decode()
    (ROOT/filename).write_text(clean(source,filename))
    manifest['pages'].append({'route':route,'file':filename,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'render_module':re.findall(r'src="(https://framerusercontent.com/sites/[^" ]+/script_main[^" ]+)"',source)})
    print(filename,len(source),'characters')
(ROOT/'assets/baseline/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
