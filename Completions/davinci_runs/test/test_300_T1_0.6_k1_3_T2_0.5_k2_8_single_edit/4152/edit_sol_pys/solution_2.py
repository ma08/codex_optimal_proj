function file(name) {
	return {
		name: name,
		type: "file",
		contents: function(contents) {
			this.contents = contents;
			return this;
		}
	};
}

function directory(name) {
	return {
		name: name,
		type: "directory",
		contents: [],
		add: function(file) {
			this.contents.push(file);
			return this;
		}
	};
}

function tree(root) {
	return {
		root: root,
		add: function(file) {
			this.root.add(file);
			return this;
		}
	}
}

// Test

var root = directory("root");
var file1 = file("file1");
file1.contents("file1 contents");
var dir1 = directory("dir1");
var file2 = file("file2");
file2.contents("file2 contents");

var tree1 = tree(root);
tree1.add(file1).add(dir1).add(file2);

console.log(tree1);

var file3 = file("file3");
file3.contents("file3 contents");
dir1.add(file3);

console.log(tree1);
