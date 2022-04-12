
import sys

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'yay'
    else:
        for i, c in enumerate(word):
            if c in 'aeiou':
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    print(' '.join(map(pig_latin, line.split())))
