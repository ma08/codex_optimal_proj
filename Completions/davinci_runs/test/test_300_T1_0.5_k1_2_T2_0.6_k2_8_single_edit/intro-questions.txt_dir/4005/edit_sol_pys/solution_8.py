// const fs = require('fs');

// fs.readFile('./hello.txt', (err, data) => {
//     if (err) {
//         console.log('errrrrrrrrrrrrrrr');
//     }
//     console.log('Async', data.toString('utf8'));
// });

// const file = fs.readFileSync('./hello.txt');
// console.log('Sync', file.toString());

// // APPEND
// fs.appendFile('./hello.txt', ' This is so cool!', err => {
//     if (err) {
//         console.log(err);
//     }
// });

// // WRITE
// fs.writeFile('bye.txt', 'Sad to see you go', err => {
//     if (err) {
//         console.log(err);
//     }
// });

// // DELETE
// fs.unlink('./bye.txt', err => {
//     if (err) {
//         console.log(err);
//     }
//     console.log('Inception');
// });

const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello World');
        res.end();
    }

    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

// server.on('connection', socket => {
//     console.log('New connection...');
// });

server.listen(3000);

console.log('Listening on port 3000...');
