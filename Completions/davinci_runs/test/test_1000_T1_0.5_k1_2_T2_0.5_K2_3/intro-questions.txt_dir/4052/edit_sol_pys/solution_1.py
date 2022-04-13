var fs = require("fs");

var data = fs.readFileSync('input.txt');

console.log(data.toString());
console.log("Program Ended");

fs.readFile('input.txt', function(err, data){
    if(err) return console.error(err);
    console.log(data.toString());
});

console.log("Program Ended");

//open and close a file
console.log("Going to open a file!");
fs.open('input.txt', 'r+', function(err, fd){
    if(err) {
        return console.error(err);
    }
    console.log("File opened successfully!");
});

//get file information
console.log("Going to get file info!");
fs.stat('input.txt', function(err, stats){
    if(err) {
        return console.error(err);
    }
    console.log(stats);
    console.log("Got file info successfully!");

    //check file type
    console.log("isFile ? " + stats.isFile());
    console.log("isDirectory ? " + stats.isDirectory());
});

//writing a file
console.log("Going to write into existing file");
fs.writeFile('input.txt', 'Simply Easy Learning!', function(err){
    if(err) {
        return console.error(err);
    }

    console.log("Data written successfully!");
    console.log("Let's read newly written data");
    fs.readFile('input.txt', function(err, data){
        if(err) {
            return console.error(err);
        }
        console.log("Asynchronous read: " + data.toString());
    });
});

//read file
console.log("Going to read file");
fs.readFile('input.txt', function(err, data){
    if(err) {
        return console.error(err);
    }
    console.log("Asynchronous read: " + data.toString());
});

//close file
console.log("Going to close the file");
fs.close('input.txt', function(err, data){
    if(err) {
        return console.error(err);
    }
    console.log("File closed successfully!");
});

//delete file
console.log("Going to delete an existing file");
fs.unlink('input.txt', function(err){
    if(err) {
        return console.error(err);
    }
    console.log("File deleted successfully!");
});

//create a directory
console.log("Going to create directory /tmp/test");
fs.mkdir('/tmp/test', function(err){
    if(err) {
        return console.error(err);
    }
    console.log("Directory created successfully!");
});

//read directory
console.log("Going to read directory /tmp");
fs.readdir("/tmp/", function(err, files){
    if(err) {
        return console.error(err);
    }
    files.forEach(function(file){
        console.log(file);
    });
});

//remove directory
console.log("Going to remove directory /tmp/test");
fs.rmdir("/tmp/test", function(err){
    if(err) {
        return console.error(err);
    }
    console.log("Going to read directory /tmp");
    fs.readdir("/tmp/", function(err, files){
        if(err) {
            return console.error(err);
        }
        files.forEach(function(file){
            console.log(file);
        });
    });
});
