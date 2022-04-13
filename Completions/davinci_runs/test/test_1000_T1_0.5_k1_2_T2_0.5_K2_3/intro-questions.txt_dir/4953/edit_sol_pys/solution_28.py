#!/usr/bin/env python3


import sys

def main():
    n = int(sys.stdin.readline())
    languages = []
    for i in range(n):
        line = sys.stdin.readline().rstrip('\n').split()
        for lang in line[2:]:
            languages.append(lang)
    languages = set(languages)
    print(n - len(languages))

main()
