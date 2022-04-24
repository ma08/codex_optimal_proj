var fs = require('fs');
var path = require('path');
var util = require('util');
var colors = require('colors');
var mkdirp = require('mkdirp');

var File = function(filepath) {
  this.filepath = filepath;
  this.file = path.basename(filepath);
  this.dir = path.dirname(filepath);
  this.ext = path.extname(filepath);
  this.name = path.basename(filepath, this.ext);
  this.stat = null;
  this.contents = null;
  this.isBinary = null;
  this.isBuffer = null;
  this.isStream = null;
  this.isNull = null;
};

File.prototype.isBuffer = function() {
  return Buffer.isBuffer(this.contents);
};

File.prototype.isStream = function() {
  return util.isStream(this.contents);
};

File.prototype.isNull = function() {
  return this.contents === null;
};

File.prototype.isDirectory = function() {
  return this.stat && this.stat.isDirectory();
};

File.prototype.isText = function() {
  if (this.isBuffer()) {
    return false;
  }
  if (this.isStream()) {
    return false;
  }
  if (this.isNull()) {
    return false;
  }
  return true;
};

File.prototype.isNull = function() {
  return this.contents === null;
};

File.prototype.isDirectory = function() {
  return this.stat && this.stat.isDirectory();
};

File.prototype.isText = function() {
  if (this.isBuffer()) {
    return false;
  }
  if (this.isStream()) {
    return false;
  }
  if (this.isNull()) {
    return false;
  }
  return true;
};

File.prototype.isBinary = function() {
  if (this.isBuffer()) {
    return true;
  }
  if (this.isStream()) {
    return true;
  }
  if (this.isNull()) {
    return true;
  }
  return false;
};

File.prototype.inspect = function() {
  var inspect = [];
  inspect.push(colors.magenta(this.file));
  inspect.push(colors.grey('(' + this.contents.length + ')'));
  return inspect.join(' ');
};

File.prototype.read = function(enc, cb) {
  var self = this;
  if (!cb && typeof enc === 'function') {
    cb = enc;
    enc = null;
  }
  if (typeof enc === 'string') {
    enc = { encoding: enc };
  }
  if (cb) {
    this.readSync(enc);
    process.nextTick(cb);
    return;
  }
  fs.readFile(this.filepath, enc, function(err, data) {
    if (err) {
      self.error = err;
      self.contents = null;
      self.stat = null;
      return cb(err);
    }
    self.contents = data;
    self.stat = fs.statSync(self.filepath);
    cb(null, self);
  });
};

File.prototype.readSync = function(enc) {
  this.contents = fs.readFileSync(this.filepath, enc);
  this.stat = fs.statSync(this.filepath);
  return this;
};

File.prototype.write = function(options, cb) {
  if (!cb && typeof options === 'function') {
    cb = options;
    options = {};
  }
  if (typeof options === 'string') {
    options = { encoding: options };
  }
  if (options.encoding !== null) {
    options.encoding = options.encoding || 'utf8';
  }
  if (!cb) {
    this.writeSync(options);
    return;
  }
  var self = this;
  var dir = path.dirname(this.filepath);
  mkdirp(dir, function(err) {
    if (err) {
      self.error = err;
      return cb(err);
    }
    fs.writeFile(self.filepath, self.contents, options, function(err) {
      if (err) {
        self.error = err;
        return cb(err);
      }
      self.stat = fs.statSync(self.filepath);
      cb(null, self);
    });
  });
};

File.prototype.writeSync = function(options) {
  if (options.encoding !== null) {
    options.encoding = options.encoding || 'utf8';
  }
  var dir = path.dirname(this.filepath);
  mkdirp.sync(dir);
  fs.writeFileSync(this.filepath, this.contents, options);
  this.stat = fs.statSync(this.filepath);
  return this;
};

File.prototype.clone = function(options) {
  if (typeof options === 'string') {
    options = {cwd: options};
  }
  options = options || {};
  var file = new File({
    cwd: options.cwd || this.cwd,
    base: options.base || this.base,
    path: options.path || this.path,
    stat: this.stat,
    contents: this.contents
  });
  return file;
};

File.prototype.pipe = function(stream, opt) {
  if (!opt) opt = {};
  if (typeof opt.end === 'undefined') opt.end = true;

  if (this.isStream()) {
    return this.contents.pipe(stream, opt);
  }

  if (this.isBuffer()) {
    if (opt.end) {
      stream.end(this.contents);
    } else {
      stream.write(this.contents);
    }
    return stream;
  }

  if (this.isNull()) {
    if (opt.end) stream.end();
    return stream;
  }

  stream.end(this.contents, opt.encoding);
  return stream;
};

File.prototype.contents = function(buf) {
  if (typeof buf === 'undefined') {
    if (!this.isBuffer()) {
      return this.contents;
    }
    if (this.isStream()) {
      throw new Error('Contents is a stream');
    }
    return this.contents;
  }
  if (typeof buf === 'string') {
    buf = new Buffer(buf);
  }
  this.contents = buf;
  return this;
};

File.prototype.relative = function(filepath) {
  if (filepath) {
    this.path = path.join(this.base, filepath);
  }
  return path.relative(this.cwd, this.path);
};

File.prototype.basename = function(ext) {
  if (ext) {
    this.path = path.join(this.dirname
