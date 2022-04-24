const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'file.txt');

fs.readFile(file, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
