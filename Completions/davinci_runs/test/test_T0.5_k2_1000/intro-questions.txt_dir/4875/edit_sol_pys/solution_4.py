

import sys

vowels = ['a','e','i','o','u']

def pig_latin(word):
    if word[0] in vowels:
        return word + 'yay' if word[-1] == 'y' else word + 'ay'
    for i in range(len(word)):
        if word[i] in vowels:
            break
    return word[i:] + word[:i] + 'ay'

def main(pname):
    sys.stdin = open(pname + '.in', 'r').read()
    sys.stdout = open(pname + '.out', 'w').write()

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
