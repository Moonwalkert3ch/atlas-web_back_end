const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const rows = data.trim().split('\n');

        const fields = {};
        
        // Iterate through each row minus header
        rows.slice(1).forEach(row => {
            const [firstname, lastname, age, field] = row.split(',');

            if (!fields[field]) {
                fields[field] = [];
            }

            fields[field].push(firstname);
        });
        
        // Calculates number_of_students number of students
        const number_of_students = Object.values(fields).reduce((newStudents, currentStudent) => newStudents + currentStudent.length, 0);
        
        console.log(`Number of students: ${number_of_students}`);
        
        // number of students in each field
        for (const field in fields) {
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
        
    } catch (err) {
        console.error('Cannot load the database');
        throw err;
    }
}

module.exports = countStudents;
