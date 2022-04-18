var fs = require('fs');
var path = require('path');

module.exports = function(dir, ext, callback) {
  fs.readdir(dir, function(err, files) {
    if (err) {
      return callback(err);
    }
    var filteredFiles = files.filter(function(file) {
      return path.extname(file) == '.' + ext;
    });
    callback(null, filteredFiles);
  });
};
