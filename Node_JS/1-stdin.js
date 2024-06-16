console.log('Welcome to Holberton School, what is your name?');
// read input from the stdin
process.stdin.setEncoding('utf8');
// event listener for users input
process.stdin.on('readable', () => {
    const chunk = process.stdin.read();
    if (chunk !== null) {
        process.stdout.write(`Your name is: ${chunk}`);
    }
});
// closer listener
process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
});
