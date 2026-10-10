/* Preview-only behavior. The published Framer renderer owns the visual page. */
(() => {
  const metadata={"index.html": ["Fractional CFO Services for SaaS | Centripetal Advisors", "Embedded strategic CFO services for Seed and Series A SaaS founders. Connect capital strategy, cash planning, board reporting, and finance operations."], "services.html": ["Strategic CFO Services for SaaS | Centripetal Advisors", "Explore fractional CFO support, fundraising readiness, cash planning, board reporting, venture debt, and treasury operations for early-stage SaaS."], "contact.html": ["Contact Centripetal Advisors | SaaS Finance Leadership", "Talk with Centripetal Advisors about embedded finance leadership, capital strategy, and the financial decisions facing your SaaS company."], "blogs.html": ["SaaS Finance Insights | Centripetal Advisors", "Read Centripetal Advisors insights on SaaS finance, financial strategy, fundraising, and the operating decisions facing founders."], "privacy-policy.html": ["Privacy Policy | Centripetal Advisors", "Read the Centripetal Advisors privacy policy covering information collection, use, and contact details."]};
  const root = new URL('../', document.currentScript.src);
  const routes = {'/':'index.html','/services':'services.html','/contact':'contact.html','/blogs':'blogs.html','/guides':'guides/index.html','/resources':'resources/index.html','/google-sheets---html/saas-finance-scorecard':'guides/saas-finance-scorecard.html','/privacy-policy':'privacy-policy.html'};
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
    notice.textContent='Your message has not been sent or saved. This is the concept preview of the conversation path.';
  };
  // Capture before the copied renderer can dispatch a production form request.
  window.addEventListener('submit',stopForm,true);
  window.addEventListener('click',event => {
    const target=event.target instanceof Element ? event.target : event.target.parentElement;
    const button=target?.closest('button');
    if(button?.closest('form') && (!button.type || button.type==='submit' || button.matches('[data-reset="button"], [data-preview-submit]'))) {stopForm(event);return;}
    const anchor=target?.closest('a[href]');
    if(!anchor) return;
    const destination=routeFor(anchor) || (anchor.origin===location.origin && Object.values(routes).some(file=>anchor.pathname===new URL(file,root).pathname) ? anchor.href : null);
    if(!destination) return;
    // Preserve browser modified-click behavior, using the rewritten local URL.
    if(event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button!==0) return;
    event.preventDefault();event.stopImmediatePropagation();location.assign(destination);
  },true);
  const keepPreviewMetadata = () => {
    const file=location.pathname.split('/').pop() || 'index.html';
    const page=metadata[file];
    if(page){
      if(document.title!==page[0]) document.title=page[0];
      [['name','description',page[1]],['property','og:title',page[0]],['property','og:description',page[1]],['name','twitter:title',page[0]],['name','twitter:description',page[1]]].forEach(([attribute,key,value])=>{
        const meta=document.head.querySelector(`meta[${attribute}="${key}"]`);
        if(meta && meta.content!==value) meta.content=value;
      });
    }
    const robots=[...document.querySelectorAll('meta[name="robots"]')];
    if(!robots.length) {const meta=document.createElement('meta');meta.name='robots';meta.content='noindex, follow';document.head.appendChild(meta);}
    robots.forEach(meta=>{if(meta.content!=='noindex, follow') meta.content='noindex, follow';});
    const canonical=document.querySelector('link[rel="canonical"]');
    // Preview topic/source/revision parameters must not create canonical variants.
    const destination='https://credyset.github.io/centripetal-advisors-site/'+(file==='index.html'?'':file);
    if(canonical && canonical.href!==destination) canonical.href=destination;
  };
  // The native additions are authored outside the copied React root, then placed
  // after its commit. They remain readable at the end of the page without JS.
  let returnNavFocus=false;
  const enhance = () => {
    const main=document.getElementById('main');
    if(!main)return;
    const resource=document.getElementById('founder-resources');
    const why=main.querySelector('[data-framer-name="Why Centripetal"]');
    if(resource && why && resource.nextElementSibling!==why) why.before(resource);
    const detail=document.getElementById('services-detail');
    const contact=[...main.querySelectorAll('[data-framer-name="Contact"]')].find(node=>node.getBoundingClientRect().height>0);
    if(detail && contact){
      // Captured phone layouts use explicit flex ordering through display:contents.
      detail.style.order=getComputedStyle(contact).order;
      if(detail.nextElementSibling!==contact) contact.before(detail);
    }
    if(location.pathname.endsWith('/contact.html'))document.dispatchEvent(new Event('ca:contact-ready'));
    main.querySelectorAll('.framer-18nscdd').forEach(blog=>{
      if(!blog.parentElement.querySelector('.ca-nav-resource')){
        const link=document.createElement('a');link.className='ca-nav-resource';link.href=new URL('resources/index.html',root).href;link.textContent='Resources';blog.after(link);
      }
    });
    main.querySelectorAll('nav.framer-xzdiZ').forEach(nav=>{
      nav.setAttribute('aria-label','Primary navigation');
      nav.querySelectorAll('a[href]').forEach(anchor=>{
        if(anchor.href===new URL('index.html',root).href && !anchor.textContent.trim())anchor.setAttribute('aria-label','Centripetal Advisors home');
      });
      if(!nav.dataset.framerName?.startsWith('Phone'))return;
      if(!nav.dataset.caEscape){
        nav.dataset.caEscape='true';
        nav.addEventListener('keydown',event=>{
          if(event.key==='Escape' && nav.dataset.framerName==='Phone Open'){
            const close=nav.querySelector('[aria-label="Close navigation"]');
            if(close){event.preventDefault();returnNavFocus=true;close.click();}
          }
        });
      }
      nav.querySelectorAll('[data-highlight]:not([data-framer-name="Top"])').forEach(icon=>{
        icon.setAttribute('role','button');
        icon.setAttribute('tabindex','0');
        icon.setAttribute('aria-label',nav.dataset.framerName==='Phone Open'?'Close navigation':'Open navigation');
        icon.setAttribute('aria-expanded',String(nav.dataset.framerName==='Phone Open'));
        if(!icon.dataset.caKeyboard){
          icon.dataset.caKeyboard='true';
          icon.addEventListener('keydown',event=>{
            if(event.key==='Enter' || event.key===' '){event.preventDefault();icon.click();}
          });
        }
      });
    });
    if(returnNavFocus){
      const open=[...main.querySelectorAll('[aria-label="Open navigation"]')].find(node=>node.getBoundingClientRect().height>0);
      if(open){open.focus();returnNavFocus=false;}
    }
    main.querySelectorAll('a[href="https://www.linkedin.com/company/centripetal-advisors/"]').forEach(anchor=>{
      if(!anchor.textContent.trim())anchor.setAttribute('aria-label','Centripetal Advisors on LinkedIn');
      anchor.closest('nav')?.setAttribute('aria-label','Footer links');
    });
    const about=[...main.querySelectorAll('[data-framer-name="About Us"]')].find(node=>node.getBoundingClientRect().height>0);
    if(about && about.id!=='about-us')about.id='about-us';
    main.querySelectorAll('img').forEach(img=>{
      const src=img.getAttribute('src')||'';
      const alt=src.includes('GVi1rwbl0Np0mpeyTnQV5QEKo')?'Charles Solomon':
        /WQ1q0OGx3RXruG6eVdgzb2HcH8|N6tuqpRrg0TWlzKyAQRPrAGeQI0/.test(src)?'Financial co-pilot support across capital, reporting, and finance operations':
        /3pjhfd8MVgoYtbZakmULrzqk|EIPowl5lbjWkiRIGY1B6B2Fqs/.test(src)?'Centripetal Advisors':null;
      if(alt && img.alt!==alt)img.alt=alt;
    });
    rewrite();
  };
  let ready=false,scheduled=false;
  const scheduleEnhance=()=>{
    if(!ready || scheduled)return;scheduled=true;
    requestAnimationFrame(()=>{scheduled=false;enhance();});
  };
  document.addEventListener('ca:render-ready',()=>{ready=true;document.documentElement.dataset.caRendered='true';scheduleEnhance();});
  window.addEventListener('resize',scheduleEnhance);
  document.addEventListener('DOMContentLoaded',()=>{
    rewrite();keepPreviewMetadata();

    new MutationObserver(keepPreviewMetadata).observe(document.head,{childList:true,subtree:true,attributes:true,characterData:true,attributeFilter:['content','href']});
    new MutationObserver(()=>{rewrite();scheduleEnhance();}).observe(document.getElementById('main'),{childList:true,subtree:true,attributes:true,attributeFilter:['href']});
  });
})();
