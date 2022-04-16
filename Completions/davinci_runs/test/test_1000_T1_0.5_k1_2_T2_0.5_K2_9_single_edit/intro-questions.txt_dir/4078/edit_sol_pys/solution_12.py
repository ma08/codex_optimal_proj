const fs = require('fs');

let file = fs.readFileSync('file.txt', 'utf8');

console.log(file);

