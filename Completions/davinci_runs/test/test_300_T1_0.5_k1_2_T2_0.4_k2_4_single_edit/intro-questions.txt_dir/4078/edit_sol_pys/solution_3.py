#!/usr/bin/env python3

import os
import sys
import re

def main():
    file = sys.argv[1]
    if os.path.isfile(file):
        print('{} is a file'.format(file))
        if os.access(file, os.R_OK):
            print('{} is a readable'.format(file))
        else:
            print('{} is not a readable'.format(file))
        if os.access(file, os.W_OK):
            print('{} is a writable'.format(file))
        else:
            print('{} is not a writable'.format(file))
        if os.access(file, os.X_OK):
            print('{} is a executable'.format(file))
        else:
            print('{} is not a executable'.format(file))
    else:
        print('{} is not a file'.format(file))

if __name__ == '__main__':
    main()
