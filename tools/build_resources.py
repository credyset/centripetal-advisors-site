"""Build the first resource hierarchy batch from existing brand shell and public sources."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,html
ROOT=Path(__file__).resolve().parents[1]
BASE='https://credyset.github.io/centripetal-advisors-site/'
e=lambda s:html.escape(s,quote=True)
data=json.loads((ROOT/'tools/resource-library.json').read_text())
source=(ROOT/'guides/saas-cash-flow-mistakes.html').read_text()
GUIDES=[
 ('saas-finance-scorecard','SaaS Finance Scorecard','Finance leadership','Review eight areas of your finance function and identify questions to address first.'),
 ('do-i-need-a-fractional-cfo','Do I Need a Fractional CFO?','Finance leadership','Clarify the work, complexity, and ownership your company needs.'),
 ('series-a-diligence-readiness','Series A Diligence Readiness','Fundraising','Connect the operating story to the evidence behind investor questions.'),
 ('first-90-days-after-raise','First 90 Days After Your Raise','Fundraising · Cash & runway','Turn the use-of-proceeds plan into an operating cadence.'),
 ('saas-cash-flow-mistakes','Cash-Flow Mistakes & Forecast Review','Cash & runway','Review the assumptions behind collections, commitments, and customer dependence.'),
 ('venture-debt-readiness','Venture Debt Readiness','Venture debt','Examine lender evidence, repayment obligations, and financing assumptions.'),
 ('treasury-hygiene','Treasury Hygiene','Treasury & finance operations','Review cash access, approvals, placement, and control ownership.')]

def link(url,label,external=False):
 return f'<a class="ca-link" href="{e(url)}"'+(' target="_blank" rel="noopener noreferrer"' if external else '')+f'>{e(label)}</a>'
def card(title,body,url,label,eyebrow=''):
 return f'<article class="ca-card">'+(f'<p class="ca-eyebrow">{e(eyebrow)}</p>' if eyebrow else '')+f'<h3>{e(title)}</h3><p>{e(body)}</p>{link(url,label)}</article>'
def section(title,body,content,stone=False,id=None):
 return f'<section class="ca-section'+(' ca-stone' if stone else '')+'"><div class="ca-inner"><h2'+(f' id="{id}" tabindex="-1"' if id else '')+f'>{e(title)}</h2><p class="ca-intro">{e(body)}</p>{content}</div></section>'
def grid(cards):return '<div class="ca-grid">'+''.join(cards)+'</div>'
def subnav(current):
 items=[('Overview','index.html'),('Guides','../guides/index.html'),('Tools & Assessments','tools.html'),('LinkedIn Posts','linkedin-posts.html'),('Media','media.html')]
 return '<nav class="ca-resource-nav" aria-label="Resource sections"><div class="ca-inner">'+''.join(f'<a href="{u}"'+(' aria-current="page"' if l==current else '')+f'>{e(l)}</a>' for l,u in items)+'</div></nav>'
def build(path,title,h1,desc,body,current,items):
 soup=BeautifulSoup(source,'html.parser')
 soup.title.string=title+' | Centripetal Advisors'
 for key in ['description','og:description','twitter:description']:
  x=soup.find('meta',attrs={'name':key}) or soup.find('meta',attrs={'property':key})
  if x:x['content']=desc
 for key in ['og:title','twitter:title']:
  x=soup.find('meta',attrs={'name':key}) or soup.find('meta',attrs={'property':key})
  if x:x['content']=title+' | Centripetal Advisors'
 url=BASE+path
 soup.find('link',rel='canonical')['href']=url
 soup.find('meta',attrs={'property':'og:url'})['content']=url
 for x in soup.select('link[href*="guide-workbook"],script[src*="cash-review"],.guide-editorial'):x.decompose()
 graph=[{'@type':'Organization','@id':BASE+'#organization','name':'Centripetal Advisors','url':'https://centripetaladvisors.com/','logo':BASE+'assets/logo-light.png'},
 {'@type':'WebSite','@id':BASE+'#website','name':'Centripetal Advisors — Website Concept','url':BASE,'publisher':{'@id':BASE+'#organization'}},
 {'@type':'CollectionPage','@id':url+'#page','name':title,'description':desc,'url':url,'isPartOf':{'@id':BASE+'#website'},'mainEntity':{'@id':url+'#list'}},
 {'@type':'ItemList','@id':url+'#list','itemListElement':[{'@type':'ListItem','position':i+1,'name':name,'url':BASE+dest if not dest.startswith('https:') else dest} for i,(name,dest) in enumerate(items)]},
 {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE}]+([] if current=='Overview' else [{'@type':'ListItem','position':2,'name':'Resources','item':BASE+'resources/index.html'}])+[{'@type':'ListItem','position':2 if current=='Overview' else 3,'name':title,'item':url}]}]
 soup.find('script',type='application/ld+json').string=json.dumps({'@context':'https://schema.org','@graph':graph})
 css=soup.new_tag('link',rel='stylesheet',href='../assets/resource-library.css?v=20261009-3');soup.head.append(css)
 nav=soup.select_one('.site-nav')
 for a in nav.select('a'):
  if a.get_text(strip=True)=='Resources':a['href']='../resources/index.html';a['aria-current']='page'
 nav.select_one('#primary-menu').find('a',string='Blogs').string='Blog'
 main=soup.main
 main.clear()
 main.append(BeautifulSoup(f'<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Founder resources · Centripetal Advisors</p><h1>{e(h1)}</h1><p>{e(desc)}</p></div></header>'+subnav(current)+body,'html.parser'))
 for a in soup.select('.ca-resource-nav a'):
  if path.startswith('guides/'):
   if a['href']!='../guides/index.html':a['href']='../resources/'+a['href']
 footer=soup.select_one('.footer-col:nth-of-type(2)')
 footer.clear()
 footer.append(BeautifulSoup('<h4>Explore</h4><a href="../resources/index.html">Resources</a><a href="../guides/index.html">Guides</a><a href="../resources/tools.html">Tools &amp; Assessments</a><a href="../resources/linkedin-posts.html">LinkedIn Posts</a><a href="../resources/media.html">Media</a><a href="../blogs.html">Blog</a>','html.parser'))
 (ROOT/path).write_text(str(soup).rstrip()+'\n')

formats=[('Guides','Frameworks and checklists for the finance decisions in front of you.','../guides/index.html','Browse guides →'),('Tools & Assessments','Work through a scorecard, checklist, or review worksheet.','tools.html','Explore tools →'),('LinkedIn Posts','Selected public posts from Charles on finance, founders, and the firm.','linkedin-posts.html','Read Charles’ posts →'),('Media','Podcast conversations with Charles about finance and company building.','media.html','Explore podcast appearances →')]
topics=[
 ('Finance leadership','What work needs a finance owner?','../guides/do-i-need-a-fractional-cfo.html','Explore the CFO decision guide →'),
 ('Fundraising readiness','What evidence supports the next capital conversation?','../guides/series-a-diligence-readiness.html','Review diligence readiness →'),
 ('Cash & runway','Which assumption could change the next commitment?','../guides/saas-cash-flow-mistakes.html','Review your cash forecast →'),
 ('Board & investor reporting','What decisions should the reporting support?','../services/board-investor-reporting.html','Explore reporting support →'),
 ('Venture debt','How does the facility fit the full capital plan?','../guides/venture-debt-readiness.html','Review venture debt readiness →'),
 ('Treasury & finance operations','Who owns cash access and approvals?','../guides/treasury-hygiene.html','Review treasury hygiene →')]
body=section('Start with the decision in front of you.','These topics connect practical resources to the work your company needs.',grid([card(*x) for x in topics]),id='topics')
body+=section('Explore the way you prefer to learn.','Read a framework, work through an assessment, or hear Charles’ perspective.',grid([card(*x) for x in formats]).replace('class="ca-grid"','class="ca-grid ca-resource-formats"'),True,id='formats')
body+=section('Looking for an article?','Explore focused perspectives on SaaS finance, capital strategy, and operating decisions.',link('../blogs.html','Explore the Blog →')+'<p class="ca-footer">'+link('../about.html','Meet the firm behind these resources →')+'</p>')
build('resources/index.html','Founder Resources','Perspective and practical tools for your next decision.','Explore Centripetal’s guides, assessments, Charles’ LinkedIn posts, and podcast appearances.',body,'Overview',[(x[0],('guides/index.html' if i==0 else 'resources/'+x[2])) for i,x in enumerate(formats)])
body=section('Frameworks you can put to work.','Start with one question. Each guide connects the evidence to an operating decision and a relevant next step.',grid([card(name,desc,'../guides/'+slug+'.html','Read the guide →',topic) for slug,name,topic,desc in GUIDES]))
body+=section('Prefer to work through the question?','Find the interactive scorecard, checklists, and cash forecast review in Tools & Assessments.',link('../resources/tools.html','Explore tools and assessments →'),True)
build('guides/index.html','SaaS Finance Guides & Checklists','Guides for the decisions in front of you.','Practical frameworks for SaaS finance leadership, fundraising, cash planning, venture debt, and treasury.',body,'Guides',[(name,'guides/'+slug+'.html') for slug,name,_,_ in GUIDES])
tools=[('SaaS Finance Scorecard','Assess eight finance areas and review the questions behind your lowest scores.','../guides/saas-finance-scorecard.html','Use the scorecard →','Self-assessment'),('Series A Diligence Checklist','Track the evidence to prepare for investor questions.','../guides/series-a-diligence-readiness.html','Open the diligence checklist →','Interactive checklist'),('Venture Debt Readiness Checklist','Review financing evidence and obligations alongside your capital plan.','../guides/venture-debt-readiness.html','Open the debt checklist →','Interactive checklist'),('Cash Forecast Review','Keep reviewed areas and unresolved follow-ups visible. This worksheet does not calculate runway.','../guides/saas-cash-flow-mistakes.html#review','Use the review worksheet →','Review worksheet')]
body=section('Work through the evidence.','Use these exercises to organize the next review with your team. Results and selections are not saved or submitted.',grid([card(*x) for x in tools]))
body+=section('Connect the exercise to the company.','The resource can help organize questions. The finance work connects those questions to your model, reporting, and decisions.',link('../services.html','Explore Centripetal’s services →'),True)
build('resources/tools.html','Finance Tools & Assessments','Turn the question into a working review.','Use Centripetal’s finance scorecard, diligence checklists, and cash forecast review worksheet.',body,'Tools & Assessments',[(x[0],'guides/'+x[2].split('/')[-1]) for x in tools])
posts=''
for p in data['posts']:
 posts+=f'<article class="ca-feed-item"><p class="ca-eyebrow">{e(p["topic"])} · Charles Solomon</p><h3>{e(p["title"])}</h3><p>{e(p["summary"])}</p><p class="ca-source-label">Summary of Charles’ public LinkedIn post.</p>{link(p["url"],"Read original on LinkedIn ↗",True)}</article>'
body=section('From Charles’ LinkedIn.','A selected feed of published posts, with summaries and links to the originals. Browse Charles’ profile for his latest updates.',link(data['linkedin_profile'],'See Charles’ latest posts on LinkedIn ↗',True)+'<div class="ca-feed">'+posts+'</div>')
body+=section('Go deeper on the finance question.','Connect the perspectives to a practical framework or the work your company needs.',link('../guides/index.html','Explore the guides →')+'<p class="ca-footer">'+link('../services.html','Explore finance support →')+'</p>',True)
build('resources/linkedin-posts.html','Charles Solomon’s LinkedIn Posts','A perspective from inside the work.','Selected LinkedIn posts from Charles Solomon on planning, founder partnerships, and Centripetal Advisors.',body,'LinkedIn Posts',[(p['title'],p['url']) for p in data['posts']])
media=''
for m in data['media']:
 listen=link(m['url'],'Listen on '+m['platform']+' ↗',True)
 media+=f'<article class="ca-media-item"><div class="ca-media-show"><span>Podcast appearance</span><p>{e(m["show"])}</p></div><div><p class="ca-eyebrow"><time datetime="{m["date"]}">{m["date_label"]}</time> · {m["duration"]}</p><h3>{e(m["title"])}</h3><p>{e(m["summary"])}</p>{listen}</div></article>'
body=section('Charles in conversation.','Listen to conversations about finance, founder decisions, and building companies.',media)
body+=section('Bring the conversation back to your company.','Explore the firm’s operating approach or the resources connected to your next decision.',link('../about.html','About Centripetal →')+'<p class="ca-footer">'+link('../guides/index.html','Explore practical guides →')+'</p>',True)
build('resources/media.html','Charles Solomon’s Podcast Appearances','Finance and company building, in conversation.','Podcast appearances featuring Charles Solomon of Centripetal Advisors.',body,'Media',[(m['title'],m['url']) for m in data['media']])

# Keep stable guide/article destinations while pointing Resources to its own hub.
import re,os
for path in list(ROOT.rglob('*.html'))+list((ROOT/'assets').glob('*.inc')):
 if 'assets/baseline' in str(path.relative_to(ROOT)):continue
 text=path.read_text()
 if 'ca-native' in text and path.suffix=='.html':text=re.sub(r'foundations.css\?v=20261009-\d+', 'foundations.css?v=20261009-9', text)
 def update_anchor(match):
  raw=match.group(0)
  label=BeautifulSoup(raw,'html.parser').get_text(' ',strip=True).lower()
  if 'guides/index.html' not in raw or not ('resources' in label):return raw
  destination=os.path.relpath(ROOT/'resources/index.html',path.parent)
  return re.sub(r'href="[^"]*guides/index.html"',lambda _:f'href="{destination}"',raw)
 text=re.sub(r'<a\b[^>]*>.*?</a>',update_anchor,text,flags=re.S)
 text=text.replace('"name": "Resources", "item": "'+BASE+'guides/index.html"','"name": "Resources", "item": "'+BASE+'resources/index.html"')
 path.write_text(text)
sitemap=ROOT/'sitemap.xml'
text=sitemap.read_text()
for name in ['index.html','tools.html','linkedin-posts.html','media.html']:
 url=BASE+'resources/'+name
 if url not in text:text=text.replace('</urlset>',f'  <url><loc>{url}</loc></url>\n</urlset>')
sitemap.write_text(text)
