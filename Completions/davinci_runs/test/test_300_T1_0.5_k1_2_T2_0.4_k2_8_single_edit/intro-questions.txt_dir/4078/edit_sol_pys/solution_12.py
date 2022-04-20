const fs = require('fs')

const file = fs.readFileSync('file.txt', 'utf8')

console.log(file)
