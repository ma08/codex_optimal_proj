// in node.js, we can access the filesystem with the 'fs' module
var fs = require('fs');

// fs.readFile('./file.txt', 'utf8', function(err, data) {
//   if (err) {
//     throw err;
//   }
//   console.log(data);
// });

// fs.writeFile('./file.txt', 'hello world', function(err) {
//   if (err) {
//     throw err;
//   }
//   console.log('file saved!');
// });

var file = fs.readFileSync('./file.txt', 'utf8');
console.log(file);

fs.writeFileSync('./file.txt', 'hello world');
