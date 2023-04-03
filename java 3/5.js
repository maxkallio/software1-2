const picArray = [
  {
    title: 'First Image',
    medium_image: 'https://picsum.photos/400/300?random=1',
    caption: 'This is the caption for the first image',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam feugiat mauris ac lectus tristique, ac interdum lorem fringilla. Integer rhoncus enim vitae turpis tincidunt, a blandit ex volutpat. '
  },
  {
    title: 'Second Image',
    medium_image: 'https://picsum.photos/400/300?random=2',
    caption: 'This is the caption for the second image',
    description: 'Nunc sit amet elit in turpis sagittis volutpat quis vel nulla. Duis rutrum nunc vel massa mattis suscipit. Proin sit amet risus vitae nulla faucibus sagittis. '
  },
  {
    title: 'Third Image',
    medium_image: 'https://picsum.photos/400/300?random=3',
    caption: 'This is the caption for the third image',
    description: 'Phasellus ac purus in leo finibus venenatis. Curabitur vitae efficitur libero. Nullam ultrices nulla eget ante scelerisque, sed ullamcorper augue pulvinar. Nam pretium luctus mauris, sed pretium eros fringilla a.'
  }
];

const articleSection = document.getElementById('article-section');

picArray.forEach((pic) => {
  const article = document.createElement('article');
  article.classList.add('card');

  const heading = document.createElement('h2');
  heading.textContent = pic.title;

  const figure = document.createElement('figure');
  const image = document.createElement('img');
  image.src = pic.medium_image;
  image.alt = pic.title;
  const caption = document.createElement('figcaption');
  caption.textContent = pic.caption;

  const description = document.createElement('p');
  description.textContent = pic.description;

  figure.appendChild(image);
  figure.appendChild(caption);

  article.appendChild(heading);
  article.appendChild(figure);
  article.appendChild(description);

  articleSection.appendChild(article);
});