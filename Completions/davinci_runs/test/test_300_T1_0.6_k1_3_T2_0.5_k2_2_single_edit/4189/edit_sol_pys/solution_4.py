const fs = require('fs')

let content = fs.readFileSync('file.txt', 'utf8')
console.log(content)
