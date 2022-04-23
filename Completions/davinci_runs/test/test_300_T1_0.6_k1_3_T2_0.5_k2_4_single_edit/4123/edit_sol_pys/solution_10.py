const fs = require('fs');

// fs.writeFileSync('notes.txt', 'This file was created by Node.js');

// fs.appendFileSync('notes.txt', ' My name is Dima');

const dataBuffer = fs.readFileSync('notes.txt');
const dataString = dataBuffer.toString();
console.log(dataString);
