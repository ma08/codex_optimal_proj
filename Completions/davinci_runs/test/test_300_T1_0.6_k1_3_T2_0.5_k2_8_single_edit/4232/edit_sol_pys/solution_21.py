var fs = require('fs');
var path = require('path');

var file = "./file.txt";

fs.readFile(file, 'utf8', function(err, data) {
  if (err) throw err;
  console.log('OK: ' + file);
  console.log(data)
});

console.log('This is after the read call');
