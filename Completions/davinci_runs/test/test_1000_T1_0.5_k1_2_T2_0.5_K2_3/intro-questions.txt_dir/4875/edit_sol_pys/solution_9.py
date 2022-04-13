#!/usr/bin/env python

import sys

def pigLatin(word):
    if word[0] in 'aeiouy':
        return word + 'yay' 
    else:
        for i, c in enumerate(word):
            if c in 'aeiouy':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(pigLatin, line.split())))
