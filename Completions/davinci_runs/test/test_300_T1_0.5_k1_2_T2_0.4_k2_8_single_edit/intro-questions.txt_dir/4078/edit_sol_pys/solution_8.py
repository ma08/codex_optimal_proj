const fs = require("fs");

fs.readFile("file.txt", "utf-8", (err, data) => {
    if (err) {
        console.log("Error: ", err);
    } else {
        console.log("Data: ", data);
    }
});

fs.writeFile("file.txt", "This is a new file", (err) => {
    if (err) {
        console.log("Error: ", err);
    } else {
        console.log("File saved");
    }
});
