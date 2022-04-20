//file.js

var fs = require('fs');

var file = {
  readFile: function(filePath) {
    return fs.readFileSync(filePath, 'utf-8');
  },
  writeFile: function(filePath, content) {
    return fs.writeFileSync(filePath, content, 'utf-8');
  }
};

module.exports = file;
