#!/usr/bin/env python3

import sys

def pig_latin(word):
    if word[0] in 'aeiouyAEIOUY':
        return word + 'yay' if word[0] in 'aeiouy' else word[0].lower() + word[1:] + 'yay' if word[0] in 'AEIOUY' else word + 'yay'
    else:
        for i in range(len(word)):
            if word[i] in 'aeiouyAEIOUY':
                return word[i:].capitalize() + word[:i].lower() + 'ay' if word[0] in 'AEIOUY' else word[i:] + word[:i] + 'ay' if word[0] in 'aeiouy' else word[i:].lower() + word[:i].lower() + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]))

if __name__ == '__main__':
    main()
