var fs = require('fs');
var path = require('path');

var file = path.join(__dirname, 'file.txt');

var content = fs.readFileSync(file, 'utf-8');

console.log(content);
