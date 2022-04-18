// create a file
// fs.writeFileSync('./file.txt', 'hello world');
// console.log('file created');

// append to a file
// fs.appendFileSync('./file.txt', '\nhello world');
// console.log('file appended');

// read a file
// const file = fs.readFileSync('./file.txt', 'utf8');
// console.log(file);

// rename a file
fs.renameSync('./file.txt', './hello.txt');
console.log('file renamed');
