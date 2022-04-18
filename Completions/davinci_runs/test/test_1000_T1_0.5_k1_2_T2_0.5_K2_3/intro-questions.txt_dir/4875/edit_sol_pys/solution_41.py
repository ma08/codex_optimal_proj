import sys

def piglatin(word):
    if word[0] in 'aeiouy':
        return word + 'ay'
    else:
        for i, c in enumerate(word):
            if c in 'aeiouy':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(piglatin, line.split())))
