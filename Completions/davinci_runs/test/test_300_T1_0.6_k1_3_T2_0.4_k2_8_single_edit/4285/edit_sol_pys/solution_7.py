const fs = require('fs');

fs.readFile('./file.txt', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data.toString());
    }
});

fs.writeFile('./file.txt', 'Hello World', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File written successfully');
    }
});

fs.appendFile('./file.txt', 'Hello World', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File written successfully');
    }
});

fs.rename('./file.txt', './file2.txt', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File renamed successfully');
    }
});

fs.unlink('./file2.txt', (err) => {
    if (err) {
        console.log(err);
    } else {
        console.log('File deleted successfully');
    }
});
