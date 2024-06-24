const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    it('should return 6 when type is SUM, and inputs are 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return -4 when type is SUBTRACT, and inputs are 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0.2 when type is DIVIDE, and inputs are 1.4 and 4.5', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when type is DIVIDE, and inputs are 1.4 and 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when type is DIVIDE and b is 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when type is DIVIDE, and both a and b are 0', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    });

    it('should return -3 when type is SUBTRACT, and inputs are 4.5 and 1.4', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 3.1);
    });

});
