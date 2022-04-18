const fs = require('fs');


fs.writeFileSync('notes.txt', 'My name is Jeremy.');
fs.appendFileSync('notes.txt', ' I am a full stack web developer.');
