const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, './files/file.txt');

const readStream = fs.createReadStream(filePath);
const writeStream = fs.createWriteStream('./files/write.txt');

readStream.pipe(writeStream);
