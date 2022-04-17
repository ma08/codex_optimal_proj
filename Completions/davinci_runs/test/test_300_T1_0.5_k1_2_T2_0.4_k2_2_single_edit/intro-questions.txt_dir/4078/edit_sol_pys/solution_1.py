const fs = require('fs')
const path = require('path')

const filePath = path.join(__dirname, 'data.txt')

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    console.log(data)
})
