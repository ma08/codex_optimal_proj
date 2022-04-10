const fs = require('fs');

fs.writeFileSync('notes.txt', 'My name is Ankit');
fs.appendFileSync('notes.txt', ' I am a developer');

const name = require('./utils.js');
const sum = require('./utils.js');

const add = sum(4, -2);
console.log(add);

const validator = require('validator');

console.log(validator.isEmail('ankit@gmail.com'));
console.log(validator.isURL('https://mead.io'));

const chalk = require('chalk');

console.log(chalk.green('Success!'));
console.log(chalk.red('Error!'));
