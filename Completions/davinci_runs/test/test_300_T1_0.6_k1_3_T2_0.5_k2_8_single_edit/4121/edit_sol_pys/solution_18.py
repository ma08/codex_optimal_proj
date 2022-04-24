function File() {

}

File.prototype.createFile = function(fileName, fileContent, callback) {
	var fs = require('fs');
	fs.writeFile(fileName, fileContent, function(err) {
		if (err) {
			return console.log(err);
		}

		console.log("The file was saved!");
	});
};

File.prototype.readFile = function(fileName, callback) {

};

File.prototype.appendFile = function(fileName, fileContent, callback) {
	var fs = require('fs');
	fs.appendFile(fileName, fileContent, function(err) {
		if (err) {
			return console.log(err);
		}

		console.log("The file was saved!");
	});
};

File.prototype.deleteFile = function(fileName, callback) {

};

File.prototype.readDir = function(dirName, callback) {

};

File.prototype.createDir = function(dirName, callback) {

};

File.prototype.deleteDir = function(dirName, callback) {

};

File.prototype.rename = function(oldName, newName, callback) {

};

File.prototype.search = function(fileName, callback) {

};

module.exports = File;
