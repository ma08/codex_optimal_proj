#!/usr/bin/env python


import sys
import re
import os
import time

def reverse(string):
    return string[::-1]

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todo] file')
        sys.exit(1)

    if not args[0] == '--todo':
        print('usage: [--todo] file')
        sys.exit(1)

    filename = args[1]

    if not os.path.exists(filename):
        print('{0} does not exist'.format(filename))
        sys.exit(1)

    if not os.path.isfile(filename):
        print('{0} is not a file'.format(filename))
        sys.exit(1)

    f = open(filename, 'r')
    for line in f:
        if re.match(r'^#.*', line):
            print(line)
    f.close()

if __name__ == '__main__':
    main()
