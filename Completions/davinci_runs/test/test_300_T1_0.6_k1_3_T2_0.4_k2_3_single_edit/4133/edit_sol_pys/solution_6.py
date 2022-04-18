#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    if len(sys.argv) > 1:
        print "Hello", sys.argv[1]
    else:
        print "Hello World!"

if __name__ == "__main__":
    main()
