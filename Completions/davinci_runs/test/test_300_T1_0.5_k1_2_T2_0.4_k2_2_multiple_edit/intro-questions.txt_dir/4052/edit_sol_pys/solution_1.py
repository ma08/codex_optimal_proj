#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:30:37 2017

@author: ycan
"""

from os import listdir
import os
import sys
import re
from os.path import isfile, join
from shutil import copyfile


def copy_files(path, target):
    """
    Copy files from path to target.

    Parameters
    ----------
    path : str
        Path to copy files from.
    target : str
        Path to copy files to.
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        copyfile(path+f, target+f)


def rename_files(path, target):
    """
    Rename files in path to the format target.

    Parameters
    ----------
    path : str
        Path to rename files from.
    target : str
        Target filename format.
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        os.rename(path+f, path+target.format(f))


def rename_files_by_regex(path, target, regex):
    """
    Rename files in path to the format target using regex.

    Parameters
    ----------
    path : str
        Path to rename files from.
    target : str
        Target filename format.
    regex : str
        Regex to extract the filename.
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        m = re.search(regex, f)
        if m:
            os.rename(path + f, path + target.format(m.group(1)))
        else:
            print("No match for {}".format(f))


def main(argv):
    """
    Main function.

    Parameters
    ----------
    argv : list
        List of arguments.
    """
    if len(argv) < 2:
        print("Please provide the path to the files to be renamed.")
        return
    path = argv[1]
    if path[-1] != '/':
        path += '/'
    if len(argv) < 3:
        print("Please provide the target filename format.")
        return
    target = argv[2]
    if len(argv) < 4:
        print("Please provide the regex to extract the filename.")
        return
    regex = argv[3]
    rename_files_by_regex(path, target, regex)


if __name__ == "__main__":
    main(sys.argv)
