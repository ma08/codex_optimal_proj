// var fs = require('fs');

// fs.readFile('input.txt', function(err, data) {
//     if (err) return console.error(err);
//     console.log(data.toString());
// });

// console.log('Program Ended');


// var events = require('events');
// var eventEmitter = new events.EventEmitter();

// var connectHandler = function connected() {
//     console.log('connection successful.');

//     eventEmitter.emit('data_received');
// }

// eventEmitter.on('connection', connectHandler);

// eventEmitter.on('data_received', function() {
//     console.log('data received successfully.');
// });

// eventEmitter.emit('connection');

// console.log('Program Ended');


// var events = require('events');
// var eventEmitter = new events.EventEmitter();

// var listener1 = function listener1() {
//     console.log('listener1 executed.');
// }

// var listener2 = function listener2() {
//     console.log('listener2 executed.');
// }

// eventEmitter.addListener('connection', listener1);

// eventEmitter.on('connection', listener2);

// var eventListeners = require('events').EventEmitter.listenerCount(eventEmitter, 'connection');
// console.log(eventListeners + ' Listener(s) listening to connection event');

// eventEmitter.emit('connection');

// eventEmitter.removeListener('connection', listener1);
// console.log('listener1 will not listen now.');

// eventEmitter.emit('connection');

// eventListeners = require('events').EventEmitter.listenerCount(eventEmitter, 'connection');
// console.log(eventListeners + ' Listener(s) listening to connection event');

// console.log('Program Ended');


// var buf = new Buffer(256);
// len = buf.write('Simply Easy Learning');
// console.log('Octets written: ' + len);


// var buf = new Buffer(26);
// for (var i = 0; i < 26; i++) {
//     buf[i] = i + 97;
// }

// console.log(buf.toString('ascii'));
// console.log(buf.toString('ascii', 0, 5));
// console.log(buf.toString('utf8', 0, 5));
// console.log(buf.toString(undefined, 0, 5));


// var buffer1 = new Buffer('TutorialsPoint');
// var buffer2 = new Buffer('Simply Easy Learning');
// var buffer3 = Buffer.concat([buffer1, buffer2]);
// console.log('buffer3 content: ' + buffer3.toString());


// var buffer1 = new Buffer('ABC');
// var buffer2 = new Buffer('ABCD');
// var result = buffer1.compare(buffer2);

// if (result < 0) {
//     console.log(buffer1 + ' comes before ' + buffer2);
// } else if (result == 0) {
//     console.log(buffer1 + ' is same as ' + buffer2);
// } else {
//     console.log(buffer1 + ' comes after ' + buffer2);
// }


// var buffer1 = new Buffer('ABC');
// var buffer2 = new Buffer(3);
// buffer1.copy(buffer2);
// console.log('buffer2 content: ' + buffer2.toString());


// var buffer1 = new Buffer('TutorialsPoint');
// var buffer2 = buffer1.slice(0, 9);
// console.log('buffer2 content: ' + buffer2.toString());


// var fs = require('fs');

// fs.open('input.txt', 'r+', function(err, fd) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log('File opened successfully!');
// });


// var fs = require('fs');

// console.log('Going to open file!');
// fs.open('input.txt', 'r+', function(err, fd) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log('File opened successfully!');
// });


// var fs = require('fs');

// console.log('Going to get file info!');
// fs.stat('input.txt', function(err, stats) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log(stats);
//     console.log('Got file info successfully!');

//     console.log('isFile ? ' + stats.isFile());
//     console.log('isDirectory ? ' + stats.isDirectory());
// });


// var fs = require('fs');

// console.log('Going to write into existing file');
// fs.writeFile('input.txt', 'Simply Easy Learning!', function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log('Data written successfully!');
//     console.log('Let\'s read newly written data');
//     fs.readFile('input.txt', function(err, data) {
//         if (err) {
//             return console.error(err);
//         }
//         console.log('Asynchronous read: ' + data.toString());
//     });
// });


// var fs = require('fs');

// console.log('Going to open file!');
// fs.open('input.txt', 'r+', function(err, fd) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log('File opened successfully!');
//     console.log('Going to truncate the file after 10 bytes');

//     fs.ftruncate(fd, 10, function(err) {
//         if (err) {
//             console.log(err);
//         }
//         console.log('File truncated successfully.');
//         console.log('Going to read the same file');
//         fs.read(fd, buf, 0, buf.length, 0, function(err, bytes) {
//             if (err) {
//                 console.log(err);
//             }
//             console.log(bytes + ' bytes read');

//             if (bytes > 0) {
//                 console.log(buf.slice(0, bytes).toString());
//             }
//         });
//     });
// });


// var fs = require('fs');

// console.log('Going to delete an existing file');
// fs.unlink('input.txt', function(err) {
//     if (err) {
//         return console.error(err);
//     }
//     console.log('File deleted successfully!');
// });


var fs = require('fs');

console.log('Going to create directory /tmp/test');
fs.mkdir('/tmp/test', function(err) {
    if (err) {
        return console.error(err);
    }
    console.log('Directory created successfully!');
});
