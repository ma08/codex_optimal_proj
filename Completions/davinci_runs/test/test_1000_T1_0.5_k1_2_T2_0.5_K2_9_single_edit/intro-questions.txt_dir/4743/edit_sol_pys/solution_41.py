

from sys import stdin
from string import ascii_lowercase, ascii_uppercase

FIRST = 'bcdfghkmnpqt'
SECOND = 'aeiou'
THIRD = 'aeiou'

def nimionese(word):
    if len(word) == 0:
        return ''
    elif len(word) == 1:
        return word[0]
    elif word[0] in FIRST:
        return word[0] + nimionese(word[1:])
    elif word[0] in SECOND:
        return 'a' + nimionese(word[1:])
    elif word[0] in THIRD:
        return 'e' + nimionese(word[1:])
    elif word[0] in ascii_uppercase:
        return word[0].lower() + nimionese(word[1:])
    else:
        return ' ' + nimionese(word[1:])

def main():
    words = stdin.readline().strip().split(' ')
    print(' '.join([nimionese(word) for word in words]))

if __name__ == '__main__':
    main()
