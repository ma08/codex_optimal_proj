

import sys
import math

def nimionian(word):
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
        word = 'h' + word
    if word[0] in ['h']:
        word = 'g' + word[1:]
    if word[0] in ['l']:
        word = 'd' + word[1:]
    if word[0] in ['m']:
        word = 'n' + word[1:]
    if word[0] in ['f']:
        word = 'b' + word[1:]
    if word[0] in ['v']:
        word = 'c' + word[1:]
    if word[0] in ['s']:
        word = 'z' + word[1:]
    if word[0] in ['r']:
        word = 'd' + word[1:]
    if word[0] in ['j']:
        word = 'g' + word[1:]
    if word[0] in ['x']:
        word = 'k' + word[1:]
    if word[0] in ['q']:
        word = 'k' + word[1:]
    if word[0] in ['w']:
        word = 'p' + word[1:]
    if word[0] in ['z']:
        word = 't' + word[1:]
    word = word.replace('each', 'dach')
    if word[-1] in ['a', 'e', 'i', 'o', 'u', 'y']:
        word += 'h'
    if word[-1] in ['h']:
        word = word[:-1] + 'o'
    if word[-1] in ['l']:
        word = word[:-1] + 'ah'
    if word[-1] in ['m']:
        word = word[:-1] + 'oh'
    if word[-1] in ['f']:
        word = word[:-1] + 'uh'
    if word[-1] in ['v']:
        word = word[:-1] + 'uh'
    if word[-1] in ['s']:
        word = word[:-1] + 'uh'
    if word[-1] in ['r']:
        word = word[:-1] + 'ah'
    if word[-1] in ['j']:
        word = word[:-1] + 'oh'
    if word[-1] in ['x']:
        word = word[:-1] + 'uh'
    if word[-1] in ['q']:
        word = word[:-1] + 'uh'
    if word[-1] in ['w']:
        word = word[:-1] + 'uh'
    if word[-1] in ['z']:
        word = word[:-1] + 'uh'
    return word

def main():
    sentence = sys.stdin.readline()
    sentence = sentence.split()
    nimioniansentence = []
    for word in sentence:
        nimioniansentence.append(nimionian(word))
    print(' '.join(nimioniansentence))

if __name__ == "__main__":
    main()
