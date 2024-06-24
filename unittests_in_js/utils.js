const Utils = {
    calculateNumber(type, a, b) {
        a = Math.round(a);
        b = Math.round(b);
        
        const operators = {
            'SUM': () => a + b,
            'SUBTRACT': () => a - b,
            'DIVIDE': () => {
                if (b === 0) {
                    return 'Error';
                }
                return a / b;
            }
        };

    // Checks if the type is an operator, if its not returns 'Invalid type'
    if (type in operators) {
        return operators[type](); // Executes function
    } else {
        return 'Invalid type';
    }
    }

};

module.exports = Utils;