var fs = require('fs');
var path = require('path');
var filepath = process.argv[2];
var extension = process.argv[3];

fs.readdir(filepath, function(err, list){
	if (err) return console.error(err);
	
	list.forEach(function(file){
		if (path.extname(file) === '.' + extension){
			console.log(file);
		}
	});
});
