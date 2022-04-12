import sys

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def translate(word):
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    words = line.split()
    translated = [translate(word) for word in words]
    print(' '.join(translated))
