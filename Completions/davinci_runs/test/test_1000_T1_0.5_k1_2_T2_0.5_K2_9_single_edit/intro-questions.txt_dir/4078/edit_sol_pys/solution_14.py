// file.js
var fs = require('fs');
var path = require('path');

exports.readFile = function(filepath, callback) {
    fs.readFile(filepath, 'utf8', function(err, data){
        if (err) {
            console.log(err);
        }
        if (callback) {
            callback(data);
        }
    });
};

exports.writeFile = function(filepath, data, callback) {
    fs.writeFile(filepath, data, function(err){
        if (err) {
            console.log(err);
        }
        if (callback) {
            callback();
        }
    });
};

exports.readDir = function(dirpath, callback) {
    fs.readdir(dirpath, function(err, data){
        if (err) {
            console.log(err);
        }
        if (callback) {
            callback(data);
        }
    });
};

exports.readJSON = function(filepath, callback) {
    fs.readFile(filepath, 'utf8', function(err, data){
        if (err) {
            console.log(err);
        }
        var json = JSON.parse(data);
        if (callback) {
            callback(json);
        }
    });
};

exports.writeJSON = function(filepath, data, callback) {
    var json = JSON.stringify(data, null, 4);
    fs.writeFile(filepath, json, function(err){
        if (err) {
            console.log(err);
        }
        if (callback) {
            callback();
        }
    });
};

exports.readDirJSON = function(dirpath, callback) {
    var filepaths = [];
    var jsons = [];

    fs.readdir(dirpath, function(err, files){
        if (err) {
            console.log(err);
        }

        var filepath;
        for (var i = 0; i < files.length; i++) {
            filepath = path.join(dirpath, files[i]);
            filepaths.push(filepath);
        }

        var count = 0;
        for (var i = 0; i < filepaths.length; i++) {
            fs.readFile(filepaths[i], 'utf8', function(err, data){
                if (err) {
                    console.log(err);
                }
                var json = JSON.parse(data);
                jsons.push(json);
                count++;
                if (count == filepaths.length) {
                    if (callback) {
                        callback(jsons);
                    }
                }
            });
        }
    });
};
