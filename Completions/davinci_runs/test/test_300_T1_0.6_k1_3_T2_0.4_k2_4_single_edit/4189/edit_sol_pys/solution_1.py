const fs = require('fs');

fs.readFile('data.txt', 'utf8', (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data);
});

fs.writeFile('data.txt', 'Hello Node.js', (err) => {
  if (err) {
    throw err;
  }
  console.log('It\'s saved!');
});
