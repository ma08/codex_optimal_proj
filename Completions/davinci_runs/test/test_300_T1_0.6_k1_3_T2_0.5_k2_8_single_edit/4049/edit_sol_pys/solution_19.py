const fs = require('fs');

// fs.readFile('./docs/blog1.txt', (err, data) => {
//     if (err) {
//         console.log(err);
//     }
//     console.log(data.toString());
// });

// fs.writeFile('./docs/blog1.txt', 'hello, world', () => {
//     console.log('file was written');
// });

// fs.writeFile('./docs/blog3.txt', 'hello, again', () => {
//     console.log('file was written');
// });

// fs.writeFile('./docs/blog2.txt', 'hello, again', () => {
//     console.log('file was written');
// });

// fs.readdir('./docs', (err, files) => {
//     if (err) {
//         console.log(err);
//     }
//     console.log(files);
// });

// fs.rename('./docs/blog1.txt', './docs/blogone.txt', (err) => {
//     if (err) {
//         console.log(err);
//     }
//     console.log('file renamed');
// });

fs.unlink('./docs/deleteme.txt', (err) => {
    if (err) {
        console.log(err);
    }
    console.log('file deleted');
});
