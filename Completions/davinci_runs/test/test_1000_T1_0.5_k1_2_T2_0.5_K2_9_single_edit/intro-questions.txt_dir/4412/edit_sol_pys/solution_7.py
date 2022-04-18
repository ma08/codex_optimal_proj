const fs = require('fs');

const readFile = (filename, enc) => {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, enc, (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
};

const writeFile = (filename, data) => {
    return new Promise((resolve, reject) => {
        fs.writeFile(filename, data, (err) => {
            if (err) {
                reject(err);
            } else {
                resolve();
            }
        });
    });
};

module.exports = {
    readFile,
    writeFile
};
