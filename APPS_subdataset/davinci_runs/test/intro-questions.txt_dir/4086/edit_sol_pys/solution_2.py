const fs = require('fs');

fs.readFile('./file.txt', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data.toString());
    }
});

fs.writeFile('./file.txt', 'Hello World!', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File has been written');
    }
});

fs.appendFile('./file.txt', '\nHello World!', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File has been written');
    }
});

fs.rename('./file.txt', './file2.txt', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File has been renamed');
    }
});

fs.unlink('./file2.txt', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File has been deleted');
    }
});
