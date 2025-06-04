let currentInput = '0';
let lastWasOperator = false;
let lastWasEquals = false;
const maxDigits = 12;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateDisplay();
    setupKeyboardSupport();
});

function updateDisplay() {
    const display = document.getElementById('result');
    // Format large numbers with commas
    let displayText = currentInput;
    if (!isNaN(currentInput) && !currentInput.includes('e')) {
        const num = parseFloat(currentInput);
        if (Math.abs(num) >= 1000) {
            displayText = num.toLocaleString('en-US', {
                maximumFractionDigits: 8
            });
        }
    }
    display.value = displayText;
}

function appendNumber(num) {
    if (lastWasEquals) {
        currentInput = num;
        lastWasEquals = false;
    } else if (currentInput === '0' && num !== '.') {
        currentInput = num;
    } else if (currentInput.length < maxDigits) {
        // Prevent multiple decimal points
        if (num === '.' && currentInput.includes('.')) return;
        currentInput += num;
    }
    lastWasOperator = false;
    updateDisplay();
}

function appendOperator(op) {
    if (!lastWasOperator) {
        currentInput += op;
        lastWasOperator = true;
        lastWasEquals = false;
    } else {
        // Replace last operator
        currentInput = currentInput.slice(0, -1) + op;
    }
    updateDisplay();
}

function clearDisplay() {
    currentInput = '0';
    lastWasOperator = false;
    lastWasEquals = false;
    updateDisplay();
}

function toggleSign() {
    if (currentInput === '0') return;
    
    try {
        // Handle expressions
        if (currentInput.match(/[+\-×÷]/)) {
            calculate();
        }
        currentInput = (parseFloat(currentInput) * -1).toString();
        updateDisplay();
    } catch (e) {
        showError();
    }
}

function percentage() {
    try {
        // Handle expressions
        if (currentInput.match(/[+\-×÷]/)) {
            calculate();
        }
        currentInput = (parseFloat(currentInput) / 100).toString();
        updateDisplay();
    } catch (e) {
        showError();
    }
}

function calculate() {
    try {
        // Replace operators with JavaScript operators
        let expression = currentInput
            .replace(/×/g, '*')
            .replace(/÷/g, '/');
            
        // Check for division by zero
        if (expression.includes('/0')) {
            throw new Error('Division by zero');
        }

        let result = eval(expression);

        // Handle large numbers and decimals
        if (Math.abs(result) > 1e12) {
            result = result.toExponential(6);
        } else if (result % 1 !== 0) {
            result = parseFloat(result.toFixed(8));
        }

        currentInput = result.toString();
        lastWasEquals = true;
        lastWasOperator = false;
        updateDisplay();
    } catch (e) {
        showError();
    }
}

function showError() {
    currentInput = 'Error';
    updateDisplay();
    setTimeout(() => {
        currentInput = '0';
        updateDisplay();
    }, 1500);
}

function setupKeyboardSupport() {
    document.addEventListener('keydown', (e) => {
        if (e.key >= '0' && e.key <= '9' || e.key === '.') {
            appendNumber(e.key);
        } else if (e.key === '+' || e.key === '-') {
            appendOperator(e.key);
        } else if (e.key === '*') {
            appendOperator('×');
        } else if (e.key === '/') {
            e.preventDefault();
            appendOperator('÷');
        } else if (e.key === 'Enter' || e.key === '=') {
            calculate();
        } else if (e.key === 'Escape') {
            clearDisplay();
        } else if (e.key === 'Backspace') {
            if (currentInput.length > 1) {
                currentInput = currentInput.slice(0, -1);
            } else {
                currentInput = '0';
            }
            updateDisplay();
        }
    });
} 