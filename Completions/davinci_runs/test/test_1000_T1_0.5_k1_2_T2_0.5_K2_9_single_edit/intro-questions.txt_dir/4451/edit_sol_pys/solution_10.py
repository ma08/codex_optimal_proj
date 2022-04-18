var fs = require('fs');

var data = fs.readFileSync('file.txt', 'utf8');
console.log(data);
console.log('end');
