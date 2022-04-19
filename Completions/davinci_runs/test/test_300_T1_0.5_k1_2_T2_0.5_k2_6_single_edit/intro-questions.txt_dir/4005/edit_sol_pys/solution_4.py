// fs.js

var fs = require('fs');

// Use fs to read a file
fs.readFile('/etc/passwd', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// Use fs to write a file
fs.writeFile('/tmp/test', 'Hey there!', function (err) {
  if (err) throw err;
  console.log('It\'s saved!');
});

// Use fs to read a directory
fs.readdir('/tmp/', function (err, files) {
  if (err) throw err;
  files.forEach(function (file) {
    console.log(file);
  });
});
