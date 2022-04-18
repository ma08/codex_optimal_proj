const fs = require('fs');

module.exports = {
    readFile: function (path) {
        return new Promise(function (resolve, reject) {
            fs.readFile(path, 'utf8', function (err, data) {
                if (err) {
                    reject(err);
                } else {
                    resolve(data);
                }
            });
        });
    },
    writeFile: function (path, data) {
        return new Promise(function (resolve, reject) {
            fs.writeFile(path, data, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    appendFile: function (path, data) {
        return new Promise(function (resolve, reject) {
            fs.appendFile(path, data, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    unlink: function (path) {
        return new Promise(function (resolve, reject) {
            fs.unlink(path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    rename: function (oldPath, newPath) {
        return new Promise(function (resolve, reject) {
            fs.rename(oldPath, newPath, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    mkdir: function (path) {
        return new Promise(function (resolve, reject) {
            fs.mkdir(path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    rmdir: function (path) {
        return new Promise(function (resolve, reject) {
            fs.rmdir(path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    readdir: function (path) {
        return new Promise(function (resolve, reject) {
            fs.readdir(path, function (err, files) {
                if (err) {
                    reject(err);
                } else {
                    resolve(files);
                }
            });
        });
    },
    stat: function (path) {
        return new Promise(function (resolve, reject) {
            fs.stat(path, function (err, stats) {
                if (err) {
                    reject(err);
                } else {
                    resolve(stats);
                }
            });
        });
    },
    readlink: function (path) {
        return new Promise(function (resolve, reject) {
            fs.readlink(path, function (err, linkString) {
                if (err) {
                    reject(err);
                } else {
                    resolve(linkString);
                }
            });
        });
    },
    symlink: function (target, path) {
        return new Promise(function (resolve, reject) {
            fs.symlink(target, path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    link: function (target, path) {
        return new Promise(function (resolve, reject) {
            fs.link(target, path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    },
    unlink: function (path) {
        return new Promise(function (resolve, reject) {
            fs.unlink(path, function (err) {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    }
};
