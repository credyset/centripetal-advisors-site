// Shared interactions; all core content and links are present without JavaScript.
document.querySelectorAll('.nav-toggle').forEach(button=>{
 const menu=document.getElementById(button.getAttribute('aria-controls'));
 const close=()=>{menu.classList.remove('open');button.setAttribute('aria-expanded','false');};
 button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')!=='true';menu.classList.toggle('open',open);button.setAttribute('aria-expanded',String(open));});
 button.closest('nav').addEventListener('keydown',event=>{if(event.key==='Escape'){close();button.focus();}});
 menu.querySelectorAll('a').forEach(link=>link.addEventListener('click',close));
});
document.querySelectorAll('[data-video]').forEach(button=>button.addEventListener('click',()=>{
 const frame=document.createElement('iframe');frame.className='testimonial-video';frame.title=button.dataset.title;
 frame.src='https://player.vimeo.com/video/'+button.dataset.video+'?autoplay=1';frame.allow='autoplay; fullscreen; picture-in-picture';frame.allowFullscreen=true;
 button.replaceWith(frame);
}));
document.querySelector('[data-calendar]')?.addEventListener('click',event=>{
 const panel=event.currentTarget.closest('.calendly-placeholder');
 const frame=document.createElement('iframe');frame.src='https://calendly.com/charles-centripetaladvisors/30min';frame.title='Schedule a conversation with Centripetal Advisors';frame.width='100%';frame.height='700';frame.style.border='0';
 panel.replaceWith(frame);
});
