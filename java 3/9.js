<label htmlFor="calculation">Enter calculation:</label>
<input type="text" id="calculation">

    <button id="calculate">Calculate</button>

    <p id="result"></p>

    <script>
        const calculationInput = document.getElementById('calculation');
        const calculateButton = document.getElementById('calculate');
        const resultOutput = document.getElementById('result');

        calculateButton.addEventListener('click', () => {
        const inputString = calculationInput.value.trim();
        if (!inputString) {
        resultOutput.textContent = 'Please enter a calculation.';
        return;
    }

        let operator;
        if (inputString.includes('+')) {
        operator = '+';
    } else if (inputString.includes('-')) {
        operator = '-';
    } else if (inputString.includes('')) {
        operator = '';
    } else if (inputString.includes('/')) {
        operator = '/';
    } else {
        resultOutput.textContent = 'Invalid calculation format.';
        return;
    }

        const operands = inputString.split(operator).map(str => parseInt(str.trim(), 10));
        if (operands.some(isNaN)) {
        resultOutput.textContent = 'Invalid number format.';
        return;
    }

        let result;
        switch (operator) {
        case '+':
        result = operands[0] + operands[1];
        break;
        case '-':
        result = operands[0] - operands[1];
        break;
        case '':
        result = operands[0] operands[1];
        break;
        case '/':
        if (operands[1] === 0) {
        resultOutput.textContent = 'Cannot divide by zero.';
        return;
    }
        result = Math.floor(operands[0] / operands[1]);
        break;
    }

        resultOutput.textContent = Result: ${result};
    });
    </script>