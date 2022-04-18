var fs = require("fs");

fs.readFile("text.txt", function(err, data) {
  if (err) throw err;
  console.log(data.toString());
});

fs.writeFile("text.txt", "Hello World", function(err) {
  if (err) throw err;
  console.log("Saved!");
});

fs.appendFile("text.txt", "Hello World", function(err) {
  if (err) throw err;
  console.log("Saved!");
});

fs.unlink("text.txt", function(err) {
  if (err) throw err;
  console.log("File deleted!");
});

fs.rename("text.txt", "text2.txt", function(err) {
  if (err) throw err;
  console.log("File Renamed!");
});
