#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

for line in input_file:
    # do something with the line
    print(line.strip())

input_file.close()
