const fs = require('fs');

fs.writeFile('test.txt', 'Hello world!', err => {
    if (err) throw err;
    console.log('The file has been saved!');
});

fs.readFile('test.txt', 'utf8', (err, data) =>
    if (err) throw err;
    console.log(data);
);

fs.appendFile('test.txt', '\nHello again!', err => {
    if (err) throw err;
    console.log('The file has been appended!');
});

fs.readFile('test.txt', 'utf8', (err, data) =>
    if (err) throw err;
    console.log(data);
);

fs.rename('test.txt', 'renamed.txt', err => {
    if (err) throw err;
    console.log('The file has been renamed!');
});

fs.readFile('renamed.txt', 'utf8', (err, data) =>
    if (err) throw err;
    console.log(data);
);

fs.unlink('renamed.txt', err => {
    if (err) throw err;
    console.log('The file has been deleted!');
});
