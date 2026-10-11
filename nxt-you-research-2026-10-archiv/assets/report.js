'use strict';
const filter=document.querySelector('#provider');
if(filter){filter.addEventListener('change',()=>{let n=0;document.querySelectorAll('.creative-card').forEach(card=>{card.hidden=!!filter.value&&card.dataset.provider!==filter.value;if(!card.hidden)n++;});document.querySelector('#filter-status').textContent=`${n} von 11 Anzeigen`;document.querySelector('.no-results').hidden=n!==0;});}
let printState=[];
window.addEventListener('beforeprint',()=>{printState=[...document.querySelectorAll('details')].map(d=>[d,d.open]);printState.forEach(([d])=>d.open=true);document.querySelectorAll('.creative-card').forEach(c=>c.hidden=false);});
window.addEventListener('afterprint',()=>{printState.forEach(([d,open])=>d.open=open);if(filter)filter.dispatchEvent(new Event('change'));});
// Incoming deep links reveal collapsed evidence without animation.
function revealHash(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const el=document.getElementById(id);if(!el)return;let p=el.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement;}}
window.addEventListener('hashchange',revealHash);revealHash();
