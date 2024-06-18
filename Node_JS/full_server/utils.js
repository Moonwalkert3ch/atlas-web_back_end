const fs = require('fs').promises;

async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const rows = data.trim().split('\n');
        const fields = {};

        rows.forEach((value, index) => {
            if (index === 0) return;

            const [firstname, lastname, age, field] = value.split(',');

            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname);
        });
        return fields;
    } catch (error) {
        return Promise.reject(error);
    }
}

module.exports =  readDatabase;
