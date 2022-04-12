

from sys import stdin
from string import ascii_lowercase, ascii_uppercase

first = 'bcdfghkmnpqt'
second = 'aeiou'
third = 'aeiou'

def nimonian(word):
    if len(word) == 0:
        return ''
    elif len(word) == 1:
        return word[0]
    elif word[0] in first:
        return word[0] + nimonian(word[1:])
    elif word[0] in second:
        return 'a' + nimonian(word[1:])
    elif word[0] in third:
        return 'e' + nimonian(word[1:])
    elif word[0] in ascii_uppercase:
        return word[0].lower() + nimonian(word[1:])
    else:
        return ' ' + nimonian(word[1:])

def main():
    words = stdin.readline().strip().split(' ')
    print(' '.join([nimonian(word) for word in words]))

if __name__ == '__main__':
    main()
