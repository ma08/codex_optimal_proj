#!/usr/bin/env python3

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split()
        for word in line:
            if word.lower() not in words:
                words.append(word.lower())
                print(word, end=' ') # end=' ' means there will be a space after the word
            else:
                print('.', end=' ') # end=' ' means there will be a space after the dot
        print()

main()
