var fs = require('fs');

function readFile(filePath) {
  return fs.readFileSync(filePath, 'utf-8');
}

function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content);
}

function getDirFiles(dirPath) {
  return fs.readdirSync(dirPath);
}

function getFileExtension(filePath) {
  var fileExtension = filePath.split('.').pop();
  return fileExtension;
}

function getFileName(filePath) {
  var fileName = filePath.split('/').pop();
  return fileName;
}

function getFileContent(filePath) {
  var fileContent = readFile(filePath);
  return fileContent;
}

function getFileSize(filePath) {
  var fileSize = fs.statSync(filePath).size;
  return fileSize;
}

function isFile(filePath) {
  return fs.statSync(filePath).isFile();
}

function isDir(filePath) {
  return fs.statSync(filePath).isDirectory();
}

function hasExtension(filePath, extension) {
  var fileExtension = getFileExtension(filePath);
  return extension === fileExtension;
}

function hasContent(filePath, content) {
  var fileContent = getFileContent(filePath);
  return content === fileContent;
}

function hasSize(filePath, size) {
  var fileSize = getFileSize(filePath);
  return size === fileSize;
}

function hasName(filePath, name) {
  var fileName = getFileName(filePath);
  return name === fileName;
}

function hasFiles(dirPath, files) {
  var dirFiles = getDirFiles(dirPath);
  return files.length === dirFiles.length && files.every(function(file) {
    return dirFiles.indexOf(file) !== -1;
  });
}

module.exports = {
  readFile: readFile,
  writeFile: writeFile,
  getDirFiles: getDirFiles,
  getFileExtension: getFileExtension,
  getFileName: getFileName,
  getFileContent: getFileContent,
  getFileSize: getFileSize,
  isFile: isFile,
  isDir: isDir,
  hasExtension: hasExtension,
  hasContent: hasContent,
  hasSize: hasSize,
  hasName: hasName,
  hasFiles: hasFiles
};
