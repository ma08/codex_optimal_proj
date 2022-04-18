#!/usr/bin/env python3

import sys

def pig_latin(word):
    if word[0].lower() in 'aeiouy':
        return word + 'yay' #if the word starts with a vowel, add 'yay' to the end
    else:
        for i in range(len(word)):
            if word[i].lower() in 'aeiouy':
                return word[i:] + word[:i] + 'ay' #if the word starts with a consonant, move the consonant to the end and add 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]))

if __name__ == '__main__':
    main()
