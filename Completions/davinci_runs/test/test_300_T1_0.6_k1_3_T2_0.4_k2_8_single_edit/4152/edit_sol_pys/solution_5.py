var fs = require('fs');
var path = require('path');

var mkdirp = require('mkdirp');

var file = {};

file.read = function(filepath, callback) {
  fs.readFile(filepath, 'utf8', function(err, data) {
    if (err) throw err;
    callback(data);
  });
};

file.write = function(filepath, data, callback) {
  mkdirp(path.dirname(filepath), function(err) {
    if (err) throw err;
    fs.writeFile(filepath, data, function(err) {
      if (err) throw err;
      callback();
    });
  });
};

module.exports = file;
