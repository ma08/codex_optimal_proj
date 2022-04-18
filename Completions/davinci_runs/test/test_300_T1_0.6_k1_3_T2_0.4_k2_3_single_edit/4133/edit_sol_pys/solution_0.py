const fs = require('fs');

var file = fs.readFileSync(process.argv[2]);

var fileString = file.toString();

var splitString = fileString.split('\n');

console.log(splitString.length - 1);
