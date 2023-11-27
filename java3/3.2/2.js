document.addEventListener("DOMContentLoaded", function () {

    var targetElement = document.getElementById("target");


    var listItem1 = document.createElement("li");
    var listItem2 = document.createElement("li");
    var listItem3 = document.createElement("li");


    listItem1.textContent = "First item";
    listItem2.textContent = "Second item";
    listItem3.textContent = "Third item";


    listItem2.classList.add("my-item");


    targetElement.appendChild(listItem1);
    targetElement.appendChild(listItem2);
    targetElement.appendChild(listItem3);
});