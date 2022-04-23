var fs = require('fs');

exports.readFile = function (fileName, cb) {
    fs.readFile(fileName, function (err, data) {
        if (err) {
            cb(err);
        }
        cb(null, data);
    });
};

exports.writeFile = function (fileName, data, cb) {
    fs.writeFile(fileName, data, function (err) {
        if (err) {
            cb(err);
        }
        cb(null);
    });
};
