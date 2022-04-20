#!/usr/bin/python3

import os
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: ./file.py <file>")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("{} does not exist".format(sys.argv[1]))
        sys.exit(1)
    if os.path.isdir(sys.argv[1]):
        print("{} is a directory".format(sys.argv[1]))
        sys.exit(1)
    if os.access(sys.argv[1], os.R_OK):
        print("{} is readable".format(sys.argv[1]))
    if os.access(sys.argv[1], os.W_OK):
        print("{} is writable".format(sys.argv[1]))
    if os.access(sys.argv[1], os.X_OK):
        print("{} is executable".format(sys.argv[1]))
    if os.path.isfile(sys.argv[1]):
        print("{} is a file".format(sys.argv[1]))
    if os.path.islink(sys.argv[1]):
        print("{} is a symbolic link".format(sys.argv[1]))
    if os.path.isfifo(sys.argv[1]):
        print("{} is a named pipe".format(sys.argv[1]))
    if os.path.ismount(sys.argv[1]):
        print("{} is a mount point".format(sys.argv[1]))
    if os.path.isabs(sys.argv[1]):
        print("{} is an absolute path".format(sys.argv[1]))
    if os.path.isdir(sys.argv[1]):
        print("{} is a directory".format(sys.argv[1]))
    if os.path.isabs(sys.argv[1]):
        print("{} is an absolute path".format(sys.argv[1]))
    if os.path.ismount(sys.argv[1]):
        print("{} is a mount point".format(sys.argv[1]))
    if os.path.isfifo(sys.argv[1]):
        print("{} is a named pipe".format(sys.argv[1]))
    if os.path.islink(sys.argv[1]):
        print("{} is a symbolic link".format(sys.argv[1]))
    if os.path.isfile(sys.argv[1]):
        print("{} is a file".format(sys.argv[1]))
    if os.access(sys.argv[1], os.X_OK):
        print("{} is executable".format(sys.argv[1]))
    if os.access(sys.argv[1], os.W_OK):
        print("{} is writable".format(sys.argv[1]))
    if os.access(sys.argv[1], os.R_OK):
        print("{} is readable".format(sys.argv[1]))


if __name__ == "__main__":
    main()
