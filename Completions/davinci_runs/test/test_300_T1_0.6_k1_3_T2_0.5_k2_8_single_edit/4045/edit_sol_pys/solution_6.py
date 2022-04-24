#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import sys


def file_type(file_name):
    """
    get the file type

    :param file_name:
    :return:
    """
    return file_name.split('.')[-1]


def file_name(file_path):
    """
    get the file name

    :param file_path:
    :return:
    """
    return file_path.split('/')[-1]


def file_path(file_path):
    """
    get the file path

    :param file_path:
    :return:
    """
    return file_path.split(file_name(file_path))[0]


def file_exist(file_path):
    """
    check if the file exist

    :param file_path:
    :return:
    """
    return os.path.exists(file_path)


def file_size(file_path):
    """
    get the file size

    :param file_path:
    :return:
    """
    return os.path.getsize(file_path)


def file_create(file_path):
    """
    create a file

    :param file_path:
    :return:
    """
    file_object = open(file_path, 'w')
    file_object.close()


def file_create_dir(dir_path):
    """
    create a directory

    :param dir_path:
    :return:
    """
    os.makedirs(dir_path)


def file_delete(file_path):
    """
    delete a file

    :param file_path:
    :return:
    """
    os.remove(file_path)


def file_delete_dir(dir_path):
    """
    delete a directory

    :param dir_path:
    :return:
    """
    os.removedirs(dir_path)


def file_rename(file_path, new_file_path):
    """
    rename a file

    :param file_path:
    :param new_file_path:
    :return:
    """
    os.rename(file_path, new_file_path)


def file_copy(file_path, new_file_path):
    """
    copy a file

    :param file_path:
    :param new_file_path:
    :return:
    """
    os.system('cp %s %s' % (file_path, new_file_path))


def file_list(dir_path):
    """
    get a file list in the directory

    :param dir_path:
    :return:
    """
    return os.listdir(dir_path)


def file_read(file_path):
    """
    read a file

    :param file_path:
    :return:
    """
    file_object = open(file_path, 'r')
    file_content = file_object.read()
    file_object.close()
    return file_content


def file_write(file_path, content):
    """
    write a file

    :param file_path:
    :param content:
    :return:
    """
    file_object = open(file_path, 'w')
    file_object.write(content)
    file_object.close()


def file_append(file_path, content):
    """
    append a file

    :param file_path:
    :param content:
    :return:
    """
    file_object = open(file_path, 'a')
    file_object.write(content)
    file_object.close()


def file_search(file_path, keyword):
    """
    search a keyword in a file

    :param file_path:
    :param keyword:
    :return:
    """
    return os.system('grep %s %s' % (keyword, file_path))


def file_search_all(dir_path, keyword):
    """
    search a keyword in all files in the directory

    :param dir_path:
    :param keyword:
    :return:
    """
    return os.system('grep -rnw %s -e %s' % (dir_path, keyword))


def file_search_all_recursive(dir_path, keyword):
    """
    search a keyword in all files in the directory recursively

    :param dir_path:
    :param keyword:
    :return:
    """
    return os.system('grep -rwn %s -e %s' % (dir_path, keyword))


if __name__ == '__main__':
    print file_type(sys.argv[1])
    print file_name(sys.argv[1])
    print file_path(sys.argv[1])
    print file_exist(sys.argv[1])
    print file_size(sys.argv[1])
    print file_create(sys.argv[1] + '.test')
    print file_create_dir(sys.argv[1] + '.test')
    print file_delete(sys.argv[1] + '.test')
    print file_delete_dir(sys.argv[1] + '.test')
    print file_rename(sys.argv[1], sys.argv[1] + '.test')
    print file_copy(sys.argv[1], sys.argv[1] + '.test')
    print file_list(sys.argv[1])
    print file_read(sys.argv[1])
    print file_write(sys.argv[1] + '.test', 'test')
    print file_append(sys.argv[1] + '.test', 'test')
    print file_search(sys.argv[1], 'test')
    print file_search_all(sys.argv[1], 'test')
    print file_search_all_recursive(sys.argv[1], 'test')
