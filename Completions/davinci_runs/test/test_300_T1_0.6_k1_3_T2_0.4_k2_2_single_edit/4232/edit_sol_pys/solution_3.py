// file.js

var fs = require('fs');

var file = {
  read: function(filepath) {
    var content = fs.readFileSync(filepath, 'utf8');
    return content;
  },
  write: function(filepath, content) {
    fs.writeFileSync(filepath, content);
  }
};

module.exports = file;
