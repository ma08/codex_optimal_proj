var fs = require('fs');

var file = fs.createReadStream('file.txt');

file.on('readable', function () {
  var chunk = null;
  while (null !== (chunk = file.read())) {
    console.log(chunk.toString());
  }
});

file.on('end', function () {
  console.log('done');
});
