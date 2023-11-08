<!DOCTYPE html>
<html>
  <head>
    <title>Chuck Norris Jokes</title>
  </head>
  <body>
    <form>
      <input id="query" name="q" type="text">
      <input type="submit" value="Search">
    </form>
    <div id="results"></div>
    <script>
      const form = document.querySelector('form');
      const queryInput = document.getElementById('query');
      const resultsDiv = document.getElementById('results');

      form.addEventListener('submit', event => {
        event.preventDefault();
        const query = queryInput.value;
        fetch(https://api.chucknorris.io/jokes/search?query=${query})
          .then(response => response.json())
          .then(data => {
            resultsDiv.innerHTML = '';
            data.result.forEach(joke => {
              const article = document.createElement('article');
              const p = document.createElement('p');
              p.textContent = joke.value;
              article.appendChild(p);
              resultsDiv.appendChild(article);
            });
          })
          .catch(error => console.error(error));
      });
    </script>
  </body>
</html>