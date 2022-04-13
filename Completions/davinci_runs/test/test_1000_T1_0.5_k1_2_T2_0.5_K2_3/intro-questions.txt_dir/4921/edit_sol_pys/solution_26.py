#!/usr/bin/env python3

import sys

def main():
    words = set()
    for line in sys.stdin:
        for word in line.split():
            if word.lower() in words: #if word is in the set
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower()) #adds words to the set
        print()

main()
