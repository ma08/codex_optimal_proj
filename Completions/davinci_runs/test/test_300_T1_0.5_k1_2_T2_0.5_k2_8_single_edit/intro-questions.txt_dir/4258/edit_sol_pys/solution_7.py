var fs = require('fs');

fs.readFile('./file.txt', function(err, data){
  if(err){
    throw err;
  }
  console.log(data.toString());
});

console.log('this will be executed before the readFile callback');
