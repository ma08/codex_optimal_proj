// var http = require('http');
// var fs = require('fs');
// var path = require('path');
// var hostname = 'localhost';
// var port = 3000;

// var server = http.createServer(function(req, res){
//     console.log('Request for ' + req.url + ' by method ' + req.method);
//     if (req.method == 'GET') {
//         var fileUrl;
//         if (req.url == '/') fileUrl = '/index.html';
//         else fileUrl = req.url;

//         var filePath = path.resolve('./public'+fileUrl);
//         var fileExt = path.extname(filePath);
//         if (fileExt == '.html') {
//             fs.exists(filePath, function(exists) {                 if (!exists) {
//                     res.writeHead(404, { 'Content-Type': 'text/html' });
//                     res.end('<html><body><h1>Error 404: ' + fileUrl + 
//                             ' not found</h1></body></html>');
//                     return;
//                 }
//                 res.writeHead(200, { 'Content-Type': 'text/html' });
//                 fs.createReadStream(filePath).pipe(res);
//             });
//         }
//         else {
//             res.writeHead(404, { 'Content-Type': 'text/html' });
//             res.end('<html><body><h1>Error 404: ' + fileUrl + 
//                     ' not a HTML file</h1></body></html>');
//         }
//     }
//     else {
//         res.writeHead(404, { 'Content-Type': 'text/html' });
//         res.end('<html><body><h1>Error 404: ' + req.method + 
//                 ' not supported</h1></body></html>');
//     }
// })

// server.listen(port, hostname, function(){
//   console.log(`Server running at http://${hostname}:${port}/`);
// });

var http = require('http');
var fs = require('fs');
var path = require('path');
var mime = require('mime');
var cache = {};

function send404(response) {
    response.writeHead(404, {'Content-Type': 'text/plain'});
    response.write('Error 404: resource not found.');
    response.end();
}

function sendFile(response, filePath, fileContents) {
    response.writeHead(
        200,
        {"content-type": mime.lookup(path.basename(filePath))}
    );
    response.end(fileContents);
}

function serveStatic(response, cache, absPath) {
    if (cache[absPath]) {
        sendFile(response, absPath, cache[absPath]);
    } else {
        fs.exists(absPath, function(exists) {
            if (exists) {
                fs.readFile(absPath, function(err, data) {
                    if (err) {
                        send404(response);
                    } else {
                        cache[absPath] = data;
                        sendFile(response, absPath, data);
                    }
                });
            } else {
                send404(response);
            }
        });
    }
}

var server = http.createServer(function(request, response) {
    var filePath = false;

    if (request.url == '/') {
        filePath = 'public/index.html';
    } else {
        filePath = 'public' + request.url;
    }

    var absPath = './' + filePath;
    serveStatic(response, cache, absPath);
});

server.listen(3000, function() {
    console.log("Server listening on port 3000.");
});
