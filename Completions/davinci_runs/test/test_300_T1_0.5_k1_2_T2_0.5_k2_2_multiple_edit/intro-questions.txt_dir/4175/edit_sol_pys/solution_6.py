#!/usr/bin/env python

import os
import sys

if len(sys.argv) == 1:
  print "Usage: %s <file>" % sys.argv[0]
  sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
  print "Error: File '%s' not found" % filename
  sys.exit(1)

f = open(filename)
try:
  print f.read()
finally:
  f.close()

sys.exit(0)
