// Native resource interactions. No tracking pixels, lead capture, or production requests.
document.querySelectorAll('.nav-toggle').forEach(button=>{
  const menu=document.getElementById(button.getAttribute('aria-controls'));
  const close=()=>{menu.classList.remove('open');button.setAttribute('aria-expanded','false');};
  button.addEventListener('click',()=>{
    const open=button.getAttribute('aria-expanded')!=='true';
    menu.classList.toggle('open',open);button.setAttribute('aria-expanded',String(open));
  });
  button.closest('nav').addEventListener('keydown',event=>{
    if(event.key==='Escape'){close();button.focus();}
  });
  menu.querySelectorAll('a').forEach(link=>link.addEventListener('click',close));
});
// No JavaScript? Keep navigation available using the same links and layout.
document.documentElement.classList.add('ca-js');
const checklist=document.querySelectorAll('input[type=checkbox]');
const checklists={'series-a-diligence-readiness.html':24,'venture-debt-readiness.html':17};
const expected=checklists[location.pathname.split('/').pop()];
if(expected && checklist.length===expected){
  const bar=document.createElement('div');bar.className='ca-check-progress';
  const status=document.createElement('span');status.setAttribute('role','status');
  const reset=document.createElement('button');reset.type='button';reset.textContent='Reset checklist';
  const update=()=>{status.textContent=`${[...checklist].filter(input=>input.checked).length} of ${expected} diligence items checked · selections are not saved or submitted`;};
  reset.addEventListener('click',()=>{
    checklist.forEach(input=>input.checked=false);update();
    document.dispatchEvent(new Event('ca:checklist-reset'));
  });
  checklist.forEach(input=>input.addEventListener('change',update));
  bar.append(status,reset);document.querySelector('header.concept-hero').after(bar);update();
}
document.querySelectorAll('.ca-print-button').forEach(button=>{
  button.hidden=false;
  button.addEventListener('click',()=>window.print());
});
// Printing disclosures should include their answers, then restore the reader's state.
let printDisclosures=[];
window.addEventListener('beforeprint',()=>{
  printDisclosures=[...document.querySelectorAll('details')].map(detail=>[detail,detail.open]);
  printDisclosures.forEach(([detail])=>{detail.open=true;});
});
window.addEventListener('afterprint',()=>{
  printDisclosures.forEach(([detail,open])=>{detail.open=open;});
  printDisclosures=[];
});
