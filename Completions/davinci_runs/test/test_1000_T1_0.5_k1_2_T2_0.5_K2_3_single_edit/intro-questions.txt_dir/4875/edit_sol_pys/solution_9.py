
import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def translate(word):
    if word[0] in vowels:
    elif word[0] == 'y':
        return word[1:] + word[0] + 'ay'
        return word + 'yay'
    else:
        for i in range(len(word)):
            if word[i] in vowels:
        return word + 'ay'
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    words = line.split()
    translated = [translate(word) for word in words]
    print(' '.join(translated))
