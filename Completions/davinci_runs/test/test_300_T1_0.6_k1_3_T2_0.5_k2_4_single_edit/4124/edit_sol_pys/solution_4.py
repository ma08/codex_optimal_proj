var fs = require('fs');
var path = require('path');


function getAllFiles(root) {
    var res = [];
    var files = fs.readdirSync(root);
    files.forEach(function(file) {
        var pathname = root+'/'+file
            , stat = fs.lstatSync(pathname);

        if (!stat.isDirectory()) {
            res.push(pathname.replace(root, ''));
        } else {
            res = res.concat(getAllFiles(pathname));
        }
    });
    return res;
}
module.exports = {
    getAllFiles: getAllFiles
};
