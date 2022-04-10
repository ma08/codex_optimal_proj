#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: %s file" % sys.argv[0])
        sys.exit(1)

    fname = sys.argv[1]
    if not os.path.exists(fname):
        print("File %s does not exist" % fname)
        sys.exit(1)

    f = open(fname, 'r')
    lines = f.readlines()
    f.close()

    f = open(fname, 'w')
    for line in lines:
        line = line.replace('\r', '')
        f.write(line)
    f.close()

if __name__ == '__main__':
    main()
