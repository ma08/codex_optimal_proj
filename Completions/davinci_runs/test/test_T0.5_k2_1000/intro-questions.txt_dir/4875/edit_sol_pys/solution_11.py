#!/usr/bin/env python3

import sys

def piglatin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        for i, c in enumerate(word):
            if c in 'aeiou':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(piglatin, line.split())))
