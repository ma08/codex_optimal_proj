function readFile(filePath) {
    return new Promise(function(resolve, reject) {
        fs.readFile(filePath, 'utf8', function(err, data) {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}

function writeFile(filePath, data) {
    return new Promise(function(resolve, reject) {
        fs.writeFile(filePath, data, function(err) {
            if (err) {
                reject(err);
            } else {
                resolve();
            }
        });
    });
}

function appendFile(filePath, data) {
    return new Promise(function(resolve, reject) {
        fs.appendFile(filePath, data, function(err) {
            if (err) {
                reject(err);
            } else {
                resolve();
            }
        });
    });
}

module.exports = {
    readFile: readFile,
    writeFile: writeFile,
    appendFile: appendFile
};
