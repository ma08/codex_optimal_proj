var fs = require('fs');

module.exports = {
  readFile : function(path, callback) {
    fs.readFile(path, function(err, data) {
      if(err) {
        console.log('readFile error');
      } else {
        callback(data);
      }
    });
  },
  writeFile : function(path, data, callback) {
    fs.writeFile(path, data, function(err) {
      if(err) {
        console.log('writeFile error');
      } else {
        callback();
      }
    });
  }
};


























