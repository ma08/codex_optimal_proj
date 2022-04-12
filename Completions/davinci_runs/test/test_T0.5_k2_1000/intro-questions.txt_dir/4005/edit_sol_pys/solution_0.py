var fs = require('fs');

var readStream = fs.createReadStream('./file.txt', 'utf8');
var writeStream = fs.createWriteStream('./write.txt');

readStream.on('data', function(chunk) {
    writeStream.write(chunk);
});
