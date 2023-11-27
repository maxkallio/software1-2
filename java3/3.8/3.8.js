document.addEventListener("DOMContentLoaded", function () {

    var num1Input = document.getElementById("num1");
    var num2Input = document.getElementById("num2");
    var operationSelect = document.getElementById("operation");
    var resultParagraph = document.getElementById("result");
    var calculateButton = document.getElementById("start");


    calculateButton.addEventListener("click", function () {

        var selectedOperation = operationSelect.value;


        var num1 = parseInt(num1Input.value);
        var num2 = parseInt(num2Input.value);


        if (isNaN(num1) || isNaN(num2)) {
            resultParagraph.textContent = "Please enter valid numbers.";
            return;
        }


        var result;
        switch (selectedOperation) {
            case "add":
                result = num1 + num2;
                break;
            case "sub":
                result = num1 - num2;
                break;
            case "multi":
                result = num1 * num2;
                break;
            case "div":

                if (num2 === 0) {
                    resultParagraph.textContent = "Cannot divide by zero.";
                    return;
                }
                result = num1 / num2;
                break;
            default:
                resultParagraph.textContent = "Invalid operation.";
                return;
        }


        resultParagraph.textContent = "Result: " + result;
    });
});