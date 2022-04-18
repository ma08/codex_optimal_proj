const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'data', 'file.txt');

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
