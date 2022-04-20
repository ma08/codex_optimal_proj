var fs = require('fs');
var path = require('path');
var file = process.argv[2];
var ext = process.argv[3];

fs.readdir(file, function(err, list) {
    if (err) {
        console.log(err);
    }
    else {
        for (var i = 0; i < list.length; i++) {
            if (path.extname(list[i]) === '.' + ext) {
                console.log(list[i]);
            }
        }
    }
});
