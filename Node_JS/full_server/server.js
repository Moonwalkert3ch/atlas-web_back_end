const express = require('express');
const app = express();
const routers = require('./routes');

app.use('/', routers);

app.listen(port, () => {
    console.log('Server is running...');
});

module.exports = app;
