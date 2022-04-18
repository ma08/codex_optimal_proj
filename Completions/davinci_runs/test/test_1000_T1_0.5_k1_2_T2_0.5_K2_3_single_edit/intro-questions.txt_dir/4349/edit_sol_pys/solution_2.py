var fs = require('fs');

module.exports = function(file, cb) {
  fs.readFile(file, function(err, data) {
    if (err) return cb(err);
    cb(null, data);
  });
}
