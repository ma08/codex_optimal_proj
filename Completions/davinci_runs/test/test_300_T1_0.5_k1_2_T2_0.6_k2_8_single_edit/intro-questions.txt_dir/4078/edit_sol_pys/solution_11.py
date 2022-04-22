#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: file.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 1/15/2020 11:19

import os


def read_file(file_name):
    f = open(file_name, 'r')
    print(f.read())
    f.close()


def write_file(file_name):
    f = open(file_name, 'w')
    f.write('Hello, world!')
    f.close()


def append_file(file_name):
    f = open(file_name, 'a')
    f.write('Hello, world!')
    f.close()


def read_file_line(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line.strip())  # 把末尾的'\n'删掉


def check_file(file_name):
    if os.path.exists(file_name):
        print('exists')
    else:
        print('not exists')


def remove_file(file_name):
    os.remove(file_name)


def rename_file(old_file_name, new_file_name):
    os.rename(old_file_name, new_file_name)


def get_file_size(file_name):
    size = os.path.getsize(file_name)
    print(size)


def list_dir(dir_name):
    for file_name in os.listdir(dir_name):
        print(file_name)


def main():
    # read_file('file.txt')
    # write_file('file.txt')
    # append_file('file.txt')
    read_file_line('file.txt')
    # check_file('file.txt')
    # remove_file('file.txt')
    # rename_file('file.txt', 'file1.txt')
    # get_file_size('file1.txt')
    # list_dir('.')


if __name__ == '__main__':
    main()
