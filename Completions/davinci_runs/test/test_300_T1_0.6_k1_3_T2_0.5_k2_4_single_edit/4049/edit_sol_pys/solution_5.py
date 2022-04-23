const fs = require('fs')

// fs.writeFile('file.txt', 'hello world', (err) => {
//     if(err) throw err;
//     console.log(`file saved`)
// })

fs.readFile('file.txt', 'utf8', (err, data) => {
    if(err) throw err;
    console.log(data)
})
