const fs = require('fs')
const path = require('path')

const filePath = path.join(__dirname, 'input.txt')

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  if (!err) {
    console.log('received data: ' + data)
    processFile(data)
  } else {
    console.log(err)
  }
})

function processFile(data) {
  const lines = data.split('\n')
  let twos = 0
  let threes = 0

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]
    const counts = {}

    for (let j = 0; j < line.length; j++) {
      const char = line[j]
      if (counts[char]) {
        counts[char]++
      } else {
        counts[char] = 1
      }
    }

    let foundTwo = false
    let foundThree = false
    for (let char in counts) {
      if (counts[char] === 2 && !foundTwo) {
        twos++
        foundTwo = true
      } else if (counts[char] === 3 && !foundThree) {
        threes++
        foundThree = true
      }
    }
  }

  console.log(twos * threes)
}
