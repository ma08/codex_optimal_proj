"use strict";

let fs = require('fs');

class File {
    constructor(path) {
        this._path = path;
    }

    get path() {
        return this._path;
    }

    get exists() {
        return fs.existsSync(this._path);
    }

    get size() {
        return fs.statSync(this._path).size;
    }

    get isFile() {
        return fs.statSync(this._path).isFile();
    }

    get isDirectory() {
        return fs.statSync(this._path).isDirectory();
    }

    get isSymbolicLink() {
        return fs.lstatSync(this._path).isSymbolicLink();
    }

    get parent() {
        return new File(this._path.substring(0, this._path.lastIndexOf('/')));
    }

    get name() {
        return this._path.substring(this._path.lastIndexOf('/') + 1);
    }

    get extension() {
        return this._path.substring(this._path.lastIndexOf('.') + 1);
    }

    get modified() {
        return fs.statSync(this._path).mtime;
    }

    get created() {
        return fs.statSync(this._path).ctime;
    }

    get lastAccessed() {
        return fs.statSync(this._path).atime;
    }

    get permissions() {
        return fs.statSync(this._path).mode;
    }

    get owner() {
        return fs.statSync(this._path).uid;
    }

    get group() {
        return fs.statSync(this._path).gid;
    }

    get children() {
        return fs.readdirSync(this._path);
    }

    get content() {
        return fs.readFileSync(this._path);
    }

    get contentAsString() {
        return fs.readFileSync(this._path, 'utf8');
    }

    get contentAsStringArray() {
        return fs.readFileSync(this._path, 'utf8').split('\n');
    }

    get contentAsStringArrayWithoutEmptyLines() {
        return fs.readFileSync(this._path, 'utf8').split('\n').filter(line => line.length > 0);
    }

    get contentAsStringArrayWithoutComments() {
        return fs.readFileSync(this._path, 'utf8').split('\n').filter(line => !line.startsWith('#'));
    }

    get contentAsStringArrayWithoutEmptyLinesOrComments() {
        return fs.readFileSync(this._path, 'utf8').split('\n').filter(line => line.length > 0 && !line.startsWith('#'));
    }

    get contentAsJSON() {
        return JSON.parse(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsYAML() {
        return YAML.parse(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsCSV() {
        return d3.csvParse(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsTSV() {
        return d3.tsvParse(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsHTML() {
        return d3.html(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsXML() {
        return d3.xml(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsSVG() {
        return d3.svg(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsImage() {
        return d3.image(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsText() {
        return d3.text(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsBlob() {
        return d3.blob(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsArrayBuffer() {
        return d3.arrayBuffer(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsResponse() {
        return d3.response(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsFormData() {
        return d3.formData(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsDSV() {
        return d3.dsv(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsTSV() {
        return d3.tsv(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsCSV() {
        return d3.csv(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsXLS() {
        return d3.xls(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsXLSX() {
        return d3.xlsx(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsHTML() {
        return d3.html(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsXML() {
        return d3.xml(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsSVG() {
        return d3.svg(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsImage() {
        return d3.image(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsText() {
        return d3.text(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsBlob() {
        return d3.blob(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsArrayBuffer() {
        return d3.arrayBuffer(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsResponse() {
        return d3.response(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsFormData() {
        return d3.formData(fs.readFileSync(this._path, 'utf8'));
    }

    get contentAsDSV() {
        return d3.dsv(fs.readFileSync(this._path, 'utf8'));
    }
}

module.exports = File;
