function readFile(filename) {
    return new Promise(function (resolve, reject) {
        fs.readFile(filename, function (err, data) {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}

function handleError(err) {
    console.log(err.message);
}

readFile('file.txt')
    .then(function (data) {
        console.log(data.toString());
    })
    .catch(handleError);
