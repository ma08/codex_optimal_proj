#!/usr/bin/python

import os
import sys
import time
import commands

def main():
    # get the command line arguments
    #
    if len(sys.argv) != 3:
        print "Usage: %s <file> <size>" % sys.argv[0]
        sys.exit(1)
    filename = sys.argv[1]
    size = int(sys.argv[2])

    # create the file
    #
    f = open(filename, 'w')
    f.write('\0' * size)
    f.close()

    # get the filesize
    #
    (status, output) = commands.getstatusoutput("ls -l %s" % filename)
    if status != 0:
        print "Error: ls failed"
        sys.exit(1)
    fields = output.split()
    filesize = int(fields[4])
    if filesize != size:
        print "Error: file size is wrong"
        sys.exit(1)

    # remove the file
    #
    os.unlink(filename)

    # success
    #
    print "Success!"

if __name__ == '__main__':
    main()
