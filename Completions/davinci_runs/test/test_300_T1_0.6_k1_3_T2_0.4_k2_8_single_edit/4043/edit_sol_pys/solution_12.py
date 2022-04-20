#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re



class File(object):
    """
    """

    def __init__(self, path):
        """
        """
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.extension = os.path.splitext(path)[1]
        self.mime = self.get_mime(self.extension)

    def get_mime(self, extension):
        """
        """
        mimes = {
            '.txt': 'text/plain',
            '.pdf': 'application/pdf',
            '.doc': 'application/msword',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.xls': 'application/vnd.ms-excel',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.zip': 'application/zip',
            '.rar': 'application/x-rar-compressed',
            '.tar': 'application/x-tar',
            '.7z': 'application/x-7z-compressed',
            '.gz': 'application/gzip',
            '.bz2': 'application/x-bzip2'
        }
        return mimes.get(extension, 'application/octet-stream')


class Directory(object):
    """
    """

    def __init__(self, path):
        """
        """
        self.path = path
        self.name = os.path.basename(path)
        self.size = self.get_size(path)
        self.files = self.get_files(path)

    def get_size(self, path):
        """
        """
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

    def get_files(self, path):
        """
        """
        files = []
        for root, dirs, files in os.walk(path):
            for name in files:
                files.append(File(os.path.join(root, name)))
        return files


class FileManager(object):
    """
    """

    def __init__(self, path):
        """
        """
        self.path = path
        self.name = os.path.basename(path)
        self.size = self.get_size(path)
        self.directories = self.get_directories(path)
        self.files = self.get_files(path)

    def get_size(self, path):
        """
        """
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

    def get_directories(self, path):
        """
        """
        directories = []
        for root, dirs, files in os.walk(path):
            for name in dirs:
                directories.append(Directory(os.path.join(root, name)))
        return directories

    def get_files(self, path):
        """
        """
        files = []
        for root, dirs, files in os.walk(path):
            for name in files:
                files.append(File(os.path.join(root, name)))
        return files


def main():
    """
    """
    print(FileManager('/home/lucas/Documents/'))


if __name__ == '__main__':
    main()
