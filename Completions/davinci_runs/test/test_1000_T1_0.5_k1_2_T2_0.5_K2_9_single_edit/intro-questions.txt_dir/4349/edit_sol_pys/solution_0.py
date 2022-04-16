// 
// 
// 

var fs = require('fs');

var file = new file();

file.readFile('./test.txt', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
