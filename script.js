let currentExpression = "";
const resultDisplay = document.getElementById("result");

function appendNumber(number) {
    if (currentExpression === "0" && number !== ".") {
        currentExpression = "";
    }
    currentExpression += number;
    updateDisplay();
}

function appendOperator(operator) {
    if (currentExpression === "") {
        currentExpression = "0";
    }
    // Replace the last operator if it exists
    if (['+', '-', '×', '÷'].includes(currentExpression[currentExpression.length - 1])) {
        currentExpression = currentExpression.slice(0, -1);
    }
    currentExpression += operator;
    updateDisplay();
}

function clearDisplay() {
    currentExpression = "";
    updateDisplay();
}

function toggleSign() {
    if (currentExpression === "") return;
    
    try {
        const value = eval(prepareExpression(currentExpression));
        currentExpression = (-value).toString();
        updateDisplay();
    } catch (error) {
        currentExpression = "Error";
        updateDisplay();
    }
}

function percentage() {
    if (currentExpression === "") return;
    
    try {
        const value = eval(prepareExpression(currentExpression));
        currentExpression = (value / 100).toString();
        updateDisplay();
    } catch (error) {
        currentExpression = "Error";
        updateDisplay();
    }
}

function calculate() {
    if (currentExpression === "") return;
    
    try {
        const result = eval(prepareExpression(currentExpression));
        currentExpression = formatResult(result);
        updateDisplay();
    } catch (error) {
        currentExpression = "Error";
        updateDisplay();
    }
}

function prepareExpression(expr) {
    return expr.replace(/×/g, '*').replace(/÷/g, '/');
}

function formatResult(number) {
    if (Number.isInteger(number)) {
        return number.toString();
    }
    return parseFloat(number.toFixed(8)).toString();
}

function updateDisplay() {
    resultDisplay.value = currentExpression || "0";
}

// Add keyboard support
document.addEventListener('keydown', (event) => {
    const key = event.key;
    
    if (key >= '0' && key <= '9' || key === '.') {
        appendNumber(key);
    } else if (key === '+' || key === '-') {
        appendOperator(key);
    } else if (key === '*') {
        appendOperator('×');
    } else if (key === '/') {
        appendOperator('÷');
    } else if (key === 'Enter' || key === '=') {
        calculate();
    } else if (key === 'Escape') {
        clearDisplay();
    } else if (key === 'Backspace') {
        currentExpression = currentExpression.slice(0, -1);
        updateDisplay();
    }
}); 