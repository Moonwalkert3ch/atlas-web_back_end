const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const expect = chai.expect;

describe('sendPaymentRequestToApi', () => {
    it('should call Utils.calculateNumber with SUM and correct arguments', () => {
        const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts that Utils.calculateNumber was called once with 'SUM', 100, and 20
        expect(calculateNumberSpy.calledOnce).to.be.true;
        expect(calculateNumberSpy.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;

        // restores the spy
        calculateNumberSpy.restore();
    });

    it('should handle negative values correctly', () => {
        const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = -100;
        const totalShipping = -20;
    
        sendPaymentRequestToApi(totalAmount, totalShipping);
    
        // Assert that Utils.calculateNumber was called once with 'SUM', -100, and -20
        expect(calculateNumberSpy.calledOnce).to.be.true;
        expect(calculateNumberSpy.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;
    
        calculateNumberSpy.restore();
    });

});