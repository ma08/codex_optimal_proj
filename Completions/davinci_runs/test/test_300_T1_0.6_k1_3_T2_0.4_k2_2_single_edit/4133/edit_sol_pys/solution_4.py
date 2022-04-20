#!/usr/bin/env python3

import sys
import os
import re

def main():
    print("file.py:")
    print(sys.argv)
    if len(sys.argv) == 1:
        print("Usage: ./file.py file ...")
        sys.exit(1)
    for i in range(1, len(sys.argv)):
        if not os.path.isfile(sys.argv[i]):
            print(sys.argv[i] + ": No such file")
            sys.exit(1)
        if not os.access(sys.argv[i], os.R_OK):
            print(sys.argv[i] + ": Permission denied")
            sys.exit(1)
        print(sys.argv[i] + ":", end = " ")
        if re.search(r"^#!.*\bpython[0-9.]*\b", open(sys.argv[i]).readline()):
            print("python script, ASCII text executable")
        else:
            print("ASCII text")

if __name__ == "__main__":
    main()
