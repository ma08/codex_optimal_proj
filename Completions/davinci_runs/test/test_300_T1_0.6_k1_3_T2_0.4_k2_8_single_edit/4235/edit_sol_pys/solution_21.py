# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:08:06 2018

@author: luolei

文件读写
"""
import os
import shutil


def file_read(file_path):
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容
    """
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def file_write(file_path, content):
    """
    写入文件内容
    :param file_path: 文件路径
    :param content: 文件内容
    :return:
    """
    with open(file_path, 'w') as f:
        f.write(content)


def file_append(file_path, content):
    """
    追加文件内容
    :param file_path: 文件路径
    :param content: 文件内容
    :return:
    """
    with open(file_path, 'a') as f:
        f.write(content)


def file_copy(src_file_path, dst_file_path):
    """
    复制文件
    :param src_file_path: 源文件路径
    :param dst_file_path: 目标文件路径
    :return:
    """
    shutil.copyfile(src_file_path, dst_file_path)


def file_move(src_file_path, dst_file_path):
    """
    移动文件
    :param src_file_path: 源文件路径
    :param dst_file_path: 目标文件路径
    :return:
    """
    shutil.move(src_file_path, dst_file_path)


def file_delete(file_path):
    """
    删除文件
    :param file_path: 文件路径
    :return:
    """
    os.remove(file_path)


def file_rename(src_file_path, dst_file_path):
    """
    重命名文件
    :param src_file_path: 源文件路径
    :param dst_file_path: 目标文件路径
    :return:
    """
    os.rename(src_file_path, dst_file_path)


def file_create(file_path):
    """
    创建文件
    :param file_path: 文件路径
    :return:
    """
    with open(file_path, 'w') as f:
        pass


def file_create_dir(dir_path):
    """
    创建文件夹
    :param dir_path: 文件夹路径
    :return:
    """
    os.makedirs(dir_path)


def file_delete_dir(dir_path):
    """
    删除文件夹
    :param dir_path: 文件夹路径
    :return:
    """
    shutil.rmtree(dir_path)


def file_rename_dir(src_dir_path, dst_dir_path):
    """
    重命名文件夹
    :param src_dir_path: 源文件夹路径
    :param dst_dir_path: 目标文件夹路径
    :return:
    """
    os.rename(src_dir_path, dst_dir_path)


def file_list_dir(dir_path):
    """
    获取文件夹下所有文件
    :param dir_path: 文件夹路径
    :return:
    """
    file_list = os.listdir(dir_path)
    return file_list


def file_is_exist(file_path):
    """
    判断文件是否存在
    :param file_path: 文件路径
    :return:
    """
    return os.path.exists(file_path)


if __name__ == '__main__':
    pass
