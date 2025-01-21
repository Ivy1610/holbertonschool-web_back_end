const http = require('http');
const fs = require('fs');
const url = require('url');

const hostname = '127.0.0.1';
const port = 1245;

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter((line) => line.trim() !== '');
            const fields = {};
            let totalStudents = 0;

            lines.forEach((line) => {
                const [firstname, , , field] = line.split(',');
                if (field) {
                    if (!fields[field]) {
                        fields[field] = [];
                    }
                    fields[field].push(firstname);
                    totalStudents += 1;
                }
            });

            let result = `Number of students: ${totalStudents}\n`;
            for (const [field, students] of Object.entries(fields)) {
                result += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
            }

            resolve(result.trim());
        });
    });
}

const app = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const path = parsedUrl.pathname;

    if (path === '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello Holberton School!\n');
    } else if (path === '/students') {
        const database = process.argv[2];

        countStudents(database)
            .then((result) => {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/plain');
                res.end(`This is the list of our students\n${result}`);
            })
            .catch((error) => {
                res.statusCode = 500;
                res.setHeader('Content-Type', 'text/plain');
                res.end(error.message);
            });
    } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Not Found');
    }
});

app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
