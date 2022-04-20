var fs = require('fs');

var file = fs.createWriteStream("file.txt");
file.write("Hello");
file.write("World");
file.end();
