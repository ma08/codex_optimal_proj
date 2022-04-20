var fs = require('fs');
var path = require('path');

var file = fs.readFileSync(path.join(__dirname, './test.txt'), 'utf8');

var lines = file.split('\n');

var words = lines.map(function(line) {
  return line.split(' ');
});

var wordCount = words.map(function(word) {
  return word.length;
});

var total = wordCount.reduce(function(a, b) {
  return a + b;
});

console.log(total);
