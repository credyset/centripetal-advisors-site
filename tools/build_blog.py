"""Build the separate Blog catalog and article structure; build evidence-focused drafts."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import html, json, os, re

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://credyset.github.io/centripetal-advisors-site/'
TEMPLATE = ROOT / 'guides/saas-cash-flow-mistakes.html'
DATA = json.loads((ROOT / 'tools/blog-content.json').read_text())
escape = lambda value: html.escape(value, quote=True)

def local(destination, path):
    return os.path.relpath(ROOT / destination, (ROOT / path).parent)

def anchor(destination, label, path, aria_label=None):
    accessible = f' aria-label="{escape(aria_label)}"' if aria_label else ''
    return f'<a class="ca-link" href="{escape(local(destination, path))}"{accessible}>{escape(label)}</a>'

def section(title, intro, content, heading_id=None, stone=False):
    heading = f' id="{heading_id}" tabindex="-1"' if heading_id else ''
    return f'<section class="ca-section{" ca-stone" if stone else ""}"><div class="ca-inner"><h2{heading}>{escape(title)}</h2><p class="ca-intro">{escape(intro)}</p>{content}</div></section>'

def shell(path, title, description, body, graph, canonical=None):
    soup = BeautifulSoup(TEMPLATE.read_text(), 'html.parser')
    # Rebase only the template's URLs before inserting destination-specific content.
    for node in soup.select('[href],[src]'):
        for attr in ('href', 'src'):
            value = node.get(attr)
            if not value or value.startswith('#') or urlsplit(value).scheme or value.startswith('//'):
                continue
            parsed = urlsplit(value)
            target = (TEMPLATE.parent / parsed.path).resolve()
            node[attr] = os.path.relpath(target, (ROOT / path).parent) + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
    for node in soup.select('script[src*="cash-review"],link[href*="cash-guide-reference"],.guide-editorial'):
        node.decompose()
    soup.body['class'] = ['ca-native']
    soup.title.string = title
    for attr, key, value in [('name','description',description),('property','og:title',title),('property','og:description',description),('name','twitter:title',title),('name','twitter:description',description),('property','og:type','website'),('property','og:url',canonical or BASE + path)]:
        node = soup.find('meta', attrs={attr:key})
        if node:
            node['content'] = value
    soup.find('link', rel='canonical')['href'] = canonical or BASE + path
    soup.find('script', type='application/ld+json').string = json.dumps({'@context':'https://schema.org','@graph':graph}, ensure_ascii=False)
    soup.main.clear()
    soup.main.append(BeautifulSoup(body, 'html.parser'))
    for item in soup.select('.site-nav a'):
        item.attrs.pop('aria-current', None)
        if item.get_text(strip=True) in ('Blogs', 'Blog'):
            item.string = 'Blog'
            item['href'] = local('blogs.html', path)
            item['aria-current'] = 'page'
    footer = soup.select_one('.footer-col:nth-of-type(2)')
    footer.clear()
    footer.append(BeautifulSoup('<h4>Explore</h4>' + ''.join(anchor(dest,label,path) for dest,label in [('blogs.html','Blog'),('resources/index.html','Resources'),('guides/index.html','Guides & Tools'),('resources/linkedin-posts.html','LinkedIn Posts'),('resources/media.html','Media')]), 'html.parser'))
    (ROOT / path).write_text(str(soup).rstrip() + '\n')

def identity():
    return [
        {'@type':'Organization','@id':BASE+'#organization','name':'Centripetal Advisors','url':'https://centripetaladvisors.com/','logo':BASE+'assets/logo-light.png'},
        {'@type':'WebSite','@id':BASE+'#website','name':'Centripetal Advisors — Website Concept','url':BASE,'publisher':{'@id':BASE+'#organization'}}]

def breadcrumbs(path, title=None):
    items = [{'@type':'ListItem','position':1,'name':'Home','item':BASE},{'@type':'ListItem','position':2,'name':'Blog','item':BASE+'blogs.html'}]
    if title:
        items.append({'@type':'ListItem','position':3,'name':title,'item':BASE+path})
    return {'@type':'BreadcrumbList','itemListElement':items}

topics = list(dict.fromkeys(a['topic'] for a in DATA['articles']))
topic_id = lambda value: re.sub(r'[^a-z0-9]+','-',value.lower()).strip('-')
path = 'blogs.html'
body = '<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Blog · Centripetal Advisors</p><h1>Perspectives on the decisions behind the numbers.</h1><p>Focused article concepts on SaaS finance, capital, and the operating questions founders face.</p></div></header>'
body += '<nav class="ca-reader-nav" aria-label="Article topics"><div class="ca-reader-inner"><p class="ca-reader-label">Explore a topic</p><ul>' + ''.join(f'<li><a href="#{topic_id(topic)}">{escape(topic)}</a></li>' for topic in topics) + '</ul></div></nav>'
body += '<div class="ca-resource-byline"><div class="ca-reader-inner">Article concepts · Content and factual review pending.</div></div>'
for topic in topics:
    cards = []
    for a in DATA['articles']:
        if a['topic'] != topic:
            continue
        cards.append('<article class="ca-card"><p class="ca-eyebrow">Article concept</p><h3>' + escape(a['title']) + '</h3><p>' + escape(a['question']) + '</p>' + anchor('blog/'+a['slug']+'.html','Read the article concept →',path,'Read article concept: '+a['title']) + '</article>')
    body += section(topic, 'A focused question to explore before the next decision.', '<div class="ca-grid">'+''.join(cards)+'</div>', topic_id(topic))
body += section('Put the perspective to work.', 'Guides bring the wider framework and working review. Services explain the finance work and how Centripetal can support it.', anchor('guides/index.html','Explore practical guides →',path)+'<p class="ca-footer">'+anchor('services.html','Explore Centripetal’s services →',path)+'</p>', stone=True)
graph = identity() + [
    {'@type':'CollectionPage','@id':BASE+path+'#page','name':'SaaS Finance Insights','url':BASE+path,'isPartOf':{'@id':BASE+'#website'},'mainEntity':{'@id':BASE+path+'#articles'}},
    {'@type':'ItemList','@id':BASE+path+'#articles','itemListElement':[{'@type':'ListItem','position':i+1,'name':a['title'],'url':BASE+'blog/'+a['slug']+'.html'} for i,a in enumerate(DATA['articles'])]},
    breadcrumbs(path)]
shell(path, 'SaaS Finance Insights | Centripetal Advisors', 'Read Centripetal Advisors insights on SaaS finance, financial strategy, fundraising, and the operating decisions facing founders.', body, graph)

for a in DATA['articles']:
    path = 'blog/' + a['slug'] + '.html'
    content = BeautifulSoup(a['body_html'], 'html.parser')
    ids = {x['id'] for x in content.select('[id]')}
    for heading in content.select('h2'):
        if not heading.get('id'):
            candidate = topic_id(heading.get_text(' ', strip=True))
            suffix = 2
            while candidate in ids:
                candidate = topic_id(heading.get_text(' ',strip=True)) + '-' + str(suffix)
                suffix += 1
            heading['id'] = candidate
            ids.add(candidate)
        heading['tabindex'] = '-1'
    toc = '<nav class="ca-reader-nav" aria-label="On this page"><div class="ca-reader-inner"><p class="ca-reader-label">On this page</p><ul>' + ''.join(f'<li><a href="#{h["id"]}">{escape(h.get_text(" ",strip=True))}</a></li>' for h in content.select('h2')) + '</ul></div></nav>'
    hero = '<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Blog · '+escape(a['topic'])+' · Article concept</p><h1>'+escape(a['title'])+'</h1><p>'+escape(a['question'])+'</p></div></header>'
    status = '<div class="ca-resource-byline"><div class="ca-reader-inner">'+anchor('blogs.html','← Back to Blog',path)+'<span>Concept article · Content and factual review pending.</span></div></div>'
    reading = '<section class="ca-section"><article class="ca-guide-article" data-article-body="">'+str(content)+'</article></section>'
    guide_name = BeautifulSoup((ROOT/a['guide']).read_text(),'html.parser').find('h1').get_text(' ',strip=True)
    service_name = BeautifulSoup((ROOT/a['service']).read_text(),'html.parser').find('h1').get_text(' ',strip=True)
    format_label, format_action = ('Preparation tool','Use the builder →') if 'board-deck-builder' in a['guide'] else (('Assessment','Explore the assessment →') if 'scorecard' in a['guide'] else ('Related guide','Explore the guide →'))
    next_step = section('Work through the wider question.', 'Continue with the related framework or explore the finance support connected to this topic.', '<div class="ca-grid ca-resource-formats"><article class="ca-card"><p class="ca-eyebrow">'+escape(format_label)+'</p><h3>'+escape(guide_name)+'</h3>'+anchor(a['guide'],format_action,path)+'</article><article class="ca-card"><p class="ca-eyebrow">Related service</p><h3>'+escape(service_name)+'</h3>'+anchor(a['service'],'Explore the service →',path)+'</article></div>', stone=True)
    graph = identity() + [{'@type':'WebPage','@id':BASE+path+'#page','name':a['title'],'url':BASE+path,'description':a['question'],'isPartOf':{'@id':BASE+'#website'},'relatedLink':[BASE+a['guide'],BASE+a['service']]} , breadcrumbs(path,a['title'])]
    # No Article publication dates or personal authorship are asserted for unreviewed concepts.
    shell(path,a['title']+' | Centripetal Advisors',a['question'],hero+status+toc+reading+next_step,graph)
    soup = BeautifulSoup((ROOT/path).read_text(),'html.parser')
    css = soup.new_tag('link',rel='stylesheet',href='../assets/resource-library.css?v=20261009-3')
    soup.head.append(css)
    (ROOT/path).write_text(str(soup).rstrip()+'\n')

# Keep the legacy collection URL usable, with one canonical catalog destination.
path = 'blog/index.html'
body = '<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Centripetal Advisors · Blog</p><h1>Explore the Blog.</h1><p>Perspectives on finance, capital, and the decisions facing SaaS founders.</p></div></header>'
body += section('Find the article for your question.', 'Browse the article collection by topic, or continue to a practical guide.', anchor('blogs.html','Browse the Blog →',path)+'<p class="ca-footer">'+anchor('guides/index.html','Explore practical guides →',path)+'</p>')
shell(path,'Explore the Blog | Centripetal Advisors','Find Centripetal’s Blog catalog and practical SaaS finance guides.',body,identity()+[breadcrumbs(path)],canonical=BASE+'blogs.html')

print('Built one Blog catalog, fifteen article concepts, and a legacy catalog entry path.')
