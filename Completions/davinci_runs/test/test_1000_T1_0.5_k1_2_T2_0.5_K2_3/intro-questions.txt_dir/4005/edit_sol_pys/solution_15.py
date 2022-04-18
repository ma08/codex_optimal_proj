var fs = require('fs');

fs.readFile('./file.txt', function (err, data) {
    console.log(data.toString());
});
