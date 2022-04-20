var fs = require('fs');

function getFileContent(fileName, callback) {
    fs.readFile(fileName, function (err, data) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null, data);
        }
    });
}

function getFileContentSync(fileName) {
    var data = fs.readFileSync(fileName);
    return data;
}

function writeFile(fileName, data, callback) {
    fs.writeFile(fileName, data, function (err) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null);
        }
    });
}

function writeFileSync(fileName, data) {
    fs.writeFileSync(fileName, data);
}

function readdir(path, callback) {
    fs.readdir(path, function (err, files) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null, files);
        }
    });
}

function readdirSync(path) {
    var files = fs.readdirSync(path);
    return files;
}

function isExist(path, callback) {
    fs.stat(path, function (err, stats) {
        if (err) {
            callback(false);
        } else {
            callback(true);
        }
    });
}

function isExistSync(path) {
    try {
        fs.statSync(path);
        return true;
    } catch (err) {
        return false;
    }
}

function isFile(path, callback) {
    fs.stat(path, function (err, stats) {
        if (err) {
            callback(false);
        } else {
            callback(stats.isFile());
        }
    });
}

function isFileSync(path) {
    try {
        var stats = fs.statSync(path);
        return stats.isFile();
    } catch (err) {
        return false;
    }
}

function isDirectory(path, callback) {
    fs.stat(path, function (err, stats) {
        if (err) {
            callback(false);
        } else {
            callback(stats.isDirectory());
        }
    });
}

function isDirectorySync(path) {
    try {
        var stats = fs.statSync(path);
        return stats.isDirectory();
    } catch (err) {
        return false;
    }
}

function mkdir(path, callback) {
    fs.mkdir(path, function (err) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null);
        }
    });
}

function mkdirSync(path) {
    fs.mkdirSync(path);
}

function rmdir(path, callback) {
    fs.rmdir(path, function (err) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null);
        }
    });
}

function rmdirSync(path) {
    fs.rmdirSync(path);
}

function unlink(path, callback) {
    fs.unlink(path, function (err) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null);
        }
    });
}

function unlinkSync(path) {
    fs.unlinkSync(path);
}

function rename(oldPath, newPath, callback) {
    fs.rename(oldPath, newPath, function (err) {
        if (err) {
            console.log(err);
            callback(err);
        } else {
            callback(null);
        }
    });
}

function renameSync(oldPath, newPath) {
    fs.renameSync(oldPath, newPath);
}

function copyFile(srcPath, destPath, callback) {
    var BUF_LENGTH = 64 * 1024;
    var buff = new Buffer(BUF_LENGTH);
    var fdr = fs.openSync(srcPath, 'r');
    var fdw = fs.openSync(destPath, 'w');
    var bytesRead = 1;
    var pos = 0;
    while (bytesRead > 0) {
        bytesRead = fs.readSync(fdr, buff, 0, BUF_LENGTH, pos);
        fs.writeSync(fdw, buff, 0, bytesRead);
        pos += bytesRead;
    }
    fs.closeSync(fdr);
    fs.closeSync(fdw);
    callback(null);
}

function copyFileSync(srcPath, destPath) {
    var BUF_LENGTH = 64 * 1024;
    var buff = new Buffer(BUF_LENGTH);
    var fdr = fs.openSync(srcPath, 'r');
    var fdw = fs.openSync(destPath, 'w');
    var bytesRead = 1;
    var pos = 0;
    while (bytesRead > 0) {
        bytesRead = fs.readSync(fdr, buff, 0, BUF_LENGTH, pos);
        fs.writeSync(fdw, buff, 0, bytesRead);
        pos += bytesRead;
    }
    fs.closeSync(fdr);
    fs.closeSync(fdw);
}

module.exports = {
    getFileContent: getFileContent,
    getFileContentSync: getFileContentSync,
    writeFile: writeFile,
    writeFileSync: writeFileSync,
    readdir: readdir,
    readdirSync: readdirSync,
    isExist: isExist,
    isExistSync: isExistSync,
    isFile: isFile,
    isFileSync: isFileSync,
    isDirectory: isDirectory,
    isDirectorySync: isDirectorySync,
    mkdir: mkdir,
    mkdirSync: mkdirSync,
    rmdir: rmdir,
    rmdirSync: rmdirSync,
    unlink: unlink,
    unlinkSync: unlinkSync,
    rename: rename,
    renameSync: renameSync,
    copyFile: copyFile,
    copyFileSync: copyFileSync
};
