var fs = require('fs');

fs.readFile('file.txt', 'utf8', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});

console.log("Reading file...");
