#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    file_name = "test.txt"
    file_path = "./"
    file_full_path = os.path.join(file_path, file_name)
    if os.path.exists(file_full_path):
        print("{} exists".format(file_full_path))
    else:
        print("{} doesn't exist".format(file_full_path))

    print("{} is a file: {}".format(file_full_path, os.path.isfile(file_full_path)))
    print("{} is a directory: {}".format(file_full_path, os.path.isdir(file_full_path)))
    print("{} is a link: {}".format(file_full_path, os.path.islink(file_full_path)))
    print("{} is absolute path: {}".format(file_full_path, os.path.isabs(file_full_path)))


if __name__ == '__main__':
    main()
