const form = document.querySelector('form');
const resultsContainer = document.querySelector('#results');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultsContainer.innerHTML = '';
  const query = e.target.elements.query.value.trim();
  const response = await fetch(https://api.tvmaze.com/search/shows?q=${query});
  const data = await response.json();
  data.forEach(tvShow => {
    const article = document.createElement('article');
    const heading = document.createElement('h2');
    const titleLink = document.createElement('a');
    const img = document.createElement('img');
    const summary = document.createElement('div');

    heading.textContent = tvShow.show.name;
    titleLink.textContent = tvShow.show.url;
    titleLink.href = tvShow.show.url;
    titleLink.target = '_blank';
    img.src = tvShow.show.image?.medium;
    img.alt = tvShow.show.name;
    summary.innerHTML = tvShow.show.summary;

    article.appendChild(heading);
    article.appendChild(titleLink);
    article.appendChild(img);
    article.appendChild(summary);

    resultsContainer.appendChild(article);
  });
});