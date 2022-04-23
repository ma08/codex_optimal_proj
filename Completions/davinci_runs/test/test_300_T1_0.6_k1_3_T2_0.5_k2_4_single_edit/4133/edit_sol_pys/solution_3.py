const fs = require('fs');

// fs.readFile('file.txt', 'utf8', (err, data) => {
//   if (err) throw err;
//   console.log(data);
// });

fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

fs.writeFile('file.txt', 'Hello World!', err => {
  if (err) throw err;
  console.log('The file has been saved!');
});
