var file = {
    open: function(path, mode) {
        var fd = this._open(path, mode);
        if (fd < 0) {
            throw new Error("open " + path + " error!");
        }
        return new File(fd);
    },
    openSync: function(path, mode) {
        var fd = this._open(path, mode);
        if (fd < 0) {
            throw new Error("open " + path + " error!");
        }
        return fd;
    },
    _open: function(path, mode) {
        var fd = 0;
        var flags = 0;
        var access = 0;
        if (mode.indexOf("w") != -1) {
            flags |= 0x02;
            access |= 0x02;
        }
        if (mode.indexOf("r") != -1) {
            flags |= 0x01;
            access |= 0x01;
        }
        if (mode.indexOf("a") != -1) {
            flags |= 0x02;
            access |= 0x02;
        }
        if (mode.indexOf("+") != -1) {
            access |= 0x02 | 0x01;
        }
        if (mode.indexOf("x") != -1) {
            flags |= 0x100;
        }
        if (mode.indexOf("b") != -1) {
            flags |= 0x800;
        }
        if (mode.indexOf("t") != -1) {
            flags |= 0x400;
        }
        if (flags == 0) {
            flags |= 0x01;
            access |= 0x01;
        }
        fd = _open(path, flags, access);
        return fd;
    },
    fopen: function(path, mode) {
        return this.open(path, mode);
    },
    fopenSync: function(path, mode) {
        return this.openSync(path, mode);
    },
    close: function(fd) {
        fd.close();
    },
    closeSync: function(fd) {
        if (typeof fd == "number") {
            _close(fd);
        } else {
            fd.close();
        }
    },
    fclose: function(fd) {
        this.close(fd);
    },
    fcloseSync: function(fd) {
        this.closeSync(fd);
    },
    read: function(fd, size) {
        return fd.read(size);
    },
    readSync: function(fd, size) {
        if (typeof fd == "number") {
            return _read(fd, size);
        } else {
            return fd.read(size);
        }
    },
    fread: function(fd, size) {
        return this.read(fd, size);
    },
    freadSync: function(fd, size) {
        return this.readSync(fd, size);
    },
    write: function(fd, data) {
        return fd.write(data);
    },
    writeSync: function(fd, data) {
        if (typeof fd == "number") {
            return _write(fd, data);
        } else {
            return fd.write(data);
        }
    },
    fwrite: function(fd, data) {
        return this.write(fd, data);
    },
    fwriteSync: function(fd, data) {
        return this.writeSync(fd, data);
    },
    stat: function(path) {
        var st = new Stat();
        if (_stat(path, st) == 0) {
            return st;
        }
        return null;
    },
    lstat: function(path) {
        var st = new Stat();
        if (_lstat(path, st) == 0) {
            return st;
        }
        return null;
    },
    fstat: function(fd) {
        return fd.fstat();
    },
    fstatSync: function(fd) {
        return fd.fstat();
    },
    unlink: function(path) {
        return _unlink(path);
    },
    unlinkSync: function(path) {
        return _unlink(path);
    },
    rename: function(oldPath, newPath) {
        return _rename(oldPath, newPath);
    },
    renameSync: function(oldPath, newPath) {
        return _rename(oldPath, newPath);
    },
    mkdir: function(path, mode, callback) {
        return _mkdir(path, mode, callback);
    },
    mkdirSync: function(path, mode) {
        return _mkdir(path, mode);
    },
    rmdir: function(path, callback) {
        return _rmdir(path, callback);
    },
    rmdirSync: function(path) {
        return _rmdir(path);
    },
    readdir: function(path, callback) {
        return _readdir(path, callback);
    },
    readdirSync: function(path) {
        return _readdir(path);
    },
    readlink: function(path, callback) {
        return _readlink(path, callback);
    },
    readlinkSync: function(path) {
        return _readlink(path);
    },
    symlink: function(target, path, callback) {
        return _symlink(target, path, callback);
    },
    symlinkSync: function(target, path) {
        return _symlink(target, path);
    },
    link: function(target, path, callback) {
        return _link(target, path, callback);
    },
    linkSync: function(target, path) {
        return _link(target, path);
    },
    chmod: function(path, mode, callback) {
        return _chmod(path, mode, callback);
    },
    chmodSync: function(path, mode) {
        return _chmod(path, mode);
    },
    fchmod: function(fd, mode, callback) {
        return fd.chmod(mode, callback);
    },
    fchmodSync: function(fd, mode) {
        return fd.chmod(mode);
    },
    chown: function(path, uid, gid, callback) {
        return _chown(path, uid, gid, callback);
    },
    chownSync: function(path, uid, gid) {
        return _chown(path, uid, gid);
    },
    fchown: function(fd, uid, gid, callback) {
        return fd.chown(uid, gid, callback);
    },
    fchownSync: function(fd, uid, gid) {
        return fd.chown(uid, gid);
    },
    truncate: function(path, len, callback) {
        return _truncate(path, len, callback);
    },
    truncateSync: function(path, len) {
        return _truncate(path, len);
    },
    ftruncate: function(fd, len, callback) {
        return fd.truncate(len, callback);
    },
    ftruncateSync: function(fd, len) {
        return fd.truncate(len);
    },
    ut
