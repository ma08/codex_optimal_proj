#!/usr/bin/env python3

import sys

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if word[0] in vowels:
        return word + "yay"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"

for line in sys.stdin:
    if line != '\n':
        words = line.split()
        for word in words:
            print(pig_latin(word), end=" ")
        print()
