function read(file) {
    var fs = require('fs');
    var contents = fs.readFileSync(file, 'utf8');
    return contents;
}

function write(file, contents) {
    var fs = require('fs');
    fs.writeFileSync(file, contents, 'utf8');
}

module.exports = {
    read: read,
    write: write
}
