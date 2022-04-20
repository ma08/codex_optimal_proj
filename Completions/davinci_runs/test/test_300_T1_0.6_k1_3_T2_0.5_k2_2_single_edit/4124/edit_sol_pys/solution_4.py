var fs = require('fs');

// // read file
// fs.readFile('input.txt', function(err, data) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("Asynchronous read: " + data.toString());
// });

// // write file
// fs.writeFile('output.txt', 'Hello world!', function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("Data written successfully!");
//     console.log("Let's read newly written data");
//     fs.readFile('output.txt', function(err, data) {
//         if (err) {
//             return console.error(err);
//         }
//         console.log("Asynchronous read: " + data.toString());
//     });
// });

// // open file
// fs.open('input.txt', 'r+', function(err, fd) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("File opened successfully!");
// });

// // get file info
// fs.stat('input.txt', function(err, stats) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log(stats);
//     console.log("Got file info successfully!");

//     // Check file type
//     console.log("isFile ? " + stats.isFile());
//     console.log("isDirectory ? " + stats.isDirectory());
// });

// // truncate file
// fs.ftruncate(fd, 10, function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("File truncated successfully.");
//     console.log("Going to read the same file");
//     fs.read(fd, buf, 0, buf.length, 0, function(err, bytes) {
//         if (err) {
//             console.log(err);
//         }
//         // Print only read bytes to avoid junk.
//         if (bytes > 0) {
//             console.log(buf.slice(0, bytes).toString());
//         }
//         // Close the opened file.
//         fs.close(fd, function(err) {
//             if (err) {
//                 console.log(err);
//             }
//             console.log("File closed successfully.");
//         });
//     });
// });

// // delete file
// fs.unlink('input.txt', function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("File deleted successfully!");
// });

// // create directory
// fs.mkdir('/tmp/test', function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("Directory created successfully!");
// });

// // read directory
// fs.readdir("/tmp/", function(err, files) {
//     if (err) {
//         return console.error(err);
//     }
//     files.forEach(function(file) {
//         console.log(file);
//     });
// });

// // remove directory
// fs.rmdir("/tmp/test", function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log("Going to read directory /tmp");
//     fs.readdir("/tmp/", function(err, files) {
//         if (err) {
//             return console.error(err);
//         }
//         files.forEach(function(file) {
//             console.log(file);
//         });
//     });
// });
