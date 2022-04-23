

var fs = require('fs');

var file = fs.readFileSync('index.html');

fs.writeFileSync('index.html', file);

var http = require('http');

var server = http.createServer(function (request, response) {
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write(file);
  response.end();
});

server.listen(8080);
