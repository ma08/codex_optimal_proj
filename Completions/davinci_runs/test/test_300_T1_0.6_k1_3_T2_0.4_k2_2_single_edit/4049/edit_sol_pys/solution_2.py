#!/usr/bin/python

import sys
import os
import re

if len(sys.argv) < 2:
    print "Usage: file.py <file>"
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print "File %s does not exist" % filename
    sys.exit(1)

if not os.access(filename, os.R_OK):
    print "File %s is not readable" % filename
    sys.exit(1)

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    m = re.search(r'^\s*\d+', line)
    if m:
        print m.group(0)
