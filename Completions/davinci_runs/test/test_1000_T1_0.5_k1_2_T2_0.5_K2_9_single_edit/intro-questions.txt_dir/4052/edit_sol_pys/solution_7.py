var fs = require('fs');
var path = require('path');

var files = fs.readdirSync(process.argv[2]);
for (var i = 0; i < files.length; i++) {
    if (path.extname(files[i]) == '.' + process.argv[3]) {
        console.log(files[i]);
    }
}
