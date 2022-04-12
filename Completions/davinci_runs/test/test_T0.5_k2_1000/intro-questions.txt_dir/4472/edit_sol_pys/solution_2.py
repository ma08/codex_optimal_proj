var fs = require('fs');

fs.readFile('file.txt', 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});

fs.writeFile('file.txt', 'Hello World!', function (err) {
  if (err) {
    return console.log(err);
  }
  console.log('The file was saved!');
});
