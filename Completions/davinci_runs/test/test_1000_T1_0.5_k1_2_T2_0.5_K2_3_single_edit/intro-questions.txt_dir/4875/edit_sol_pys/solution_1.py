
import re
import sys

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[0] in vowels or word[0] == 'y':
        return word + "yay"
    else:
        for i in range(len(word)):
            if word[i] in vowels or word[i] == 'y':

def has_special_characters(word):
    special_characters = ['.', ',', '?', '!']
    for i in range(len(word)):
        if word[i] in special_characters:
            return True
    return False

                return word[i:] + word[:i] + "ay"

for line in sys.stdin:
    words = line.split()
    for word in words:
        print(pig_latin(word), end=" ")
    print()
