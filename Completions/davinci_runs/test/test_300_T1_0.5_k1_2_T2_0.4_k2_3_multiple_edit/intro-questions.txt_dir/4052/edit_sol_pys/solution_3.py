#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 下午3:43
# @Author  : Aries
# @Site    : 
# @File    : file.py
# @Software: PyCharm
import os
import sys


def file_read(filename):
    """
    文件读取
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    print(f.read())
    f.close()


def file_write(filename, content):
    """
    文件写入
    :param filename:
    :param content:
    :return:
    """
    f = open(filename, 'w')
    f.write(content)
    f.close()


def file_append(filename, content):
    """
    文件追加
    :param filename:
    :param content:
    :return:
    """
    f = open(filename, 'a')
    f.write(content)
    f.close()


def file_read_line(filename):
    """
    文件读取每一行
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    for line in f.readlines():
        print(line.strip())
    f.close()


def file_read_line_by_line(filename):
    """
    文件读取一行一行
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    for line in f:
        print(line.strip())
    f.close()


def file_read_line_by_line_with_open_close(filename):
    """
    文件读取一行一行，每次读取一行就关闭文件，每次读取一行就打开文件
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    for line in f:
        print(line.strip())
        f.close()
        f = open(filename, 'r')
    f.close()


def file_read_line_by_line_with_open_close_2(filename):
    """
    文件读取一行一行，每次读取一行就关闭文件，每次读取一行就打开文件
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())


def file_read_line_by_line_with_open_close_3(filename):
    """
    文件读取一行一行，每次读取一行就关闭文件，每次读取一行就打开文件
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line.strip())


def file_read_line_by_line_with_open_close_4(filename):
    """
    文件读取一行一行，每次读取一行就关闭文件，每次读取一行就打开文件
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())
            f.close()
            f = open(filename, 'r')
        f.close()


if __name__ == '__main__':
    filename = '/Users/houruixiang/Documents/GitHub/python-study/file/test.txt'
    # file_read(filename)
    # file_write(filename, '\nhello world')
    # file_append(filename, '\nhello world')
    # file_read_line(filename)
    # file_read_line_by_line(filename)
    # file_read_line_by_line_with_open_close(filename)
    # file_read_line_by_line_with_open_close_2(filename)
    # file_read_line_by_line_with_open_close_3(filename)
    file_read_line_by_line_with_open_close_4(filename)
