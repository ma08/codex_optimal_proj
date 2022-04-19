var fs = require('fs');
var path = require('path');

var file = {
  /**
   * 判断文件或文件夹是否存在
   * @param  {String}  filePath 文件或文件夹路径
   * @return {Boolean}
   */
  exists: function(filePath) {
    return fs.existsSync(filePath);
  },
  /**
   * 创建文件夹
   * @param  {String} dir 文件夹路径
   * @return {Boolean}
   */
  mkdir: function(dir) {
    if (this.exists(dir)) {
      return true;
    }

    if (this.mkdir(path.dirname(dir))) {
      fs.mkdirSync(dir);
      return true;
    }
  },
  /**
   * 创建文件
   * @param  {String} filePath 文件路径
   * @param  {String} content  文件内容
   * @return {Boolean}
   */
  create: function(filePath, content) {
    this.mkdir(path.dirname(filePath));
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  },
  /**
   * 读取文件
   * @param  {String} filePath 文件路径
   * @return {String}
   */
  read: function(filePath) {
    return fs.readFileSync(filePath, 'utf8');
  },
  /**
   * 删除文件
   * @param  {String} filePath 文件路径
   * @return {Boolean}
   */
  delete: function(filePath) {
    if (this.exists(filePath)) {
      fs.unlinkSync(filePath);
      return true;
    }
    return false;
  },
  /**
   * 遍历文件夹
   * @param  {String} dirPath  文件夹路径
   * @param  {Function} callback 回调函数
   * @return {Boolean}
   */
  travel: function(dirPath, callback) {
    if (this.exists(dirPath)) {
      fs.readdirSync(dirPath).forEach(function(file) {
        var pathname = path.join(dirPath, file);

        if (fs.statSync(pathname).isDirectory()) {
          this.travel(pathname, callback);
        } else {
          callback(pathname);
        }
      }.bind(this));
    }
  }
};

module.exports = file;
