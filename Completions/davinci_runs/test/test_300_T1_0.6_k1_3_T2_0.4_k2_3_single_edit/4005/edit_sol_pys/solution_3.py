var fs = require('fs');

var file = fs.readFileSync(process.argv[2]);
var str = file.toString();
var split = str.split('\n');

console.log(split.length-1);
