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
if(checklist.length===24 && location.pathname.endsWith('series-a-diligence-readiness.html')){
  const bar=document.createElement('div');bar.className='ca-check-progress';
  const status=document.createElement('span');status.setAttribute('role','status');
  const reset=document.createElement('button');reset.type='button';reset.textContent='Reset checklist';
  const update=()=>{status.textContent=`${[...checklist].filter(input=>input.checked).length} of 24 diligence items checked · selections are not saved or submitted`;};
  reset.addEventListener('click',()=>{checklist.forEach(input=>input.checked=false);update();});
  checklist.forEach(input=>input.addEventListener('change',update));
  bar.append(status,reset);document.querySelector('header.concept-hero').after(bar);update();
}
