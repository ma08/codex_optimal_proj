var fs = require('fs');

fs.readFile('file.js', 'utf8', function(err, data) {
  if (err) throw err;
  console.log('OK: ' + 'file.js');
  console.log(data);
});

console.log('after calling readFile');
