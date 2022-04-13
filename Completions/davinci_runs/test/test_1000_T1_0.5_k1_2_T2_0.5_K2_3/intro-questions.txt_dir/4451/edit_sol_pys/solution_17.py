"use strict";

const fs = require("fs");

let file = fs.readFileSync("./file.txt", "utf8");

console.log(file);

let array = file.split("\n");

array.forEach(function (line, index) {
  let array = line.split(" ");
  if (array.length > 1) {
    let word = array[0];
    let number = array[1];
    console.log(word + " " + number);
  }
});
