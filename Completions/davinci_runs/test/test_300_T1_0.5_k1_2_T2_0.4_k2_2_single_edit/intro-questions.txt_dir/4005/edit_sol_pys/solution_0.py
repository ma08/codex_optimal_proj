const fs = require('fs');

// fs.readFile('file.txt', 'utf8', (err, data) => {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(data);
//     }
// });

const data = fs.readFileSync('file.txt', 'utf8');
console.log(data);
