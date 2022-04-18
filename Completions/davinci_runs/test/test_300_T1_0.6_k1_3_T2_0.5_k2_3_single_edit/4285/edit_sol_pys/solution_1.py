var fs = require('fs');
var http = require('http');

http.createServer(function(request, response) {
    response.writeHead(200, {'Content-Type': 'text/html'});
    fs.readFile('index.html', function(err, contents) {
        response.write(contents);
        response.end();
    });
}).listen(8080);

console.log('Server running on port 8080.');
