#!/usr/bin/env python

import sys
import os
import os.path

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("%s does not exist" % filename)
        sys.exit(2)

    print("%s is a %s" % (filename, filetype(filename)))

def filetype(filename):
    if os.path.isdir(filename):
        return "directory"
    elif os.path.isfile(filename):
        return "file"
    else:
        return "other"

if __name__ == "__main__":
    main()
