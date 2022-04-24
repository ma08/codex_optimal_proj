#!/usr/bin/env python3

import os
import sys
import subprocess

# change working directory to the directory of this script
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# find all files in the current directory
files = os.listdir()

# remove this script from the list
files.remove('file.py')

# remove files that are not .py files
for f in files:
    if not f.endswith('.py'):
        files.remove(f)

# remove files that are not executable
for f in files:
    if not os.access(f, os.X_OK):
        files.remove(f)

# print the list of files
print('\n'.join(files))

# if there are no files, exit
if len(files) == 0:
    sys.exit()

# otherwise, ask the user which file to run
print('\nWhich file would you like to run?')

# get the user's choice
choice = input()

# if the choice is valid, run it
if choice in files:
    subprocess.call(['python3', choice])
# otherwise, exit
else:
    sys.exit()
