var fs = require('fs');

// var file = fs.readFileSync(process.argv[2]);
// var file = file.toString();
// var file = file.split('\n');
// console.log(file.length - 1);

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  var file = data.split('\n');
  console.log(file.length - 1);
});
