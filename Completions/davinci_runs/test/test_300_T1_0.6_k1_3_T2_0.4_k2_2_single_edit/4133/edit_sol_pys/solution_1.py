const fs = require('fs');

fs.readFile('./file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('An error occurred:', err);
    } else {
        console.log(data);
    }
});
