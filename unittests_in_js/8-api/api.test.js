const { expect } = require('chai');
const request = require('request');
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

    it('should return status 200', (done) => {
        request.get('http://localhost:7865', (error, response, body) => {
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
