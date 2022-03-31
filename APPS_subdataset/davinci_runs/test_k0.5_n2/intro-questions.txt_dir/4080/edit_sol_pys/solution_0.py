const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "file.txt");

fs.readFile(filePath, (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});
