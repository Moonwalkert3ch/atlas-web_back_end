const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
    it('returns status 200', (done) => {
        request('http://localhost:7865', (err, res) => {
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

describe('Cart page', () => {
    it('returns status 200 for valid cart ID', (done) => {
        request('http://localhost:7865/cart/123', (err, res) => {
            expect(res.statusCode).to.equal(200);
            done();
        });
    });

    it('returns correct message for valid cart ID', (done) => {
        request('http://localhost:7865/cart/123', (err, res, body) => {
            expect(body).to.equal('Payment methods for cart 123');
            done();
        });
    });

    it('returns status 404 for invalid cart ID', (done) => {
        request('http://localhost:7865/cart/abc', (err, res) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    });
});
