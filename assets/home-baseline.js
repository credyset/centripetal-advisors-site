/* Preview-only behavior. The published Framer renderer owns the visual page. */
(() => {
  const root = new URL('../', document.currentScript.src);
  const routes = {'/':'index.html','/services':'services.html','/contact':'contact.html','/blogs':'blogs.html','/privacy-policy':'privacy-policy.html'};
  const routeFor = anchor => {
    const raw=anchor.getAttribute('href');
    if(!raw || raw.startsWith('#')) return null;
    const url=new URL(raw, location.href);
    if(url.origin!==location.origin && url.origin!=='https://centripetaladvisors.com') return null;
    let path=url.pathname;
    if(path.startsWith(root.pathname)) path='/'+path.slice(root.pathname.length);
    path=path.replace(/\/$/,'') || '/';
    return routes[path] ? new URL(routes[path]+url.search+url.hash,root).href : null;
  };
  const rewrite = () => document.querySelectorAll('a[href]').forEach(anchor => {
    const destination=routeFor(anchor);
    if(destination && anchor.href!==destination) anchor.href=destination;
  });
  const stopForm = event => {
    event.preventDefault();event.stopImmediatePropagation();
    const form=event.target.closest('form');
    let notice=form.querySelector('[data-preview-notice]');
    if(!notice) {notice=document.createElement('p');notice.dataset.previewNotice='';notice.setAttribute('role','alert');form.appendChild(notice);}
    notice.textContent='Your message has not been sent. This is the concept preview. Please use Centripetal’s live contact page to send a message.';
  };
  // Capture before the copied renderer can dispatch a production form request.
  window.addEventListener('submit',stopForm,true);
  window.addEventListener('click',event => {
    const target=event.target instanceof Element ? event.target : event.target.parentElement;
    const button=target?.closest('button');
    if(button?.closest('form') && (!button.type || button.type==='submit')) {stopForm(event);return;}
    const anchor=target?.closest('a[href]');
    if(!anchor) return;
    const destination=routeFor(anchor) || (anchor.origin===location.origin && Object.values(routes).some(file=>anchor.pathname===new URL(file,root).pathname) ? anchor.href : null);
    if(!destination) return;
    // Preserve browser modified-click behavior, using the rewritten local URL.
    if(event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button!==0) return;
    event.preventDefault();event.stopImmediatePropagation();location.assign(destination);
  },true);
  const keepPreviewMetadata = () => {
    const robots=[...document.querySelectorAll('meta[name="robots"]')];
    if(!robots.length) {const meta=document.createElement('meta');meta.name='robots';meta.content='noindex, follow';document.head.appendChild(meta);}
    robots.forEach(meta=>{if(meta.content!=='noindex, follow') meta.content='noindex, follow';});
    const canonical=document.querySelector('link[rel="canonical"]');
    const destination=location.pathname===root.pathname || location.pathname===new URL('index.html',root).pathname ? root.href : location.href;
    if(canonical && canonical.href!==destination) canonical.href=destination;
  };
  document.addEventListener('DOMContentLoaded',()=>{
    rewrite();keepPreviewMetadata();
    new MutationObserver(keepPreviewMetadata).observe(document.head,{childList:true,subtree:true,attributes:true,attributeFilter:['content','href']});
    new MutationObserver(rewrite).observe(document.getElementById('main'),{childList:true,subtree:true,attributes:true,attributeFilter:['href']});
  });
})();
