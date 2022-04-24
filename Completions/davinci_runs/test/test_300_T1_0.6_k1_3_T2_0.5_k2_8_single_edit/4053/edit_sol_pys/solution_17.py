var fs = require('fs');
var path = require('path');

function file(dir, ext, callback) {
  fs.readdir(dir, function(err, list) {
    if (err) {
      return callback(err);
    }
    var filtered = list.filter(function(file) {
      return path.extname(file) === '.' + ext;
    });
    callback(null, filtered);
  });
}

module.exports = file;
