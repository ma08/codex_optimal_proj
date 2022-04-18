#!/usr/bin/env python

import sys

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'yay'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiou':
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]))

if __name__ == '__main__':
    main()
