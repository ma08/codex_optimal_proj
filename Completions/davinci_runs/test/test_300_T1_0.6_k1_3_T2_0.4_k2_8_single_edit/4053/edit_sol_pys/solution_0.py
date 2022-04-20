var fs = require('fs');

// read file
fs.readFile('file.txt', 'utf-8', function(err, data) {
  if (err) throw err;
  console.log(data);
});

// write file
fs.writeFile('newfile.txt', 'Hello content!', function(err) {
  if (err) throw err;
  console.log('Saved!');
});

// append file
fs.appendFile('newfile.txt', ' This is my text.', function(err) {
  if (err) throw err;
  console.log('Updated!');
});

// rename file
fs.rename('newfile.txt', 'renamedfile.txt', function(err) {
  if (err) throw err;
  console.log('File Renamed!');
});

// delete file
fs.unlink('renamedfile.txt', function(err) {
  if (err) throw err;
  console.log('File deleted!');
});
