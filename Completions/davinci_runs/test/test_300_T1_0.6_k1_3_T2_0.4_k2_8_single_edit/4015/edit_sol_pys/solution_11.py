var fs = require('fs');

function read(file, callback) {
  fs.readFile(file, 'utf8', function(err, data) {
    if (err) {
      console.log(err);
    }
    callback(data);
  });
}

function write(file, data, callback) {
  fs.writeFile(file, data, function(err) {
    if (err) {
      console.log(err);
    }
    callback();
  });
}

module.exports = {
  read: read,
  write: write
};
