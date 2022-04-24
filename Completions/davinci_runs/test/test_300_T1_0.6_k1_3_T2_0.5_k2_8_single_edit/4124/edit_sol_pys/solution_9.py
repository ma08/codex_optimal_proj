'use strict';

var fs = require('fs');
var path = require('path');
var cp = require('child_process');

var _require = require('./util'),
    log = _require.log;

var _require2 = require('./config'),
    getConfig = _require2.getConfig,
    getFiles = _require2.getFiles,
    getIgnoreFiles = _require2.getIgnoreFiles;

var _require3 = require('./git'),
    getBranch = _require3.getBranch;

var _require4 = require('./ask'),
    ask = _require4.ask;

var _require5 = require('./run'),
    run = _require5.run;

var _require6 = require('./check'),
    checkBranch = _require6.checkBranch,
    checkFiles = _require6.checkFiles;

var _require7 = require('./commit'),
    commit = _require7.commit;

var _require8 = require('./push'),
    push = _require8.push;

var _require9 = require('./pull'),
    pull = _require9.pull;

function getFile(name) {
  var filePath = path.join(process.cwd(), name);
  var file = fs.readFileSync(filePath, 'utf8');
  return file;
}

function getFilesInDir(dir) {
  var files = fs.readdirSync(dir);
  return files;
}

function getFilesInDirRecursive(dir, filelist) {
  var files = fs.readdirSync(dir);
  filelist = filelist || [];
  files.forEach(function (file) {
    if (fs.statSync(path.join(dir, file)).isDirectory()) {
      filelist = getFilesInDirRecursive(path.join(dir, file), filelist);
    } else {
      filelist.push(path.join(dir, file));
    }
  });
  return filelist;
}

function getDir(name) {
  var dirPath = path.join(process.cwd(), name);
  var files = fs.readdirSync(dirPath);
  return files;
}

function getDirectories(name) {
  var dirPath = path.join(process.cwd(), name);
  var files = getFilesInDirRecursive(dirPath);
  return files;
}

function getFileList(name) {
  var dirPath = path.join(process.cwd(), name);
  var files = getFilesInDirRecursive(dirPath);
  return files;
}

function getFileListInDir(name) {
  var dirPath = path.join(process.cwd(), name);
  var files = getFilesInDir(dirPath);
  return files;
}

function getFileListInDirRecursive(name) {
  var dirPath = path.join(process.cwd(), name);
  var files = getFilesInDirRecursive(dirPath);
  return files;
}

function getFileName(filePath) {
  var fileName = filePath.split('/').pop();
  return fileName;
}

function getFilePath(filePath) {
  var fileName = filePath.split('/').pop();
  return fileName;
}

function getFileExtension(filePath) {
  var fileExtension = filePath.split('.').pop();
  return fileExtension;
}

module.exports = {
  getFile: getFile,
  getDir: getDir,
  getFileList: getFileList,
  getFileListInDir: getFileListInDir,
  getFileListInDirRecursive: getFileListInDirRecursive,
  getFileName: getFileName,
  getFilePath: getFilePath,
  getFileExtension: getFileExtension,
  getDirectories: getDirectories
};
