#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def main():
    if len(sys.argv) == 1:
        print('Usage: {} file1 file2 ...'.format(os.path.basename(sys.argv[0])), file=sys.stderr)
        sys.exit()

    for filename in sys.argv[1:]:
        if os.path.isfile(filename):
            print('{} is a file'.format(filename), file=sys.stderr)
        elif os.path.isdir(filename):
            print('{} is a directory'.format(filename), file=sys.stderr)
        else:
            print('{} is neither a file nor a directory'.format(filename), file=sys.stderr)

if __name__ == '__main__':
    main()
