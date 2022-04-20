// var fs = require('fs');
// var readme = fs.readFileSync('readme.txt', 'utf8');
// console.log(readme);
// fs.writeFileSync('writeme.txt', readme);

// var fs = require('fs');
// fs.readFile('readme.txt', 'utf8', function(err, data){
// 	console.log(data);
// });
// console.log('test');

// var fs = require('fs');
// fs.unlink('writeme.txt');

// var fs = require('fs');
// fs.mkdirSync('stuff');
// fs.rmdirSync('stuff');

// var fs = require('fs');
// fs.mkdir('stuff', function(){
// 	fs.readFile('readme.txt', 'utf8', function(err, data){
// 		fs.writeFile('./stuff/writeme.txt', data);
// 	});
// });

// var fs = require('fs');
// fs.unlink('./stuff/writeme.txt', function(){
// 	fs.rmdir('stuff');
// });

var http = require('http');
var fs = require('fs');

var server = http.createServer(function(req, res){
	console.log('request was made: ' + req.url);
	res.writeHead(200, {'Content-Type': 'text/plain'});
	var myReadStream = fs.createReadStream(__dirname + '/readme.txt', 'utf8');
	myReadStream.pipe(res);
});

server.listen(3000, '127.0.0.1');
console.log('yo dawgs, now listening to port 3000');
