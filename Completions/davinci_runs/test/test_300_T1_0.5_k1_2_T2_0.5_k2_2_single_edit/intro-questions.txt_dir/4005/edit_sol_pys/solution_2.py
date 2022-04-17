const fs = require('fs');
const path = require('path');

const getFilePath = (file) => {
  return path.resolve(__dirname, 'files', file);
};

const getFile = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(getFilePath(file), 'utf-8', (err, data) => {
      if (err) {
        reject(err);
      }
      resolve(data);
    });
  });
};

const writeFile = (file, data) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(getFilePath(file), data, 'utf-8', (err) => {
      if (err) {
        reject(err);
      }
      resolve();
    });
  });
};

const appendFile = (file, data) => {
  return new Promise((resolve, reject) => {
    fs.appendFile(getFilePath(file), data, 'utf-8', (err) => {
      if (err) {
        reject(err);
      }
      resolve();
    });
  });
};

const deleteFile = (file) => {
  return new Promise((resolve, reject) => {
    fs.unlink(getFilePath(file), (err) => {
      if (err) {
        reject(err);
      }
      resolve();
    });
  });
};

const renameFile = (file, newFile) => {
  return new Promise((resolve, reject) => {
    fs.rename(getFilePath(file), getFilePath(newFile), (err) => {
      if (err) {
        reject(err);
      }
      resolve();
    });
  });
};

module.exports = {
  getFilePath,
  getFile,
  writeFile,
  appendFile,
  deleteFile,
  renameFile
};
