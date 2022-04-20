const fs = require('fs');

// fs.writeFileSync('file.txt', 'Hello from node.js');
// console.log(fs.readFileSync('file.txt').toString());

fs.writeFile('file.txt', 'Hello from node.js', (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
});

fs.readFile('file.txt', (err, data) => {
    if (err) throw err;
    console.log(data.toString());
});
