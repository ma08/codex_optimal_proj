const fs = require('fs');

fs.writeFileSync('notes.txt', 'This file was created by Node.js!');

fs.appendFileSync('notes.txt', '\nThis text was appended by Node.js!');
