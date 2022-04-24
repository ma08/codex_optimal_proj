function readFile(fileName) {
    const fs = require('fs');
    const fileContents = fs.readFileSync(fileName);
    console.log(fileContents.toString());
}

function writeFile(fileName, data) {
    const fs = require('fs');
    fs.writeFileSync(fileName, data, 'utf8');
}

function appendFile(fileName, data) {
    const fs = require('fs');
    fs.appendFileSync(fileName, data, 'utf8');
}

function main() {
    const fileName = './file.txt';
    const data = 'Hello, World!';
    writeFile(fileName, data);
    appendFile(fileName, data);
    readFile(fileName);
}

main();
