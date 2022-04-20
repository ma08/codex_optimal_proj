#!/usr/bin/env python

import os
import sys

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <filename>" % sys.argv[0]
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print "Error: %s is not a file" % filename
        sys.exit(1)

    print "File: %s" % filename
    print "Owner: %s" % os.stat(filename).st_uid
    print "Permissions: %s" % oct(os.stat(filename).st_mode)[4:]
    print "Size: %s" % os.stat(filename).st_size
    print "Modified: %s" % os.stat(filename).st_mtime

if __name__ == '__main__':
    main()
