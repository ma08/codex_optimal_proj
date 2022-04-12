#!/usr/bin/env python3

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.lower().strip().split()
        for word in line:
            if word in words:
                print(".", end=" ")
            else:
                words.append(word)
                print(word, end=" ")
        print()

main()
