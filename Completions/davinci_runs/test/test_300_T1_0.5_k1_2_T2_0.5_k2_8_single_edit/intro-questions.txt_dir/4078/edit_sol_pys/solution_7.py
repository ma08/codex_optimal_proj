var fs = require('fs');

var path = process.argv[2];

fs.readFile(path, 'utf8', function(err, data) {
  if (err) {
    throw err;
  }
  var lines = data.split('\n');
  var numNewlines = lines.length - 1;
  console.log(numNewlines);
});
