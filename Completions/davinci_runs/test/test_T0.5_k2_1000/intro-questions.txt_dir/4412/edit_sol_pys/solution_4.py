#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def main():
    """
    main function
    """
    # get the current working directory
    cwd = os.getcwd()
    # get the directory name
    dir_name = os.path.basename(cwd)
    # get the file name
    file_name = os.path.basename(sys.argv[0])
    # print out the directory name and the file name
    print("Directory name: " + dir_name + "\n")
    print("File name: " + file_name + "\n")


if __name__ == "__main__":
    main()
