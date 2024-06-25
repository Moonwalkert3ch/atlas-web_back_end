const request = require('request');
const { expect } = require('chai');
const app = require('./api');
const http = require('http');

let server;

describe('Index page', () => {
    before((done) => {
        server = http.createServer(app);
        server.listen(7865, done);
    });

    after((done) => {
        server.close(done);
    });

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
    before((done) => {
        server = http.createServer(app);
        server.listen(7866, done);  // Use a different port for this test suite
    });

    after((done) => {
        server.close(done);
    });

    it('returns status 200 for valid cart ID', (done) => {
        request('http://localhost:7866/cart/123', (err, res) => {
            expect(res.statusCode).to.equal(200);
            done();
        });
    });

    it('returns correct message for valid cart ID', (done) => {
        request('http://localhost:7866/cart/123', (err, res, body) => {
            expect(body).to.equal('Payment methods for cart 123');
            done();
        });
    });

    it('returns status 404 for invalid cart ID', (done) => {
        request('http://localhost:7866/cart/abc', (err, res) => {
            expect(res.statusCode).to.equal(404);
            done();
        });
    });
});
