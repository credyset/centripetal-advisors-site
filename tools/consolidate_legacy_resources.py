"""Keep old resource URLs useful without exposing duplicate/unvalidated prototypes."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit
import json
from html import escape
ROOT=Path(__file__).resolve().parents[1]
BASE='https://credyset.github.io/centripetal-advisors-site/'
PAGES={
 'cfo-fit-calculator':('Compare your finance leadership needs.','The finance leadership guide replaces the earlier fit-calculator prototype. Compare responsibilities, continuity, and ownership against the work your company actually needs.','do-i-need-a-fractional-cfo.html','Read the finance leadership guide','This resource helps you prepare a scope and ownership brief. It does not calculate a staffing recommendation from revenue or a few inputs.'),
 'finance-diagnostic':('Use the SaaS Finance Scorecard.','One assessment now brings the eight finance areas together, with evidence-based self-review descriptions and a category breakdown.','saas-finance-scorecard.html','Open the Scorecard','The Scorecard adapts the category structure of Centripetal’s client diagnostic. It generates review prompts, not a funding-readiness verdict.'),
 'fundraise-readiness':('Prepare the evidence behind your raise.','The Series A guide combines the investor questions, evidence checklist, and working follow-up list in one place.','series-a-diligence-readiness.html','Read the Series A diligence guide','Use the inventory to locate records, assign owners, and resolve open questions against the actual request list. Completing a checklist does not establish that an investor will approve a round.'),
 'runway-modeler':('Start with the assumptions behind your cash plan.','The earlier runway-model prototype is not part of the current concept library. Its calculation assumptions and interpretation need validation before use.','saas-cash-flow-mistakes.html','Review the cash forecast guide','The cash guide provides a worked timing example and a review worksheet. It organizes follow-ups; it does not calculate runway. For a financing decision, compare the company’s dated receipts, commitments, and actual facility terms in a maintained model.')
}
for slug,(title,intro,target,action,method) in PAGES.items():
 path='guides/tools/'+slug+'.html'
 s=BeautifulSoup((ROOT/'guides/saas-cash-flow-mistakes.html').read_text(),'html.parser')
 for el in s.select('[href],[src]'):
  for attr in ('href','src'):
   value=el.get(attr)
   if not value or value.startswith(('http:','https:','data:','mailto:','#')):continue
   el[attr]='../'+value
 for el in s.select('link[href*="cash-guide-reference"],script[src*="cash-review"],.guide-editorial'):el.decompose()
 s.title.string=title.rstrip('.')+' | Centripetal Advisors'
 for meta in s.select('meta[name="description"],meta[property="og:description"],meta[name="twitter:description"]'):meta['content']=intro
 for meta in s.select('meta[property="og:title"],meta[name="twitter:title"]'):meta['content']=s.title.string
 canonical=BASE+'guides/'+target
 s.select_one('link[rel="canonical"]')['href']=canonical
 if s.select_one('meta[property="og:url"]'):s.select_one('meta[property="og:url"]')['content']=canonical
 s.select_one('script[type="application/ld+json"]').string=json.dumps({'@context':'https://schema.org','@type':'WebPage','name':title,'url':BASE+path,'isPartOf':{'@type':'WebSite','url':BASE},'relatedLink':canonical})
 s.main.clear()
 s.main.append(BeautifulSoup('<header class="concept-hero"><div class="concept-hero-inner"><p class="eyebrow">Centripetal Advisors · Guides &amp; Tools</p><h1>'+escape(title)+'</h1><p>'+escape(intro)+'</p></div></header><section class="ca-section"><div class="ca-inner"><h2>Continue with the current resource.</h2><p class="ca-intro">'+escape(method)+'</p><a class="ca-link" href="../'+target+'">'+escape(action)+' →</a><p><a class="ca-link" href="../index.html">Explore all Guides &amp; Tools →</a></p></div></section>','html.parser'))
 (ROOT/path).write_text(str(s).rstrip()+'\n')
print('Consolidated four legacy tool entry URLs into the current resource paths.')
