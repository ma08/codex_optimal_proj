function readFile(fileName) {
    return new Promise((resolve, reject) => {
        fs.readFile(fileName, (error, data) => {
            if (error) {
                reject(error);
            }
            resolve(data);
        });
    });
}

function writeFile(fileName, data) {
    return new Promise((resolve, reject) => {
        fs.writeFile(fileName, data, (error) => {
            if (error) {
                reject(error);
            }
            resolve();
        });
    });
}

function appendFile(fileName, data) {
    return new Promise((resolve, reject) => {
        fs.appendFile(fileName, data, (error) => {
            if (error) {
                reject(error);
            }
            resolve();
        });
    });
}

function deleteFile(fileName) {
    return new Promise((resolve, reject) => {
        fs.unlink(fileName, (error) => {
            if (error) {
                reject(error);
            }
            resolve();
        });
    });
}

function readDir(path) {
    return new Promise((resolve, reject) => {
        fs.readdir(path, (error, files) => {
            if (error) {
                reject(error);
            }
            resolve(files);
        });
    });
}

function createDir(path) {
    return new Promise((resolve, reject) => {
        fs.mkdir(path, (error) => {
            if (error) {
                reject(error);
            }
            resolve();
        });
    });
}

function deleteDir(path) {
    return new Promise((resolve, reject) => {
        fs.rmdir(path, (error) => {
            if (error) {
                reject(error);
            }
            resolve();
        });
    });
}

module.exports = {
    readFile,
    writeFile,
    appendFile,
    deleteFile,
    readDir,
    createDir,
    deleteDir
};
