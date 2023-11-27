document.addEventListener("DOMContentLoaded", function () {

    var triggerElement = document.getElementById("trigger");
    var targetImage = document.getElementById("target");


    var originalImageSrc = "img/picA.jpg";
    var hoverImageSrc = "img/picB.jpg";


    triggerElement.addEventListener("mouseover", function () {

        targetImage.src = hoverImageSrc;
    });

    triggerElement.addEventListener("mouseout", function () {

        targetImage.src = originalImageSrc;
    });
});