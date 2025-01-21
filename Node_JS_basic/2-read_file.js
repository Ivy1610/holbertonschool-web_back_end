const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length < 2) {
      throw new Error('Cannot load the database');
    }

    const students = lines.slice(1).map((line) => line.split(','));
    const totalStudents = students.length;

    console.log(`Number of students: ${totalStudents}`);

    const fields = {};
    students.forEach(([firstname, field]) => {
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    for (const [field, firstnames] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`,
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
