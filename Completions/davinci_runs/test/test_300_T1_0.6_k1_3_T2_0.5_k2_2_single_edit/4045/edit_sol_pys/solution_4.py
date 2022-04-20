function read(file) {
    fs.readFile(file, function(err, data) {
        if (err) {
            return console.log(err);
        }
        console.log(data.toString());
    });
}

function write(file, content) {
    fs.writeFile(file, content, function(err) {
        if (err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });
}

function append(file, content) {
    fs.appendFile(file, content, function(err) {
        if (err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });
}
