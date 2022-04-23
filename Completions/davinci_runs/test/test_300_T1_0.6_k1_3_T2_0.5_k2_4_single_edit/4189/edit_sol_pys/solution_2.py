import os, sys

# Open a file
path = "/Users/sarah/Documents/python/file.txt"
fo = open(path, "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()
