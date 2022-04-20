var fs = require('fs');

var file = fs.readFileSync(process.argv[2]);
var str = file.toString();
var array = str.split('\n');

console.log(array.length - 1);
