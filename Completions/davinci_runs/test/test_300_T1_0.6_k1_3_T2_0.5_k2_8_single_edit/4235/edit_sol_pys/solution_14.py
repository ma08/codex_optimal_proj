const fs = require('fs');

// fs.writeFileSync('notes.txt', 'My name is jin');
// fs.appendFileSync('notes.txt', ' I am 25 years old');



// const add = require('./utils.js');
// const sum = add(4, -2);
// console.log(sum);

// const validator = require('validator');
// console.log(validator.isEmail('jin@gmail.com'));
// console.log(validator.isURL('https://www.google.com'));

const chalk = require('chalk');
const yargs = require('yargs');

const command = process.argv[2];

if (command === 'add') {
    console.log('Adding note!');
} else if (command === 'remove') {
    console.log('Removing note!');
}

yargs.command({
    command: 'add',
    describe: 'Add a new note',
    handler: function () {
        console.log('Adding a new note!');
    }
})

yargs.command({
    command: 'remove',
    describe: 'Remove a note',
    handler: function () {
        console.log('Removing the note');
    }
})

yargs.command({
    command: 'list',
    describe: 'List your notes',
    handler: function () {
        console.log('Listing out all notes');
    }
})

yargs.command({
    command: 'read',
    describe: 'Read a note',
    handler: function () {
        console.log('Reading a note');
    }
})

console.log(yargs.argv);
