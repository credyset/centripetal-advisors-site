
(function() {
  const numCategories = 8;
  const totalMin = 8;
  const totalMax = 40;
  const scores = {};

  const progressBar = document.getElementById('progress-bar');
  const completedCountEl = document.getElementById('completed-count');
  const runningTotalEl = document.getElementById('running-total');
  const totalScoreEl = document.getElementById('total-score');
  const pendingEl = document.getElementById('result-pending');
  const bandBlocks = document.querySelectorAll('.band-block');
  const resetButton = document.getElementById('reset-scorecard');
  const summary = document.getElementById('score-summary');
  const priorities = document.getElementById('score-priorities');
  const rows = document.getElementById('score-rows');
  const areas = [
    ['legal', 'Legal', 'Locate missing agreements and approvals, and review the requirements with counsel.', 'series-a-diligence-readiness.html', 'Organize diligence evidence'],
    ['cap_table', 'Cap Table', 'Reconcile ownership records and the instruments behind your dilution scenarios.', '../services/fundraising-readiness.html', 'Explore fundraising preparation'],
    ['team', 'Team', 'Clarify which finance decisions lack an owner and the scope the team needs.', 'do-i-need-a-fractional-cfo.html', 'Compare finance leadership needs'],
    ['systems', 'Systems', 'Identify where financial information is duplicated, delayed, or difficult to reconcile.', '../services/treasury-finance-operations.html', 'Explore finance operations'],
    ['treasury', 'Treasury & Banking', 'Review account access, payment approvals, and the ownership of cash controls.', 'treasury-hygiene.html', 'Review treasury controls'],
    ['accounting', 'Accounting', 'Find the reconciliations or close responsibilities that are still unresolved.', '../services/treasury-finance-operations.html', 'Explore finance operations'],
    ['finance', 'Finance', 'Connect the forecast assumptions to cash timing and the next operating decision.', '../services/cash-flow-runway-planning.html', 'Explore cash and runway planning'],
    ['investor_faq', 'Investor FAQ Readiness', 'Identify the questions that need a supporting schedule or a clearer explanation.', 'series-a-diligence-readiness.html', 'Work through investor questions']
  ];

  function updateNextSteps() {
    const complete = Object.keys(scores).length === numCategories;
    summary.hidden = !complete;
    priorities.replaceChildren();
    rows.replaceChildren();
    if (!complete) return;
    areas.forEach(([key, name]) => {
      const row = document.createElement('tr');
      const label = document.createElement('th'); label.scope = 'row'; label.textContent = name;
      const score = document.createElement('td'); score.textContent = `${scores[key]} / 5`;
      row.append(label, score); rows.append(row);
    });
    [...areas].sort((a, b) => scores[a[0]] - scores[b[0]]).slice(0, 3).forEach(([key, name, action, href, linkText]) => {
      const item = document.createElement('li');
      const heading = document.createElement('h3'); heading.textContent = `${name} · ${scores[key]} / 5`;
      const text = document.createElement('p'); text.textContent = action;
      const link = document.createElement('a'); link.href = href; link.textContent = `${linkText} →`;
      item.append(heading, text, link); priorities.append(item);
    });
  }

  function updateScoreboard() {
    const completed = Object.keys(scores).length;
    const sum = Object.values(scores).reduce((a, b) => a + b, 0);
    completedCountEl.textContent = completed;
    progressBar.style.width = (completed / numCategories * 100) + '%';
    progressBar.parentElement.setAttribute('aria-valuenow', completed);
    progressBar.parentElement.setAttribute('aria-valuetext', `${completed} of 8 categories scored`);

    if (completed === 0) {
      runningTotalEl.textContent = '—';
      totalScoreEl.textContent = '—';
    } else {
      runningTotalEl.textContent = sum + ' so far';
      totalScoreEl.textContent = sum;
    }

    if (completed === numCategories) {
      pendingEl.style.display = 'none';
      bandBlocks.forEach(b => {
        const min = parseInt(b.dataset.min, 10);
        const max = parseInt(b.dataset.max, 10);
        b.hidden = !(sum >= min && sum <= max);
      });
    } else {
      pendingEl.style.display = 'block';
      bandBlocks.forEach(b => { b.hidden = true; });
    }
    updateNextSteps();
  }

  function updateCommentaryFor(category, score) {
    const panel = document.querySelector('.commentary-panel[data-category="' + category + '"]');
    panel.classList.remove('empty');
    panel.querySelectorAll('.commentary').forEach(p => {
      p.classList.toggle('active', parseInt(p.dataset.showWhen, 10) === score);
    });
  }

  document.querySelectorAll('input[type="radio"][data-category]').forEach(input => {
    input.addEventListener('change', function() {
      const category = this.dataset.category;
      const score = parseInt(this.value, 10);
      scores[category] = score;
      const grid = this.closest('.score-grid');
      grid.querySelectorAll('.score-option').forEach(opt => opt.classList.remove('selected'));
      this.closest('.score-option').classList.add('selected');
      updateCommentaryFor(category, score);
      updateScoreboard();
    });
  });

  document.querySelectorAll('.commentary-panel').forEach(panel => {
    panel.classList.add('empty');
  });
  resetButton.hidden = false;
  resetButton.addEventListener('click', () => {
    Object.keys(scores).forEach(key => delete scores[key]);
    document.querySelectorAll('input[data-category]').forEach(input => { input.checked = false; });
    document.querySelectorAll('.score-option').forEach(option => option.classList.remove('selected'));
    document.querySelectorAll('.commentary-panel').forEach(panel => {
      panel.classList.add('empty');
      panel.querySelectorAll('.commentary').forEach(text => text.classList.remove('active'));
    });
    updateScoreboard();
  });
  updateScoreboard();
})();
