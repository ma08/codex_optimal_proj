#!/usr/bin/env python

import os
import sys
import string
import random

def random_string(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def create_file(name, size):
    with open(name, 'w') as f:
        f.write(random_string(size))

def main():
    if len(sys.argv) < 3:
        print "Usage: {0} <file_name> <file_size>".format(sys.argv[0])
        sys.exit(1)

    name = sys.argv[1]
    size = int(sys.argv[2])

    create_file(name, size)

if __name__ == '__main__':
    main()
