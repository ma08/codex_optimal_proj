#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='fix spelling mistakes')
    parser.add_argument('-f', '--file', help='the file to fix')
    parser.add_argument('-w', '--word', help='the word to fix')
    parser.add_argument('-r', '--replace', help='the word to replace')
    if args.word is None or args.replace is None:
        print('word and replace are required arguments')  # pragma: no cover
        sys.exit(1)
    args = parser.parse_args()
    if args.file is None or not os.path.isfile(args.file):
        print('the file does not exist')  # pragma: no cover
        sys.exit(1)
    with open(args.file) as f:
        lines = f.readlines()
    with open(args.file, 'w') as f:
        for line in lines:
            f.write(line.replace(args.word, args.replace))

if __name__ == '__main__':
    main()
