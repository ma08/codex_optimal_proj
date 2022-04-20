

#-------------------------------------------------------------------------------
# Name:        file
# Purpose:
#
# Author:      v.osipov, k.kuklin
#
# Created:     16/10/2018
# Copyright:   (c) v.osipov, k.kuklin 2018
import os
import sys
import argparse
import shutil
import time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', nargs='?', default=os.getcwd())
    parser.add_argument('-d', '--destination', nargs='?', default=os.getcwd())
    parser.add_argument('-n', '--name', nargs='?', default='')
    parser.add_argument('-t', '--type', nargs='?', default='file')
    return parser


def get_list(path):
    list_of_files = os.listdir(path)
    return list_of_files


def get_file_list(path):
    list_of_files = get_list(path)
    file_list = []
    for file in list_of_files:
        if os.path.isfile(os.path.join(path, file)):
            file_list.append(file)
    return file_list


def get_dir_list(path):
    list_of_files = get_list(path)
    dir_list = []
    for dir in list_of_files:
        if os.path.isdir(os.path.join(path, dir)):
            dir_list.append(dir)
    return dir_list


def get_file_ext(file_name):
    return os.path.splitext(file_name)[1]


def get_file_name(file_name):
    return os.path.splitext(file_name)[0]


def copy_files(source, destination, file_list):
    for file in file_list:
        shutil.copy(os.path.join(source, file), destination)


def copy_dirs(source, destination, dir_list):
    for dir in dir_list:
        shutil.copytree(os.path.join(source, dir), os.path.join(destination, dir))


def copy_file(source, destination, file_name):
    shutil.copy(os.path.join(source, file_name), destination)


def copy_dir(source, destination, dir_name):
    shutil.copytree(os.path.join(source, dir_name), os.path.join(destination, dir_name))


def copy_files_by_ext(source, destination, file_list, ext):
    for file in file_list:
        if get_file_ext(file) == ext:
            copy_file(source, destination, file)


def copy_files_by_name(source, destination, file_list, name):
    for file in file_list:
        if get_file_name(file) == name:
            copy_file(source, destination, file)


def copy_dirs_by_name(source, destination, dir_list, name):
    for dir in dir_list:
        if dir == name:
            copy_dir(source, destination, dir)


def copy_by_ext(source, destination, ext):
    file_list = get_file_list(source)
    copy_files_by_ext(source, destination, file_list, ext)


def copy_by_name(source, destination, name):
    file_list = get_file_list(source)
    dir_list = get_dir_list(source)
    copy_files_by_name(source, destination, file_list, name)
    copy_dirs_by_name(source, destination, dir_list, name)


def copy_all(source, destination):
    file_list = get_file_list(source)
    dir_list = get_dir_list(source)
    copy_files(source, destination, file_list)
    copy_dirs(source, destination, dir_list)


def copy_file_by_time(source, destination, file_name, time_delta):
    if time.time() - os.path.getmtime(os.path.join(source, file_name)) < time_delta:
        copy_file(source, destination, file_name)


def copy_dir_by_time(source, destination, dir_name, time_delta):
    if time.time() - os.path.getmtime(os.path.join(source, dir_name)) < time_delta:
        copy_dir(source, destination, dir_name)


def copy_by_time(source, destination, time_delta):
    file_list = get_file_list(source)
    dir_list = get_dir_list(source)
    for file in file_list:
        copy_file_by_time(source, destination, file, time_delta)
    for dir in dir_list:
        copy_dir_by_time(source, destination, dir, time_delta)

# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.type == 'file':
        if namespace.name:
            copy_by_name(namespace.source, namespace.destination, namespace.name)
        else:
            copy_all(namespace.source, namespace.destination)
    elif namespace.type == 'dir':
        if namespace.name:
            copy_dirs_by_name(namespace.source, namespace.destination, get_dir_list(namespace.source), namespace.name)
        else:
            copy_dirs(namespace.source, namespace.destination, get_dir_list(namespace.source))
    elif namespace.type == 'ext':
        copy_by_ext(namespace.source, namespace.destination, namespace.name)
    elif namespace.type == 'time':
        copy_by_time(namespace.source, namespace.destination, namespace.name)
    else:
        print('Error')


if __name__ == '__main__':
    main()
