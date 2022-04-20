import sys
import os

path = os.path.abspath(sys.argv[1])

if os.path.isdir(path):
    print("{} is a directory".format(path))
elif os.path.isfile(path):
    print("{} is a file".format(path))
else:
    print("{} is not a file or directory".format(path))
