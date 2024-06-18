const express = require('express');
const path = require('./3-read_file_async')
const app = express();
const port = 1245;

app.get('/', (req, res) => {
    res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    const filePath = './database.csv';
    const data = await path(filePath);
    req.status(200).send(`This is the list of our students\n${data}`);
});

app.listen(port, () => {
    console.log('server is running')
});

module.exports = app;
