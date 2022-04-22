const fs = require('fs');

// fs.writeFileSync('notes.txt', 'this file was created by node.js');

// fs.appendFileSync('notes.txt', 'data to append');

// const name = 'Andrew';
// const age = 27;
// const newNote = `My name is ${name} and I am ${age} years old.`;
// fs.appendFileSync('notes.txt', newNote);

// Challenge: Append a message to notes.txt
// 1. Use appendFileSync to append to the file
// 2. Run the script
// 3. Check your work by opening the file and viewing the appended text

const name = 'Andrew';
const age = 27;
const newNote = `My name is ${name} and I am ${age} years old.`;
fs.appendFileSync('notes.txt', newNote);
