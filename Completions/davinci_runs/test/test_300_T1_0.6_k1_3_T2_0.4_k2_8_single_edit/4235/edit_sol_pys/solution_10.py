#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import urllib
import urllib2
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取文件列表
def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


# 获取文件内容
def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


# 写入文件内容
def write_file_content(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


# 获取文件名
def get_file_name(file_path):
    return os.path.basename(file_path)


# 获取文件后缀名
def get_file_type(file_path):
    return os.path.splitext(file_path)[1]


# 获取文件大小
def get_file_size(file_path):
    return os.path.getsize(file_path)


# 获取文件修改时间
def get_file_mtime(file_path):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))


# 获取文件创建时间
def get_file_ctime(file_path):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(file_path)))


# 获取文件访问时间
def get_file_atime(file_path):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getatime(file_path)))


# 获取文件绝对路径
def get_file_absolute_path(file_path):
    return os.path.abspath(file_path)


# 获取文件相对路径
def get_file_relative_path(file_path):
    return os.path.relpath(file_path)


# 判断文件是否存在
def is_file_exists(file_path):
    return os.path.exists(file_path)


# 判断文件是否可读
def is_file_readable(file_path):
    return os.access(file_path, os.R_OK)


# 判断文件是否可写
def is_file_writable(file_path):
    return os.access(file_path, os.W_OK)


# 判断文件是否可执行
def is_file_executable(file_path):
    return os.access(file_path, os.X_OK)


# 判断文件是否是绝对路径
def is_file_absolute_path(file_path):
    return os.path.isabs(file_path)


# 判断文件是否是目录
def is_file_directory(file_path):
    return os.path.isdir(file_path)


# 判断文件是否是文件
def is_file_file(file_path):
    return os.path.isfile(file_path)


# 判断文件是否是链接文件
def is_file_link(file_path):
    return os.path.islink(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)


# 判断文件是否是组合文件
def is_file_mount(file_path):
    return os.path.ismount(file_path)
