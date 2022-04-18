// var fs = require('fs');
// var readStream = fs.createReadStream('/Users/shuvojit/Desktop/1.mp4');
// var writeStream = fs.createWriteStream('/Users/shuvojit/Desktop/2.mp4');
// readStream.pipe(writeStream);
// console.log('done');


// var fs = require('fs');
// var readStream = fs.createReadStream('/Users/shuvojit/Desktop/1.mp4');
// var writeStream = fs.createWriteStream('/Users/shuvojit/Desktop/2.mp4');

// readStream.on('data',function(chunk){
// 	if(writeStream.write(chunk) === false){
// 		console.log('still cached');
// 		readStream.pause();
// 	}
// });

// readStream.on('end',function(){
// 	writeStream.end();
// });

// writeStream.on('drain',function(){
// 	console.log('data drains');
// 	readStream.resume();
// });


// var fs = require('fs');
// var readStream = fs.createReadStream('/Users/shuvojit/Desktop/1.mp4');
// var n = 0;
// readStream
// 	.on('data',function(chunk){
// 		n++;
// 		console.log('data emits');
// 		console.log(Buffer.isBuffer(chunk));
// 		console.log(chunk.toString('utf8'));
// 	})
// 	.on('readable',function(){
// 		console.log('data readable');
// 	})
// 	.on('end',function(){
// 		console.log(n);
// 		console.log('data ends');
// 	})
// 	.on('close',function(){
// 		console.log('data close');
// 	})
// 	.on('error',function(e){
// 		console.log('data read error'+e);
// 	});


var fs = require('fs');
var readStream = fs.createReadStream('/Users/shuvojit/Desktop/1.mp4');
var writeStream = fs.createWriteStream('/Users/shuvojit/Desktop/2.mp4');
readStream.pipe(writeStream);
console.log('done');
