#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re


class File(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = os.path.abspath(file_name)
        self.file_size = os.path.getsize(self.file_path)
        self.file_type = self.file_name.split('.')[-1]

    def get_file_name(self):
        return self.file_name

    def get_file_path(self):
        return self.file_path

    def get_file_size(self):
        return self.file_size

    def get_file_type(self):
        return self.file_type

    def get_file_content(self):
        file_content = ''
        try:
            with open(self.file_path, 'r') as f:
                file_content = f.read()
        except Exception as e:
            print(e)
        return file_content


class FileManager(object):
    def __init__(self, path):
        self.path = path
        self.file_list = self.__get_file_list(path)

    def __get_file_list(self, path):
        file_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def get_file_list(self):
        return self.file_list

    def get_file_list_by_type(self, file_type):
        file_list = []
        for file in self.file_list:
            if file.split('.')[-1] == file_type:
                file_list.append(file)
        return file_list

    def get_file_list_by_size(self, size):
        file_list = []
        for file in self.file_list:
            if os.path.getsize(file) > size:
                file_list.append(file)
        return file_list

    def get_file_list_by_keyword(self, keyword):
        file_list = []
        for file in self.file_list:
            if re.search(keyword, file):
                file_list.append(file)
        return file_list


if __name__ == '__main__':
    file_manager = FileManager('.')
    file_list = file_manager.get_file_list_by_keyword('file')
    for file in file_list:
        print(file)
