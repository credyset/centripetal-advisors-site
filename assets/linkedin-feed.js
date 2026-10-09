// Create a LinkedIn frame only after its native disclosure is opened.
document.querySelectorAll('[data-linkedin-embed]').forEach(disclosure => {
  const label = disclosure.querySelector('[data-embed-label]');
  disclosure.addEventListener('toggle', () => {
    label.textContent = disclosure.open ? 'Hide LinkedIn preview' : 'View LinkedIn preview';
    if (!disclosure.open || disclosure.querySelector('iframe')) return;
    const url = new URL(disclosure.dataset.embedUrl);
    if (url.origin !== 'https://www.linkedin.com' || !url.pathname.startsWith('/embed/feed/update/')) return;
    const frame = document.createElement('iframe');
    frame.src = url.href;
    frame.title = 'LinkedIn post by Charles Solomon: ' + disclosure.dataset.embedTitle;
    frame.width = '504';
    frame.height = disclosure.dataset.embedHeight;
    frame.loading = 'lazy';
    frame.referrerPolicy = 'no-referrer';
    frame.allowFullscreen = true;
    disclosure.querySelector('[data-embed-frame]').append(frame);
  });
});
