const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => console.log(data));
