var fs = require('fs');

fs.readFile('file.txt', 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
