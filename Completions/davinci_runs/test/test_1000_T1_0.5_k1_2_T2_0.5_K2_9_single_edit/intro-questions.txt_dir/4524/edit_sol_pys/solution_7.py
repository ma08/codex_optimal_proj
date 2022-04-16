#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import re

def get_file_list(path):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list(f))
        else:
            files.append(f)
    return files

def get_file_list_re(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re2(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re2(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re3(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re3(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re4(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re4(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re5(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re5(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re6(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re6(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re7(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re7(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re8(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re8(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re9(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re9(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re10(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re10(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re11(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re11(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re12(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re12(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re13(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re13(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re14(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re14(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re15(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            files.extend(get_file_list_re15(f, re_str))
        else:
            if re.search(re_str, f):
                files.append(f)
    return files

def get_file_list_re16(path, re_str):
    files = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
       
