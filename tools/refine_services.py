"""Build the service concept copy into the existing concept page shells."""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape as e
from urllib.parse import urlencode
import json

ROOT=Path(__file__).resolve().parents[1]
CONTENT=json.loads((ROOT/'tools/service-content.json').read_text())

def paragraphs(items):return ''.join(f'<p>{e(x)}</p>' for x in items)
def contact_link(topic,source,prefix='../'):
    return prefix+'contact.html?'+urlencode({'topic':topic,'from':source})+'#conversation-form'

for slug,c in CONTENT.items():
    path=ROOT/'services'/f'{slug}.html'
    soup=BeautifulSoup(path.read_text(),'html.parser')
    soup.select_one('.concept-hero p:not(.eyebrow)').string=c['intro']
    html=f'<article class="service-copy"><h2 id="read-1" tabindex="-1">{e(c["trigger"])}</h2>'+paragraphs(c['situation'])
    html+='<h2 id="read-2" tabindex="-1">The work we help you own</h2>'
    html+=''.join(f'<h3>{e(title)}</h3><p>{e(body)}</p>' for title,body in c['scope'])
    html+='<h2 id="read-3" tabindex="-1">Working outputs</h2><p>These are practical materials the work can produce. We agree priorities and deliverables around your company and the engagement scope.</p><dl class="ca-service-outputs">'
    html+=''.join(f'<div><dt>{e(title)}</dt><dd>{e(body)}</dd></div>' for title,body in c['outputs'])+'</dl>'
    html+='<div class="ca-working-decision"><p class="ca-eyebrow">A decision this work can clarify</p><h2 id="working-decision" tabindex="-1">'+e(c['decision'][0])+'</h2><dl>'
    html+=''.join(f'<div><dt>{label}</dt><dd>{e(body)}</dd></div>' for label,body in zip(['Working inputs','The analysis','A useful output'],c['decision'][1:]))+'</dl></div>'
    html+='<h2 id="read-4" tabindex="-1">How we begin</h2><ol class="ca-service-steps">'
    html+=''.join(f'<li>{e(step)}</li>' for step in c['begin'])+'</ol>'
    html+='<section class="faq-section"><h2 id="read-5" tabindex="-1">Questions founders ask</h2>'
    html+=''.join(f'<details><summary>{e(q)}</summary><div class="faq-answer">{e(a)}</div></details>' for q,a in c['faqs'])+'</section></article>'
    soup.select_one('.service-copy').replace_with(BeautifulSoup(html,'html.parser').article)
    toc=soup.select_one('.ca-reader-nav ul');toc.clear()
    for target,label in [('read-1',c['trigger']),('read-2','The work we help you own'),('read-3','Working outputs'),('working-decision','A working decision'),('read-4','How we begin'),('read-5','Questions founders ask')]:
        li=soup.new_tag('li');a=soup.new_tag('a',href='#'+target);a.string=label;li.append(a);toc.append(li)
    cta=soup.select_one('.home-cta');cta.h2.string=c['cta'];cta.p.string=c['ctaDetail']
    a=cta.select_one('.pill-button');a.string=c['cta'];a['href']=contact_link(c['topic'],'service-'+slug)
    if slug == 'board-investor-reporting':
        sidebar=soup.select_one('.service-sidebar')
        if not sidebar.select_one('a[href*="board-deck-builder"]'):
            link=soup.new_tag('a',href='../guides/tools/board-deck-builder.html');link.string='Build the board conversation outline →';sidebar.select_one('a').insert_before(link)
    # Correct historical double escaping in the related-service labels.
    for a in soup.select('.service-sidebar a'):
        if a.string:a.string=a.string.replace('&amp;','&')
    for l in soup.select('link[href*="foundations.css"]'):l['href']='../assets/foundations.css?v=20261009-9'
    path.write_text(str(soup).rstrip()+'\n')

overview=ROOT/'assets/services-detail.inc'
soup=BeautifulSoup(overview.read_text(),'html.parser')
for old in soup.select('.ca-service-trigger, .ca-service-scope'):old.decompose()
for old in soup.select('details'):
    if old.summary.get_text() in ['What should we bring to the first conversation?','Are these six separate packages?']:old.decompose()
cards=soup.select('.ca-card')
card_copy={
    'fractional-cfo-for-saas':('Finance still runs through the founder.','Connect the operating model, finance owners, capital decisions, and reporting cadence.'),
    'fundraising-readiness':('A raise is approaching.','Prepare financial statements, customer schedules, cap table records, and use-of-proceeds scenarios.'),
    'cash-flow-runway-planning':('Cash timing could change a commitment.','Maintain a rolling 13-week cash view and compare hiring, collections, and financing scenarios.'),
    'board-investor-reporting':('The board needs a clearer decision.','Explain budget variances, operating assumptions, customer concentration, and the cash outlook.'),
    'venture-debt-readiness':('A debt facility is under consideration.','Connect lender evidence, proposed terms, draw timing, and repayment to the full capital plan.'),
    'treasury-finance-operations':('Approvals or handoffs are becoming fragile.','Clarify banking controls, the QuickBooks or Xero foundation, close ownership, and specialist coordination.')
}
for card in cards:
    link=card.select_one('a');slug=Path(link['href']).stem
    trigger,body=card_copy[slug]
    card.select_one('p:not(.ca-eyebrow)').string=body
    p=soup.new_tag('p',attrs={'class':'ca-service-trigger'});p.string=trigger;card.h3.insert_after(p)
    link.string='Explore '+card.h3.get_text()+' →'
new=BeautifulSoup('''<div class="ca-service-scope"><h2>One engagement.<br>Connected responsibilities.</h2><p class="ca-intro">These service areas connect within an embedded finance role. The work can extend from financial strategy to the accounting foundation, capital processes, revenue and sales analysis, tax and tax-credit coordination, and back-office ownership. We agree the responsibilities with your team and the specialists involved.</p><div class="ca-split"><div><h3>Begin with the work that needs an owner.</h3><p>An approaching financing, a revised hiring plan, a sharper board question, or an unreliable close can be the starting point. We review the existing records and processes, then prioritize the dependencies behind that decision.</p></div><div><h3>Make the outputs usable.</h3><p>A maintained model, a rolling cash forecast, financial schedules, succinct board materials, and a clear responsibility map should work together. The scope and cadence follow the company’s needs; these are examples rather than a fixed package or timetable.</p><a class="ca-link" href="about.html">Meet the firm behind the work →</a></div></div></div>''','html.parser').div
first_h2=soup.select_one('.ca-inner').find_all('h2',recursive=False)[1];first_h2.insert_before(new)
begin=soup.find('h3',string='How the engagement begins')
begin.parent.find('ol').clear()
for label,body in [('Map the decision and deadline.','Identify the financing, cash, board, or operational question and the people who own it today.'),('Review the supporting foundation.','Examine the books, customer schedules, cap table, model, cash view, and handoffs relevant to that question.'),('Agree the work and cadence.','Name priorities, deliverables, owners, and specialist responsibilities; revisit them as the company changes.')]:
    li=soup.new_tag('li');strong=soup.new_tag('strong');strong.string=label;li.append(strong);li.append(' '+body);begin.parent.ol.append(li)
last=soup.select_one('.ca-footer a');last['href']=contact_link('finance-leadership','services-overview','');last.string='Discuss the finance work that needs an owner →'
extra=BeautifulSoup('''<details><summary>What should we bring to the first conversation?</summary><p>Start with the decision or deadline, who owns finance today, and where your current model, reporting, or processes are falling short. You do not need to upload financial documents to begin the conversation.</p></details><details><summary>Are these six separate packages?</summary><p>They describe connected areas of finance work. The engagement scope follows the company’s needs, including coordination with its existing team and specialists.</p></details>''','html.parser')
soup.select_one('.ca-footer').insert_before(extra)
inner=str(soup).strip();overview.write_text(inner+'\n')
path=ROOT/'services.html';text=path.read_text();page=BeautifulSoup(text,'html.parser');old=page.select_one('#services-detail');old_inner=old.decode_contents();assert old_inner in text
text=text.replace(old_inner,inner,1);path.write_text(text)

# Add a single, specific next step to each curated guide, close to its conclusion.
guide_map={
    'saas-finance-scorecard':('finance-foundation','Discuss your finance priorities','Bring the categories that need attention and the decision or deadline behind them. Your scores stay in this page; they are not sent with the contact link.'),
    'series-a-diligence-readiness':('fundraising','Pressure-test your diligence plan','Start with the intended raise, your timeline, and the financial evidence or investor question that still needs work.'),
    'venture-debt-readiness':('venture-debt','Discuss your lender-readiness questions','Start with the intended use of capital, lender questions, and proposed terms if you have them.'),
    'treasury-hygiene':('finance-operations','Review your treasury setup','Start with the cash-access, payment-approval, or ownership gap you would like to resolve.'),
    'do-i-need-a-fractional-cfo':('finance-leadership','Talk through your finance leadership needs','Start with the work your founder still owns, the team supporting it, and the next inflection point.'),
    'first-90-days-after-raise':('cash-runway','Discuss the post-raise operating plan','Start with your use-of-proceeds plan, hiring commitments, and the cadence for reviewing cash and performance.')
}
for slug,(topic,label,body) in guide_map.items():
    path=ROOT/'guides'/f'{slug}.html';soup=BeautifulSoup(path.read_text(),'html.parser')
    for old in soup.select('.ca-guide-next, .cta-page'):old.decompose()
    cta=BeautifulSoup(f'<section class="ca-section ca-guide-next"><div class="ca-inner"><p class="ca-eyebrow">Connect the framework to your company</p><h2>{e(label)}</h2><p class="ca-intro">{e(body)}</p><a class="pill-button" href="{e(contact_link(topic,"guide-"+slug))}">{e(label)} →</a></div></section>','html.parser').section
    soup.main.append(cta)
    # Existing conclusion CTAs lead to the same contextual destination.
    for a in soup.select('main a[href="../contact.html"], .cta-page a[href="../contact.html"]'):
        a['href']=contact_link(topic,'guide-'+slug)
    for l in soup.select('link[href*="foundations.css"]'):l['href']='../assets/foundations.css?v=20261009-9'
    path.write_text(str(soup).rstrip()+'\n')
