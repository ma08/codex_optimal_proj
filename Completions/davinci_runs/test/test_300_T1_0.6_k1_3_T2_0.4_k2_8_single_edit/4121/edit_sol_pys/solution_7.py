#!/usr/bin/env python
import sys
import os
import time
import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--file', type=str, help='file name')
    parser.add_argument('--dir', type=str, help='dir name')
    parser.add_argument('--regex', type=str, help='regex')
    parser.add_argument('--replace', type=str, help='replace')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.file is not None:
        print(args.file)
        file = args.file
        if os.path.exists(file):
            with open(file, 'r') as f:
                content = f.read()
                if args.regex is not None:
                    regex = args.regex
                    if args.replace is not None:
                        replace = args.replace
                        content = re.sub(regex, replace, content)
                    else:
                        content = re.findall(regex, content)
                print(content)
    elif args.dir is not None:
        print(args.dir)
        dir = args.dir
        if os.path.exists(dir):
            for root, dirs, files in os.walk(dir):
                for file in files:
                    print(os.path.join(root, file))
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        if args.regex is not None:
                            regex = args.regex
                            if args.replace is not None:
                                replace = args.replace
                                content = re.sub(regex, replace, content)
                            else:
                                content = re.findall(regex, content)
                        print(content)
        else:
            print('dir is not exists')

if __name__ == '__main__':
    main()
