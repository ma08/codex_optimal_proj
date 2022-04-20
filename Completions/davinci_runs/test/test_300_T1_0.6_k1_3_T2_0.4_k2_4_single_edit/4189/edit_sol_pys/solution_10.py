var fs = require('fs');
var path = require('path');

var file = {
    read: function(filepath, encoding) {
        return fs.readFileSync(filepath, encoding);
    },
    write: function(filepath, content, encoding) {
        fs.writeFileSync(filepath, content, encoding);
    },
    copy: function(src, dst) {
        var content = fs.readFileSync(src);
        fs.writeFileSync(dst, content);
    },
    mkdirs: function(dirpath, mode) {
        if (!fs.existsSync(dirpath)) {
            var pathtmp;
            dirpath.split(path.sep).forEach(function(dirname) {
                if (pathtmp) {
                    pathtmp = path.join(pathtmp, dirname);
                }
                else {
                    pathtmp = dirname;
                }
                if (!fs.existsSync(pathtmp)) {
                    if (!fs.mkdirSync(pathtmp, mode)) {
                        return false;
                    }
                }
            });
        }
        return true;
    },
    rmdirs: function(dirpath) {
        if (fs.existsSync(dirpath)) {
            fs.readdirSync(dirpath).forEach(function(file, index) {
                var curPath = path.join(dirpath, file);
                if (fs.statSync(curPath).isDirectory()) {
                    file.rmdirs(curPath);
                } else {
                    fs.unlinkSync(curPath);
                }
            });
            fs.rmdirSync(dirpath);
        }
    },
    list: function(dirpath) {
        if (fs.existsSync(dirpath)) {
            var files = fs.readdirSync(dirpath);
            return files;
        } else {
            return [];
        }
    },
    isDir: function(dirpath) {
        if (fs.existsSync(dirpath)) {
            return fs.statSync(dirpath).isDirectory();
        } else {
            return false;
        }
    },
    isFile: function(filepath) {
        if (fs.existsSync(filepath)) {
            return fs.statSync(filepath).isFile();
        } else {
            return false;
        }
    }
};

module.exports = file;
