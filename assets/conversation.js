/* Topic-aware concept conversation. Only fixed topic/source slugs enter URLs.
   Draft fields stay in memory; nothing is stored, tracked, or transmitted. */
(() => {
  const panel=document.getElementById('conversation-context');
  if(!panel)return;
  const topics={
    general:{title:'Start a conversation',intro:'Start with the decision in front of you and the finance work behind it.',prompts:['What decision or deadline is approaching?','Who owns finance today?','What would you like to clarify?']},
    'finance-leadership':{title:'Discuss your finance leadership needs',intro:'Connect the work your company needs to the people who own it.',prompts:['Which finance decisions still run through the founder?','Who supports bookkeeping, reporting, and forecasting today?','What is the next inflection point or deadline?']},
    fundraising:{title:'Discuss the finance work behind your raise',intro:'Start with the capital plan and the evidence that still needs work.',prompts:['What milestones would the raise fund?','What is your intended financing timeline?','Which financial schedules or investor questions need attention?']},
    'cash-runway':{title:'Pressure-test your cash plan',intro:'Start with the assumption or commitment that could change your next decision.',prompts:['Which hiring, spending, or financing decision needs a clearer cash view?','Which collection or payment assumptions are uncertain?','When does the decision need to be made?']},
    'board-reporting':{title:'Discuss your next board conversation',intro:'Connect the question your board needs to discuss to the evidence behind it.',prompts:['When is the next board meeting or investor update?','What decision or variance needs discussion?','What do the current materials leave unclear?']},
    'venture-debt':{title:'Discuss your lender-readiness questions',intro:'Connect the intended use of capital to the lender questions and repayment assumptions.',prompts:['How would the debt capital be used?','Are lender conversations or proposed terms already in progress?','Which cash or repayment assumptions need further review?']},
    'finance-operations':{title:'Review your treasury and finance setup',intro:'Start with the cash-control, close, or handoff gap creating pressure.',prompts:['Which approval, close, or back-office handoff needs attention?','Who owns that work today?','What changes as the company grows or someone is unavailable?']},
    'finance-foundation':{title:'Discuss your finance priorities',intro:'Bring the areas you want to strengthen and the decision behind them. Scorecard results are not included in this link.',prompts:['Which Scorecard categories deserve attention?','What decision or deadline makes those gaps important now?','Who currently owns the relevant finance work?']}
  };
  const sources={
    'services-overview':['Services','services.html'],
    'service-fractional-cfo-for-saas':['Fractional CFO for SaaS','services/fractional-cfo-for-saas.html'],
    'service-fundraising-readiness':['Fundraising Readiness','services/fundraising-readiness.html'],
    'service-cash-flow-runway-planning':['Cash Flow & Runway Planning','services/cash-flow-runway-planning.html'],
    'service-board-investor-reporting':['Board & Investor Reporting','services/board-investor-reporting.html'],
    'service-venture-debt-readiness':['Venture Debt Readiness','services/venture-debt-readiness.html'],
    'service-treasury-finance-operations':['Treasury & Finance Operations','services/treasury-finance-operations.html'],
    'tool-board-deck-builder':['Board Deck Structure Builder','guides/tools/board-deck-builder.html'],
    'guide-saas-finance-scorecard':['SaaS Finance Scorecard','guides/saas-finance-scorecard.html'],
    'guide-series-a-diligence-readiness':['Series A Diligence Readiness','guides/series-a-diligence-readiness.html'],
    'guide-venture-debt-readiness':['Venture Debt Readiness Checklist','guides/venture-debt-readiness.html'],
    'guide-treasury-hygiene':['Treasury Hygiene','guides/treasury-hygiene.html'],
    'guide-do-i-need-a-fractional-cfo':['Do I Need a Fractional CFO?','guides/do-i-need-a-fractional-cfo.html'],
    'guide-first-90-days-after-raise':['First 90 Days After Your Raise','guides/first-90-days-after-raise.html'],
    'guide-saas-cash-flow-mistakes':['Cash-Flow Mistakes & Forecast Review','guides/saas-cash-flow-mistakes.html']
  };
  const params=new URLSearchParams(location.search);
  const has=(object,key)=>Object.prototype.hasOwnProperty.call(object,key);
  const select=panel.querySelector('select');
  select.value=has(topics,params.get('topic'))?params.get('topic'):'general';
  const source=params.get('from');
  const back=panel.querySelector('[data-context-back]');
  if(has(sources,source)){back.href=new URL(sources[source][1],location.href).href;back.textContent='Return to '+sources[source][0]+' →';back.hidden=false;}
  const draft={Name:'',Email:'',Message:''};
  let firstPlacement=true;
  const visibleForm=()=>[...document.querySelectorAll('#main form')].find(form=>form.getBoundingClientRect().height>0);
  const setValue=(input,value)=>{
    if(input.value===value)return;
    const prototype=input.tagName==='TEXTAREA'?HTMLTextAreaElement.prototype:HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(prototype,'value').set.call(input,value);
    input.dispatchEvent(new Event('input',{bubbles:true}));
  };
  const place=()=>{
    if(document.documentElement.dataset.caRendered!=='true')return;
    const form=visibleForm();if(!form)return;
    form.id='conversation-form';
    const heading=form.querySelector('h1,h2');if(!heading)return;
    if(panel.parentElement!==form)heading.parentElement.after(panel);
    panel.hidden=false;
    const topic=topics[select.value];
    if(heading.textContent!==topic.title)heading.textContent=topic.title;
    for(const [name,value] of Object.entries(draft)){
      const input=form.querySelector(`[name="${name}"]`);
      if(!input)continue;
      // A browser-restored/autofilled value is retained on the first placement.
      if(firstPlacement && !value && input.value)draft[name]=input.value;
      else setValue(input,value);
    }
    const first=firstPlacement;firstPlacement=false;
    const message=form.querySelector('textarea[name="Message"]');
    message.placeholder=topic.prompts.join('\n');
    message.setAttribute('aria-describedby','ca-context-note');
    form.querySelectorAll('button[data-reset="button"]').forEach(button=>{
      button.dataset.previewSubmit='';button.type='button';
      const label=button.querySelector('p');
      if(label && label.textContent!=='Preview message')label.textContent='Preview message';
    });
    if(first && location.hash==='#conversation-form')requestAnimationFrame(()=>form.scrollIntoView({block:'start'}));
  };
  const update=()=>{
    const topic=topics[select.value];
    panel.querySelector('[data-context-intro]').textContent=topic.intro;
    const list=panel.querySelector('[data-context-prompts]');list.replaceChildren();
    topic.prompts.forEach(prompt=>{const li=document.createElement('li');li.textContent=prompt;list.append(li);});
    place();
  };
  document.addEventListener('input',event=>{
    const input=event.target;
    if(input.closest?.('#main form') && has(draft,input.name))draft[input.name]=input.value;
  });
  select.addEventListener('change',()=>{
    const url=new URL(location.href);url.searchParams.set('topic',select.value);
    if(!has(sources,url.searchParams.get('from')))url.searchParams.delete('from');
    history.replaceState(null,'',url);
    update();panel.querySelector('[data-context-status]').textContent='Conversation topic changed. Your message has been kept.';
  });
  panel.querySelector('[data-add-prompts]').addEventListener('click',()=>{
    const form=visibleForm();if(!form)return;
    const message=form.querySelector('textarea[name="Message"]');
    const topic=topics[select.value];
    const template=topic.title+'\n\n'+topic.prompts.map(prompt=>prompt+'\n').join('\n');
    if(!message.value.includes(template.trim())){
      setValue(message,(message.value?message.value.trimEnd()+'\n\n':'')+template);
    }
    message.focus();
    panel.querySelector('[data-context-status]').textContent='Prompts added to your message. Edit them as you like; nothing has been sent.';
  });
  document.addEventListener('ca:contact-ready',place);
  update();
  // The helper places this panel only after the copied renderer has committed.
  // Defer initial insertion if its ready signal has not arrived yet.
})();
