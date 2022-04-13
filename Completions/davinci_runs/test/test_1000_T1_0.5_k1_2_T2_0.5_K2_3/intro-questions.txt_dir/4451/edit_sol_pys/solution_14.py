#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='fix spelling mistakes')
    parser.add_argument('-f', '--file', help='the file to fix', required=True)
    parser.add_argument('-w', '--word', help='the word to fix', required=True)
    parser.add_argument('-r', '--replace', help='the word to replace', required=True)
    args = parser.parse_args()
    if not os.path.isfile(args.file):
        print('the file does not exist')
        sys.exit(1)
    with open(args.file, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.write(text.replace(args.word, args.replace))
        f.truncate()

if __name__ == '__main__':
    main()
