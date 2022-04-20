var fs = require('fs');
var path = require('path');

function print(error, files) {
  if (error) {
    return console.error(error);
  }
  files.forEach(function(file) {
    console.log(file);
  });
}

fs.readdir(process.argv[2], function(error, files) {
  if (error) {
    return console.error(error);
  }
  var filtered = files.filter(function(file) {
    return path.extname(file) === '.' + process.argv[3];
  });
  print(null, filtered);
});
