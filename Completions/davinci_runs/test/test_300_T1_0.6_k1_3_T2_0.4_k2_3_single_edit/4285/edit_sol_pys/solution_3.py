const fs = require('fs');

fs.readFile('./file.js', 'utf8', function(err, data) {
    if (err) throw err;
    console.log(data);
});

fs.writeFile('./file.js', 'utf8', function(err, data) {
    if (err) throw err;
    console.log(data);
});

fs.appendFile('./file.js', 'utf8', function(err, data) {
    if (err) throw err;
    console.log(data);
});

fs.open('./file.js', 'r', function(err, data) {
    if (err) throw err;
    console.log(data);
});

fs.close('./file.js', 'r', function(err, data) {
    if (err) throw err;
    console.log(data);
});

fs.unlink('./file.js', 'r', function(err, data) {
    if (err) throw err;
    console.log(data);
});
