var fs = require('fs');

var file = fs.readFileSync('file.txt', 'utf8');

console.log(file);
