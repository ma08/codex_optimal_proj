#!/usr/bin/env python3

import sys
import os


def file_exists(file):
    """
    Checks if a file exists and is accessible.
    :param file:
    :return:
    """
    if not os.path.exists(file):
        print("Error: File does not exist.")
        sys.exit(1)


def file_is_empty(file):
    """
    Checks if a file is empty
    :param file:
    :return:
    """
    if os.path.getsize(file) == 0:
        print("Error: File is empty.")
        sys.exit(1)


def file_is_readable(file):
    """
    Checks if a file is readable.
    :param file:
    :return:
    """
    if not os.access(file, os.R_OK):
        print("Error: File is not readable.")
        sys.exit(1)


def file_is_writable(file):
    """
    Checks if a file is writable.
    :param file:
    :return:
    """
    if not os.access(file, os.W_OK):
        print("Error: File is not writable.")
        sys.exit(1)


def file_is_executable(file):
    """
    Checks if a file is executable.
    :param file:
    :return:
    """
    if not os.access(file, os.X_OK):
        print("Error: File is not executable.")
        sys.exit(1)


def file_is_regular(file):
    """
    Checks if a file is a regular file.
    :param file:
    :return:
    """
    if not os.path.isfile(file):
        print("Error: File is not a regular file.")
        sys.exit(1)


def file_is_directory(file):
    """
    Checks if a file is a directory.
    :param file:
    :return:
    """
    if not os.path.isdir(file):
        print("Error: File is not a directory.")
        sys.exit(1)


def file_is_symlink(file):
    """
    Checks if a file is a symlink.
    :param file:
    :return:
    """
    if not os.path.islink(file):
        print("Error: File is not a symlink.")
        sys.exit(1)


def file_is_socket(file):
    """
    Checks if a file is a socket.
    :param file:
    :return:
    """
    if not os.path.exists(file):
        print("Error: File is not a socket.")
        sys.exit(1)
