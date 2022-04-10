const fs = require('fs');

fs.readFile('./file.txt', 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

fs.writeFile('./file.txt', 'Hello World!', (error) => {
  if (error) {
    console.log(error);
  } else {
    console.log('File created!');
  }
});
