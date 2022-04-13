#!/usr/bin/env python


import sys
import os
import time

def reverse(string):
    return string[::-1]

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: file [--todo] file [file ...]')
        sys.exit(1)

    if args[0] == '--todo':
        del args[0]

        for arg in args:
            print(reverse(arg))

if __name__ == '__main__':
    main()
