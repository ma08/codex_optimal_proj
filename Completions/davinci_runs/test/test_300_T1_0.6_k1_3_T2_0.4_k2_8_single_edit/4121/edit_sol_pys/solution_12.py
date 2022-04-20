const fs = require('fs');

function readFile(filename, callback) {
  fs.readFile(filename, 'utf8', function(err, data) {
    if (err) {
      console.log(err);
    } else {
      callback(data);
    }
  });
}

function writeFile(filename, data, callback) {
  fs.writeFile(filename, data, function(err) {
    if (err) {
      console.log(err);
    } else {
      callback();
    }
  });
}

module.exports = {
  readFile: readFile,
  writeFile: writeFile
};
