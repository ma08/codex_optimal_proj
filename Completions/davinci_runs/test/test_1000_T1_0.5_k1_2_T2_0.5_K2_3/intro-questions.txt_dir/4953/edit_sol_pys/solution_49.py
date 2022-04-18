#!/usr/bin/env python


import sys

def main():
    n = int(raw_input())
    languages = []
    for i in range(n):
        line = raw_input().rstrip().split()
        for lang in line[2:]:
            languages.append(lang)
    languages = set(languages)
    print n - len(languages)

main()
