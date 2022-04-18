var fs = require('fs');

var file = fs.readFileSync('file.txt');

console.log(file.toString());
