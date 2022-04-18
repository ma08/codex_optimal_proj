from __future__ import print_function
import os
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def readlines(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).readlines()


if __name__ == '__main__':
    print(read('file.txt'))
