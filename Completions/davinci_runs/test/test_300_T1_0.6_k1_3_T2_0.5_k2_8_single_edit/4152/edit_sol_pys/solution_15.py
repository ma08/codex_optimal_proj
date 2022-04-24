//file.js

var fs = require('fs');

fs.readFile('file.js', function (err, data) {
  if (err) throw err;
  console.log(data);
});

fs.writeFile('message.txt', 'Hello Node.js', function (err) {
  if (err) throw err;
  console.log('It\'s saved!');
});
