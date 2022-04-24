var fs = require("fs");

fs.readFile("./file.txt", "utf8", function(err, data) {
  if (err) {
    throw err;
  }
  var arr = data.split("\n");
  // console.log(arr);
  var result = arr.reduce(function(acc, curr) {
    if (acc[curr]) {
      acc[curr] = acc[curr] + 1;
    } else {
      acc[curr] = 1;
    }
    return acc;
  }, {});
  console.log(result);
});
