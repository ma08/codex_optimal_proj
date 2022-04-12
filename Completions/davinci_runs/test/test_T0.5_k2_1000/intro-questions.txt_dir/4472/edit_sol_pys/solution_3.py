// file.js

var fs = require('fs');

var file = {};

file.read = function(path, callback) {
  fs.readFile(path, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    callback(data);
  });
};

file.write = function(path, data, callback) {
  fs.writeFile(path, data, function (err) {
    if (err) {
      console.log(err);
      return;
    }
    callback();
  });
};

module.exports = file;
