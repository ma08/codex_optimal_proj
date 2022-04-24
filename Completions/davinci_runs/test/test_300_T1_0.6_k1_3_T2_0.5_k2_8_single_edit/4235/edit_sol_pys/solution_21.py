#!/usr/bin/python

import os
import sys

def main():
	if len(sys.argv) < 2:
		print "Usage: file.py <file>"
		return
	else:
		filename = sys.argv[1]
		if not os.path.exists(filename):
			print "File does not exist"
			return
		else:
			print "File exists"

if __name__ == "__main__":
	main()
