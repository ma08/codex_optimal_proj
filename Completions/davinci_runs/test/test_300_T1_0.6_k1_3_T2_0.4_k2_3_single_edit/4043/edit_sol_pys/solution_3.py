function readFile(file) {
  var fs = require('fs');
  var content;
  fs.readFile(file, 'utf8', function(err, data) {
    if (err) {
      return console.log(err);
    }
    content = data;
  });
  return content;
}

function writeFile(file, data) {
  var fs = require('fs');
  fs.writeFile(file, data, function(err) {
    if (err) {
      return console.log(err);
    }
  });
}

module.exports = {
  readFile: readFile,
  writeFile: writeFile
}
