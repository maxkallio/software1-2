<form id="search-form">
  <input id="query" name="q" type="text">
  <input type="submit" value="Search">
</form>

const form = document.getElementById('search-form');
form.addEventListener('submit', async function(e) {
  e.preventDefault(); // prevent the form from submitting

  const query = document.getElementById('query').value;
  const response = await fetch(https://api.tvmaze.com/search/shows?q=${query});
  const data = await response.json();

  console.log(data); // print the search result to the console
});