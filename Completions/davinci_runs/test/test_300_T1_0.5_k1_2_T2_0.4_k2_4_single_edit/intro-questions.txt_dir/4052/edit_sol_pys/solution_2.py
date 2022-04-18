const fs = require('fs');

fs.readFile('file.js', function(err, data){
    if(err) {
        console.log(err);
    } else {
        console.log(data.toString());
    }
})

console.log('end');
