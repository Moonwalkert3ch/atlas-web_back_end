const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    let consoleSpy;

    beforeEach(() => {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        consoleSpy.restore();
    });

    it('should call Utils.calculateNumber with SUM and correct args', () => {
        const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts that Utils.calculateNumber was called once with SUM 100 and 20
        expect(calculateNumberSpy.calledOnce).to.be.true;
        expect(calculateNumberSpy.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;

        // resets spy
        calculateNumberSpy.restore();
    });

    it('should log correct total of 100 and 20', () => {
        sendPaymentRequestToApi(100, 20);

        expect(consoleSpy.calledOnce).to.be.true;

        // Asserts console.log was called once with The total is: 10
        expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
    });

    it('should give correct values for negative numbers', () => {
        const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
        const totalAmount = -100;
        const totalShipping = -20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts that Utils.calculateNumber was called once with SUM -100 and -20
        expect(calculateNumberSpy.calledOnce).to.be.true;
        expect(calculateNumberSpy.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;

        calculateNumberSpy.restore();
    });

    it('should log correct total of 10 and 10', () => {
        sendPaymentRequestToApi(10, 10);

        expect(consoleSpy.calledOnce).to.be.true;
        // Asserts console.log was called once with The total is: 10
        expect(consoleSpy.calledWithExactly('The total is: 20')).to.be.true;
    });
});
