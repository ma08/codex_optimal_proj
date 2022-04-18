var fs = require('fs');

function readFile(filename) {
  var data = fs.readFileSync(filename, 'utf8');
  return data;
}

function writeFile(filename, data) {
  fs.writeFileSync(filename, data);
}

function readLines(filename) {
  var data = readFile(filename);
  var lines = data.split('\n');
  return lines;
}

function writeLines(filename, lines) {
  var data = lines.join('\n');
  writeFile(filename, data);
}

module.exports = {
  readFile: readFile,
  writeFile: writeFile,
  readLines: readLines,
  writeLines: writeLines
};
