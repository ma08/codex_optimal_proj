// The file system module allows you to work with the file system on your computer.

// To include the File System module, use the require() method:

var fs = require('fs');

// Create a File:

// To create a file in Node.js, you can use one of the following methods:

// fs.appendFile()
// fs.open()
// fs.writeFile()

// The fs.appendFile() method appends specified content to a file. If the file does not exist, the file will be created:

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});

// The fs.open() method takes a "flag" as the second argument, if the flag is "w" for "writing", the specified file is opened for writing. If the file does not exist, an empty file is created:

fs.open('mynewfile2.txt', 'w', function (err, file) {
  if (err) throw err;
  console.log('Saved!');
});

// The fs.writeFile() method replaces the specified file and content if it exists. If the file does not exist, a new file, containing the specified content, will be created:

fs.writeFile('mynewfile3.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});

// The fs.writeFile() method is used to update the specified file with the specified data:

fs.writeFile('mynewfile3.txt', 'This is my text', function (err) {
  if (err) throw err;
  console.log('Replaced!');
});

// The fs.appendFile() method appends the specified content at the end of the specified file:

fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
  if (err) throw err;
  console.log('Updated!');
});

// The fs.appendFile() method appends the specified content at the end of the specified file:

fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
  if (err) throw err;
  console.log('Updated!');
});

// The fs.unlink() method deletes the specified file:

fs.unlink('mynewfile2.txt', function (err) {
  if (err) throw err;
  console.log('File deleted!');
});

// The fs.rename() method renames the specified file:

fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err) {
  if (err) throw err;
  console.log('File Renamed!');
});

// Read a File:

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// To read the file, you can use the following method:

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});

// The fs.readFile() method is used to read files on your computer.

fs.readFile('mynewfile3.txt', 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
