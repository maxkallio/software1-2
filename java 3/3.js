const target = document.getElementById('target');
const names = ['John', 'Paul', 'Jones'];
let html = '';
for (let i = 0; i < names.length; i++) {
  html += <li>${names[i]}</li>;
}
target.innerHTML = html;