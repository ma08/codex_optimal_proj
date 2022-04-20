var fs = require('fs');
var path = require('path');
var util = require('util');

var filepath = path.join(__dirname, 'file.js');

fs.stat(filepath, function(err, stats) {
  if (err) {
    console.log(err);
  } else {
    console.log(stats);
    console.log(util.inspect(stats));
    console.log(stats.isFile());
    console.log(stats.isDirectory());
    console.log(stats.isBlockDevice());
    console.log(stats.isCharacterDevice());
    console.log(stats.isFIFO());
    console.log(stats.isSocket());
    console.log(stats.size);
    console.log(stats.birthtime);
    console.log(stats.mtime);
  }
});
