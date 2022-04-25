#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(0)

file_name = sys.argv[1]

# check if file exists
if not os.path.isfile(file_name):
    print("File {} does not exist".format(file_name))
    sys.exit(0)

# check if file is readable
if not os.access(file_name, os.R_OK):
    print("File {} is not readable".format(file_name))
    sys.exit(0)

# check if file is executable
if not os.access(file_name, os.X_OK):
    print("File {} is not executable".format(file_name))
    sys.exit(0)

# check if file is writable
if not os.access(file_name, os.W_OK):
    print("File {} is not writable".format(file_name))
    sys.exit(0)

print("File {} is OK".format(file_name))
