function getPaymentTokenFromAPI(success) {
    if (success === true){
        return new Promise((resolve) => {
            resolve({ data: 'Successful response from the API' });
        });
    }
    // When false function does nothing
    return new Promise(() => {});
}

module.exports = getPaymentTokenFromAPI;
