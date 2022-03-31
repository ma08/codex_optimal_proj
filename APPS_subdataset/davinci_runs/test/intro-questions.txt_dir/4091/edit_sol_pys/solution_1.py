var fs = require('fs');

var file = fs.readFileSync(process.argv[2], 'utf8');

var arr = file.split('\n');

console.log(arr.length - 1);
