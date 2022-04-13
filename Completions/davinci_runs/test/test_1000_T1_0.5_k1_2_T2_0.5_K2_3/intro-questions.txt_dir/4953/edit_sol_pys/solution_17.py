#!/usr/bin/env python3


import sys

def main():
    n = int(sys.stdin.readline())
    languages = set()
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        for lang in line[2:]:
            languages.add(lang)
    print(n - len(languages))

main()
