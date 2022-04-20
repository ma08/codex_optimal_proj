// var fs = require('fs');
// var rs = fs.createReadStream('./demofile.txt');
// rs.on('open', function () {
//   console.log('The file is open');
// });


// var fs = require('fs');
// var data = '';
// var readerStream = fs.createReadStream('./demofile.txt');
// readerStream.setEncoding('UTF8');
// readerStream.on('data', function(chunk) {
//   data += chunk;
// });
// readerStream.on('end',function(){
//   console.log(data);
// });
// readerStream.on('error', function(err){
//   console.log(err.stack);
// });
// console.log("Program Ended");


// var fs = require("fs");
// var data = 'Simply Easy Learning';
// var writerStream = fs.createWriteStream('output.txt');
// writerStream.write(data,'UTF8');
// writerStream.end();
// writerStream.on('finish', function() {
//     console.log("Write completed.");
// });
// writerStream.on('error', function(err){
//    console.log(err.stack);
// });
// console.log("Program Ended");


// var fs = require("fs");
// var data = 'Simply Easy Learning';
// var readerStream = fs.createReadStream('input.txt');
// var writerStream = fs.createWriteStream('output.txt');
// readerStream.pipe(writerStream);
// console.log("Program Ended");


// var fs = require("fs");
// var zlib = require('zlib');
// fs.createReadStream('input.txt')
//   .pipe(zlib.createGzip())
//   .pipe(fs.createWriteStream('input.txt.gz'));
// console.log("File Compressed.");


// var fs = require("fs");
// var zlib = require('zlib');
// fs.createReadStream('input.txt.gz')
//   .pipe(zlib.createGunzip())
//   .pipe(fs.createWriteStream('input.txt'));
// console.log("File Decompressed.");


// var fs = require("fs");
// fs.unlink('input.txt', function(err) {
//    if (err) throw err;
//    console.log('File deleted!');
// });


var fs = require("fs");
fs.rename('input.txt', 'input2.txt', function (err) {
  if (err) throw err;
  console.log('File Renamed!');
});
