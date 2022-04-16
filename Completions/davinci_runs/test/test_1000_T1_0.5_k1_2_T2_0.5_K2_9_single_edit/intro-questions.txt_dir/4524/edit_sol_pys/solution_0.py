var fs = require('fs');
var path = require('path');
var file = path.join(__dirname, 'file.txt');

fs.readFile(file, function(err, data) {
  if (err) {
    throw err;
  }

  var lines = data.toString().split('\n');

  console.log(lines);
});
