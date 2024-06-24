const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should return a resolved promise with object data when true success', (done) => {
        getPaymentTokenFromAPI(true).then((response) => {
            try {
                expect(response).to.deep.equal({ data: 'Successful response from the API' });
                done();
            } catch (error) {
                done(error);
            }
        });
    });

    it('should return unresolved promise with false success', (done) => {
        const notResolved = true;
        const promise = getPaymentTokenFromAPI(false);

        setTimeout(() => {
            promise.then(
                () => {
                    notResolved = false;
                    done(new Error('Promise not resolved'));
                },
                () => {
                    done();
                }

            );

            if (notResolved) {
                done();
            }
        }, 100);
    });
});