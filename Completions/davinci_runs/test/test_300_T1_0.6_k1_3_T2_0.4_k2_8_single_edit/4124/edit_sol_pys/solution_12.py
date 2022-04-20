var fs = require('fs');

var readStream = fs.createReadStream('file.txt');

readStream.on('open', function () {
  console.log('The file is open');
});
