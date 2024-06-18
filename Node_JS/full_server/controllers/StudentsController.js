const readDatabase = require('../utils')

class StudentsController {
    static async getAllStudents(req, res) {
        const filePath = './utils.js';

        try {
            const fields = await readDatabase(filePath);
            let responseText = 'This is the list of our students\n';

            // Get the fields in alphabetical order (case insensitive)
            const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

            sortedFields.forEach(field => {
            const students = fields[field];
            responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        });

        res.status(200).send(responseText);
    } catch (error) {
        res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const databaseFilePath = './utils.js';
        const major = req.query.major;

        if (!['CS', 'SWE'].includes(major)) {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const fields = await readDatabase(databaseFilePath);
            const students = fields[major];

            if (!students) {
                return res.status(200).send(`List: `);
            }

            const responseText = `List: ${students.join(', ')}`;
            res.status(200).send(responseText);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

module.exports = StudentsController;
