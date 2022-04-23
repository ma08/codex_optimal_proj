#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def main(argv):
    if len(argv) != 2:
        print "Usage: %s [file]" % argv[0]
        sys.exit()

    file_name = argv[1]
    if os.path.exists(file_name):
        print "File '%s' exists." % file_name
    else:
        print "File '%s' does not exist." % file_name

if __name__ == "__main__":
    main(sys.argv)
