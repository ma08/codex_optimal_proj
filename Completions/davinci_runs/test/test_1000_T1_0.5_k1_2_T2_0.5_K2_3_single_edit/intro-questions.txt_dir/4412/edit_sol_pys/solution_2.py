"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
function writeFile(path, content) {
    fs.writeFile(path, content, function (err) {
        if (err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });
}
exports.writeFile = writeFile;
function appendFile(path, content) {
    fs.appendFile(path, content, function (err) {
        if (err) {
            return console.log(err);
        }
        console.log("The " + path + " was appended!");
    });
}
exports.appendFile = appendFile;
function readFile(path) {
    fs.readFile(path, 'utf8', function (err, data) {
        if (err) {
            return console.log(err);
        }
        console.log(data);
    });
}
exports.readFile = readFile;
//# sourceMappingURL=file.js.map
