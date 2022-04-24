const fs = require('fs');
const path = require('path');

module.exports = {
  /**
   * @description 创建目录
   * @param {String} dirPath 目录路径
   */
  mkdirsSync: function (dirPath) {
    if (fs.existsSync(dirPath)) {
      return true;
    } else {
      if (this.mkdirsSync(path.dirname(dirPath))) {
        fs.mkdirSync(dirPath);
        return true;
      }
    }
  },
  /**
   * @description 写入文件
   * @param {String} filePath 文件路径
   * @param {Object} data 数据
   */
  writeFile: function (filePath, data) {
    return new Promise((resolve, reject) => {
      fs.writeFile(filePath, data, function (err) {
        if (err) {
          console.log('写入失败', err);
          reject(err);
        } else {
          console.log('写入成功');
          resolve(true);
        }
      });
    });
  }
};
