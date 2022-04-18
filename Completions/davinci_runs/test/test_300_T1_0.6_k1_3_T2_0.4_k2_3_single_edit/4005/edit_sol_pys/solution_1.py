const fs = require('fs');

const file = fs.readFileSync('./file.js', 'utf8');

console.log(file);
