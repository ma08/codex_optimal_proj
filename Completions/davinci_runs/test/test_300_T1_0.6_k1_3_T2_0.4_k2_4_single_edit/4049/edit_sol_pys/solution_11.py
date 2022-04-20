var fs = require('fs');

var read = fs.readFileSync('read.txt', 'utf8');

var write = fs.writeFileSync('write.txt', read);
