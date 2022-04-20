"use strict";

var fs = require("fs");

function readFile(fileName) {
  return new Promise(function (resolve, reject) {
    fs.readFile(fileName, function (err, result) {
      if (err) {
        reject(err);
      } else {
        resolve(result);
      }
    });
  });
}

function writeFile(fileName, data) {
  return new Promise(function (resolve, reject) {
    fs.writeFile(fileName, data, function (err) {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

module.exports = {
  readFile: readFile,
  writeFile: writeFile
};
