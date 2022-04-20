#!/usr/bin/env python3

import sys
import os

#print(sys.argv)

#print(os.getcwd())

#print(os.getenv('HOME'))

try:
    with open(sys.argv[1]) as f:
        print(f.read())
except:
    print("Could not open file")

