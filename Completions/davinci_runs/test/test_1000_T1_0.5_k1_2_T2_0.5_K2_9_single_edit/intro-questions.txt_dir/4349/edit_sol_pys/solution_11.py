#!/usr/bin/python

import os
import sys

def main():
	if len(sys.argv) < 2:
		sys.exit("Usage: %s <file>" % sys.argv[0])
	
	file = sys.argv[1]

	if not os.path.exists(file):
		sys.exit("Error: File '%s' not found" % file)

	# file exists
	print "File:", file
	print "Size:", os.path.getsize(file)
	print "Type:", get_file_type(file)

def get_file_type(filename):
	return os.popen("file -b " + filename).read().strip()

if __name__ == "__main__":
	main()
