#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            newWord = ""
            i = 0
            while i < len(word):
                if word[i] in "aeiouAEIOU":
                    newWord += word[i:i+3]
                    i += 3
                else:
                    newWord += word[i]
                    i += 1
            print(newWord, end="")
            print(" ", end="")
        print()

main()
