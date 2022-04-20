function File(name, content, parent) {
  this.name = name;
  this.content = content;
  this.parent = parent;
}

File.prototype.getPath = function() {
  if (this.parent === null) {
    return this.name;
  } else {
    return this.parent.getPath() + "/" + this.name;
  }
}

File.prototype.getContent = function() {
  return this.content;
}

File.prototype.setContent = function(content) {
  this.content = content;
}

File.prototype.getParent = function() {
  return this.parent;
}

File.prototype.setParent = function(parent) {
  this.parent = parent;
}

File.prototype.getName = function() {
  return this.name;
}

File.prototype.setName = function(name) {
  this.name = name;
}

File.prototype.getType = function() {
  return "file";
}

File.prototype.getSize = function() {
  return this.content.length;
}

File.prototype.getChildren = function() {
  return null;
}

File.prototype.getChild = function(name) {
  return null;
}

File.prototype.addChild = function(child) {
  return null;
}

File.prototype.removeChild = function(name) {
  return null;
}

File.prototype.toString = function() {
  return this.getPath() + ": " + this.getContent();
}

module.exports = File;
