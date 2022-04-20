var fs = require('fs');

var getFile = function(path) {
  return fs.readFileSync(path, 'utf8');
};

var writeFile = function(path, content) {
  return fs.writeFileSync(path, content, 'utf8');
};

var getFileLines = function(path) {
  return getFile(path).split('\n');
};

var getFileLinesWithIndex = function(path) {
  var lines = getFileLines(path);
  var linesWithIndex = [];
  for (var i = 0; i < lines.length; i++) {
    linesWithIndex.push({
      index: i,
      line: lines[i]
    });
  }
  return linesWithIndex;
};

var getFileLinesWithIndexAndContent = function(path) {
  var lines = getFileLinesWithIndex(path);
  var linesWithIndexAndContent = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var content = line.line.split(':');
    linesWithIndexAndContent.push({
      index: line.index,
      content: content
    });
  }
  return linesWithIndexAndContent;
};

var getFileLinesWithIndexAndContentAndType = function(path) {
  var lines = getFileLinesWithIndexAndContent(path);
  var linesWithIndexAndContentAndType = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var type = line.content[0];
    var content = line.content[1];
    linesWithIndexAndContentAndType.push({
      index: line.index,
      type: type,
      content: content
    });
  }
  return linesWithIndexAndContentAndType;
};

var getFileLinesWithIndexAndContentAndTypeAndTitle = function(path) {
  var lines = getFileLinesWithIndexAndContentAndType(path);
  var linesWithIndexAndContentAndTypeAndTitle = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var title = line.content.split(' ')[0];
    var content = line.content.replace(title, '').trim();
    linesWithIndexAndContentAndTypeAndTitle.push({
      index: line.index,
      type: line.type,
      title: title,
      content: content
    });
  }
  return linesWithIndexAndContentAndTypeAndTitle;
};

var getFileLinesWithIndexAndContentAndTypeAndTitleAndTags = function(path) {
  var lines = getFileLinesWithIndexAndContentAndTypeAndTitle(path);
  var linesWithIndexAndContentAndTypeAndTitleAndTags = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var tags = line.content.split(' ');
    var content = line.content.replace(tags.join(' '), '').trim();
    linesWithIndexAndContentAndTypeAndTitleAndTags.push({
      index: line.index,
      type: line.type,
      title: line.title,
      tags: tags,
      content: content
    });
  }
  return linesWithIndexAndContentAndTypeAndTitleAndTags;
};

var getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDate = function(path) {
  var lines = getFileLinesWithIndexAndContentAndTypeAndTitleAndTags(path);
  var linesWithIndexAndContentAndTypeAndTitleAndTagsAndDate = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var date = line.content.split(' ')[0];
    var content = line.content.replace(date, '').trim();
    linesWithIndexAndContentAndTypeAndTitleAndTagsAndDate.push({
      index: line.index,
      type: line.type,
      title: line.title,
      tags: line.tags,
      date: date,
      content: content
    });
  }
  return linesWithIndexAndContentAndTypeAndTitleAndTagsAndDate;
};

var getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks = function(path) {
  var lines = getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDate(path);
  var linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var links = line.content.split(' ');
    var content = line.content.replace(links.join(' '), '').trim();
    linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks.push({
      index: line.index,
      type: line.type,
      title: line.title,
      tags: line.tags,
      date: line.date,
      links: links,
      content: content
    });
  }
  return linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks;
};

var getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor = function(path) {
  var lines = getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks(path);
  var linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor = [];
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var author = line.content.split(' ')[0];
    var content = line.content.replace(author, '').trim();
    linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor.push({
      index: line.index,
      type: line.type,
      title: line.title,
      tags: line.tags,
      date: line.date,
      links: line.links,
      author: author,
      content: content
    });
  }
  return linesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor;
};

module.exports = {
  getFile: getFile,
  writeFile: writeFile,
  getFileLines: getFileLines,
  getFileLinesWithIndex: getFileLinesWithIndex,
  getFileLinesWithIndexAndContent: getFileLinesWithIndexAndContent,
  getFileLinesWithIndexAndContentAndType: getFileLinesWithIndexAndContentAndType,
  getFileLinesWithIndexAndContentAndTypeAndTitle: getFileLinesWithIndexAndContentAndTypeAndTitle,
  getFileLinesWithIndexAndContentAndTypeAndTitleAndTags: getFileLinesWithIndexAndContentAndTypeAndTitleAndTags,
  getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDate: getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDate,
  getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks: getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinks,
  getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor: getFileLinesWithIndexAndContentAndTypeAndTitleAndTagsAndDateAndLinksAndAuthor
};
