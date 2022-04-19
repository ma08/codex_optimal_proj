//File.js

function File(name, type, size, data) {
  this.name = name;
  this.type = type;
  this.size = size;
  this.data = data;
}

File.prototype.getName = function() {
  return this.name;
}

File.prototype.getType = function() {
  return this.type;
}

File.prototype.getSize = function() {
  return this.size;
}

File.prototype.getData = function() {
  return this.data;
}
