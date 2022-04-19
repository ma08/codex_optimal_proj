const fs = require('fs')
const util = require('util')

const readFile = util.promisify(fs.readFile)
const writeFile = util.promisify(fs.writeFile)

const read = async () => {
  const file = await readFile('./file.txt')
  return file.toString()
}

const write = async (data) => {
  await writeFile('./file.txt', data)
}

module.exports = {
  read,
  write
}
