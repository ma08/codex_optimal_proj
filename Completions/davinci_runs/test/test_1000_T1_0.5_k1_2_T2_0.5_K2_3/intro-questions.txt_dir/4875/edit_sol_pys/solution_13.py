# pig latin

import sys

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    """
    >>> pig_latin('pig')
    'igpay'
    >>> pig_latin('latin')
    'atinlay'
    >>> pig_latin('banana')
    'ananabay'
    """
    if word[0] in vowels:
        return word + 'yay'
    for i in range(len(word)):
        if word[i] in vowels:
            break
    return word[i:] + word[:i] + 'ay'

    """
    >>> main('pig')
    """
def main(pname):
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
    main('pig')
