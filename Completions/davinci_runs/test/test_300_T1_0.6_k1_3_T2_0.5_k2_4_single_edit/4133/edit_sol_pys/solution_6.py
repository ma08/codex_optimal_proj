var fs = require('fs');

function readFile(fileName) {
    return function(cb) {
        fs.readFile(fileName, 'utf-8', cb);
    };
}

function writeFile(fileName, contents) {
    return function(cb) {
        fs.writeFile(fileName, contents, cb);
    };
}

function appendFile(fileName, contents) {
    return function(cb) {
        fs.appendFile(fileName, contents, cb);
    };
}

function deleteFile(fileName) {
    return function(cb) {
        fs.unlink(fileName, cb);
    };
}

function renameFile(oldName, newName) {
    return function(cb) {
        fs.rename(oldName, newName, cb);
    };
}

function getFiles(dirPath) {
    return function(cb) {
        fs.readdir(dirPath, cb);
    };
}

function getFileSize(fileName) {
    return function(cb) {
        fs.stat(fileName, function(err, stats) {
            if (err) {
                cb(err);
            } else {
                cb(null, stats.size);
            }
        });
    };
}

function getFileModifiedTime(fileName) {
    return function(cb) {
        fs.stat(fileName, function(err, stats) {
            if (err) {
                cb(err);
            } else {
                cb(null, stats.mtime);
            }
        });
    };
}

function getFileCreatedTime(fileName) {
    return function(cb) {
        fs.stat(fileName, function(err, stats) {
            if (err) {
                cb(err);
            } else {
                cb(null, stats.birthtime);
            }
        });
    };
}

function getFileAccessTime(fileName) {
    return function(cb) {
        fs.stat(fileName, function(err, stats) {
            if (err) {
                cb(err);
            } else {
                cb(null, stats.atime);
            }
        });
    };
}

function getFileChangedTime(fileName) {
    return function(cb) {
        fs.stat(fileName, function(err, stats) {
            if (err) {
                cb(err);
            } else {
                cb(null, stats.ctime);
            }
        });
    };
}

module.exports = {
    readFile: readFile,
    writeFile: writeFile,
    appendFile: appendFile,
    deleteFile: deleteFile,
    renameFile: renameFile,
    getFiles: getFiles,
    getFileSize: getFileSize,
    getFileModifiedTime: getFileModifiedTime,
    getFileCreatedTime: getFileCreatedTime,
    getFileAccessTime: getFileAccessTime,
    getFileChangedTime: getFileChangedTime
};
