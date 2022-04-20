var fs = require('fs');

var readStream = fs.createReadStream('file.txt');

readStream.on('data', function(chunk) {
  console.log(chunk);
});

readStream.on('end', function() {
  console.log('finished reading file');
});
