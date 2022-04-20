const fs = require('fs');

const file = './file.txt';

fs.readFile(file, 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log(data);
});
