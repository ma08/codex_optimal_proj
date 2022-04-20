var fs = require('fs');

fs.readFile('file.txt', 'utf8', function(err, data) {
  if (err) {
    console.log('Error: ' + err);
    return;
  }

  data = data.replace(/somecompany\.com/g, 'burningbird.net');

  fs.writeFile('file.txt', data, function(err) {
    if (err) {
      console.log('Error: ' + err);
      return;
    }

    console.log('file.txt successfully updated');
  });
});
