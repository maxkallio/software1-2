document.addEventListener("DOMContentLoaded", function () {

    var form = document.getElementById("source");
    var targetParagraph = document.getElementById("target");


    form.addEventListener("submit", function (event) {
        // Prevent the default form submission
        event.preventDefault();


        var firstName = document.querySelector('input[name="firstname"]').value;
        var lastName = document.querySelector('input[name="lastname"]').value;


        targetParagraph.textContent = "Your name is " + firstName + " " + lastName;
    });
});