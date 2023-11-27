document.addEventListener("DOMContentLoaded", function () {

    var sectionElement = document.getElementById("pictures");


    const picArray = [

    ];


    for (var i = 0; i < picArray.length; i++) {

        var articleElement = document.createElement("article");
        articleElement.classList.add("card");


        var h2Element = document.createElement("h2");
        h2Element.textContent = picArray[i].title;


        var figureElement = document.createElement("figure");


        var imgElement = document.createElement("img");
        imgElement.src = picArray[i].image.medium;
        imgElement.alt = picArray[i].title;


        var figcaptionElement = document.createElement("figcaption");
        figcaptionElement.textContent = picArray[i].caption;


        var pElement = document.createElement("p");
        pElement.textContent = picArray[i].description;


        figureElement.appendChild(imgElement);
        figureElement.appendChild(figcaptionElement);

        articleElement.appendChild(h2Element);
        articleElement.appendChild(figureElement);
        articleElement.appendChild(pElement);


        articleElement.dataset.large = picArray[i].image.large;


        sectionElement.appendChild(articleElement);


        articleElement.addEventListener("click", function (event) {

            var largeImageSrc = event.currentTarget.dataset.large;


            openModal(largeImageSrc);
        });
    }


    function openModal(largeImageSrc) {

        var modal = document.querySelector("dialog");

        var modalImg = modal.querySelector("img");


        modalImg.src = largeImageSrc;

        modalImg.alt = "Large Image";


        modal.showModal();


        modal.querySelector("span").addEventListener("click", function () {

            closeModal();
        });


        modal.addEventListener("click", function (event) {
            if (event.target === modal) {
                closeModal();
            }
        });
    }


    function closeModal() {

        var modal = document.querySelector("dialog");

        modal.close();
    }
});