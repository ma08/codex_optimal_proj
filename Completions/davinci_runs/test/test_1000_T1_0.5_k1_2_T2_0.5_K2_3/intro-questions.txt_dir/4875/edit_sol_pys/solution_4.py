

import sys
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def pig_latin(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
        return word + "yay" 
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"

for line in sys.stdin:
    words = line.split()
    for word in words:
        print(pig_latin(word), end=" ")
    print()
