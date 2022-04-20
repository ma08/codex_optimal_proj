const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'file.txt');

fs.readFile(filePath, {encoding: 'utf-8'}, (err, data) => {
    console.log(data);
});

console.log('Reading file...');
