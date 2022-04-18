#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 下午9:39
# @Author  : Hou Rong
# @Site    : 
# @File    : file.py
# @Software: PyCharm
import os
import io


def get_file_content(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()


def save_file_content(filename, content):
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
