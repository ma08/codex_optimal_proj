var fs = require('fs');

var fileName = './file.txt'

function readFile(fileName, callback) {
  fs.readFile(fileName, 'utf-8', function(err, data) {
    if (err) {
      console.log(err);
    } else {
      callback(data);
    }
  });
}

function writeFile(fileName, data, callback) {
  fs.writeFile(fileName, data, function(err) {
    if (err) {
      console.log(err);
    } else {
      callback();
    }
  });
}

function appendFile(fileName, data, callback) {
  fs.appendFile(fileName, data, function(err) {
    if (err) {
      console.log(err);
    } else {
      callback();
    }
  });
}

function deleteFile(fileName, callback) {
  fs.unlink(fileName, function(err) {
    if (err) {
      console.log(err);
    } else {
      callback();
    }
  });
}

// readFile(fileName, function(data) {
//   console.log(data);
// });
//
// writeFile(fileName, 'hello world', function() {
//   console.log('write file success');
// });
//
// appendFile(fileName, '\nhello world again', function() {
//   console.log('append file success');
// });

deleteFile(fileName, function() {
  console.log('delete file success');
});
