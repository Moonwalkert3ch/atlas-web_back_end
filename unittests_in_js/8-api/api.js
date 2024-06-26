const express = require('express');

const app = express();
const port = 7865;


app.listen(port, () => {
  console.log(`API available on localhost ${port}`);
});

app.get('/', (req, res) => {
	res.end('Welcome to the payment system');
});

module.exports = app;
