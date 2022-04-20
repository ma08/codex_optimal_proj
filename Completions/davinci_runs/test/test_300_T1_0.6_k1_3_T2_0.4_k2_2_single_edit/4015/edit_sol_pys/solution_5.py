var fs = require("fs");
var path = require("path");

// var file = process.argv[2];
// var ext = "." + process.argv[3];

// fs.readdir(file, function(err, list){
// 	for(var i = 0; i < list.length; i++){
// 		if(path.extname(list[i]) === ext){
// 			console.log(list[i]);
// 		}
// 	}
// });


module.exports = function(file, ext, callback){
	fs.readdir(file, function(err, list){
		if(err){
			return callback(err);
		}
		var data = [];
		for(var i = 0; i < list.length; i++){
			if(path.extname(list[i]) === ext){
				data.push(list[i]);
			}
		}
		callback(null, data);
	});
}
