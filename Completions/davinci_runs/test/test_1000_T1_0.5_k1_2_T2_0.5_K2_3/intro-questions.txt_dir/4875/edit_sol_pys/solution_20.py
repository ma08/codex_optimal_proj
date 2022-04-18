

import sys

def main():
    for line in sys.stdin:
        words = line.split()
        for word in words:
            if word[0] in ['a', 'e', 'i', 'o', 'u']:
                print(word + 'yay', end=' ')
            else:
                first_vowel = word.index(next(c for c in word if c in ['a', 'e', 'i', 'o', 'u'])) # get the index of the first vowel
                print(word[first_vowel:] + word[:first_vowel] + 'ay', end=' ')
        print()

main()
