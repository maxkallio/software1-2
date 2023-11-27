document.addEventListener("DOMContentLoaded", function () {

    var targetElement = document.getElementById("target");


    var names = ["John", "Paul", "Jones"];


    for (var i = 0; i < names.length; i++) {
        targetElement.innerHTML += "<li>" + names[i] + "</li>";
    }
});