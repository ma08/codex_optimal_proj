const fs = require('fs');
const path = require('path');
const dir = path.resolve(__dirname, './');

fs.readdir(dir, (err, files) => {
    if (err) {
        console.log(err);
        return;
    }
    files.forEach((file) => {
        console.log(file);
    });
});
