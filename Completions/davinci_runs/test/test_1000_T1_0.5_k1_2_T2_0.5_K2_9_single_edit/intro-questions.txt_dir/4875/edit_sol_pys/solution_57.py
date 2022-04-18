

import sys,re

def pig_latin(word):
    if word[0] in 'aeiouAEIOU':
        return word + 'yay' + ' '
    else:
        for i in range(len(word)):
            if word[i] in 'aeiouAEIOU':
                return word[i:] + word[:i] + 'ay' + ' '

def main():
    for line in sys.stdin:
        final = ''
        line = line.strip().split(' ')
        for i in range(len(line)):
            final += pig_latin(line[i])
        print(final)

if __name__ == '__main__':
    main()
