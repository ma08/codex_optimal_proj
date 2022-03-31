#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time


def get_file_list(dir_name):
    file_list = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_file_info(file_name):
    file_info = {}
    file_info['name'] = file_name
    file_info['size'] = os.path.getsize(file_name)
    file_info['ctime'] = time.ctime(os.path.getctime(file_name))
    file_info['mtime'] = time.ctime(os.path.getmtime(file_name))
    return file_info


def print_file_info(file_info):
    print('name:', file_info['name'])
    print('size:', file_info['size'])
    print('ctime:', file_info['ctime'])
    print('mtime:', file_info['mtime'])


def main():
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], 'dir_name')
        sys.exit(1)

    dir_name = sys.argv[1]
    file_list = get_file_list(dir_name)
    for file in file_list:
        file_info = get_file_info(file)
        print_file_info(file_info)


if __name__ == '__main__':
    main()
