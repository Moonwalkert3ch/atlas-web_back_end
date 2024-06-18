const express = require('express');
const app = express();
const route = require('./routes');

app.use('/', route);

app.listen(port, () => {
    console.log('Server is running...');
});

module.exports = app;
