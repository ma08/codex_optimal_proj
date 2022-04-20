var fs = require('fs');

var readStream = fs.createReadStream('file.txt');
var writeStream = fs.createWriteStream('file2.txt');

readStream.pipe(writeStream);

console.log('finished');
