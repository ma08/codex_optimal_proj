var fs = require('fs');

function read(file) {
  return new Promise(function(resolve, reject) {
    fs.readFile(file, function(err, data) {
      if (err) reject(err);
      resolve(data);
    });
  });
}

function write(file, data) {
  return new Promise(function(resolve, reject) {
    fs.writeFile(file, data, function(err) {
      if (err) reject(err);
      resolve();
    });
  });
}

module.exports = {
  read: read,
  write: write
};
