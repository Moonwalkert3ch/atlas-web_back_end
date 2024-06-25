const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
    it('should return 6 when type is SUM, and inputs are 1.4 and 4.5', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return -4 when type is SUBTRACT, and inputs are 1.4 and 4.5', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0.2 when type is DIVIDE, and inputs are 1.4 and 4.5', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.closeTo(0.2, 0.01);
    });

    it('should return "Error" when type is DIVIDE, and inputs are 1.4 and 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE and b is 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, and both a and b are 0', () => {
        expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    });

    it('should return 4 when type is SUBTRACT, and inputs are 4.5 and 1.4', () => {
        expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
    });

});
