const fs = require('fs');

const readFile = (filename, enc) => {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, enc, (err, data) => {
            if (err) reject(err);
            resolve(data);
        });
    });
};

const writeFile = (filename, data, enc) => {
    return new Promise((resolve, reject) => {
        fs.writeFile(filename, data, enc, (err) => {
            if (err) reject(err);
            resolve();
        });
    });
};

module.exports = {
    readFile,
    writeFile
};
