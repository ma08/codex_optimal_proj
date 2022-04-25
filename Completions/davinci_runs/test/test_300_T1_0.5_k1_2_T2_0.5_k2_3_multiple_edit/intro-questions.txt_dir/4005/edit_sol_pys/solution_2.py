#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(0)

f = sys.argv[1]

# check if file exists
if not os.path.isfile(f):
    print("File {} does not exist".format(f))
    sys.exit(0)

# check if file is readable
if not os.access(f, os.R_OK):
    print("File {} is not readable".format(f))
    sys.exit(0)

# check if file is executable
if not os.access(f, os.X_OK):
    print("File {} is not executable".format(f))
    sys.exit(0)

# check if file is writable
if not os.access(f, os.W_OK):
    print("File {} is not writable".format(f))
    sys.exit(0)

print("File {} is OK".format(f))
