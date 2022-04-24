const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'file.txt');

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

console.log('TEST');
