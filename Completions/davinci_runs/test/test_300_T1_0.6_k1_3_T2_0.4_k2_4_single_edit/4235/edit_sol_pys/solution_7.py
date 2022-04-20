// read file

var fs = require('fs');

fs.readFile('file.txt', 'utf8', function(err, data) {
  if (err) throw err;
  console.log(data);
});

// write file

fs.writeFile('file.txt', 'Hello Node.js', function(err) {
  if (err) throw err;
  console.log('It\'s saved!');
});

// delete file

fs.unlink('file.txt', function(err) {
  if (err) throw err;
  console.log('file deleted');
});
