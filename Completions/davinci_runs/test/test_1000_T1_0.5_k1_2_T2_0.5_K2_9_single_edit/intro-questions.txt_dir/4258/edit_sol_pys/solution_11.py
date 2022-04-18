#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil


def main():
    if len(sys.argv) < 2:
        print('Usage: file.py <filename>')
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('Error: {0} file not found'.format(filename))
        sys.exit(2)

    basename = os.path.basename(filename)
    dirname = os.path.dirname(filename)

    dirname = os.path.join(dirname, 'backup')
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    shutil.copy(filename, dirname)

    os.remove(filename)


if __name__ == '__main__':
    main()
