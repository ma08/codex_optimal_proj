var fs = require('fs');

var readFile = function (file) {
    return new Promise(function (resolve, reject) {
        fs.readFile(file, function(error, data) {
            if (error) return reject(error);
            resolve(data);
        });
    });
};

var asyncReadFile = async function () {
    var f1 = await readFile('file1.txt');
    var f2 = await readFile('file2.txt');
    console.log(f1.toString());
    console.log(f2.toString());
};

asyncReadFile();
