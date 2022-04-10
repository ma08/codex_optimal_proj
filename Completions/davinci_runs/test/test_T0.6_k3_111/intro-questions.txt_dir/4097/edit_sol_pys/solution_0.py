var fs = require('fs');

fs.writeFile('mynewfile4.txt', 'Hello content!', function (err) {
    if (err) throw err;
    console.log('Saved!');
});
