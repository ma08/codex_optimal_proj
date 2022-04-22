var fs = require('fs');
var Promise = require('bluebird');

function readFileAsync(fileName) {
  return new Promise(function(resolve, reject) {
    fs.readFile(fileName, function(err, data) {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

function* gen() {
  try {
    var f1 = yield readFileAsync('a.txt');
    var f2 = yield readFileAsync('b.txt');
    console.log(f1.toString());
    console.log(f2.toString());
  } catch (err) {
    console.log(err);
  }
}

var g = gen();

var r1 = g.next();
r1.value.then(function(data) {
  var r2 = g.next(data);
  r2.value.then(function(data) {
    var r3 = g.next(data);
  });
});
