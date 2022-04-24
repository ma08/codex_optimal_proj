var fs = require('fs');

var data = fs.readFileSync('file.txt', 'utf8');
console.log(data);

fs.writeFileSync('file2.txt', 'Hello World');
