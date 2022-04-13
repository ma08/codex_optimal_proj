

import sys
import math

def convert(word):
    letters = list(word)
    for i in range(len(letters)):
        if letters[i].isupper():
    if len(letters) == 1:
        return ''.join(letters)
            letters[i] = letters[i].lower()
    if letters[0] not in 'bcdfghklmnpqrstvw':
        if letters[0] == 'a':
            letters[0] = 'z'
        else:
            letters[0] = chr(ord(letters[0])-1)
    if letters[0] == 'e':
        letters[0] = 'y'
    else:
        letters[0] = chr(ord(letters[0])-5)
    for i in range(1,len(letters)):
        if letters[i] in 'bcdfghklmnpqrstvw' and letters[i] != letters[0]:
            letters[i] = letters[i].replace(letters[i],letters[0])
    if letters[-1] in 'bcdfghklmnpqrstvw':
        letters[-1] = letters[-1].replace(letters[-1],letters[-1]+'ah')
    return ''.join(letters)

def main():
    for line in sys.stdin:
        words = line.strip().split()
        for i in range(len(words)):
            if '-' in words[i]:
                words[i] = ''.join(words[i].split('-'))
        for i in range(len(words)):
            words[i] = convert(words[i])
        print(' '.join(words))

main()
