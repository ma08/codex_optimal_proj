var fs = require('fs');

function readFile(filename) {
    fs.readFile(filename, function(err, data) {
        if (err) {
            console.log(err);
        }
        else {
            console.log(data);
        }
    });
}

function writeFile(filename, data) {
    fs.writeFile(filename, data, function(err) {
        if (err) {
            console.log(err);
        }
        else {
            console.log('Write success!');
        }
    });
}

function readDir(dir) {
    fs.readdir(dir, function(err, data) {
        if (err) {
            console.log(err);
        }
        else {
            console.log(data);
        }
    });
}

function checkFileExistence(filename) {
    fs.exists(filename, function(exists) {
        console.log(exists ? 'File exists' : 'File not found');
    });
}

function checkFileStats(filename) {
    fs.stat(filename, function(err, stats) {
        if (err) {
            console.log(err);
        }
        else {
            console.log(stats);
        }
    });
}

function createReadStream(filename) {
    var stream = fs.createReadStream(filename);
    stream.on('data', function(data) {
        console.log(data);
    });
    stream.on('end', function() {
        console.log('Read stream end');
    });
    stream.on('error', function(err) {
        console.log(err);
    });
}

function createWriteStream(filename) {
    var stream = fs.createWriteStream(filename);
    stream.write('Hello');
    stream.write('World');
    stream.end();
}

// readFile('file.js');
// writeFile('test.txt', 'Hello World!');
// readDir('.');
// checkFileExistence('test.txt');
// checkFileStats('test.txt');
// createReadStream('test.txt');
// createWriteStream('test.txt');
