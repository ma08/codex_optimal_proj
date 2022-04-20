let fs = require('fs');

fs.writeFileSync('test.txt', 'Hello world');

let fileContents = fs.readFileSync('test.txt');
console.log(fileContents.toString());

// fs.writeFile('test.txt', 'Hello world', (err) => {
//   if (err) {
//     console.log(err);
//   }
// });

// fs.readFile('test.txt', (err, data) => {
//   if (err) {
//     console.log(err);
//   }
//   console.log(data.toString());
// });
