const fs = require('fs');

const readFile = (filepath, encoding) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filepath, encoding, (err, data) => {
      if (err) reject(err);
      resolve(data);
    });
  });
};

const writeFile = (filepath, data, encoding) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(filepath, data, encoding, (err) => {
      if (err) reject(err);
      resolve();
    });
  });
};

const appendFile = (filepath, data, encoding) => {
  return new Promise((resolve, reject) => {
    fs.appendFile(filepath, data, encoding, (err) => {
      if (err) reject(err);
      resolve();
    });
  });
};

const unlinkFile = (filepath) => {
  return new Promise((resolve, reject) => {
    fs.unlink(filepath, (err) => {
      if (err) reject(err);
      resolve();
    });
  });
};

module.exports = {
  readFile,
  writeFile,
  appendFile,
  unlinkFile,
};
