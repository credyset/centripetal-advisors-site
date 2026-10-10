// Local evidence inventory; no readiness score, storage, or document submission.
(() => {
  const output = document.querySelector('[data-diligence-output]');
  if (!output) return;
  const items = [...document.querySelectorAll('.ca-doc')];
  const update = () => {
    const open = items.filter(item => !item.querySelector('input').checked);
    output.querySelector('[data-diligence-status]').textContent = `${open.length} items still to locate and review. Assign an owner and next action for each; confirm the actual diligence scope separately.`;
    const list = output.querySelector('[data-diligence-list]'); list.replaceChildren();
    for (const item of open) {
      const li = document.createElement('li'), link = document.createElement('a');
      link.href = '#' + item.id;
      link.textContent = item.querySelector('input').getAttribute('aria-label');
      li.append(link); list.append(li);
    }
    output.querySelector('.ca-open-items').hidden = open.length === 0;
    output.querySelector('[data-diligence-complete]').hidden = open.length !== 0;
  };
  document.addEventListener('change', update);
  // The existing reset button is created by foundations.js before this script.
  document.querySelector('.ca-check-progress button')?.addEventListener('click', update);
  output.hidden = false; update();
})();
