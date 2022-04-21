var fs = require('fs');

var data = process.argv[2];

fs.writeFile('hello.txt', data, function(err){
    if (err) throw err;
    console.log('Saved!');
});
