#!/usr/bin/python

import os
import sys
import argparse
from argparse import RawTextHelpFormatter


class File:
    def __init__(self, file_name, file_path, file_extension):
        self.file_name = file_name
        self.file_path = file_path
        self.file_extension = file_extension
        self.file_full_path = os.path.join(file_path, file_name)
        self.file_size = os.stat(self.file_full_path).st_size

    def __str__(self):
        return '{} {} {} {}'.format(self.file_name, self.file_path, self.file_size, self.file_extension)

    def __repr__(self):
        return '{} {} {} {}'.format(self.file_name, self.file_path, self.file_size, self.file_extension)


def get_file_list(path, extension):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_list.append(File(file, root, extension))
    return file_list


def print_files(file_list):
    for file in file_list:
        print(file)


def print_files_size(file_list):
    for file in file_list:
        print(file.file_size)


def print_files_size_sum(file_list):
    size_sum = 0
    for file in file_list:
        size_sum += file.file_size
    print(size_sum)


def print_files_size_avg(file_list):
    size_sum = 0
    for file in file_list:
        size_sum += file.file_size
    print(size_sum / len(file_list))


def print_files_size_max(file_list):
    size_max = 0
    for file in file_list:
        if file.file_size > size_max:
            size_max = file.file_size
    print(size_max)


def print_files_size_min(file_list):
    size_min = sys.maxsize
    for file in file_list:
        if file.file_size < size_min:
            size_min = file.file_size
    print(size_min)


def print_files_size_max_file(file_list):
    size_max = 0
    max_file = None
    for file in file_list:
        if file.file_size > size_max:
            max_file = file
            size_max = file.file_size
    print(max_file)


def print_files_size_min_file(file_list):
    size_min = sys.maxsize
    min_file = None
    for file in file_list:
        if file.file_size < size_min:
            min_file = file
            size_min = file.file_size
    print(min_file)


def print_files_size_median(file_list):
    file_list.sort(key=lambda x: x.file_size)
    print(file_list[int(len(file_list) / 2)])


def main():
    parser = argparse.ArgumentParser(description='Prints files in the specified path and extension',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-p', '--path', type=str, help='Path to search for files in')
    parser.add_argument('-e', '--extension', type=str, help='File extension to search for')
    parser.add_argument('-m', '--mode', type=str, help='Print mode',
                        choices=['all', 'size', 'size_sum', 'size_avg', 'size_max', 'size_min', 'size_max_file',
                                 'size_min_file', 'size_median'])

    args = parser.parse_args()

    if not args.path or not args.extension or not args.mode:
        parser.print_help()
        sys.exit(1)

    file_list = get_file_list(args.path, args.extension)

    if args.mode == 'all':
        print_files(file_list)
    elif args.mode == 'size':
        print_files_size(file_list)
    elif args.mode == 'size_sum':
        print_files_size_sum(file_list)
    elif args.mode == 'size_avg':
        print_files_size_avg(file_list)
    elif args.mode == 'size_max':
        print_files_size_max(file_list)
    elif args.mode == 'size_min':
        print_files_size_min(file_list)
    elif args.mode == 'size_max_file':
        print_files_size_max_file(file_list)
    elif args.mode == 'size_min_file':
        print_files_size_min_file(file_list)
    elif args.mode == 'size_median':
        print_files_size_median(file_list)


if __name__ == '__main__':
    main()
