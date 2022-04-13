import os

import sys

def pig_latyn(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if word[0] in vowels:
        return word + 'yay'
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latyn(word) for word in line.split()]))

if __name__ == '__main__':
    main()
