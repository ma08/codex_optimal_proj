var fs = require('fs');

fs.readFile('file.txt', 'utf8', function(err, data) {
	console.log(data);
});

console.log('end');
