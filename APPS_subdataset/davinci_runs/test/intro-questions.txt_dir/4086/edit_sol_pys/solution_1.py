const fs = require('fs');

fs.readFile('./file.txt', (err, data) => { // Read file
    if (err) {
        console.log(err);
    } else {
        console.log(data.toString());
    }
});

fs.writeFile('./file.txt', 'Hello World', (err) => { // Write file
    if (err) {
        console.log(err);
    } else {
        console.log('File has been written');
    }
});

fs.appendFile('./file.txt', '\nHello World', (err) => { // Append file
    if (err) {
        console.log(err);
    } else {
        console.log('File has been written');
    }
});

fs.rename('./file.txt', './file2.txt', (err) => { // Rename file
    if (err) {
        console.log(err);
    } else {
        console.log('File has been renamed');
    }
});

fs.unlink('./file2.txt', (err) => { // Delete file
    if (err) {
        console.log(err);
    } else {
        console.log('File has been deleted');
    }
});
