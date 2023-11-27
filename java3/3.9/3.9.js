document.addEventListener("DOMContentLoaded", function () {

    var calculationInput = document.getElementById("calculation");
    var resultParagraph = document.getElementById("result");
    var calculateButton = document.getElementById("start");


    calculateButton.addEventListener("click", function () {

        var userInput = calculationInput.value;


        if (!userInput.includes("+") && !userInput.includes("-") && !userInput.includes("*") && !userInput.includes("/")) {
            resultParagraph.textContent = "Invalid calculation. Please use +, -, *, or /";
            return;
        }


        var operands = userInput.split(/[\+\-\*\/]/);
        var operator = userInput.split("").find(char => ['+', '-', '*', '/'].includes(char));


        var num1 = parseInt(operands[0]);
        var num2 = parseInt(operands[1]);


        if (isNaN(num1) || isNaN(num2)) {
            resultParagraph.textContent = "Please enter valid numbers.";
            return;
        }


        var result;
        switch (operator) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":

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