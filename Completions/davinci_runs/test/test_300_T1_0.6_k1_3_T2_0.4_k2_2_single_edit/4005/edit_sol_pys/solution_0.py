#!/usr/bin/python

import sys, os

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("%s does not exist!" % filename)
        sys.exit(1)

    if not os.path.isfile(filename):
        print("%s is not a file!" % filename)
        sys.exit(1)

    if os.access(filename, os.R_OK):
        print("%s is readable" % filename)
    else:
        print("%s is not readable" % filename)

    if os.access(filename, os.W_OK):
        print("%s is writeable" % filename)
    else:
        print("%s is not writeable" % filename)

    if os.access(filename, os.X_OK):
        print("%s is executable" % filename)
    else:
        print("%s is not executable" % filename)

if __name__ == "__main__":
    main()
