const fs = require('fs');

fs.writeFileSync('notes.txt', 'This is a file created by Node.js!\n');

fs.appendFileSync('notes.txt', 'This is an appended text.\n');
