const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const endpoint = 'http://localhost:7865';

  it('Returns the right status', function (done) {
    request(endpoint, function (err, res, body) {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });
});
