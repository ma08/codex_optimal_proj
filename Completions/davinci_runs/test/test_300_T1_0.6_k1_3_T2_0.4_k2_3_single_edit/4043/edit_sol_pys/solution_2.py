function readFile(file) {
	var fs = require('fs');
	fs.readFile(file, 'utf8', function(err, data) {
		if (err) {
			return console.log(err);
		}
		console.log(data);
	});
}

function writeFile(file, data) {
	var fs = require('fs');
	fs.writeFile(file, data, function(err) {
		if (err) {
			return console.log(err);
		}
		console.log("The file was saved!");
	});
}

function appendFile(file, data) {
	var fs = require('fs');
	fs.appendFile(file, data, function(err) {
		if (err) {
			return console.log(err);
		}
		console.log("The file was saved!");
	});
}

function main() {
	var file = process.argv[2];
	var data = process.argv[3];
	var action = process.argv[4];

	if (action == 'read') {
		readFile(file);
	}
	else if (action == 'write') {
		writeFile(file, data);
	}
	else if (action == 'append') {
		appendFile(file, data);
	}
}

main();
