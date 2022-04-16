
import sys

def piglatin(word):
    if word[0] in 'aeiouyAEIOUY':
        return word + 'yay'
    else:
        for i, c in enumerate(word):
            if c in 'aeiouyAEIOUY':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(piglatin, line.split())))
