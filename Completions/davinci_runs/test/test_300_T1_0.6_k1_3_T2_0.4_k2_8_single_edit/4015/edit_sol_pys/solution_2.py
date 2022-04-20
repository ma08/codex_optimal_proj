// file.js

var fs = require('fs');
var path = require('path');

var file = {
  /**
   * 创建文件夹
   * @param  {String} dirname 目录
   * @return {Boolean}        创建结果
   */
  mkdirsSync: function(dirname) {
    if (fs.existsSync(dirname)) {
      return true;
    } else {
      if (file.mkdirsSync(path.dirname(dirname))) {
        fs.mkdirSync(dirname);
        return true;
      }
    }
  },
  /**
   * 创建文件夹
   * @param  {String}   dirname     目录
   * @param  {Function} callback    回调
   */
  mkdirs: function(dirname, callback) {
    fs.exists(dirname, function(exists) {
      if (exists) {
        callback();
      } else {
        //尝试创建父目录，然后再创建当前目录
        file.mkdirs(path.dirname(dirname), function() {
          fs.mkdir(dirname, callback);
          console.log('在' + path.dirname(dirname) + '目录创建好' + dirname + '目录');
        });
      }
    });
  },
  /**
   * 创建文件
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  createFile: function(filename, callback) {
    fs.open(filename, 'w', function(err, fd) {
      if (err) {
        throw 'could not open file: ' + err;
      }
      //文件创建成功后，写入内容，如果文件原来存在，则会被截断为零长度
      fs.write(fd, '', 0, 'utf8', function(err, written, buffer) {});
      callback();
    });
  },
  /**
   * 删除文件
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  deleteFile: function(filename, callback) {
    fs.unlink(filename, function(err) {
      if (err) {
        throw err;
      }
      callback();
    });
  },
  /**
   * 写入文件
   * @param  {String}   filename 文件名
   * @param  {String}   content  内容
   * @param  {Function} callback 回调
   */
  writeFile: function(filename, content, callback) {
    fs.writeFile(filename, content, function(err) {
      if (err) throw err;
      callback();
    });
  },
  /**
   * 追加文件
   * @param  {String}   filename 文件名
   * @param  {String}   content  内容
   * @param  {Function} callback 回调
   */
  appendFile: function(filename, content, callback) {
    fs.appendFile(filename, content, function(err) {
      if (err) throw err;
      callback();
    });
  },
  /**
   * 读取文件
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  readFile: function(filename, callback) {
    fs.readFile(filename, 'utf-8', function(err, data) {
      if (err) throw err;
      callback(data);
    });
  },
  /**
   * 读取文件
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  readImg: function(filename, callback) {
    fs.readFile(filename, function(err, data) {
      if (err) throw err;
      callback(data);
    });
  },
  /**
   * 获取文件信息
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  statFile: function(filename, callback) {
    fs.stat(filename, function(err, stat) {
      if (err) throw err;
      callback(stat);
    });
  },
  /**
   * 获取文件信息
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  isFile: function(filename, callback) {
    file.statFile(filename, function(stat) {
      callback(stat.isFile());
    });
  },
  /**
   * 获取文件信息
   * @param  {String}   filename 文件名
   * @param  {Function} callback 回调
   */
  isDir: function(filename, callback) {
    file.statFile(filename, function(stat) {
      callback(stat.isDirectory());
    });
  },
  /**
   * 遍历目录
   * @param  {String}   pathname  路径
   * @param  {Function} callback  回调
   */
  readDir: function(pathname, callback) {
    fs.readdir(pathname, function(err, files) {
      if (err) throw err;
      callback(files);
    });
  }
};

module.exports = file;
