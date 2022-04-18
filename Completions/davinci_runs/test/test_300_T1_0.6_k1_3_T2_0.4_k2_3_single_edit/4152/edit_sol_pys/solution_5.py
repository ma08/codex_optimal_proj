// file.js

var fs = require('fs');

var file = {
  read: function(path) {
    return fs.readFileSync(path, 'utf8');
  },
  write: function(path, data) {
    fs.writeFileSync(path, data, 'utf8');
  }
};

module.exports = file;
