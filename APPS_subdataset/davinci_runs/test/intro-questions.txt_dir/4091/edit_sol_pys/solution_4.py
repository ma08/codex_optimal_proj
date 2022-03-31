var fs = require('fs');

var file = fs.readFileSync('file.txt', 'utf8');

var lines = file.split('\n');

var newLines = [];

lines.forEach(function(line) {
  var words = line.split(' ');

  var newWords = [];

  words.forEach(function(word) {
    var newWord = word.replace(/[^a-zA-Z]/g, '');

    newWords.push(newWord);
  });

  var newLine = newWords.join(' ');

  newLines.push(newLine);
});

var newFile = newLines.join('\n');

fs.writeFileSync('newFile.txt', newFile);
