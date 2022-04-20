// var fs = require('fs');
// var path = require('path');

// fs.readdir(process.argv[2], function(err, list){
// 	for(var i = 0; i < list.length; i++){
// 		if(path.extname(list[i]) === '.' + process.argv[3]){
// 			console.log(list[i]);
// 		}
// 	}
// })

var fs = require('fs');
var path = require('path');

function fileFilter(err, list){
	for(var i = 0; i < list.length; i++){
		if(path.extname(list[i]) === '.' + process.argv[3]){
			console.log(list[i]);
		}
	}
}

function getFiles(dir){
	fs.readdir(dir, fileFilter);
}

getFiles(process.argv[2]);
