// A transient review list, not a readiness score or financial model.
(() => {
  const review=document.querySelector('[data-cash-review]');
  if(!review)return;
  const areas=[...review.querySelectorAll('fieldset')];
  const panel=review.querySelector('[data-review-result]');
  const reset=review.querySelector('[data-review-reset]');
  const update=()=>{
    const rows=areas.map(area=>({
      state:area.querySelector('input:checked').value,
      title:area.dataset.title,
      target:area.dataset.target,
      prompt:area.dataset.prompt
    }));
    const count=state=>rows.filter(row=>row.state===state).length;
    review.querySelector('[data-review-status]').textContent=`${count('reviewed')} reviewed · ${count('followup')} for follow-up · ${count('pending')} not reviewed`;
    const list=review.querySelector('[data-review-list]');list.replaceChildren();
    const open=[...rows.filter(row=>row.state==='followup'),...rows.filter(row=>row.state==='pending')];
    for(const row of open){
      const li=document.createElement('li');
      const a=document.createElement('a');a.href='#'+row.target;a.textContent=row.title;
      const note=document.createElement('span');note.textContent=row.state==='followup'?'Follow-up needed':'Not reviewed';
      const prompt=document.createElement('p');prompt.textContent=row.prompt;
      li.append(a,note,prompt);list.append(li);
    }
    review.querySelector('[data-review-empty]').hidden=open.length!==0;
  };
  review.addEventListener('change',update);
  reset.addEventListener('click',()=>{
    areas.forEach(area=>area.querySelector('input[value="pending"]').checked=true);
    update();
  });
  panel.hidden=false;reset.hidden=false;update();
})();
