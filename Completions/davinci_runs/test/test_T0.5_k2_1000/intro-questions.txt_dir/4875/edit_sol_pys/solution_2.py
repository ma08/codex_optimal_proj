import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def translate(word):
    if word[0].lower() in vowels:
        return word + 'yay'
    else:
        for i in range(len(word)):
            if word[i].lower() in vowels:
                return word[i:] + word[:i] + 'ay'

for line in sys.stdin:
    words = line.split()
    translated = [translate(word) for word in words]
    print(' '.join(translated))
