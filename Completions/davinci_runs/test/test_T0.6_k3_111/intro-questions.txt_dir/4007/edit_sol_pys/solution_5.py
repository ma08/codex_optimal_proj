const fs = require('fs');

function readFile(file) {
    return new Promise((resolve, reject) => {
        fs.readFile(file, (err, data) => {
            if (err) {
                reject(err);
            }
            resolve(data);
        });
    });
}

function writeFile(file, data) {
    return new Promise((resolve, reject) => {
        fs.writeFile(file, data, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function appendFile(file, data) {
    return new Promise((resolve, reject) => {
        fs.appendFile(file, data, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function unlink(file) {
    return new Promise((resolve, reject) => {
        fs.unlink(file, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function rename(oldPath, newPath) {
    return new Promise((resolve, reject) => {
        fs.rename(oldPath, newPath, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function copyFile(src, dest) {
    return new Promise((resolve, reject) => {
        fs.copyFile(src, dest, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function readDir(path) {
    return new Promise((resolve, reject) => {
        fs.readdir(path, (err, files) => {
            if (err) {
                reject(err);
            }
            resolve(files);
        });
    });
}

function mkdir(path) {
    return new Promise((resolve, reject) => {
        fs.mkdir(path, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function rmdir(path) {
    return new Promise((resolve, reject) => {
        fs.rmdir(path, (err) => {
            if (err) {
                reject(err);
            }
            resolve();
        });
    });
}

function stat(path) {
    return new Promise((resolve, reject) => {
        fs.stat(path, (err, stats) => {
            if (err) {
                reject(err);
            }
            resolve(stats);
        });
    });
}

function exists(path) {
    return new Promise((resolve) => {
        fs.exists(path, (exists) => {
            resolve(exists);
        });
    });
}

function createReadStream(path) {
    return fs.createReadStream(path);
}

function createWriteStream(path) {
    return fs.createWriteStream(path);
}

module.exports = {
    readFile,
    writeFile,
    appendFile,
    unlink,
    rename,
    copyFile,
    readDir,
    mkdir,
    rmdir,
    stat,
    exists,
    createReadStream,
    createWriteStream
};
