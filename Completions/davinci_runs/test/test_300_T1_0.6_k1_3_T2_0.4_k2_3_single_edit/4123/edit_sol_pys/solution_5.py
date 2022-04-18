var fs = require('fs');

module.exports = function(filePath, fileExtension, callback) {
  var extension = "." + fileExtension;
  fs.readdir(filePath, function(err, list) {
    if (err) {
      return callback(err);
    } else {
      var filteredList = list.filter(function(file) {
        return file.endsWith(extension);
      });
      return callback(null, filteredList);
    }
  });
};
