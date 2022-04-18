"use strict";

const fs = require('fs');

let file = fs.readFileSync('./file.txt', 'utf8'); // read the file

// console.log(file);

let array = file.split('\n'); // convert the file to an array

array.forEach(function(line, index){ // iterate through the lines
    let array = line.split(' '); // convert the line to an array
    if(array.length > 1){ // if the line has two items
        let word = array[0]; // assign the first item to a variable
        let number = array[1]; // assign the second item to a variable
        console.log(word + ' ' + number); // print the variables
    }
});
