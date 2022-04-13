// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');
// const writePath = path.join(__dirname, './files/write.txt');

// // console.log(filePath);
// // fs.readFile(filePath, function(err, data) {
// //     if (err) {
// //         console.log(err);
// //     } else {
// //         // console.log(data);
// //         console.log(data.toString());
// //     }
// // })

// // fs.writeFile(writePath, 'Hello World', function(err) {
// //     if (err) {
// //         console.log(err);
// //     } else {
// //         console.log('Write file success');
// //     }
// // })

// // fs.appendFile(writePath, '\nHello World', function(err) {
// //     if (err) {
// //         console.log(err);
// //     } else {
// //         console.log('Append file success');
// //     }
// // })

// fs.rename(writePath, './files/rename.txt', function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log('Rename file success');
//     }
// })

// fs.unlink('./files/rename.txt', function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log('Delete file success');
//     }
// })

// fs.mkdir('./files/test', function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log('Create folder success');
//     }
// })

// fs.rmdir('./files/test', function(err) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log('Delete folder success');
//     }
// })

// fs.readdir('./files', function(err, files) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(files);
//     }
// })


// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.readFile(filePath, function(err, data) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(data.toString());
//     }
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// const readStream = fs.createReadStream(filePath);
// // const writeStream = fs.createWriteStream('./files/write.txt');

// readStream.on('data', function(chunk) {
//     console.log(chunk);
//     // writeStream.write(chunk);
// })

// readStream.on('end', function() {
//     console.log('Read file success');
// })

// readStream.on('error', function(err) {
//     console.log(err);
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// const readStream = fs.createReadStream(filePath);
// const writeStream = fs.createWriteStream('./files/write.txt');

// readStream.pipe(writeStream);

// readStream.on('end', function() {
//     console.log('Read file success');
// })

// readStream.on('error', function(err) {
//     console.log(err);
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.stat(filePath, function(err, stats) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(stats.isFile());
//         console.log(stats.isDirectory());
//         console.log(stats);
//     }
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.open(filePath, 'r+', function(err, fd) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(fd);
//     }
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.open(filePath, 'r+', function(err, fd) {
//     if (err) {
//         console.log(err);
//     } else {
//         fs.ftruncate(fd, 10, function(err) {
//             if (err) {
//                 console.log(err);
//             } else {
//                 console.log('Truncate file success');
//             }
//         })
//     }
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.open(filePath, 'r+', function(err, fd) {
//     if (err) {
//         console.log(err);
//     } else {
//         var buff = new Buffer(255);
//         fs.read(fd, buff, 0, buff.length, 0, function(err, bytes) {
//             if (err) {
//                 console.log(err);
//             } else {
//                 if (bytes > 0) {
//                     console.log(buff.slice(0, bytes).toString());
//                 }
//                 fs.close(fd, function(err) {
//                     if (err) {
//                         console.log(err);
//                     } else {
//                         console.log('Close file success');
//                     }
//                 })
//             }
//         })
//     }
// })

// const fs = require('fs');
// const path = require('path');
// const filePath = path.join(__dirname, './files/file.txt');

// fs.open(filePath, 'r+', function(err, fd) {
//     if (err) {
//         console.log(err);
//     } else {
//         var buff = new Buffer('Hello World');
//         fs.write(fd, buff, 0, buff.length, 0, function(err, bytes) {
//             if (err) {
//                 console.log(err);
//             } else {
//                 console.log('Write file success');
//                 fs.close(fd, function(err) {
//                     if (err) {
//                         console.log(err);
//                     } else {
//                         console.log('Close file success');
//                     }
//                 })
//             }
//         })
//     }
// })
