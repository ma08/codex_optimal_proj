import os
import sys

#print(sys.argv)

#file_name = sys.argv[1]
#file_name = "file.txt"
#file_name = "file.py"
#file_name = "file.pyc"
file_name = "file.py~"

if os.path.exists(file_name):
	print("file exists")
else:
	print("file does not exist")

if os.path.isfile(file_name):
	print("file is a regular file")
else:
	print("file is not a regular file")

if os.path.isdir(file_name):
	print("file is a directory")
else:
	print("file is not a directory")

if os.path.islink(file_name):
	print("file is a symbolic link")
else:
	print("file is not a symbolic link")
