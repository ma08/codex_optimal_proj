var fs = require("fs");

fs.readFile("best_things_ever.txt", "utf8", function(err, data) {
    if (err) {
        return console.log(err);
    }
    var dataArr = data.split(",");
    console.log(dataArr);
    for (var i = 0; i < dataArr.length; i++) {
        console.log(dataArr[i]);
    }
});

fs.appendFile("best_things_ever.txt", "garbage", function(err) {
    if (err) {
        return console.log(err);
    }
    console.log("Content Added!");
});
