// imports module
const http = require('http');

// declare hostname and port server listens on
const hostname = '127.0.0.1';
const port = 1245;

// creates the http server
const app = http.createServer((req, res) => {
    // set http status and content type
    res.statusCode = 200;
    res.setHeader('Content-type', 'text/plain');
    // send response to the client
    res.end('Hello Holberton School!\n')
});

// make server listen on defined hostname and port
app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
