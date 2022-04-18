const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'file.txt');

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data);
    }
});

console.log('TEST');
