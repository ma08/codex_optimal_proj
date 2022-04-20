var fs = require("fs");

var text = fs.readFileSync("text.txt", "utf8");
var textByLine = text.split("\n")

for(i=0;i<textByLine.length;i++){
    console.log(textByLine[i]);
}
