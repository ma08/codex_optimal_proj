var fs = require('fs');

fs.stat('file.js', function (err, stats) {
    if (err) {
        console.log(err);
        return;
    }

    console.log('stats: ' + JSON.stringify(stats, null, '  '));

    // Check file type
    console.log('isFile: ' + stats.isFile());
    console.log('isDirectory: ' + stats.isDirectory());
    if (stats.isFile()) {
        // Check file size
        console.log('size: ' + stats.size);
        console.log('birth time: ' + stats.birthtime);
        console.log('modified time: ' + stats.mtime);
    }
});
