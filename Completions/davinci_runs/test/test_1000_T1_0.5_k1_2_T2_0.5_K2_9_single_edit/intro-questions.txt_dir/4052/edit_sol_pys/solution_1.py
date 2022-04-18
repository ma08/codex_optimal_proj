const fs = require('fs');

fs.writeFile('./test.txt', 'Hello world', (err) => {
  if (err) throw err;
  console.log('The file has been saved!');
});

fs.readFile('./test.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
