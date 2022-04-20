var fs = require('fs');

var file = fs.readFileSync(process.argv[2]);

var count = file.toString().split('\n').length - 1;

console.log(count);
