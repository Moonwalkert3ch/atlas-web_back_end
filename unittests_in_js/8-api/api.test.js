const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
    it('Returns the right status', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        done();
      });
    });
  
    it('returns correct result', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
});
