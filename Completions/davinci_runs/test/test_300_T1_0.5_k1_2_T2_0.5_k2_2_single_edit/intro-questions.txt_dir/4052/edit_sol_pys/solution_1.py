var fs = require('fs')

fs.readFile('./file.js', function (err, data) {
  if (err) throw err;
  console.log(data);
});
