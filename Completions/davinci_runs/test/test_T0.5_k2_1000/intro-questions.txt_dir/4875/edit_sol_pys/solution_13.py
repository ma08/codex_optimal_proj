
import sys

def pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if word[0] in vowels:
        return word + 'ay'
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'

def main():
    for line in sys.stdin:
        print(' '.join([pig_latin(word) for word in line.split()]) + '\n')

if __name__ == '__main__':
    main()
