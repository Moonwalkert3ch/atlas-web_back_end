const express = require('express');
const app = express();
const port = 7865;

// route get /
app.get('/', (req, res) => {
    res.status(200);
    res.end('Welcome to the payment system');
});

// listen to server
app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
});

module.exports = app;
