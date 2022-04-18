

import sys

vowels = ['a','e','i','o','u','y']

def pig_latin(word):
    if word[0] in vowels:
        return word + 'yay'
    for index in range(len(word)):
        if word[index] in vowels:
            break
    return word[index:] + word[:index] + 'ay'

def main(pname='pig'):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    for line in lines:
        words = line.split()
        for i in range(len(words)):
            words[i] = pig_latin(words[i])
        print(' '.join(words))

if __name__ == "__main__":
    main()
