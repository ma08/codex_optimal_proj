const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '/input.txt');

fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        console.log('received data: ' + data);
        processData(data);
    } else {
        console.log(err);
    }
});

function processData(data) {
    const lines = data.split('\n');
    const numCases = lines[0];
    for (var i = 1; i <= numCases; i++) {
        const num = lines[i];
        const output = countDigits(num);
        console.log(`Case #${i}: ${output}`);
    }
}

function countDigits(num) {
    let count = 0;
    for (var i = 0; i < num.length; i++) {
        const digit = parseInt(num[i]);
        if (digit !== 0 && num % digit === 0) {
            count++;
        }
    }
    return count;
}
