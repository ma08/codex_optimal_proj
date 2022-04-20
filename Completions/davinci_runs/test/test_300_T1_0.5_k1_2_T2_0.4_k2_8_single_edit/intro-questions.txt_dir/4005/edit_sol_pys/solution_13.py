const fs = require('fs');

// fs.writeFile('hello.txt', 'Hello World!', (err) => {
//     if (err) {
//         console.log(err);
//     }
// });

// fs.appendFile('hello.txt', ' This is my text.', (err) => {
//     if (err) {
//         console.log(err);
//     }
// });

// fs.readFile('hello.txt', 'utf8', (err, data) => {
//     if (err) {
//         console.log(err);
//     }
//     console.log(data);
// });

fs.rename('hello.txt', 'helloworld.txt', (err) => {
    if (err) {
        console.log(err);
    }
});
