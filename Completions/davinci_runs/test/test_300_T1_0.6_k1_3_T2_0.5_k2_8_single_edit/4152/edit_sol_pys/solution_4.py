const fs = require('fs');

const file = fs.readFileSync(process.argv[2]);
const str = file.toString();

const lines = str.split('\n').length - 1;

console.log(lines);
