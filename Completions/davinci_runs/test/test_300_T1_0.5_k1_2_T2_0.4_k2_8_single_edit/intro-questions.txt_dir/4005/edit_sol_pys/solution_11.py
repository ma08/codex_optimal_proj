//file.js

var fs = require('fs');

var file = fs.readFileSync('./file.js', 'utf8');

console.log(file);
