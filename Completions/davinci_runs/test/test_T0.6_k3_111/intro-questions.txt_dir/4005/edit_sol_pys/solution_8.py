const fs = require('fs');

fs.readFile('./file.txt', 'utf8', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});

fs.writeFile('./file.txt', 'Hello World!', function (err) {
    if (err) {
        console.log(err);
    } else {
        console.log('File created!');
    }
});
