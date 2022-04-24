// file.js

var fs = require('fs');
var path = require('path');

// You can use fs.readFile to read the file.
//
// fs.readFile(path.join(__dirname, 'file.txt'), function(err, data) {
//   console.log(data.toString());
// });

// You can use fs.writeFile to write the file.
//
// fs.writeFile(path.join(__dirname, 'file.txt'), 'Hello World', function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('File written');
// });

// You can use fs.appendFile to append the file.
//
// fs.appendFile(path.join(__dirname, 'file.txt'), 'Hello World', function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('File written');
// });

// You can use fs.rename to rename the file.
//
// fs.rename(path.join(__dirname, 'file.txt'), path.join(__dirname, 'file2.txt'), function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('File renamed');
// });

// You can use fs.unlink to delete the file.
//
// fs.unlink(path.join(__dirname, 'file2.txt'), function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('File deleted');
// });

// You can use fs.mkdir to create a directory.
//
// fs.mkdir(path.join(__dirname, 'test'), function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('Directory created');
// });

// You can use fs.rmdir to remove the directory.
//
// fs.rmdir(path.join(__dirname, 'test'), function(err) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log('Directory removed');
// });

// You can use fs.readdir to read the directory.
//
// fs.readdir(__dirname, function(err, files) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   files.forEach(function(file) {
//     console.log(file);
//   });
// });

// You can use fs.stat to get the file statistics.
//
// fs.stat(path.join(__dirname, 'file.txt'), function(err, stats) {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   console.log(stats);
// });

// You can use fs.exists to check if the file exists.
//
// fs.exists(path.join(__dirname, 'file.txt'), function(exists) {
//   console.log(exists);
// });
