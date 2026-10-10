// Progressive enhancement: introductions remain readable without JavaScript.
(() => {
  const feed = document.querySelector('.ca-media-layout');
  if (!feed) return;
  const episodes = [...feed.querySelectorAll('.ca-media-card')];
  const links = [...feed.querySelectorAll('.ca-media-rail nav a[data-episode]')];
  const introductions = [...feed.querySelectorAll('.ca-media-introduction')];
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

  // Track the episode crossing the reading line, including gaps between entries.
  let scheduled = false;
  function updateEpisode() {
    scheduled = false;
    const readingLine = Math.min(220, Math.max(120, window.innerHeight * 0.25));
    const bounds = feed.getBoundingClientRect();
    let current = null;
    if (bounds.top <= readingLine && bounds.bottom > readingLine) {
      current = episodes[0];
      episodes.forEach(episode => {
        if (episode.getBoundingClientRect().top <= readingLine) current = episode;
      });
    }
    links.forEach(link => {
      if (current && link.dataset.episode === current.dataset.episode) {
        link.setAttribute('aria-current', 'location');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }
  function scheduleEpisode() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(updateEpisode);
  }
  window.addEventListener('scroll', scheduleEpisode, {passive: true});
  window.addEventListener('resize', scheduleEpisode);
  window.addEventListener('hashchange', scheduleEpisode);
  updateEpisode();
})();
