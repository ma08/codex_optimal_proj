import os
from os.path import join
import glob
import json

# get all the folders in the current directory
folders = glob.glob('./*')

# iterate through each folder
for folder in folders:
    # get all the files in the current folder
    files = glob.glob(join(folder, '*'))
    # iterate through each file
    for file in files:
        # open and read the file
        with open(file, 'r') as f:
            data = f.read()
        # write the file
        with open(file, 'w') as f:
            f.write(data)
