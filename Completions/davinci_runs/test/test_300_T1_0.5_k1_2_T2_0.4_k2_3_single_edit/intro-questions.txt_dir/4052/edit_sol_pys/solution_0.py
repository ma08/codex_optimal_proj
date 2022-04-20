const fs = require('fs');
const path = require('path');

function readFile(fileName) {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

function writeFile(fileName, data) {
  return new Promise((resolve, reject) => {
    fs.writeFile(fileName, data, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function readDir(dirName) {
  return new Promise((resolve, reject) => {
    fs.readdir(dirName, (err, files) => {
      if (err) {
        reject(err);
      } else {
        resolve(files);
      }
    });
  });
}

function createDir(dirName) {
  return new Promise((resolve, reject) => {
    fs.mkdir(dirName, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function stat(fileName) {
  return new Promise((resolve, reject) => {
    fs.stat(fileName, (err, stats) => {
      if (err) {
        reject(err);
      } else {
        resolve(stats);
      }
    });
  });
}

function copyFile(src, dest) {
  return new Promise((resolve, reject) => {
    fs.copyFile(src, dest, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function moveFile(src, dest) {
  return new Promise((resolve, reject) => {
    fs.rename(src, dest, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function deleteFile(fileName) {
  return new Promise((resolve, reject) => {
    fs.unlink(fileName, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function deleteDir(dirName) {
  return new Promise((resolve, reject) => {
    fs.rmdir(dirName, (err) => {
      if (err) {
        reject(err);
      } else {
        resolve();
      }
    });
  });
}

function deleteDirRecursive(dirName) {
  return readDir(dirName).then((files) => {
    const promises = files.map((file) => {
      const filePath = path.join(dirName, file);
      return stat(filePath).then((stats) => {
        if (stats.isDirectory()) {
          return deleteDirRecursive(filePath);
        }
        return deleteFile(filePath);
      });
    });
    return Promise.all(promises).then(() => deleteDir(dirName));
  });
}

function deleteFileOrDir(fileName) {
  return stat(fileName).then((stats) => {
    if (stats.isDirectory()) {
      return deleteDirRecursive(fileName);
    }
    return deleteFile(fileName);
  });
}

function getFileName(filePath) {
  return path.basename(filePath);
}

function getFileExtension(filePath) {
  return path.extname(filePath);
}

function getFileNameWithoutExtension(filePath) {
  const fileName = getFileName(filePath);
  const fileExtension = getFileExtension(fileName);
  return fileName.substring(0, fileName.length - fileExtension.length);
}

function getFilePathWithoutExtension(filePath) {
  const fileName = getFileName(filePath);
  const fileExtension = getFileExtension(fileName);
  return filePath.substring(0, filePath.length - fileExtension.length);
}

function getFileNameWithoutPath(filePath) {
  return path.basename(filePath);
}

function getFilePathWithoutFileName(filePath) {
  return path.dirname(filePath);
}

function getFilePath(...args) {
  return path.join(...args);
}

function getFilePathRelative(...args) {
  return path.relative(...args);
}

function getFilePathNormalized(...args) {
  return path.normalize(...args);
}

module.exports = {
  readFile,
  writeFile,
  readDir,
  createDir,
  stat,
  copyFile,
  moveFile,
  deleteFile,
  deleteDir,
  deleteDirRecursive,
  deleteFileOrDir,
  getFileName,
  getFileExtension,
  getFileNameWithoutExtension,
  getFilePathWithoutExtension,
  getFileNameWithoutPath,
  getFilePathWithoutFileName,
  getFilePath,
  getFilePathRelative,
  getFilePathNormalized,
};
