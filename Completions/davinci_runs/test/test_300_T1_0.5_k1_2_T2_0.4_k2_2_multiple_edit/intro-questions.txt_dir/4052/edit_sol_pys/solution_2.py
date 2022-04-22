const fs = require('fs');

fs.readFile('file.txt', 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

fs.writeFile('file.txt', 'Hello World', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Write operation complete.');
  }
});

fs.appendFile('file.txt', '\nHello World', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Append operation complete.');
  }
});

fs.rename('file.txt', 'newfile.txt', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Rename operation complete.');
  }
});

fs.unlink('newfile.txt', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Delete operation complete.');
  }
});

fs.mkdir('newfolder', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Directory created.');
  }
});

fs.rmdir('newfolder', function (err) {
  if (err) {
    console.log(err);
  } else {
    console.log('Directory removed.');
  }
});
