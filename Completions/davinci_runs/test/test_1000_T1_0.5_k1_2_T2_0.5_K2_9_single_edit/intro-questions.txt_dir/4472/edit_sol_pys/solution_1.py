var fs = require('fs')
var path = require('path')
var pathToConfigFile = path.join(__dirname, 'config.json')


var config = JSON.parse(fs.readFileSync(pathToConfigFile))

console.log(config.port)



var http = require('http')
var server = http.createServer(function (req, res) {
    res.writeHead(200)
    res.end('Hello world')
})

server.listen(config.port, function () {
    console.log('Server started on port ' + config.port)
})
