// FILE

// The fs module provides an API for interacting with the file system in a manner closely modeled around standard POSIX functions.

// All file system operations have synchronous and asynchronous forms.

// The asynchronous form always takes a completion callback as its last argument. The arguments passed to the completion callback depend on the method, but the first argument is always reserved for an exception. If the operation was completed successfully, then the first argument will be null or undefined.

// SYNTAX

// fs.readFile(path[, options], callback)
// Asynchronous readFile - Asynchronously reads the entire contents of a file.

// fs.readFileSync(path[, options])
// Synchronous readFile - Synchronously reads the entire contents of a file.

// fs.writeFile(file, data[, options], callback)
// Asynchronous writeFile - Asynchronously writes data to a file, replacing the file if it already exists. data can be a string or a buffer.

// fs.writeFileSync(file, data[, options])
// Synchronous writeFile - Synchronously writes data to a file, replacing the file if it already exists. data can be a string or a buffer.

// fs.appendFile(file, data[, options], callback)
// Asynchronous appendFile - Asynchronously appends data to a file, creating the file if it not yet exists. data can be a string or a buffer.

// fs.appendFileSync(file, data[, options])
// Synchronous appendFile - Synchronously appends data to a file, creating the file if it not yet exists. data can be a string or a buffer.

// fs.open(path, flags[, mode], callback)
// Asynchronous file open - Asynchronously opens a file for reading or writing.

// fs.openSync(path, flags[, mode])
// Synchronous file open - Synchronously opens a file for reading or writing.

// fs.close(fd, callback)
// Asynchronous close - Asynchronously closes a file descriptor.

// fs.closeSync(fd)
// Synchronous close - Synchronously closes a file descriptor.

// fs.read(fd, buffer, offset, length, position, callback)
// Asynchronous read - Reads data from the file specified by fd.

// fs.readSync(fd, buffer, offset, length, position)
// Synchronous read - Reads data from the file specified by fd.

// fs.write(fd, buffer, offset, length[, position], callback)
// Asynchronous write - Writes buffer to the file specified by fd.

// fs.writeSync(fd, buffer, offset, length[, position])
// Synchronous write - Writes buffer to the file specified by fd.

// fs.rename(oldPath, newPath, callback)
// Asynchronous rename - Renames the file specified by oldPath to newPath.

// fs.renameSync(oldPath, newPath)
// Synchronous rename - Renames the file specified by oldPath to newPath.

// fs.truncate(path, len, callback)
// Asynchronous truncate - Truncates the file specified by path to a specified length.

// fs.truncateSync(path, len)
// Synchronous truncate - Truncates the file specified by path to a specified length.

// fs.ftruncate(fd, len, callback)
// Asynchronous ftruncate - Truncates the file specified by fd to a specified length.

// fs.ftruncateSync(fd, len)
// Synchronous ftruncate - Truncates the file specified by fd to a specified length.

// fs.rmdir(path, callback)
// Asynchronous rmdir - Removes the directory specified by path.

// fs.rmdirSync(path)
// Synchronous rmdir - Removes the directory specified by path.

// fs.mkdir(path[, mode], callback)
// Asynchronous mkdir - Creates the directory specified by path.

// fs.mkdirSync(path[, mode])
// Synchronous mkdir - Creates the directory specified by path.

// fs.readdir(path, callback)
// Asynchronous readdir - Reads the contents of a directory.

// fs.readdirSync(path)
// Synchronous readdir - Synchronously reads the contents of a directory.

// fs.fstat(fd, callback)
// Asynchronous fstat - Gets the file status.

// fs.fstatSync(fd)
// Synchronous fstat - Gets the file status.

// fs.lstat(path, callback)
// Asynchronous lstat - Gets the file status. Does not dereference symbolic links.

// fs.lstatSync(path)
// Synchronous lstat - Gets the file status. Does not dereference symbolic links.

// fs.stat(path, callback)
// Asynchronous stat - Gets the file status.

// fs.statSync(path)
// Synchronous stat - Gets the file status.

// fs.link(srcpath, dstpath, callback)
// Asynchronous link - Creates a hard link.

// fs.linkSync(srcpath, dstpath)
// Synchronous link - Creates a hard link.

// fs.symlink(srcpath, dstpath[, type], callback)
// Asynchronous symlink - Creates a symbolic link.

// fs.symlinkSync(srcpath, dstpath[, type])
// Synchronous symlink - Creates a symbolic link.

// fs.readlink(path, callback)
// Asynchronous readlink - Reads the value of a symbolic link.

// fs.readlinkSync(path)
// Synchronous readlink - Reads the value of a symbolic link.

// fs.realpath(path[, cache], callback)
// Asynchronous realpath - Returns the canonicalized absolute pathname.

// fs.realpathSync(path[, cache])
// Synchronous realpath - Returns the canonicalized absolute pathname.

// fs.unlink(path, callback)
// Asynchronous unlink - Removes the file specified by path.

// fs.unlinkSync(path)
// Synchronous unlink - Removes the file specified by path.

// fs.fsync(fd, callback)
// Asynchronous fsync - Synchronizes a file's in-core state with the underlying storage device.

// fs.fsyncSync(fd)
// Synchronous fsync - Synchronizes a file's in-core state with the underlying storage device.

// fs.writeSync(fd, data[, position[, encoding]])
// Synchronous write - Writes buffer to the file specified by fd.

// fs.write(fd, data[, position[, encoding]], callback)
// Asynchronous write - Writes buffer to the file specified by fd.

// fs.read(fd, buffer, offset, length, position, callback)
// Asynchronous read - Reads data from the file specified by fd.

// fs.readSync(fd, buffer, offset, length, position)
// Synchronous read - Reads data from the file specified by fd.
