// file.js

var fs = require('fs');

var file = {

  read: function(path, callback) {
    fs.readFile(path, 'utf8', function(err, data) {
      if (err) {
        console.log(err);
        return;
      }
      callback(data);
    });
  },

  write: function(path, data, callback) {
    fs.writeFile(path, data, function(err) {
      if (err) {
        console.log(err);
        return;
      }
      callback();
    });
  }
};

module.exports = file;
