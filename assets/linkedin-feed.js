// Progressive enhancement: introductions remain readable without JavaScript.
(() => {
  const feed = document.querySelector('.ca-linkedin-layout');
  if (!feed) return;
  const posts = [...feed.querySelectorAll('.ca-linkedin-card')];
  const links = [...feed.querySelectorAll('.ca-linkedin-rail nav a[data-topic]')];
  const introductions = [...feed.querySelectorAll('.ca-linkedin-introduction')];
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const running = new Set();

  function syncMotion() {
    feed.dataset.motionMode = motion.matches ? 'reduced' : 'full';
    if (motion.matches) running.forEach(animation => animation.finish());
  }
  syncMotion();
  motion.addEventListener('change', syncMotion);

  if ('IntersectionObserver' in window) {
    const entrances = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const introduction = entry.target;
        if (introduction.dataset.revealState === 'complete') return;
        entrances.unobserve(introduction);
        introduction.dataset.revealState = 'complete';
        if (motion.matches || typeof introduction.animate !== 'function') return;
        const animation = introduction.animate([
          {opacity: 0.2, transform: 'translateY(12px)'},
          {opacity: 1, transform: 'translateY(0)'}
        ], {duration: 440, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'none'});
        running.add(animation);
        animation.addEventListener('finish', () => running.delete(animation), {once: true});
      });
    }, {threshold: 0.12});
    introductions.forEach(introduction => entrances.observe(introduction));
  }

  // Track the post crossing the reading line, including gaps between entries.
  let scheduled = false;
  function updateTopic() {
    scheduled = false;
    const readingLine = Math.min(220, Math.max(120, window.innerHeight * 0.25));
    const bounds = feed.getBoundingClientRect();
    let current = null;
    if (bounds.top <= readingLine && bounds.bottom > readingLine) {
      current = posts[0];
      posts.forEach(post => {
        if (post.getBoundingClientRect().top <= readingLine) current = post;
      });
    }
    links.forEach(link => {
      if (current && link.dataset.topic === current.dataset.topic) {
        link.setAttribute('aria-current', 'location');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }
  function scheduleTopic() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(updateTopic);
  }
  window.addEventListener('scroll', scheduleTopic, {passive: true});
  window.addEventListener('resize', scheduleTopic);
  window.addEventListener('hashchange', scheduleTopic);
  updateTopic();
})();
