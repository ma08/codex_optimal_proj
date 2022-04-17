var fs = require('fs');

// fs.open('file.txt', 'r', function(err, fd) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file opened successfully');
// });

// fs.stat('file.txt', function(err, stats) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log(stats);
// 	console.log('file stats successfully');
// });

// fs.writeFile('file.txt', 'Hello World!', function(err) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file write successfully');
// });

// fs.readFile('file.txt', function(err, data) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file read successfully');
// 	console.log(data.toString());
// });

// fs.rename('file.txt', 'file2.txt', function(err) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file renamed successfully');
// });

// fs.appendFile('file2.txt', 'Hello World!', function(err) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file append successfully');
// });

// fs.unlink('file2.txt', function(err) {
// 	if (err) {
// 		return console.error(err);
// 	}
// 	console.log('file deleted successfully');
// });

fs.readdir('.', function(err, files) {
	if (err) {
		return console.error(err);
	}
	files.forEach(function(file) {
		console.log(file);
	});
});
