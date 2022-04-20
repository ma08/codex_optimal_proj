/**
 * Created by YYW on 2017/4/13.
 */
var fs = require('fs');
var path = require('path');

var file = {
    // 读取文件内容
    readFile: function(fileName) {
        return new Promise(function(resolve, reject) {
            fs.readFile(fileName, function(error, data) {
                if (error) return reject(error);
                resolve(data);
            });
        });
    },
    // 写入文件内容
    writeFile: function(fileName, data) {
        return new Promise(function(resolve, reject) {
            fs.writeFile(fileName, data, function(error) {
                if (error) return reject(error);
                resolve();
            });
        });
    },
    // 获取文件列表
    readDir: function(filePath) {
        return new Promise(function(resolve, reject) {
            fs.readdir(filePath, function(error, files) {
                if (error) return reject(error);
                resolve(files);
            });
        });
    },
    // 获取文件信息
    stat: function(filePath) {
        return new Promise(function(resolve, reject) {
            fs.stat(filePath, function(error, stats) {
                if (error) return reject(error);
                resolve(stats);
            });
        });
    },
    // 删除文件
    unlink: function(filePath) {
        return new Promise(function(resolve, reject) {
            fs.unlink(filePath, function(error) {
                if (error) return reject(error);
                resolve();
            });
        });
    },
    // 创建文件夹
    mkdir: function(filePath) {
        return new Promise(function(resolve, reject) {
            fs.mkdir(filePath, function(error) {
                if (error) return reject(error);
                resolve();
            });
        });
    },
    // 删除文件夹
    rmdir: function(filePath) {
        return new Promise(function(resolve, reject) {
            fs.rmdir(filePath, function(error) {
                if (error) return reject(error);
                resolve();
            });
        });
    },
    // 删除文件夹（递归删除）
    rmdirRecursive: function(filePath) {
        var me = this;
        return me.readDir(filePath).then(function(files) {
            return Promise.all(files.map(function(file) {
                return me.stat(path.join(filePath, file)).then(function(stats) {
                    if (stats.isDirectory()) {
                        return me.rmdirRecursive(path.join(filePath, file));
                    } else {
                        return me.unlink(path.join(filePath, file));
                    }
                });
            }));
        }).then(function() {
            return me.rmdir(filePath);
        });
    },
    // 复制文件
    copyFile: function(sourcePath, targetPath) {
        var me = this;
        return me.readFile(sourcePath).then(function(data) {
            return me.writeFile(targetPath, data);
        });
    },
    // 复制文件夹
    copyDir: function(sourcePath, targetPath) {
        var me = this;
        return me.readDir(sourcePath).then(function(files) {
            return Promise.all(files.map(function(file) {
                return me.stat(path.join(sourcePath, file)).then(function(stats) {
                    if (stats.isDirectory()) {
                        return me.mkdir(path.join(targetPath, file)).then(function() {
                            return me.copyDir(path.join(sourcePath, file), path.join(targetPath, file));
                        });
                    } else {
                        return me.copyFile(path.join(sourcePath, file), path.join(targetPath, file));
                    }
                });
            }));
        });
    }
};

module.exports = file;
