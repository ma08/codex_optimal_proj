// var fs = require('fs');
// var file = fs.readFileSync(process.argv[2]);
// var lines = file.toString().split('\n').length - 1;
// console.log(lines);

var fs = require('fs');
var file = fs.readFile(process.argv[2], function (err, data) {
  var lines = data.toString().split('\n').length - 1;
  console.log(lines);
});
