const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
    it('should return status 200', (done) => {
        request('http://localhost:7865', (error, response) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return correct message', (done) => {
        request.get('http://localhost:7865', (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});
