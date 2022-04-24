const fs = require('fs');

fs.stat('./file.js', (err, stats) => {
    if (err) {
        console.log(err);
    } else {
        console.log(stats);
    }
});
