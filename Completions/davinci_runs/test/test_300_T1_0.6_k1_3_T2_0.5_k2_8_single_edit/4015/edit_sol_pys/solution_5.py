var fs = require('fs');

fs.readFile('./data.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
  console.log(data.split('\n').length);
});
