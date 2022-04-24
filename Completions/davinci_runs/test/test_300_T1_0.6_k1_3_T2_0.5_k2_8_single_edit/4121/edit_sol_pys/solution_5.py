var fs = require('fs');

fs.readFile('input.txt', function (err, data) {
    if (err) {
        return console.error(err);
    }
    console.log("Asynchronous read: " + data.toString());
});

var data = fs.readFileSync('input.txt');
console.log("Synchronous read: " + data.toString());

console.log("Program Ended");

fs.open('input.txt', 'r+', function (err, fd) {
    if (err) {
        return console.error(err);
    }
    console.log("File opened successfully!");
});

console.log("Going to get file info!");
fs.stat('input.txt', function (err, stats) {
    if (err) {
        return console.error(err);
    }
    console.log(stats);
    console.log("Got file info successfully!");

    // Check file type
    console.log("isFile ? " + stats.isFile());
    console.log("isDirectory ? " + stats.isDirectory());
});

console.log("Going to write into existing file");
fs.writeFile('input.txt', 'Simply Easy Learning!', function (err) {
    if (err) {
        return console.error(err);
    }

    console.log("Data written successfully!");
    console.log("Let's read newly written data");
    fs.readFile('input.txt', function (err, data) {
        if (err) {
            return console.error(err);
        }
        console.log("Asynchronous read: " + data.toString());
    });
});

console.log("Going to delete an existing file");
fs.unlink('input.txt', function (err) {
    if (err) {
        return console.error(err);
    }
    console.log("File deleted successfully!");
});

console.log("Going to create directory /tmp/test");
fs.mkdir('/tmp/test', function (err) {
    if (err) {
        return console.error(err);
    }
    console.log("Directory created successfully!");
});

console.log("Going to read directory /tmp");
fs.readdir("/tmp/", function (err, files) {
    if (err) {
        return console.error(err);
    }
    files.forEach(function (file) {
        console.log(file);
    });
});

console.log("Going to delete directory /tmp/test");
fs.rmdir("/tmp/test", function (err) {
    if (err) {
        return console.error(err);
    }
    console.log("Going to read directory /tmp");

    fs.readdir("/tmp/", function (err, files) {
        if (err) {
            return console.error(err);
        }
        files.forEach(function (file) {
            console.log(file);
        });
    });
});
