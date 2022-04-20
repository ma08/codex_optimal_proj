#!/usr/bin/env python

import sys
import os

if len(sys.argv) != 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    print("Error: File '%s' not found" % filename)
    sys.exit(1)

f = open(filename, 'r')

for line in f:
    print(line)

f.close()
