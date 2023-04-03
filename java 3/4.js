const target = document.getElementById('target');
const students = [
  { id: '2345768', name: 'John' },
  { id: '2134657', name: 'Paul' },
  { id: '5423679', name: 'Jones' },
];
const select = document.createElement('select');
for (let i = 0; i < students.length; i++) {
  const option = document.createElement('option');
  option.value = students[i].id;
  option.textContent = students[i].name;
  select.appendChild(option);
}
target.appendChild(select);