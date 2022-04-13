const fs = require('fs');

fs.readFile('test.txt', 'utf-8', (err, data) => { // eslint-disable-line
  if (err) {
    throw err;
  }
  console.log(data); // eslint-disable-line
});
