const fs = require('fs');
const path = require('path');

const readFile = (fileName) => {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

const writeFile = (fileName, data) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(fileName, data, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
};

const file = {
  readFile: readFile,
  writeFile: writeFile
};

module.exports = file;
