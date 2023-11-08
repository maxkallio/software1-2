<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>TV Series Search</title>
  </head>
  <body>
    <form>
      <label for="query">Search for TV Series:</label>
      <input id="query" name="q" type="text">
      <input type="submit" value="Search">
    </form>

    <script src="script.js"></script>
  </body>
</html>

const form = document.querySelector('form');
const queryInput = document.querySelector('#query');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const query = queryInput.value;

  fetch(https://api.tvmaze.com/search/shows?q=${query})
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.log(error);
    });
});