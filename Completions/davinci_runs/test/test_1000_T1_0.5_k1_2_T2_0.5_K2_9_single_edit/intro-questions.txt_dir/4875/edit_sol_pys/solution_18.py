
import sys

def piglatin(word):
    if word[0] in 'aeiouy':
        return word + 'yay'
    else:
        for i, c in enumerate(word):
            if c in 'aeiou':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(piglatin, line.split())))
