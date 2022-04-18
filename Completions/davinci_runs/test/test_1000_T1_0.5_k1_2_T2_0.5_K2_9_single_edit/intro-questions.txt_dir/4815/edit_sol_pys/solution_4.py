var fs = require('fs');
var path = require('path');

function File(fileName) {
    this.fileName = fileName;
}

File.prototype.getName = function() {
    return this.fileName;
}

File.prototype.getExtension = function() {
    return path.extname(this.fileName);
}

File.prototype.getSize = function() {
    return fs.statSync(this.fileName).size;
}

File.prototype.getModifiedDate = function() {
    return fs.statSync(this.fileName).mtime.toLocaleDateString();
}

File.prototype.read = function() {
    return fs.readFileSync(this.fileName, 'utf8');
}

File.prototype.write = function(content) {
    fs.writeFileSync(this.fileName, content);
}

module.exports = File;
