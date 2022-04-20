var fs = require('fs');

var file = fs.readFileSync(process.argv[2]);
var str = file.toString();
var lines = str.split('\n');

console.log(lines.length - 1);
