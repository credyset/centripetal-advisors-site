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
def card(title,body,url,label,eyebrow='',external=False):
 return f'<article class="ca-card">'+(f'<p class="ca-eyebrow">{e(eyebrow)}</p>' if eyebrow else '')+f'<h3>{e(title)}</h3><p>{e(body)}</p>{link(url,label,external)}</article>'
def section(title,body,content,stone=False,id=None):
 return f'<section class="ca-section'+(' ca-stone' if stone else '')+'"><div class="ca-inner"><h2'+(f' id="{id}" tabindex="-1"' if id else '')+f'>{e(title)}</h2><p class="ca-intro">{e(body)}</p>{content}</div></section>'
def grid(cards):return '<div class="ca-grid">'+''.join(cards)+'</div>'
def subnav(current):
 items=[('Overview','index.html'),('Guides & Tools','../guides/index.html'),('LinkedIn Posts','linkedin-posts.html'),('Media','media.html')]
 return '<nav class="ca-resource-nav" aria-label="Resource sections"><div class="ca-inner">'+''.join(f'<a href="{u}"'+(' aria-current="page"' if l==current else '')+f'>{e(l)}</a>' for l,u in items)+'</div></nav>'
def build(path,title,h1,desc,body,current,items):
 soup=BeautifulSoup(source,'html.parser')
 soup.body['class']=['ca-native']
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
 for x in soup.select('link[href*="guide-workbook"],script[src*="cash-review"],link[href*="cash-guide-reference"],.guide-editorial'):x.decompose()
 graph=[{'@type':'Organization','@id':BASE+'#organization','name':'Centripetal Advisors','url':'https://centripetaladvisors.com/','logo':BASE+'assets/logo-light.png'},
 {'@type':'WebSite','@id':BASE+'#website','name':'Centripetal Advisors — Website Concept','url':BASE,'publisher':{'@id':BASE+'#organization'}},
 {'@type':'CollectionPage','@id':url+'#page','name':title,'description':desc,'url':url,'isPartOf':{'@id':BASE+'#website'},'mainEntity':{'@id':url+'#list'}},
 {'@type':'ItemList','@id':url+'#list','itemListElement':[{'@type':'ListItem','position':i+1,'name':name,'url':BASE+dest if not dest.startswith('https:') else dest} for i,(name,dest) in enumerate(items)]},
 {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE}]+([] if current=='Overview' else [{'@type':'ListItem','position':2,'name':'Resources','item':BASE+'resources/index.html'}])+[{'@type':'ListItem','position':2 if current=='Overview' else 3,'name':title,'item':url}]}]
 soup.find('script',type='application/ld+json').string=json.dumps({'@context':'https://schema.org','@graph':graph})
 css=soup.new_tag('link',rel='stylesheet',href='../assets/resource-library.css?v=20261009-4');soup.head.append(css)
 if current=='LinkedIn Posts':
  soup.body['class'].append('ca-linkedin-feed')
  soup.head.append(soup.new_tag('link',rel='stylesheet',href='../assets/linkedin-feed.css?v=20261010-1'))
  motion=soup.new_tag('script',src='../assets/linkedin-feed.js?v=20261010-1');motion['defer']='';soup.body.append(motion)
 if current=='Media':
  soup.body['class'].append('ca-media-feed')
  soup.head.append(soup.new_tag('link',rel='stylesheet',href='../assets/media-feed.css?v=20261009-2'))
  motion=soup.new_tag('script',src='../assets/media-feed.js?v=20261009-1');motion['defer']='';soup.body.append(motion)
 nav=soup.select_one('.site-nav')
 for a in nav.select('a'):
  if a.get_text(strip=True)=='Resources':a['href']='../resources/index.html';a['aria-current']='page'
 for a in nav.select('#primary-menu a'):
  if a.get_text(strip=True) in ('Blogs','Blog'):a.string='Blog'
 main=soup.main
 main.clear()
 main.append(BeautifulSoup(f'<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Founder resources · Centripetal Advisors</p><h1>{e(h1)}</h1><p>{e(desc)}</p></div></header>'+subnav(current)+body,'html.parser'))
 if current=='LinkedIn Posts':
  orbit=soup.new_tag('img',src='../assets/reference/home-orbit.png',width='1269',height='1208',alt='',**{'class':'ca-linkedin-hero-orbit','aria-hidden':'true'})
  soup.select_one('.concept-hero-inner').append(orbit)
 if current=='Media':
  orbit=soup.new_tag('img',src='../assets/reference/home-orbit.png',width='1269',height='1208',alt='',**{'class':'ca-media-hero-orbit','aria-hidden':'true'})
  soup.select_one('.concept-hero-inner').append(orbit)
 for a in soup.select('.ca-resource-nav a'):
  if path.startswith('guides/'):
   if a['href']!='../guides/index.html':a['href']='../resources/'+a['href']
 footer=soup.select_one('.footer-col:nth-of-type(2)')
 footer.clear()
 footer.append(BeautifulSoup('<h4>Explore</h4><a href="../resources/index.html">Resources</a><a href="../guides/index.html">Guides &amp; Tools</a><a href="../resources/linkedin-posts.html">LinkedIn Posts</a><a href="../resources/media.html">Media</a><a href="../blogs.html">Blog</a>','html.parser'))
 (ROOT/path).write_text(str(soup).rstrip()+'\n')

formats=[('Guides & Tools','Read a framework, work through a checklist, or build a preparation outline.','../guides/index.html','Explore guides and tools →'),('LinkedIn Posts','Selected public posts from Charles on finance, founders, and the firm.','linkedin-posts.html','Read Charles’ posts →'),('Media','Podcast conversations with Charles about finance and company building.','media.html','Explore podcast appearances →')]
topics=[
 ('Finance leadership','What work needs a finance owner?','../guides/do-i-need-a-fractional-cfo.html','Explore the CFO decision guide →'),
 ('Fundraising readiness','What evidence supports the next capital conversation?','../guides/series-a-diligence-readiness.html','Review diligence readiness →'),
 ('Cash & runway','Which assumption could change the next commitment?','../guides/saas-cash-flow-mistakes.html','Review your cash forecast →'),
 ('Board & investor reporting','What decisions should the reporting support?','../guides/tools/board-deck-builder.html','Build a board-meeting outline →'),
 ('Venture debt','How does the facility fit the full capital plan?','../guides/venture-debt-readiness.html','Review venture debt readiness →'),
 ('Treasury & finance operations','Who owns cash access and approvals?','../guides/treasury-hygiene.html','Review treasury hygiene →')]
body=section('Start with the decision in front of you.','These topics connect practical resources to the work your company needs.',grid([card(*x) for x in topics]),id='topics')
body+=section('Explore the way you prefer to learn.','Read a framework, work through an assessment, or hear Charles’ perspective.',grid([card(*x) for x in formats]).replace('class="ca-grid"','class="ca-grid ca-resource-formats"'),True,id='formats')
body+=section('Looking for an article?','Explore focused perspectives on SaaS finance, capital strategy, and operating decisions.',link('../blogs.html','Explore the Blog →')+'<p class="ca-footer">'+link('../about.html','Meet the firm behind these resources →')+'</p>')
build('resources/index.html','Founder Resources','Perspective and practical tools for your next decision.','Explore Centripetal’s guides, assessments, Charles’ LinkedIn posts, and podcast appearances.',body,'Overview',[(x[0],('guides/index.html' if i==0 else 'resources/'+x[2])) for i,x in enumerate(formats)])
guide_formats={'saas-finance-scorecard':'Assessment','do-i-need-a-fractional-cfo':'Guide','series-a-diligence-readiness':'Guide with checklist','first-90-days-after-raise':'Guide','saas-cash-flow-mistakes':'Guide with worksheet','venture-debt-readiness':'Guide with checklist','treasury-hygiene':'Guide'}
library_items=[(name,'guides/'+slug+'.html') for slug,name,_,_ in GUIDES]
library_items.insert(4,('Board Deck Structure Builder','guides/tools/board-deck-builder.html'))
library=[card(name,desc,'../guides/'+slug+'.html',{'Assessment':'Use the assessment →','Guide with checklist':'Read and review →','Guide with worksheet':'Read and review →'}.get(guide_formats[slug],'Read the guide →'),guide_formats[slug]+' · '+topic) for slug,name,topic,desc in GUIDES]
library.insert(4,card('Board Deck Structure Builder','Choose the main discussion and organize the recommendation, evidence, assumptions, and owners.','../guides/tools/board-deck-builder.html','Build your meeting outline →','Builder · Board & investor reporting'))
body=section('One question. A useful way to work through it.','Guides explain the framework. Tools help you organize a review or outline. When a guide includes an exercise, both live on the same page.',grid(library),id='library')
body+=section('Connect the resource to your company.','These concept resources are for firm review. Interactive selections stay on the page; they are not saved or submitted. Use the relevant service page to explore the work behind the question.',link('../services.html','Explore Centripetal’s services →'),True)
build('guides/index.html','SaaS Finance Guides & Tools','Guides and tools for the decisions in front of you.','Explore practical frameworks, review checklists, and a board-meeting outline for SaaS finance, cash planning, fundraising, and treasury.',body,'Guides & Tools',library_items)
body=section('Guides and tools now share one library.','Find each resource once, with a clear label for the reading framework or interactive exercise it offers.',link('../guides/index.html','Explore Guides & Tools →'))
build('resources/tools.html','Finance Tools Library Entry','Find your next guide or tool.','Centripetal’s finance tools and guides are now collected in one library, with a single page for each resource.',body,'Guides & Tools',[('Guides & Tools','guides/index.html')])

POST_ICON='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11.5a7.5 7.5 0 0 1-7.5 7.5H5l-3 3V11.5A7.5 7.5 0 0 1 9.5 4h3a7.5 7.5 0 0 1 7.5 7.5Z"/><path d="M7 9h8M7 13h5"/></svg>'
ARTICLE_ICON='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v15M12 5C9 3 5 3 2 4v14c3-1 7-1 10 2 3-3 7-3 10-2V4c-3-1-7-1-10 1Z"/></svg>'
def linkedin_button(url,label,icon,secondary=False):
 return f'<a class="ca-linkedin-button'+(' ca-linkedin-button-secondary' if secondary else '')+f'" href="{e(url)}" target="_blank" rel="noopener noreferrer" aria-label="{e(label)} on LinkedIn (opens in a new tab)">'+icon+f'<span>{e(label)}</span></a>'

def linkedin_card(p,index):
 id=p.get('id',f'earlier-{index}')
 topic={'SaaS metrics':'saas-metrics','Company building':'company-building','Capital & founders':'capital-founders'}[p['topic']]
 head=f'<p class="ca-eyebrow">{e(p["topic"])}</p><h2 id="post-title-{id}">{e(p["title"])}</h2><p class="ca-linkedin-summary">{e(p["summary"])}</p>'
 actions='<div class="ca-linkedin-actions">'+linkedin_button(p['url'],'Read original post',POST_ICON)
 if p.get('article_url'):actions+=linkedin_button(p['article_url'],'Read article',ARTICLE_ICON,True)
 actions+='</div>'
 embed=''
 if p.get('embed_url'):
  embed=f'<div class="ca-linkedin-embed"><iframe src="{e(p["embed_url"])}" title="LinkedIn post by Charles Solomon: {e(p["title"])}" width="504" height="{int(p["embed_height"])}" loading="lazy" referrerpolicy="no-referrer" allowfullscreen=""></iframe></div>'
 return f'<li class="ca-linkedin-entry"><span class="ca-linkedin-position" aria-hidden="true">{index:02d}</span><article class="ca-linkedin-card" id="post-{id}" aria-labelledby="post-title-{id}" data-topic="{topic}">'+'<div class="ca-linkedin-introduction">'+head+actions+'</div>'+embed+'</article></li>'
recent=[p for p in data['posts'] if p.get('selection')=='recent']
rail='<aside class="ca-linkedin-rail" aria-label="About this feed"><div class="ca-linkedin-author"><h3>Charles Solomon</h3><p>CFO · Board Member · Investor</p>'+'<div class="ca-linkedin-contacts">'+f'<a class="ca-linkedin-social" href="{e(data["linkedin_profile"])}" target="_blank" rel="noopener noreferrer" aria-label="Charles Solomon on LinkedIn (opens in a new tab)" title="Charles Solomon on LinkedIn"><img src="../assets/linkedin-social.svg" width="24" height="24" alt=""/></a>'+link('mailto:charles@centripetaladvisors.com','charles@centripetaladvisors.com')+'</div></div><nav aria-label="Explore the selected posts"><p class="ca-eyebrow">In this selection</p><a data-topic="saas-metrics" href="#post-7514431254625337344">SaaS metrics</a><a data-topic="company-building" href="#post-7514007604109647872">Company building</a><a data-topic="capital-founders" href="#post-7513311314568515584">Capital &amp; founders</a></nav><p class="ca-linkedin-rail-note">Our summaries introduce the idea. Charles’s original posts appear below each introduction.</p></aside>'
body='<section class="ca-section ca-linkedin-section" aria-label="Selected LinkedIn posts"><div class="ca-inner"><div class="ca-linkedin-layout">'+rail+'<ol class="ca-linkedin-timeline" aria-label="Recent selected LinkedIn posts">'+''.join(linkedin_card(p,i+1) for i,p in enumerate(recent))+'</ol></div></div></section>'
body+=section('Put the perspective to work.','Explore the frameworks and finance support connected to your next decision.',link('../guides/index.html','Explore guides and tools →')+'<p class="ca-footer">'+link('../services.html','Explore finance support →')+'</p>',True)
build('resources/linkedin-posts.html','Charles Solomon’s LinkedIn Posts','A perspective from inside the work.','Selected LinkedIn posts from Charles Solomon on SaaS metrics, capital, and company building—with original-post previews.',body,'LinkedIn Posts',[(p['title'],p['url']) for p in recent])

PLAY_ICON='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m10 8 6 4-6 4Z"/></svg>'
LISTEN_ICON='<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="12" width="4" height="8" rx="2"/><rect x="17" y="12" width="4" height="8" rx="2"/></svg>'

def media_button(destination,secondary=False):
 platform=destination['platform']
 watching=platform=='YouTube'
 label=('Watch on ' if watching else 'Listen on ')+platform
 return f'<a class="ca-media-button'+(' ca-media-button-secondary' if secondary else '')+f'" href="{e(destination["url"])}" target="_blank" rel="noopener noreferrer" aria-label="{e(label)} (opens in a new tab)">'+(PLAY_ICON if watching else LISTEN_ICON)+f'<span>{e(label)}</span></a>'

def media_embed(m):
 embed=m['embed']
 # Native players stay stable; only the editorial introduction receives motion.
 allow='encrypted-media; fullscreen; picture-in-picture'
 if embed['kind']=='audio':allow+='; autoplay'
 if embed['platform']=='YouTube':allow+='; accelerometer; gyroscope; web-share'
 return f'<div class="ca-media-embed ca-media-embed-{e(embed["kind"])}"><iframe src="{e(embed["url"])}" title="{e(embed["platform"])} player: {e(m["title"])}" width="504" height="{int(embed["height"])}" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="{allow}" allowfullscreen=""></iframe></div>'

media=''
media_navigation=''
for i,m in enumerate(data['media'],1):
 episode=f'episode-{i:02d}'
 metadata=[]
 if m.get('date'):metadata.append(f'<time datetime="{e(m["date"])}">{e(m["date_label"])}</time>')
 if m.get('duration'):metadata.append(e(m['duration']))
 metadata=f'<p class="ca-media-metadata">{" · ".join(metadata)}</p>' if metadata else ''
 destinations=[{'url':m['url'],'platform':m['platform']}]+m.get('alternate_links',[])
 actions='<div class="ca-media-actions">'+''.join(media_button(x,j>0) for j,x in enumerate(destinations))+'</div>'
 media+=f'<li class="ca-media-entry"><span class="ca-media-position" aria-hidden="true">{i:02d}</span><article class="ca-media-card" id="{episode}" aria-labelledby="{episode}-title" data-episode="{episode}"><div class="ca-media-introduction"><p class="ca-eyebrow">{e(m["show"])}</p>{metadata}<h2 id="{episode}-title">{e(m["title"])}</h2><p class="ca-media-summary">{e(m["summary"])}</p>{actions}</div>{media_embed(m)}</article></li>'
 media_navigation+=f'<a data-episode="{episode}" href="#{episode}">{e(m["show"])}</a>'
media_rail='<aside class="ca-media-rail" aria-label="About these appearances"><div class="ca-media-author"><h3>Charles Solomon</h3><p>CFO · Board Member · Investor</p><div class="ca-media-contacts">'+f'<a class="ca-media-social" href="{e(data["linkedin_profile"])}" target="_blank" rel="noopener noreferrer" aria-label="Charles Solomon on LinkedIn (opens in a new tab)" title="Charles Solomon on LinkedIn"><img src="../assets/linkedin-social.svg" width="24" height="24" alt=""/></a>'+link('mailto:charles@centripetaladvisors.com','charles@centripetaladvisors.com')+'</div></div><nav aria-label="Explore podcast appearances"><p class="ca-eyebrow">In this selection</p>'+media_navigation+'</nav></aside>'
body='<section class="ca-section ca-media-section" aria-label="Podcast appearances"><div class="ca-inner"><div class="ca-media-layout">'+media_rail+'<ol class="ca-media-timeline" aria-label="Selected podcast appearances">'+media+'</ol></div></div></section>'
body+=section('Bring the conversation back to your company.','Explore the firm’s operating approach or the resources connected to your next decision.',link('../about.html','About Centripetal →')+'<p class="ca-footer">'+link('../guides/index.html','Explore guides and tools →')+'</p>',True)
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
 if 'ca-native' in text:
  text=re.sub(r'(<a\b[^>]*href="[^"]*guides/index\.html"[^>]*>)Guides(</a>)',r'\1Guides &amp; Tools\2',text)
 path.write_text(text)
sitemap=ROOT/'sitemap.xml'
text=sitemap.read_text()
for name in ['index.html','tools.html','linkedin-posts.html','media.html']:
 url=BASE+'resources/'+name
 if url not in text:text=text.replace('</urlset>',f'  <url><loc>{url}</loc></url>\n</urlset>')
sitemap.write_text(text)
