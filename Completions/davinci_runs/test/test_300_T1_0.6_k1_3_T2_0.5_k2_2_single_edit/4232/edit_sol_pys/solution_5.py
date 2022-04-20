var fs = require('fs');

function readFile(filename, callback) {
    fs.readFile(filename, function(err, data) {
        if (err) throw err;
        callback(data.toString());
    });
}

function writeFile(filename, data, callback) {
    fs.writeFile(filename, data, function(err) {
        if (err) throw err;
        callback();
    });
}

function readJSON(filename, callback) {
    readFile(filename, function(data) {
        callback(JSON.parse(data));
    });
}

function writeJSON(filename, data, callback) {
    writeFile(filename, JSON.stringify(data), callback);
}

module.exports = {
    readFile: readFile,
    writeFile: writeFile,
    readJSON: readJSON,
    writeJSON: writeJSON
};
