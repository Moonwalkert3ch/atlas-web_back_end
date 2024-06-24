const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    let calculateNumberStub;
    let consoleLogSpy;

    beforeEach(() => {
        calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleLogSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        calculateNumberStub.restore();
        consoleLogSpy.restore();
    });

    it('should call Utils.calculateNumber with SUM and correct args', () => {
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts that Utils.calculateNumber was called once with SUM 100 and 20
        expect(calculateNumberStub.calledOnce).to.be.true;
        expect(calculateNumberStub.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;
    });

    it('should log correct message to console', () => {
        const totalAmount = 100;
        const totalShipping = 20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts console.log was called once with The total is: 10
        expect(consoleLogSpy.calledWithExactly('The total is: 10')).to.be.true;
    });

    it('should give correct values for negative numbers', () => {
        const totalAmount = -100;
        const totalShipping = -20;

        sendPaymentRequestToApi(totalAmount, totalShipping);

        // Asserts that Utils.calculateNumber was called once with SUM 100 and 20
        expect(calculateNumberStub.calledOnce).to.be.true;
        expect(calculateNumberStub.calledWithExactly('SUM', totalAmount, totalShipping)).to.be.true;

        expect(consoleLogSpy.calledWithExactly('The total is: 10')).to.be.true;
    });

});