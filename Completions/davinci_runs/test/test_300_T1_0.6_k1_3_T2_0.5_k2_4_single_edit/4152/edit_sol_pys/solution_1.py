var fs = require('fs');

function write(path, content) {
    fs.writeFile(path, content, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");
    });
}

function append(path, content) {
    fs.appendFile(path, content, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was updated!");
    });
}

function read(path) {
    fs.readFile(path, 'utf8', function(err, data) {
        if(err) {
            return console.log(err);
        }
        console.log(data);
    });
}

function readSync(path) {
    var data = fs.readFileSync(path, 'utf8');
    console.log(data);
}

function create(path, content) {
    fs.open(path, 'w', function(err, file) {
        if(err) {
            throw err;
        }
        console.log('Saved!');
    });
}

function remove(path) {
    fs.unlink(path, function(err) {
        if(err) {
            throw err;
        }
        console.log('Removed!');
    });
}

function rename(path, newPath) {
    fs.rename(path, newPath, function(err) {
        if(err) {
            throw err;
        }
        console.log('Renamed!');
    });
}

function changePermission(path, mode) {
    fs.chmod(path, mode, function(err) {
        if(err) {
            throw err;
        }
        console.log('Changed!');
    });
}

function changeOwner(path, uid, gid) {
    fs.chown(path, uid, gid, function(err) {
        if(err) {
            throw err;
        }
        console.log('Changed!');
    });
}

function stat(path) {
    fs.stat(path, function(err, stats) {
        if(err) {
            throw err;
        }
        console.log(stats);
    });
}

function truncate(path, len) {
    fs.truncate(path, len, function(err) {
        if(err) {
            throw err;
        }
        console.log('Truncated!');
    });
}

function readDir(path) {
    fs.readdir(path, function(err, files) {
        if(err) {
            throw err;
        }
        console.log(files);
    });
}

function readDirSync(path) {
    var files = fs.readdirSync(path);
    console.log(files);
}

function createDir(path) {
    fs.mkdir(path, function(err) {
        if(err) {
            throw err;
        }
        console.log('Created!');
    });
}

function removeDir(path) {
    fs.rmdir(path, function(err) {
        if(err) {
            throw err;
        }
        console.log('Removed!');
    });
}

function watch(path, callback) {
    fs.watch(path, callback);
}

function watchFile(path, callback) {
    fs.watchFile(path, callback);
}

function unwatchFile(path, callback) {
    fs.unwatchFile(path, callback);
}

function createReadStream(path) {
    var stream = fs.createReadStream(path);
    stream.on('data', function(chunk) {
        console.log(chunk);
    });
}

function createWriteStream(path) {
    var stream = fs.createWriteStream(path);
    stream.on('open', function() {
        console.log('Opened!');
    });
}

function createWriteStream(path) {
    var stream = fs.createWriteStream(path);
    stream.on('open', function() {
        console.log('Opened!');
    });
}

function close(fd) {
    fs.close(fd, function(err) {
        if(err) {
            throw err;
        }
        console.log('Closed!');
    });
}

function open(path, flags, mode, callback) {
    fs.open(path, flags, mode, function(err, fd) {
        if(err) {
            throw err;
        }
        callback(fd);
    });
}

function openSync(path, flags, mode) {
    var fd = fs.openSync(path, flags, mode);
    return fd;
}

function writeSync(fd, buffer, offset, length, position) {
    fs.writeSync(fd, buffer, offset, length, position);
}

function readSync(fd, buffer, offset, length, position) {
    fs.readSync(fd, buffer, offset, length, position);
}

function link(src, dest) {
    fs.link(src, dest, function(err) {
        if(err) {
            throw err;
        }
        console.log('Linked!');
    });
}

function linkSync(src, dest) {
    fs.linkSync(src, dest);
}

function symlink(src, dest) {
    fs.symlink(src, dest, function(err) {
        if(err) {
            throw err;
        }
        console.log('Symlinked!');
    });
}

function symlinkSync(src, dest) {
    fs.symlinkSync(src, dest);
}

function readlink(path) {
    fs.readlink(path, function(err, linkString) {
        if(err) {
            throw err;
        }
        console.log(linkString);
    });
}

function readlinkSync(path) {
    var linkString = fs.readlinkSync(path);
    console.log(linkString);
}

function realpathSync(path) {
    var realPath = fs.realpathSync(path);
    console.log(realPath);
}
