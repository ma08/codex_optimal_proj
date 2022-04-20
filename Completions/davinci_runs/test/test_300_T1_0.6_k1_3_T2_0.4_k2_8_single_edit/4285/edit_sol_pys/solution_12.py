var fs = require('fs');
var readline = require('readline');
var stream = require('stream');
var instream = fs.createReadStream('input.txt');
var outstream = new stream;
var rl = readline.createInterface(instream, outstream);

rl.on('line', function(line) {
  var line = line.split(" ");
  var a = parseInt(line[0]);
  var b = parseInt(line[1]);
  console.log(a+b);
});

rl.on('close', function() {
  console.log('done');
});
