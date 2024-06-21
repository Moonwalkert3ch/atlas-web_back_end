const http = require('http');
const countStudents = require('./3-read_file_async');

// Declare hostname and port server listens on
const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;

     // Handle different routes
     if (req.url === '/') {
        res.end('Hello Holberton School!\n');
    } else if (req.url === '/students') {
        const filePath = process.argv[2]; // Get file path from command line argument
        console.log(`${filePath}`);

        if (filePath) {
            try {
                const data = await countStudents(filePath);
                console.log(`${data}`);
                res.end(`This is the list of our students\n${data}`);
            } catch (error) {
                res.end('This is the list of our students\nCannot load the database');
            }
        } else {
            res.end('This is the list of our students\nCannot load the database');
        }
    } else {
        res.end('Route not found');
    }
});

// Make server listen on defined hostname and port
app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
