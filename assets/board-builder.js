// A transient meeting-preparation outline; no financial inputs, storage, or scoring.
(() => {
  const builder = document.querySelector('[data-board-builder]');
  if (!builder) return;
  const data = JSON.parse(document.getElementById('board-builder-data').textContent);
  const areas = [...builder.querySelectorAll('[data-board-area]')];
  const update = () => {
    const focus = data.focuses.find(item => item.id === builder.querySelector('[name="board-focus"]:checked').value);
    const request = builder.querySelector('[name="board-request"]:checked').value;
    builder.querySelector('[data-board-opening]').textContent = request === 'decision'
      ? 'Open with the proposal, the alternatives, and the specific decision requested. Confirm the formal approval process separately.'
      : 'Open with the recommendation, the alternatives, and the input you want from the board.';
    builder.querySelector('[data-board-focus-outline] a').textContent = focus.title;
    const result = builder.querySelector('[data-board-focus-result]');
    result.replaceChildren();
    const title = document.createElement('h3'); title.textContent = focus.title; result.append(title);
    for (const [label, value] of [['', focus.body], ['Evidence to bring: ', focus.evidence], ['Discussion prompt: ', focus.question]]) {
      const p = document.createElement('p');
      if (label) { const strong = document.createElement('strong'); strong.textContent = label; p.append(strong); }
      p.append(document.createTextNode(value)); result.append(p);
    }
    const rows = areas.map(area => ({id: area.dataset.boardArea, title: area.dataset.title, state: area.querySelector('input:checked').value}));
    const count = state => rows.filter(row => row.state === state).length;
    builder.querySelector('[data-board-status]').textContent = `${focus.label} · ${request === 'decision' ? 'Decision requested' : 'Input requested'} · ${count('reviewed')} reviewed · ${count('followup')} for follow-up · ${count('pending')} not reviewed`;
    const open = [...rows.filter(row => row.state === 'followup'), ...rows.filter(row => row.state === 'pending')];
    const list = builder.querySelector('[data-board-followups]'); list.replaceChildren();
    for (const row of open) {
      const li = document.createElement('li'), a = document.createElement('a'), note = document.createElement('span');
      a.href = '#' + row.id; a.textContent = row.title;
      note.textContent = row.state === 'followup' ? 'Follow-up needed' : 'Not reviewed';
      li.append(a, note); list.append(li);
    }
    builder.querySelector('[data-board-empty]').hidden = open.length !== 0;
    const note = [
      'BOARD MEETING PREPARATION', 'Focus: ' + focus.label,
      'Request: ' + (request === 'decision' ? 'Decision on a proposal. Confirm formal approval requirements separately.' : 'Input on a recommendation.'),
      '', 'Opening: ' + builder.querySelector('[data-board-opening]').textContent, '',
      ...data.sections.flatMap((section, index) => [
        `${index + 1}. ${section.title}`, section.body,
        'Evidence: ' + section.evidence, 'Question: ' + section.question, ''
      ]),
      'FOCUS: ' + focus.title, focus.body, 'Evidence: ' + focus.evidence,
      'Question: ' + focus.question, '', 'EVIDENCE FOLLOW-UPS',
      ...open.map(row => `${row.title} — ${row.state === 'followup' ? 'Follow-up needed' : 'Not reviewed'}: ${data.sections.find(section => section.id === row.id).evidence}`),
      ...(open.length ? [] : ['All six areas marked reviewed. This records your review; it does not verify the evidence.']),
      '', 'Before the meeting: name an evidence owner and next review date for each open area.',
      'Working concept — editorial framework for firm review. Adapt to your board agenda.'
    ].join('\n');
    builder.querySelector('[data-board-note]').value = note;
    builder.querySelector('[data-copy-status]').textContent = '';

  };
  builder.querySelector('[data-copy-note]').addEventListener('click', async () => {
    const note = builder.querySelector('[data-board-note]');
    const status = builder.querySelector('[data-copy-status]');
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(note.value);
      status.textContent = 'Preparation note copied.';
    } catch {
      note.focus(); note.select();
      status.textContent = 'The note is selected. Use your device’s Copy command to keep it.';
    }
  });
  builder.addEventListener('change', update);
  builder.querySelector('[data-board-reset]').addEventListener('click', () => {
    builder.querySelector('[name="board-focus"][value="operating"]').checked = true;
    builder.querySelector('[name="board-request"][value="input"]').checked = true;
    areas.forEach(area => area.querySelector('[value="pending"]').checked = true);
    update();
  });
  builder.querySelector('[data-board-review-result]').hidden = false;
  update();
})();
