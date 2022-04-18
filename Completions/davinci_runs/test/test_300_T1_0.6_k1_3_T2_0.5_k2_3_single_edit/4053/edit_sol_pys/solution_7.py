#!/usr/bin/python3

import sys

file_name = sys.argv[1]

f = open(file_name, 'r')

for line in f:
    print(line, end='')

f.close
