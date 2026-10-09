"""Build the guide reference independently of the other page compositions."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,html
ROOT=Path(__file__).resolve().parents[1]
PATH='guides/saas-cash-flow-mistakes.html'
BASE='https://credyset.github.io/centripetal-advisors-site/'
D=json.loads((ROOT/'tools/cash-guide-content.json').read_text())
e=lambda v:html.escape(v,quote=True)
soup=BeautifulSoup((ROOT/PATH).read_text(),'html.parser')
soup.body['class']=['ca-native','ca-cash-guide-reference']
for node in soup.select('link[href*="cash-guide-reference"],.guide-editorial'):node.decompose()
css=soup.new_tag('link',rel='stylesheet',href='../assets/cash-guide-reference.css?v=20261009-1');soup.head.append(css)
for node in soup.select('script[src*="cash-review"]'):node['src']='../assets/cash-review.js?v=20261009-3'
for a in soup.select('.site-nav a'):
 if a.get_text(strip=True)=='Blogs':a.string='Blog'
 if a.get_text(strip=True)=='Resources':a['aria-current']='page'
title='SaaS Cash-Flow Forecast Review | Centripetal Advisors'
desc='Review collection timing, dated commitments, customer dependence, and forecast ownership before your next SaaS cash decision. Includes a five-area review worksheet.'
soup.title.string=title
for attr,key,value in [('name','description',desc),('property','og:title',title),('name','twitter:title',title),('property','og:description',desc),('name','twitter:description',desc)]:
 node=soup.find('meta',attrs={attr:key})
 if node:node['content']=value
schema=json.loads(soup.find('script',type='application/ld+json').string)
schema['@graph']=[x for x in schema['@graph'] if x['@type']!='Article']
for x in schema['@graph']:
 if x['@type']=='WebPage':x['name']=title;x['description']=desc
 if x['@type']=='BreadcrumbList':
  x['itemListElement']=[{'@type':'ListItem','position':i+1,'name':name,'item':BASE+path} for i,(name,path) in enumerate([('Home',''),('Resources','resources/index.html'),('Guides & Tools','guides/index.html'),('Cash forecast review',PATH)])]
soup.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
hero='<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Cash &amp; runway · Guide with review worksheet</p><h1>Five cash-flow mistakes that distort SaaS runway.</h1><p>Trace the assumptions behind the next commitment—and identify the evidence that could change it.</p></div></header>'
intro='''<section class="ca-section ca-guide-opening"><div class="ca-inner"><nav class="ca-guide-breadcrumb" aria-label="Breadcrumb"><a href="../resources/index.html">Resources</a><span aria-hidden="true">/</span><a href="index.html">Guides &amp; Tools</a><span aria-hidden="true">/</span><span>Cash forecast review</span></nav><div class="ca-guide-opening-grid"><div><p class="ca-eyebrow">For Seed and Series A SaaS founders</p><h2 id="cash-decision" tabindex="-1">How do you pressure-test a cash forecast before committing spend?</h2><p class="ca-guide-lead">Start with one decision and its deadline. Trace the cash it depends on to dated receipts, committed payments, and reconciled opening balances. Then test the assumption most likely to move—and identify which commitment changes if it does.</p><p>A forecast can be mathematically correct and still carry an unsupported payment date or an unowned assumption. These five reviews help connect the model to the operating decision.</p><div class="ca-guide-actions"><a class="pill-button" href="#collections">Read the five reviews →</a><a class="ca-link" href="#review">Go to the worksheet →</a></div></div><aside class="ca-guide-intro-note" aria-label="What this guide helps you do"><p class="ca-eyebrow">Leave with</p><ul><li>The receipt or commitment that needs a closer look.</li><li>The evidence and owner behind that assumption.</li><li>A follow-up list for your finance conversation.</li></ul><p>This is an evidence review. It does not calculate runway.</p></aside></div><p class="ca-guide-review-note"><a href="../about.html">Centripetal Advisors</a> · Working concept · Framework and wording for firm review.</p></div></section>'''
nav='<aside class="ca-guide-contents"><nav aria-label="On this page"><p class="ca-eyebrow">In this guide</p><ol>'+''.join(f'<li><a href="#{s["id"]}">{e(s["label"])}</a></li>' for s in D['sections'])+'</ol><a href="#example">A receipt moves →</a><a href="#review">Review worksheet →</a><a href="#questions">Questions &amp; sources →</a><button class="ca-print-button" hidden type="button">Print this page</button></nav></aside>'
reading=''.join('<section class="ca-guide-chapter">'+s['body_html']+'</section>' for s in D['sections'])
example='''<section class="ca-guide-chapter ca-guide-worked"><p class="ca-eyebrow">Illustrative decision · no client results</p><h2 id="example" tabindex="-1">A hire depends on one invoice.</h2><p>The receipt is expected before the new hire’s first payroll run. Move that receipt until after payroll, keeping the other assumptions unchanged. The question becomes which commitment depends on that timing.</p><div class="ca-guide-timing"><div><p class="ca-eyebrow">Planned timing</p><h3>Receipt, then payroll</h3><p>The customer payment is expected to support the first payroll commitment.</p></div><div><p class="ca-eyebrow">Alternative timing</p><h3>Payroll, then receipt</h3><p>The payment moves. Check cash and existing commitments in the affected weeks.</p></div></div><div class="ca-guide-evidence"><p><strong>Evidence to resolve:</strong> the billing milestone, payment terms, recent payment behavior, and collection owner.</p><p><strong>Decision to revisit:</strong> the hiring start date or another commitment, with leadership deciding how to respond.</p></div><p>The forecast makes the dependency visible. Keep the owner and next review date beside the assumption.</p></section>'''
body=hero+intro+'<section class="ca-section ca-guide-reading"><div class="ca-inner ca-guide-reading-layout">'+nav+'<article class="ca-guide-main" aria-label="Five cash forecast reviews">'+reading+example+'</article></div></section>'
review=BeautifulSoup(D['worksheet_html'],'html.parser')
for node in review.select('noscript'):node.decompose()
review.select_one('h2')['id']='review'
review.select_one('h2').string='Turn the review into a follow-up list.'
review.select_one('[data-review-fields]').insert(0,BeautifulSoup('<noscript><p>Enable JavaScript to generate the review list. You can still read the five reviews and use the questions to prepare a manual follow-up list.</p></noscript>','html.parser'))
review.select_one('[data-review-result]')['id']='cash-review-list'
review.select_one('[data-review-result]')['tabindex']='-1'
review.select_one('[data-review-fields]').insert(0,BeautifulSoup('<p class="ca-guide-review-jump"><a class="ca-link" href="#cash-review-list">View your review list →</a></p>','html.parser'))
review.select_one('[data-review-empty]').string='All five areas are marked reviewed. Keep the evidence, assumption owners, and next review date alongside the forecast. This records your review; it does not verify the forecast.'
for field in review.select('fieldset'):
 a=BeautifulSoup(f'<a class="ca-link ca-review-reference" href="#{field["data-target"]}">Review the evidence for this area →</a>','html.parser')
 field.append(a)
body+='<section class="ca-section ca-cash-review ca-guide-worksheet" data-cash-review>'+str(review)+'</section>'
questions=BeautifulSoup(D['questions_html'],'html.parser')
questions.select_one('.ca-guide-sources')['id']='sources'
body+='<section class="ca-section ca-guide-questions"><div class="ca-inner ca-guide-reading-layout"><div class="ca-guide-section-label"><p class="ca-eyebrow">Resolve the open question</p><p>Use the explanation and source material to prepare the next review with your team.</p></div><div class="ca-guide-main">'+str(questions)+'</div></div></section>'
body+='''<section class="ca-section ca-guide-next ca-stone"><div class="ca-inner"><p class="ca-eyebrow">Connect the evidence to your company</p><h2>Which cash assumption needs attention before your next decision?</h2><p class="ca-intro">Start with the commitment, deadline, and evidence you want to clarify. Worksheet selections stay on this page and are not included in the contact link.</p><div class="ca-guide-actions"><a class="pill-button" href="../contact.html?topic=cash-runway&amp;from=guide-saas-cash-flow-mistakes#conversation-form">Discuss your cash forecast →</a><a class="ca-link" href="../services/cash-flow-runway-planning.html">Explore cash planning support →</a></div><p class="ca-guide-related">Related article concept: <a class="ca-link" href="../blog/13-week-cash-flow-forecast.html">What a 13-week forecast shows—and what it hides →</a></p></div></section>'''
soup.main.clear();soup.main.append(BeautifulSoup(body,'html.parser'))
(ROOT/PATH).write_text(str(soup).rstrip()+'\n')
