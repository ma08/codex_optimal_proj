#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-d', '--directory', help='directory', dest='directory', default=os.getcwd())
    parser.add_argument('-f', '--file', help='file', dest='filename', default='')
    parser.add_argument('-p', '--pattern', help='pattern', dest='pattern', default='')
    parser.add_argument('-r', '--replace', help='replace', dest='replace', default='')
    parser.add_argument('-m', '--mode', help='mode', dest='mode', default='r')
    parser.add_argument('-e', '--encoding', help='encoding', dest='encoding', default='utf-8')
    args = parser.parse_args()
    return vars(args)

def find_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename == file:
                yield os.path.join(root, file)

def main():
    args = parse_args()
    directory = args['directory']
    filename = args['filename']
    pattern = args['pattern']
    replace = args['replace']
    mode = args['mode']
    encoding = args['encoding']
    for file in find_file(directory, filename):
        with open(file, mode, encoding=encoding) as f:
            data = f.read()
            data = re.sub(pattern, replace, data)
            print(data)

if __name__ == '__main__':
    main()
