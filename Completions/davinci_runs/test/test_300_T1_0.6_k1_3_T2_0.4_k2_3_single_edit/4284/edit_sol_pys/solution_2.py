

# -------------------------------------------------------------------------------
# Name:        file
# Purpose:     Обработка файлов
#
# Author:      v.osipov
#
# Created:     16/10/2018
# Copyright:   (c) v.osipov 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import os
import sys
import shutil
import re


def read_file(path):
    """
    Чтение файла
    :param path: путь к файлу
    :return: содержимое файла
    """
    with open(path) as f:
        return f.read()


def write_file(path, content):
    """
    Запись в файл
    :param path: путь к файлу
    :param content: содержимое файла
    :return:
    """
    with open(path, 'w') as f:
        f.write(content)


def copy_file(path, new_path):
    """
    Копирование файла
    :param path: путь к файлу
    :param new_path: путь к новому файлу
    :return:
    """
    shutil.copy(path, new_path)


def get_file_name(path):
    """
    Получение имени файла
    :param path: путь к файлу
    :return: имя файла
    """
    return os.path.basename(path)


def get_file_ext(path):
    """
    Получение расширения файла
    :param path: путь к файлу
    :return: расширение файла
    """
    return os.path.splitext(path)[1]


def get_file_size(path):
    """
    Получение размера файла
    :param path: путь к файлу
    :return: размер файла
    """
    return os.path.getsize(path)


def get_file_list(path):
    """
    Получение списка файлов в директории
    :param path: путь к директории
    :return: список файлов
    """
    return os.listdir(path)


def get_dir_list(path):
    """
    Получение списка поддиректорий в директории
    :param path: путь к директории
    :return: список поддиректорий
    """
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]


def get_file_list_recursive(path):
    """
    Получение списка файлов в директории с учетом поддиректорий
    :param path: путь к директории
    :return: список файлов
    """
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            result.append(os.path.join(root, name))
    return result


def get_dir_list_recursive(path):
    """
    Получение списка поддиректорий в директории с учетом поддиректорий
    :param path: путь к директории
    :return: список поддиректорий
    """
    result = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            result.append(os.path.join(root, name))
    return result


def get_file_list_by_ext(path, ext):
    """
    Получение списка файлов в директории по расширению
    :param path: путь к директории
    :param ext: расширение файла
    :return: список файлов
    """
    return [name for name in os.listdir(path) if os.path.splitext(name)[1] == ext]


def get_file_list_by_ext_recursive(path, ext):
    """
    Получение списка файлов в директории по расширению с учетом поддиректорий
    :param path: путь к директории
    :param ext: расширение файла
    :return: список файлов
    """
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[1] == ext:
                result.append(os.path.join(

if __name__ == '__main__':
    main()
