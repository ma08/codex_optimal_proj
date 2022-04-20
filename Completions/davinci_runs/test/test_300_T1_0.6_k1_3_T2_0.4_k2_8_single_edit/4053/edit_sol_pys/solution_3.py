/*
 * File: file.js
 * Project: expressway
 * File Created: Wednesday, 5th June 2019 1:47:27 pm
 * Author: Temitayo Bodunrin (temitayo@camelcase.co)
 * -----
 * Last Modified: Wednesday, 5th June 2019 1:47:30 pm
 * Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
 * -----
 * Copyright 2019, CamelCase Technologies Ltd
 */

const fs = require('fs');
const path = require('path');

/**
 * Create a new file
 * @param {string} filePath
 * @param {string} content
 * @param {string} encoding
 * @returns {boolean}
 */
function createFile(filePath, content, encoding = 'utf8') {
    try {
        fs.writeFileSync(filePath, content, encoding);
        return true;
    } catch (error) {
        return false;
    }
}

/**
 * Create a new directory
 * @param {string} dirPath
 * @returns {boolean}
 */
function createDirectory(dirPath) {
    try {
        fs.mkdirSync(dirPath);
        return true;
    } catch (error) {
        return false;
    }
}

/**
 * Check if a file exists
 * @param {string} filePath
 * @returns {boolean}
 */
function fileExists(filePath) {
    try {
        return fs.existsSync(filePath);
    } catch (error) {
        return false;
    }
}

/**
 * Check if a directory exists
 * @param {string} dirPath
 * @returns {boolean}
 */
function directoryExists(dirPath) {
    try {
        return fs.existsSync(dirPath);
    } catch (error) {
        return false;
    }
}

/**
 * Read a file
 * @param {string} filePath
 * @param {string} encoding
 * @returns {string}
 */
function readFile(filePath, encoding = 'utf8') {
    try {
        return fs.readFileSync(filePath, encoding);
    } catch (error) {
        return null;
    }
}

/**
 * Get file extension
 * @param {string} filePath
 * @returns {string}
 */
function getFileExtension(filePath) {
    return path.extname(filePath);
}

/**
 * Get file name
 * @param {string} filePath
 * @returns {string}
 */
function getFileName(filePath) {
    return path.basename(filePath);
}

/**
 * Get file name without extension
 * @param {string} filePath
 * @returns {string}
 */
function getFileNameWithoutExtension(filePath) {
    return path.basename(filePath, path.extname(filePath));
}

/**
 * Get file path
 * @param {string} filePath
 * @returns {string}
 */
function getFilePath(filePath) {
    return path.dirname(filePath);
}

/**
 * Get all files in a directory
 * @param {string} dirPath
 * @returns {array}
 */
function getFilesInDirectory(dirPath) {
    try {
        return fs.readdirSync(dirPath);
    } catch (error) {
        return [];
    }
}

/**
 * Get all files in a directory recursively
 * @param {string} dirPath
 * @returns {array}
 */
function getFilesInDirectoryRecursive(dirPath) {
    const files = [];
    const filesInDir = getFilesInDirectory(dirPath);

    filesInDir.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);

        if (stats.isDirectory()) {
            const subFiles = getFilesInDirectoryRecursive(filePath);
            files.push(...subFiles);
        } else {
            files.push(filePath);
        }
    });

    return files;
}

/**
 * Get all directories in a directory
 * @param {string} dirPath
 * @returns {array}
 */
function getDirectoriesInDirectory(dirPath) {
    try {
        return fs.readdirSync(dirPath).filter(file => {
            const filePath = path.join(dirPath, file);
            return fs.statSync(filePath).isDirectory();
        });
    } catch (error) {
        return [];
    }
}

/**
 * Get all directories in a directory recursively
 * @param {string} dirPath
 * @returns {array}
 */
function getDirectoriesInDirectoryRecursive(dirPath) {
    const directories = [];
    const filesInDir = getFilesInDirectory(dirPath);

    filesInDir.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);

        if (stats.isDirectory()) {
            directories.push(filePath);
            const subFiles = getDirectoriesInDirectoryRecursive(filePath);
            directories.push(...subFiles);
        }
    });

    return directories;
}

/**
 * Get all files in a directory with a specific extension
 * @param {string} dirPath
 * @param {string} extension
 * @returns {array}
 */
function getFilesInDirectoryWithExtension(dirPath, extension) {
    try {
        return fs.readdirSync(dirPath).filter(file => {
            return path.extname(file) === extension;
        });
    } catch (error) {
        return [];
    }
}

/**
 * Get all files in a directory with a specific extension recursively
 * @param {string} dirPath
 * @param {string} extension
 * @returns {array}
 */
function getFilesInDirectoryWithExtensionRecursive(dirPath, extension) {
    const files = [];
    const filesInDir = getFilesInDirectory(dirPath);

    filesInDir.forEach(file => {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);

        if (stats.isDirectory()) {
            const subFiles = getFilesInDirectoryWithExtensionRecursive(filePath, extension);
            files.push(...subFiles);
        } else if (path.extname(file) === extension) {
            files.push(filePath);
        }
    });

    return files;
}

module.exports = {
    createFile,
    createDirectory,
    fileExists,
    directoryExists,
    readFile,
    getFileExtension,
    getFileName,
    getFileNameWithoutExtension,
    getFilePath,
    getFilesInDirectory,
    getFilesInDirectoryRecursive,
    getDirectoriesInDirectory,
    getDirectoriesInDirectoryRecursive,
    getFilesInDirectoryWithExtension,
    getFilesInDirectoryWithExtensionRecursive
};
