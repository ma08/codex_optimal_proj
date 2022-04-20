const fs = require('fs');

fs.writeFileSync('notes.txt', 'My name is Akshay.');
fs.appendFileSync('notes.txt', '\nI am a web developer.');
