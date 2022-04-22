//write a function that takes a filename as a parameter
//The file contains an ended Tic-Tac-Toe match
//We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
//Return "X", "O" or "Draw" based on the input file
//example:
//console.log(ticTacResult('win-o.txt'))
//console.log(ticTacResult('win-x.txt'))
//console.log(ticTacResult('draw.txt'))

const fs = require('fs');

function ticTacResult(fileName) {
  let result = fs.readFileSync(fileName, 'utf-8');
  if (result.indexOf('OOO') > -1) {
    return 'O';
  } else if (result.indexOf('XXX') > -1) {
    return 'X';
  } else {
    return 'Draw';
  }
}

console.log(ticTacResult('win-o.txt'));
console.log(ticTacResult('win-x.txt'));
console.log(ticTacResult('draw.txt'));
