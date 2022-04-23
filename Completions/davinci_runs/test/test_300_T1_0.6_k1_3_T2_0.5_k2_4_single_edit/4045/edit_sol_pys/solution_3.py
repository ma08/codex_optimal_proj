
var fs = require('fs');

module.exports = {
    readFile: function(file) {
        return new Promise(function(resolve, reject) {
            fs.readFile(file, function(err, data) {
                if (err) return reject(err);
                resolve(data);
            });
        });
    },
    writeFile: function(file, data) {
        return new Promise(function(resolve, reject) {
            fs.writeFile(file, data, function(err) {
                if (err) return reject(err);
                resolve();
            });
        });
    }
};
