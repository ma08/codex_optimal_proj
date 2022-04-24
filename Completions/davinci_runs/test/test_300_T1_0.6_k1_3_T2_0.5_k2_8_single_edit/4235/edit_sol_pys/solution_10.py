const fs = require('fs');

const contents = fs.readFileSync('./file.txt', 'utf8');

console.log('contents', contents);

fs.writeFileSync('./file.txt', 'Hello World');

fs.readFile('./file.txt', 'utf8', (err, contents) => {
  if (err) {
    console.log('err', err);
    return;
  }

  console.log('contents', contents);
});

fs.writeFile('./file.txt', 'Hello World', (err) => {
  if (err) {
    console.log('err', err);
    return;
  }

  console.log('Successfully wrote to file');
});
