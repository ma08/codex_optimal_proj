var fs = require('fs');

fs.writeFile('/tmp/test', 'Hey there!', function (err) {
  if (err) throw err;
  console.log('It\'s saved!');
});

fs.readFile('/tmp/test', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
