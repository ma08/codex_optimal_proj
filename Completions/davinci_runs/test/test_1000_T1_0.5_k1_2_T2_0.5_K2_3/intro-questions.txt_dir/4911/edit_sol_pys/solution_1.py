

import os
import sys

def read_lines(path):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    main()
