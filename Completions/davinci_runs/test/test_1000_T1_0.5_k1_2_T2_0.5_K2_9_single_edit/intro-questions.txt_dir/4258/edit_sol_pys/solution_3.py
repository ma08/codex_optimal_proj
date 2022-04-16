#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
file: file.py

Description: file object for working with files in the file system

author: Yoann Dupont

MIT License

Copyright (c) 2018 Yoann Dupont

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import codecs

class File(object):
    def __init__(self, file):
        self.file = file
        self.path = os.path.abspath(file)
        self.name = os.path.basename(file)
        self.dir = os.path.dirname(file)
        self.is_dir = os.path.isdir(file)
        self.is_file = os.path.isfile(file)
        self.is_link = os.path.islink(file)
        self.is_abs = os.path.isabs(file)
        self.is_hidden = self.name.startswith(".")
        self.stat = os.stat(file)
        self.size = self.stat.st_size
    
    def __str__(self):
        return self.file
    __repr__ = __str__
    
    def __eq__(self, other):
        return self.path == other.path
    
    def __hash__(self):
        return hash(self.path)
    
    def __getitem__(self, key):
        if key == "path":
            return self.path
        elif key == "name":
            return self.name
        elif key == "dir":
            return self.dir
        elif key == "is_dir":
            return self.is_dir
        elif key == "is_file":
            return self.is_file
        elif key == "is_link":
            return self.is_link
        elif key == "is_abs":
            return self.is_abs
        elif key == "is_hidden":
            return self.is_hidden
        elif key == "stat":
            return self.stat
        elif key == "size":
            return self.size
        else:
            raise KeyError("File object has no attribute '%s'" % key)
    
    def __setitem__(self, key, value):
        if key == "path":
            self.path = value
        elif key == "name":
            self.name = value
        elif key == "dir":
            self.dir = value
        elif key == "is_dir":
            self.is_dir = value
        elif key == "is_file":
            self.is_file = value
        elif key == "is_link":
            self.is_link = value
        elif key == "is_abs":
            self.is_abs = value
        elif key == "is_hidden":
            self.is_hidden = value
        elif key == "stat":
            self.stat = value
        elif key == "size":
            self.size = value
        else:
            raise KeyError("File object has no attribute '%s'" % key)
    
    def __contains__(self, key):
        if key == "path":
            return True
        elif key == "name":
            return True
        elif key == "dir":
            return True
        elif key == "is_dir":
            return True
        elif key == "is_file":
            return True
        elif key == "is_link":
            return True
        elif key == "is_abs":
            return True
        elif key == "is_hidden":
            return True
        elif key == "stat":
            return True
        elif key == "size":
            return True
        else:
            return False
    
    def __iter__(self):
        return iter(["path", "name", "dir", "is_dir", "is_file", "is_link", "is_abs", "is_hidden", "stat", "size"])
    
    def __len__(self):
        return 10
    
    def __delitem__(self, key):
        raise NotImplementedError("File object has no attribute '%s'" % key)
    
    def __delattr__(self, key):
        raise NotImplementedError("File object has no attribute '%s'" % key)
    
    def __getattr__(self, key):
        if key == "path":
            return self.path
        elif key == "name":
            return self.name
        elif key == "dir":
            return self.dir
        elif key == "is_dir":
            return self.is_dir
        elif key == "is_file":
            return self.is_file
        elif key == "is_link":
            return self.is_link
        elif key == "is_abs":
            return self.is_abs
        elif key == "is_hidden":
            return self.is_hidden
        elif key == "stat":
            return self.stat
        elif key == "size":
            return self.size
        else:
            raise AttributeError("File object has no attribute '%s'" % key)
    
    def __setattr__(self, key, value):
        if key == "path":
            self.__dict__["path"] = value
        elif key == "name":
            self.__dict__["name"] = value
        elif key == "dir":
            self.__dict__["dir"] = value
        elif key == "is_dir":
            self.__dict__["is_dir"] = value
        elif key == "is_file":
            self.__dict__["is_file"] = value
        elif key == "is_link":
            self.__dict__["is_link"] = value
        elif key == "is_abs":
            self.__dict__["is_abs"] = value
        elif key == "is_hidden":
            self.__dict__["is_hidden"] = value
        elif key == "stat":
            self.__dict__["stat"] = value
        elif key == "size":
            self.__dict__["size"] = value
        else:
            raise AttributeError("File object has no attribute '%s'" % key)
    
    def open(self, mode="r", encoding="utf-8"):
        return codecs.open(self.file, mode, encoding)
