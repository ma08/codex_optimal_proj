var fs = require('fs')

var file = fs.createWriteStream('file.txt')
file.write('hello')
file.write('world')
file.end()

console.log('done')
