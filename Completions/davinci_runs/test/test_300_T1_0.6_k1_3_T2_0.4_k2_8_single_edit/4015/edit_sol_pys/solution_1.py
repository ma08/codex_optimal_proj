var fs = require('fs');

var contents = fs.readFileSync('file.txt', 'utf8');
console.log(contents);

fs.writeFileSync('file.txt', 'Hello World');

var contents = fs.readFileSync('file.txt', 'utf8');
console.log(contents);
