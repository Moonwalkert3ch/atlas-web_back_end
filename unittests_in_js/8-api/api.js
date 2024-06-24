const express = require('express');

const app = express();
const port = 7865;

// route get /
app.get('/', (req, res) => {
    res.status(200).send('Welcome to the payment system');
});

// listen to server
app.listen(port, () => {
    console.log(`Running on localhost: ${port}`);
});

module.exports = app;
