#!/usr/bin/env python3

import os
import re
import sys

def main():
    out = open(sys.argv[1], 'w')
    for root, dirs, files in os.walk(sys.argv[2]):
        for file in files:
            if re.search(r'\.txt$', file):
                f = open(os.path.join(root, file), 'r')
                out.write(f.read())
                f.close()
    out.close()

if __name__ == '__main__':
    main()
