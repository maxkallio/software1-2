<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>TV Series Search</title>
  </head>
  <body>
    <form>
      <input id="query" type="text" placeholder="Enter TV series name">
      <button id="search-btn" type="submit">Search</button>
    </form>
    <div id="results"></div>

    <script>
      const form = document.querySelector('form');
      const queryInput = document.querySelector('#query');
      const resultsContainer = document.querySelector('#results');

      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = queryInput.value;
        const response = await fetch(https://api.tvmaze.com/search/shows?q=${query});
        const data = await response.json();
        resultsContainer.innerHTML = '';
        data.forEach((tvShow) => {
          const article = document.createElement('article');
          const imgSrc = tvShow.show.image ? tvShow.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
          const summary = tvShow.show.summary;

          article.innerHTML = `
            <h2>${tvShow.show.name}</h2>
            <a href="${tvShow.show.url}" target="_blank"><img src="${imgSrc}" alt="${tvShow.show.name}"></a>
            <div>${summary}</div>
          `;

          resultsContainer.appendChild(article);
        });
      });
    </script>
  </body>
</html>

fetch('https://api.chucknorris.io/jokes/random')
  .then(response => response.json())
  .then(data => console.log(data.value))
  .catch(error => console.error(error));