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


        sectionElement.appendChild(articleElement);
    }
});