const fs = require('fs');


const writeFile = (path, content) => {
    fs.writeFile(path, content, (err) => {
        if (err) throw err;
        console.log('The file has been saved!');
    });
}

const readFile = (path, callback) => {
    fs.readFile(path, 'utf8', (err, data) => {
        if (err) throw err;
        callback(data);
    });
}

const readFileSync = (path) => {
    return fs.readFileSync(path, 'utf8');
}

const readDir = (path, callback) => {
    fs.readdir(path, (err, files) => {
        if (err) throw err;
        callback(files);
    });
}

const readDirSync = (path) => {
    return fs.readdirSync(path);
}

const mkdir = (path) => {
    fs.mkdir(path, (err) => {
        if (err) throw err;
        console.log('Directory created!');
    });
}

const mkdirSync = (path) => {
    fs.mkdirSync(path);
}

const unlink = (path) => {
    fs.unlink(path, (err) => {
        if (err) throw err;
        console.log('File deleted!');
    });
}

const unlinkSync = (path) => {
    fs.unlinkSync(path);
}

const exists = (path) => {
    return fs.existsSync(path);
}

const rmdir = (path) => {
    fs.rmdir(path, (err) => {
        if (err) throw err;
        console.log('Directory deleted!');
    });
}

const rmdirSync = (path) => {
    fs.rmdirSync(path);
}




module.exports = {
    writeFile: writeFile,
    readFile: readFile,
    readFileSync: readFileSync,
    readDir: readDir,
    readDirSync: readDirSync,
    mkdir: mkdir,
    mkdirSync: mkdirSync,
    unlink: unlink,
    unlinkSync: unlinkSync,
    exists: exists,
    rmdir: rmdir,
    rmdirSync: rmdirSync
}
