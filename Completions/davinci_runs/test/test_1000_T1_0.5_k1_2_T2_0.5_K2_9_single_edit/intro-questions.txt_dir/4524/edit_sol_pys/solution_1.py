var fs = require('fs');

fs.readFile('test.txt', 'utf8', function(err, data) {
  if (err) throw err;
  console.log('OK: ' + 'test.txt');
  console.log(data)
});

console.log('after calling readFile');
