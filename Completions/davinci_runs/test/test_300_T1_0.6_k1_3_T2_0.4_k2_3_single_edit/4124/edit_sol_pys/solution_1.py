var fs = require('fs');

// fs.readFile('sample.txt', 'utf8', function(err, data){
//     console.log(data);
// });

// fs.writeFile('sample.txt', 'hello world', function(err){
//     console.log('file created');
// });

// fs.appendFile('sample.txt', 'hello world', function(err){
//     console.log('file created');
// });

// fs.unlink('sample.txt', function(err){
//     console.log('file deleted');
// });

// fs.rename('sample.txt', 'sample2.txt', function(err){
//     console.log('file renamed');
// });

fs.readdir('.', function(err, files){
    console.log(files);
});
