var fs = require('fs');

// fs.readFile('./file.js', 'utf-8', function(err, data){
//   console.log(data);
// });

// fs.writeFile('./write.txt', 'hello world', function(err, data){
//   console.log(data);
// });

// fs.appendFile('./write.txt', '\nhello world', function(err, data){
//   console.log(data);
// });

// fs.open('./file.js', 'r', function(err, fd){
//   console.log(fd);
// });

// fs.rename('./file.js', './file.js', function(err, data){
//   console.log(data);
// });

// fs.stat('./file.js', function(err, stats){
//   if (stats.isFile()) {
//     console.log('is file');
//   } else if (stats.isDirectory()) {
//     console.log('is directory');
//   }
// });

// fs.unlink('./file.js', function(err, data){
//   console.log(data);
// });

// fs.readdir('./', function(err, files){
//   console.log(files);
// });

// fs.mkdir('./newDir', function(err, data){
//   console.log(data);
// });

fs.rmdir('./newDir', function(err, data){
  console.log(data);
});
