const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'data.json');

const data = fs.readFileSync(filePath, 'utf-8');

const json = JSON.parse(data);

console.log(json);
