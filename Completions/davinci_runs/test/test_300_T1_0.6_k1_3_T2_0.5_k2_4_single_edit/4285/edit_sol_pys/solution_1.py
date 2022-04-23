var fs = require('fs');

// asynchronous

fs.readFile('file.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// synchronous

var data = fs.readFileSync('file.txt', 'utf8');
console.log(data);
