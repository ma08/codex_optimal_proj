const fs = require('fs');

const file = fs.createReadStream('./file.txt');

file.on('data', data => {
    console.log(data.toString('utf8'));
})
