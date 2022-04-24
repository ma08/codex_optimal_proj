#!/usr/bin/env node

var fs = require('fs');
var path = require('path');

var file = process.argv[2];
var extension = path.extname(file);

if (extension === '.txt') {
  fs.readFile(file, 'utf8', function(err, data) {
    if (err) throw err;
    console.log(data);
  });
} else {
  console.log('Please provide a .txt file');
}
