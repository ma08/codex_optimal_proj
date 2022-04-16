const fs = require("fs");

fs.writeFile("data.txt", "Hello, world", (err) => {
  if (err) {
    console.log("There was an error writing to the file");
  } else {
    console.log("Successfully wrote to the file");
  }
});

// fs.readFile("data.txt", (err, data) => {
//   if (err) {
//     console.log("There was an error reading the file");
//   } else {
//     console.log("Successfully read the file");
//     console.log(data.toString());
//   }
// });

fs.readFile("data.txt", "utf-8", (err, data) => {
  if (err) {
    console.log("There was an error reading the file");
  } else {
    console.log("Successfully read the file");
    console.log(data);
  }
});
