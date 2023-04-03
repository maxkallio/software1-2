<section id="article-section"></section>

<dialog>
  <span>&#x2715;</span>
  <img alt="Large Image">
</dialog>

<script>
  const picArray = [
    {
      title: 'Pic 1',
      medium_image: 'pic1-medium.jpg',
      large_image: 'pic1-large.jpg',
      caption: 'This is the caption for Pic 1',
      description: 'Description for Pic 1'
    },
    {
      title: 'Pic 2',
      medium_image: 'pic2-medium.jpg',
      large_image: 'pic2-large.jpg',
      caption: 'This is the caption for Pic 2',
      description: 'Description for Pic 2'
    },
    {
      title: 'Pic 3',
      medium_image: 'pic3-medium.jpg',
      large_image: 'pic3-large.jpg',
      caption: 'This is the caption for Pic 3',
      description: 'Description for Pic 3'
    }
  ];

  const articleSection = document.getElementById('article-section');
  const dialog = document.querySelector('dialog');
  const dialogImg = dialog.querySelector('img');
  const dialogCloseBtn = dialog.querySelector('span');

  picArray.forEach((pic) => {
    const article = document.createElement('article');
    article.classList.add('card');

    const heading = document.createElement('h2');
    heading.textContent = pic.title;

    const figure = document.createElement('figure');
    const image = document.createElement('img');
    image.src = pic.medium_image;
    image.alt = pic.title;
    image.addEventListener('click', () => {
      dialogImg.src = pic.large_image;
      dialog.showModal();
    });
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

  dialogCloseBtn.addEventListener('click', () => {
    dialog.close();
  });
</script>