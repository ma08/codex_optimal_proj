function File(name, size) {
  this.name = name;
  this.size = size;
}

File.prototype.getSize = function() {
  return this.size;
}

File.prototype.getName = function() {
  return this.name;
}

File.prototype.rename = function(newName) {
  this.name = newName;
}

function Folder(name) {
  this.name = name;
  this.files = [];
}

Folder.prototype.addFile = function(file) {
  this.files.push(file);
}

Folder.prototype.removeFile = function(file) {
  this.files = this.files.filter(function(f) {
    return f.getName() !== file.getName();
  });
}

Folder.prototype.getSize = function() {
  var total = 0;
  for (var i = 0; i < this.files.length; i++) {
    total += this.files[i].getSize();
  }
  return total;
}

Folder.prototype.getName = function() {
  return this.name;
}

Folder.prototype.rename = function(newName) {
  this.name = newName;
}

var f1 = new File('f1', 10);
var f2 = new File('f2', 20);
var f3 = new File('f3', 30);
var f4 = new File('f4', 40);
var f5 = new File('f5', 50);

var folder1 = new Folder('folder1');
var folder2 = new Folder('folder2');

folder1.addFile(f1);
folder1.addFile(f2);
folder2.addFile(f3);
folder2.addFile(f4);
folder2.addFile(f5);
folder1.addFile(folder2);

console.log(folder1.getSize());
