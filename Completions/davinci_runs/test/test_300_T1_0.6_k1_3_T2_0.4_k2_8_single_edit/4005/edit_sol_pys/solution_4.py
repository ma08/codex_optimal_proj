#!/usr/bin/python

import os
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print "[-] " + filename + " does not exist."
        exit(0)
    if not os.access(filename, os.R_OK):
        print "[-] " + filename + " access denied."
        exit(0)
    print "[+] Reading Vulnerabilities From: " + filename
else:
    print "[-] Usage: " + str(sys.argv[0]) + " <vuln filename>"
    exit(0)

file = open(filename, 'r')
for line in file.readlines():
    print line
