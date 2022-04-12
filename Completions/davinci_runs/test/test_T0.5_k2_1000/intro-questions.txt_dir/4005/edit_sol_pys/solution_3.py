var fs = require('fs');

var readStream = fs.createReadStream('file.txt');
var writeStream = fs.createWriteStream('write.txt');

readStream.on('data', function(chunk) {
    writeStream.write(chunk);
});
