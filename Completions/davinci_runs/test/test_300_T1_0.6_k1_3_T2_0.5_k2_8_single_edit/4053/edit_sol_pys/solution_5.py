const fs = require('fs');

fs.readFile('data.txt', (err, data) => {
	if (err) {
		console.log('error', err);
	}
	console.log(data.toString());
});
