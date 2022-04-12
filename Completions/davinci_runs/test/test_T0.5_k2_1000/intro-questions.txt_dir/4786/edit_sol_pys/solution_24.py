#!/usr/bin/env python3

import sys

def main():
    keywords = set()
    for line in sys.stdin.readlines()[1:]:
        keywords.add(line.replace('-', ' ').lower().strip())
    print(len(keywords))

if __name__ == '__main__':
    main()
