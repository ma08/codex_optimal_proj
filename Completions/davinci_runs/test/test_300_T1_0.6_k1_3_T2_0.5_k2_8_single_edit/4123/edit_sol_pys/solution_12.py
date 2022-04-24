var fs = require('fs');

var fileName = process.argv[2];

var file = fs.readFileSync(fileName).toString();

var lines = file.split('\n').length - 1;

console.log(lines);
