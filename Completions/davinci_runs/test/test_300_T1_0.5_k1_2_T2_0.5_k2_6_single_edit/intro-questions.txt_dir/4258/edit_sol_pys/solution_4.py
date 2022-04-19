var fs = require('fs');

// var file = fs.readFileSync(process.argv[2]);
// var str = file.toString();
// var splitStr = str.split('\n');
// var numLines = splitStr.length - 1;

// console.log(numLines);

fs.readFile(process.argv[2], function(err, data) {
	var str = data.toString();
	var splitStr = str.split('\n');
	var numLines = splitStr.length - 1;
	console.log(numLines);
});


