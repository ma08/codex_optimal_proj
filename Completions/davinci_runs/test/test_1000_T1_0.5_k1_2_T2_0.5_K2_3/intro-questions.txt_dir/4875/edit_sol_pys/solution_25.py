

import sys

    '''
    Returns a word in pig latin
    '''
def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if word[0] in vowels:
        return word + 'ay'
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'

    '''
    Outputs a line in pig latin
    '''
def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]))

if __name__ == '__main__':
    main()
