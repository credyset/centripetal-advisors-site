// Exercise the actual Copy handler without changing the user's browser permissions.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const source=fs.readFileSync(new URL('../assets/board-builder.js',import.meta.url),'utf8');
const data=JSON.parse(fs.readFileSync(new URL('./board-builder-content.json',import.meta.url),'utf8'));
class Node {
  value=''; textContent=''; hidden=false; dataset={}; children=[]; listeners={};
  append(...items){this.children.push(...items);} replaceChildren(...items){this.children=items;}
  addEventListener(name,fn){this.listeners[name]=fn;}
  focus(){this.focused=true;} select(){this.selected=true;}
  querySelector(){return new Node();}
}
for(const mode of ['denied','unavailable','success']){
  const nodes=new Map();const get=key=>{if(!nodes.has(key))nodes.set(key,new Node());return nodes.get(key);};
  get('[name="board-focus"]:checked').value=data.focuses[0].id;
  get('[name="board-request"]:checked').value='input';
  const rows=data.sections.map(s=>{const n=new Node();n.dataset={boardArea:s.id,title:s.title};n.querySelector=()=>({value:'pending'});return n;});
  const builder=new Node();builder.querySelector=get;builder.querySelectorAll=()=>rows;
  const document={querySelector:()=>builder,getElementById:()=>({textContent:JSON.stringify(data)}),createElement:()=>new Node(),createTextNode:text=>text};
  let copied;
  const navigator=mode==='unavailable'?{}:{clipboard:{writeText:async text=>{if(mode==='denied')throw new Error('Permission denied');copied=text;}}};
  vm.runInNewContext(source,{document,navigator});
  const note=get('[data-board-note]');const original=note.value;
  assert.ok(original.includes('BOARD MEETING PREPARATION'));
  await get('[data-copy-note]').listeners.click();
  if(mode==='success'){
    assert.equal(copied,original);assert.equal(get('[data-copy-status]').textContent,'Preparation note copied.');
  }else{
    assert.ok(note.focused&&note.selected);assert.equal(note.value,original);
    assert.match(get('[data-copy-status]').textContent,/Use your device’s Copy command/);
  }
  console.log('PASS: actual Copy handler — '+mode);
}
