const fs = require('fs');
const path = require('path');

function File(filePath) {
    this.path = filePath;
    this.name = path.basename(filePath);
    this.extension = path.extname(filePath);
    this.size = fs.statSync(filePath).size;
}

File.prototype.read = function(callback) {
    fs.readFile(this.path, function(err, data) {
        if (err) {
            callback(err);
        } else {
            callback(null, data);
        }
    });
};

File.prototype.write = function(data, callback) {
    fs.writeFile(this.path, data, function(err) {
        if (err) {
            callback(err);
        } else {
            callback(null);
        }
    });
};

module.exports = File;
